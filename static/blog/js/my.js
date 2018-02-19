/**
 * Created by Suki on 2017/10/15.
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

// 注册
$(function() {
    $("#modal-register").on("click", function() {
    var user = $('#id-register-modal-user').val()
    var pwde = $('#id-register-modal-pwd')
    var pwd = pwde.val()
    if (pwd.length < 6){
        pwde.val('*密码太简单')
        pwde.css('color', '#d9534f')
        return
    }
    $.ajax({
        url: '/account/quick-register/',
        type: 'POST',
        data: {user: user, pwd: pwd},
        success: function () {
             $('#id-close-register-modal').trigger("click");
             alert('注册成功，进入邮箱点击链接即可激活账号。')
        }
        }
    )
});
});

// 登录
$(function() {
    $("#modal-login").on("click", function() {
    var user = $('#id-login-modal-user').val()
    var pwde = $('#id-login-modal-pwd')
    var pwd = pwde.val()
    if (pwd.length < 6){
        pwde.val('*密码太简单')
        pwde.css('color', '#d9534f')
        return
    }
    $.ajax({
        url: '/account/user-login/',
        type: 'POST',
        data: {user: user, pwd: pwd},
        success: function () {window.location.reload()},
        error: function () {
            $('#id-modal-input').find('p').remove()
            $('#id-modal-input').append('<p style="margin-left:12px; color:#d9534f">账号密码不正确！</p>')
        }
        }
    )
});
});

// 添加喜欢
$(function() {
    $("#id-add-thank").on("click", function () {
        var addThank = $('#id-add-thank')
        if (addThank.attr('disabled') === 'disabled') {
            return
        }
        var post_id = addThank.parent().attr('id')
        var url = 'post/' + post_id + '/thank/'
        $.ajax({
            url: url,
            data: {},
            type: 'POST',
            dataType: 'json'
        }).done(function (data) {
            if (!data.r) {
                window.data = data
                var count = data.count;
                addThank.text(count + '感谢')
                addThank.css('color', 'red');
                addThank.children('a').css('color', 'red')
                addThank.attr('disabled', true)
            } else {
                alert('failed')
            }
        })
    });
});

