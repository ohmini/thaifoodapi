(function($) {
    'use strict';

    var baseUrl = 'https://thaifoodapi.appspot.com/api/foods/';

    var minNutrientSelection = [
        "minwater", "minprotien", "minfat", "mincarbohydrate", "mindiearyfiber",
        "minash", "mincalcium", "minphosphorus", "miniron", "minretinol",
        "minbetacarotene", "minvitamin_a", "minvitamin_e", "minthiamin", "minriboflavin",
        "minniacin", "minvitamin_c"
    ]
    var maxNutrientSelection = [
        "maxwater", "minprotien", "maxfat", "maxcarbohydrate", "maxdiearyfiber",
        "maxash", "maxcalcium", "maxphosphorus", "maxiron", "maxretinol",
        "maxbetacarotene", "maxvitamin_a", "maxvitamin_e", "maxthiamin", "maxriboflavin",
        "maxniacin", "maxvitamin_c"
    ]

    addOption(minNutrientSelection, "#minNutrients");
    addOption(maxNutrientSelection, "#maxNutrients")


    var url = baseUrl;

    $('#url').text(baseUrl);

    var inputIdElement = $('#searchId');
    var urlText = $('#url');
    var limitElement = $('#limit');
    var offsetElement = $('#offset');
    var minCaloriesElement = $('#minCalories');
    var maxCaloriesElement = $('#maxCalories');
    var earthElement = $('#earth');
    var waterElement = $('#water');
    var windElement = $('#wind');
    var fireElement = $('#fire');
    var excludeElement = $('#exclude');
    var randomElement = $('#random');


    $('#addMaxNutrients').click(function(){
        var index = $('#maxNutrients').val();
        var param = maxNutrientSelection[index];
        var value = $('#maxNutrientsField').val();
        addNutrientParameter(param, value);
    });
    $('#addMinNutrients').click(function(){
        var index = $('#minNutrients').val();
        var param = minNutrientSelection[index];
        var value = $('#minNutrientsField').val();
        addNutrientParameter(param, value);
    });


    $('#submit').click(function(){
        setUrl();
        $.ajax({
            method: 'GET',
            url: urlText.text()
        }).done(function(result){
            console.log(result);
            if(result.results){
                displayData(result.results);
            }else if(result.id){
                displayOneData(result);
            }else{
                $('#data').children().remove();
            }
        })

    })

    function setUrl(){
        var params = [];
        if(inputIdElement.val().length > 0){
            params.push(createParamObj('ingredients', inputIdElement.val()))
        }
        if(limitElement.val().length > 0){
            params.push(createParamObj('limit', limitElement.val()));
        }
        if(offsetElement.val().length > 0){
            params.push(createParamObj('offset', offsetElement.val()));
        }
        if(minCaloriesElement.val().length > 0){
            params.push(createParamObj('mincalories', minCaloriesElement.val()));
        }
        if(maxCaloriesElement.val().length > 0){
            params.push(createParamObj('maxcalories', maxCaloriesElement.val()));
        }
        if(earthElement.is(":checked") || waterElement.is(":checked") ||
            windElement.is(":checked") || fireElement.is(":checked")
        ){
            var val = getElementParamValue();
            params.push(createParamObj('elements', val));
        }

        if(excludeElement.is(":checked")){
            params.push(createParamObj('exclude', 'true'));

        }
        if(randomElement.is(":checked")){
            params.push(createParamObj('random', 'true'));
        }

        console.log(params);
        var completeUrl = baseUrl + getUrl(params);
        $('#url').text(completeUrl);

    }

    function getUrl(params){
        var paramsUrl = '?';
        $.each(params, function(index, value){
            paramsUrl += value.key + '=' + value.value;
            if(index+1 < params.length)
                paramsUrl += '&';
        })

        return paramsUrl;
    }

    function createParamObj(key, value){
        var obj = {};
        obj.key = key;
        obj.value = value;
        return obj;
    }

    function getElementParamValue(){
        var values = [];
        if(earthElement.is(":checked")){
            values.push('earth');
        }
        if(waterElement.is(":checked")){
            values.push('water');
        }
        if(windElement.is(":checked")){
            values.push('wind');
        }
        if(fireElement.is(":checked")){
            values.push('fire');
        }
        console.log(values);

        var value = '';
        for(var i=0; i<values.length; i++){
            value += values[i];
            if(i+1 >= values.length){
                break;
            }else{
                value += ',';
            }
        }

        return value;
    }

    function displayData(data){
        $('#data').children().remove()
        $.each(data, function(index, value){
            addRow(value);
        })

    }

    function displayOneData(data){
        $('#data').children().remove();
        addRow(data);
    }

    function addRow(value){

        var jsonUrl = baseUrl + value.id + "/?format=json";
        var element = "<tr><td>";
        element += value.id + "</td><td>";
        element += value.name + "</td><td>";
        element += value.calories + "</td><td>";
        element += "<a class='btn btn-info btn-sm' href='";
        element += jsonUrl + "' >";
        element += "json</a></td>";
        $('#data').append(element);

    }

    function addOption(options, target_id){
        $.each(options, function(index, value){
            var item = "<option value='";
            item += index;
            item += "'>" + value;
            item += "</option>";
            $(target_id).append(item)
        })
    }

    function addNutrientParameter(parameter, value){
        var item = "<li class='list-group-item'>";
        //item += "<span class='glyphicon glyphicon-minus-sign' style='float:right;cursor:pointer'></span>";
        item += parameter + '=' + value;

        item += "</li>"

        $('#nutrients').append(item);
    }

}(jQuery));