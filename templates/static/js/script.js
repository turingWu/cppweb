/**
 * Created by Administrator on 2015/10/2.
 */

var nameSpace = {};
//ui层类
nameSpace.ui = {};

nameSpace.ui.changeStr = function($jq,str,password){
    if($jq.val()==''){
        $jq.val(str);
    }
    $jq.focus(function(){
        if(password!=undefined){
            $jq.attr('type','password');
        }
        if($(this).val()==str){

            $(this).val('');
        }
    });
    $jq.blur(function(){
        if($(this).val()==''){
            $(this).val(str);
            if(password !=undefined){
                $(this).attr('type','text');
            }
        }
    });
};
//app层次
nameSpace.app = {};


nameSpace.app.toNav = function(){
    $('#nav').find('.end').hover(function(){
        $(this).find('li').addClass('forDisplay');
    },function(){
        $(this).find('li').removeClass('forDisplay');
    });
};
nameSpace.app.toLoginBg = function(){
    var height = $(window).height;
    $('#blink').scroll(function(){
        $('#blink').css('height',height())
    }).find('.exit').click(function(){
        $('#blink').css('top',-2000+'px');
    });
    $('#nav').find('.log').find('a').click(function(){
        $('#blink').css('top','0');
    });

};
nameSpace.app.toLoginInput = function(){
    var userInput = $('#blink').find('.username');
    var passwordInput = $('#blink').find('.password');
    nameSpace.ui.changeStr(userInput,'请输入用户名或邮箱');
    nameSpace.ui.changeStr(passwordInput,'请输入密码','password');
    userInput.focus(function(){
        $('#blink').find('.form').addClass('focus');
    });
    userInput.blur(function(){
         $('#blink').find('.form').removeClass('focus');
    });
    passwordInput.focus(function(){
        $('#blink').find('.form').addClass('focus');
    });
    passwordInput.blur(function(){
        $('#blink').find('.form').removeClass('focus');
    });
};
nameSpace.app.toResgiter = function(){
    var register = $('#nav').find('.register');
    $('#nav').find('.reg').click(function(e){
            register.attr('style','display:block');
            e.stopPropagation();
    });
   $('body').click(function () {
       register.attr('style','display:none');
   })
};
nameSpace.tool = {};


$(function(){
    nameSpace.app.toNav();
    nameSpace.app.toLoginBg();
    nameSpace.app.toLoginInput();
    nameSpace.app.toResgiter();
});