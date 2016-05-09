(function($) {
    'use strict';

    var baseUrl = 'https://thaifoodapi.appspot.com/';
    var url = baseUrl;

    $('#url').text(baseUrl);

    var searchByElement = $('#searchBy');
    var inputIdElement = $('#searchId');
    var urlText = $('#url');

    searchByElement.change(function(){
        var val = $(this).val();
        var param = '';
        url = baseUrl;
        if(val === 'ingredient'){
            param = '?ingredients='
        }
        url += param;
        setIdUrl();
    })

    inputIdElement.change(function(){
        setIdUrl();
    })

    function setIdUrl(){
        var val = inputIdElement.val();
        var idUrl = url;
        idUrl += val;
        urlText.text(idUrl);
    }

}(jQuery));