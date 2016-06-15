from django.shortcuts import render
from light_sensor.models import SensorData
from datetime import datetime
import urllib2
import json


def index(request):
    query_set = SensorData.objects.all().last()
    response = urllib2.urlopen('http://184.106.153.149/channels/113321/feeds.json?results=1')
    data = json.loads(response.read())
    entry_id = data['feeds'][0]['entry_id']
    light_value = int(data['feeds'][0]['field1'])
    temp_value = float(data['feeds'][0]['field2'])

    sms_base_url = 'http://www.thsms.com/api/rest?method=send'
    sms_username = '&username=ohmini'
    sms_password = '&password=nros3517'
    sms_from = '&from=0000'
    sms_to = '&to=' + query_set.tel
    sms_msg = '&message=Alert!!'

    sms_get = sms_base_url + sms_username + sms_password + sms_from + sms_to + sms_msg

    if query_set is not None:
        if query_set.entry_id < entry_id:
            query_set.light_value = light_value
            query_set.entry_id = entry_id
            query_set.temp_value = temp_value
            query_set.save()
            if light_value > query_set.alert_value or temp_value > 40:
                urllib2.urlopen(sms_get)

    else:
        sensor_data = SensorData(entry_id=0, light_value=0, temp_value=0, create_time=datetime.now(), version=0)
        sensor_data.save()

    return render(request, 'embedded/index.html')
