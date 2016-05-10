(function($) {
    'use strict';

    var baseUrl = 'https://thaifoodapi.appspot.com/api/foods/';

    var url = baseUrl;

    $('#url').text(baseUrl);

    var searchByElement = $('#searchBy');
    var inputIdElement = $('#searchId');
    var urlText = $('#url');
    var limitElement = $('#limit');
    var offsetElement = $('#offset');

    searchByElement.change(function(){
        var val = $(this).val();
        var param = '';
        url = baseUrl;
        if(val === 'ingredient' && inputIdElement.val() ){
            param = '?ingredients='
        }
        url += param;
        setIdUrl();
    })

    inputIdElement.change(function(){
        setIdUrl();
    })

    

    function isNoneFirstParam(){
        setIdUrl();
        var tempUrl = urlText.text();
        if(tempUrl.search('?') === -1){
            return true;
        }
        return false;
    }



    $('#submit').click(function(){
        setIdUrl();
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

    function setIdUrl(){
        var val = inputIdElement.val();
        var idUrl = url;
        idUrl += val;
        urlText.text(idUrl);
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

}(jQuery));