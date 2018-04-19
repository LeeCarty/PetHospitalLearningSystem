;(function () {
	

	'use strict';

	// Placeholder 
	var placeholderFunction = function() {
		$('input, textarea').placeholder({ customClass: 'my-placeholder' });
	}
	
	// Placeholder 
	var contentWayPoint = function() {
		var i = 0;
		$('.animate-box').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('animated-fast') ) {
				
				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .animate-box.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn animated-fast');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft animated-fast');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight animated-fast');
							} else {
								el.addClass('fadeInUp animated-fast');
							}

							el.removeClass('item-animate');
						},  k * 200, 'easeInOutExpo' );
					});
					
				}, 100);
				
			}

		} , { offset: '85%' } );
	};
	// On load
	$(function(){
		placeholderFunction();
		contentWayPoint();

	});

}());

function cookieRmemberPassword()
{
	var userEmail = document.getElementById("id_account_email").value;
    if(userName == ''){
        alert("请输入邮箱。");
        return;
    }
    var userPass = document.getElementById("id_account_password").value;
    if(userPass == ''){
        alert("请输入密码。");
        return;
    }
	if($('#remember').is(':checked'))
	{
		var expdate = new Date();
		expdate.setTime(expdate.getTime() + 14 * (24 * 60 * 60 * 1000));
		SetCookie("useremail",userEmail, expdate)
		SetCookie(userEmail,userPass, expdate);
		alert("记住了你的密码登录。");
	}
	var form1 = document.loginform;
	form1.action="main.html";
	form1.submit();
}
//取Cookie的值
function GetCookie (name)
{
	var arg = name + "=";
	var alen = arg.length;
	var clen = document.cookie.length;
	var i = 0;
	while (i < clen)
	{
		var j = i + alen;
		//alert(j);
		if (document.cookie.substring(i, j) == arg)
		return getCookieVal (j);
		i = document.cookie.indexOf(" ", i) + 1;
		if (i == 0) break;
	}
	return null;
}
var isPostBack = "<%= IsPostBack %>";
function getCookieVal (offset)
{
	var endstr = document.cookie.indexOf (";", offset);
	if (endstr == -1)
	endstr = document.cookie.length;
	return unescape(document.cookie.substring(offset, endstr));
}
//写入到Cookie
function SetCookie(name, value, expires)
{
	var argv = SetCookie.arguments;
	//本例中length = 3
	var argc = SetCookie.arguments.length;
	var expires = (argc > 2) ? argv[2] : null;
	var path = (argc > 3) ? argv[3] : null;
	var domain = (argc > 4) ? argv[4] : null;
	var secure = (argc > 5) ? argv[5] : false;
	document.cookie = name + "=" + escape (value) +
	((expires == null) ? "" : ("; expires=" + expires.toGMTString())) +
	((path == null) ? "" : ("; path=" + path)) +
	((domain == null) ? "" : ("; domain=" + domain)) +
	((secure == true) ? "; secure" : "");
}
function checkCookie()
{
	var UserEmail = GetCookie("useremail");
	if(UserName != null)
	{
		document.getElementById('remember').checked = true;
		document.getElementById('userEmail').value = UserEmail;
		var PassWord = GetCookie(UserEmail);
		document.getElementById('passWord').value = PassWord;
	}
	else
	{
		document.getElementById('remember').checked = false;
		document.getElementById('userEmail').value = "";
	}

}
