/**
 * Created by Suki on 2017/10/29.
 */

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$(function() {
    $("#upload-image").on("click", function() {
    var img = $('#img-file')[0].files[0];
    var data = new FormData();
    data.append('image', img);
    $.ajax({
        url: '/common/upload-image/',
        type: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (data) {
             var img_url = data.imgPath;
             var addNode = '<p>' + img_url + '</p>'
             $('#upload-image').after(addNode)
        }
        }
    )
});
});

