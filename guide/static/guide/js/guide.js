$(document).ready(function () {
    $(window).scroll(function () {
        var items = $("#content").find(".item");
        var menu = $("#menu");
        var top = $(document).scrollTop();
        var currentId = ""; //滚动条现在所在位置的item id
        items.each(function () {
            var m = $(this);
            //注意：m.offset().top代表每一个item的顶部位置
            if (top > m.offset().top - 300) {
                currentId = "#" + m.attr("id");
            } else {
                return false;
            }
        });

        var currentLink = menu.find(".current");
        if (currentId && currentLink.attr("href") != currentId) {
            currentLink.removeClass("current");
            menu.find("[href=" + currentId + "]").addClass("current");
        }
    });

    $('#content .item .relative a').mouseover(function () {
        $(this).css("background","#FFFF33");
        $(this).css("opacity",0.5);
    });
    $('#content .item .relative a').mouseout(function () {
        $(this).css("background","transparent");
        $(this).css("opacity",0.5);
    });

    //关闭modal对话框处理事件
    $('.modal').on('hide.bs.modal',function () {
        //如果有视频则停止播放
        var video=document.getElementById("depart2_video");
        video.pause();
        video.currentTime=0;

        //如果是显示名称状态，就显示名称
        var switchcheck=document.getElementById("switch-checkbox");
        if(switchcheck.checked == true){
            $(".depart-tooltip").tooltip('show');
        }else{
            $(".depart-tooltip").tooltip('hide');
        }

        //恢复tooltip特性
        $('.depart-tooltip').on('hidden.bs.tooltip',function () {
            //如果是显示名称状态，就显示名称
            var sc=document.getElementById("switch-checkbox");
            if(sc.checked == true){
                $(this).tooltip('show');
            }else{

            }
        });

    });
    //打开modal对话框处理事件
    $('.modal').on('show.bs.modal',function () {
        $(".depart-tooltip").tooltip('destroy');
    });

    //保证名称显示持续
    $('.depart-tooltip').on('hidden.bs.tooltip',function () {
        //如果是显示名称状态，就显示名称
        var switchcheck=document.getElementById("switch-checkbox");
        if(switchcheck.checked == true){
            $(this).tooltip('show');
        }else{

        }
    });

    // $('#mySwitch').on('switch-change', function (e, data) {
    //     var $el = $(data.el)
    //         , value = data.value;
    //     console.log(e, $el, value);
    // });

});

function shineTwice(departId) {
    var depart = $('#depart'+departId);
    depart.css('background','#FFFF66');
    depart.fadeOut(500).fadeIn(500).fadeOut(500).fadeIn(500,function () {
        depart.css('background','transparent');
    });
}

function scrollToFloor(floor,departId) {
    if(floor === 1){
        $("html,body").animate({scrollTop:$("body").offset().top},600);

    }else if(floor === 2){
        $("html,body").animate({scrollTop:$("#item2").offset().top-80},600);
    }else if(floor === 3){
        $("html,body").animate({scrollTop:$("#item3").offset().top-80},600);
    }

    if(departId === 0)return;
    setTimeout(shineTwice(departId),600);
}


