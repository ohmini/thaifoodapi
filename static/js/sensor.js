(function($) {
    'use strict';

    var url = 'http://184.106.153.149/channels/113321/fields/1.json?results=10';

    var tel = '080-261-8207';

    $('#tel').val(tel);

    feedData();

    $('#refresh').click(function(){
        feedData();
    });

    function feedData(){
        $.ajax({
            method: 'GET',
            url: url
        }).done(function(result){
            var data = result.feeds;
            var latestData = data[data.length - 1];
            setLatestData(latestData);
            generateDataTable(data);
            console.log(data);
            console.log(latestData);
        })
    }

    function setLatestData(latestData){
        $('#light').val(latestData.field1)
        $('#time').val(moment(latestData.created_at, moment.ISO_8601).format('DD-MM-YYYY HH:mm น.'));
    }

    function generateDataTable(data){
        $.each(data.reverse(), function(index, value){
            addRow(value);
        })
    }

    function addRow(value){

        var element = "<tr><td>";
        element += value.entry_id + "</td><td>";
        element += value.field1 + "</td><td>";
        element += moment(value.created_at, moment.ISO_8601).format('DD-MM-YYYY HH:mm น.') + "</td>";
        element += "</tr>";
        $('#data').append(element);
    }


}(jQuery));