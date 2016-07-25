(function(window){
    document.cookie = 'lan=;Path=/;expires='+new Date(+new Date()+1000*60*60*24*-100);
    var pathName = window.location.pathname,sHost = 'https://www.ucloud.cn',sPath = pathName.replace('/en/','/') ;
    var lanLink = window.location.href.indexOf('/en/') != -1,lanCookie=document.cookie.indexOf('lan=EN') != -1;
    var lan =  lanLink ? 'EN' : 'CN';
    var expiresTime = new Date(new Date().getTime() + 24*60*60*1000*1000);
    var lans = {
        CN : sHost + sPath,
        EN : sHost + '/en' + sPath
    };
    //读取link地址
    var getLink = function(){
        //设置官网记录的cookie
        document.cookie = 'lan='+ lan=='EN' ? 'CN' : 'EN' +';domain = .ucloud.cn;Path=/;expires='+expiresTime+';';
        return  lanCookie ? lans.EN : lans.CN;
    };
    var getLan = function(str){
        return document.cookie.indexOf('lan='+str) == -1
    };
    if((getLan('EN') && getLan('CN')) || window.location.pathname != '/'){
        return document.cookie = 'lan='+ lan +';domain = .ucloud.cn;Path=/;expires='+expiresTime+';';
    }
    (lanLink != lanCookie) && (window.location.href = getLink());
})(window);
$(document).ready(function(){
    var reg = /^(ytag\=).*(?=(\&|$))/g;
    //url匹配正则表达式
    var Ytag = window.location.search.substr(1).match(reg);
    if (Ytag != null) {
        document.cookie = Ytag + ';domain = .ucloud.cn;Path=/';
    }
//导航hover下拉菜单
    $(".sub-menu").hover(function(){
        var dropdown_menu=$(this).children(".dropdown-menu-top");
        dropdown_menu.addClass("db");
    }, function () {
        var dropdown_menu=$(this).children(".dropdown-menu-top");
        dropdown_menu.removeClass('db');
    });
    $(".dropdown-menu-toVp").hover(function () {
        $(this).addClass('db');
    }, function () {
        $(this).removeClass('db');
    });
//tab切换
    $("ul.tabs-nav li,.anchor li").click(function(){
        $(this).addClass("active").siblings().removeClass("active");
    });
    //产品页tab切换跳转
    $(".anchor li").click(function(e){
        e.preventDefault();
        $(this).addClass("active").siblings().removeClass("active");
        var tardiv_id=$(this).find('a').attr('href'),
            tar_div=$(tardiv_id);
        if(tar_div.html()!=null){
            var tar_div_top=tar_div.offset().top;
            $('body,html').animate({scrollTop:tar_div_top-158},0);
        }
    });
    var tabs = $(".tabs-nav li");
    var tab_contents = $(".tab-content .tab-pane");
    tabs.find("a").click(function(e){
        e.preventDefault();
        var target = $(e.currentTarget);
        var href = target.attr('href');
        tabs.removeClass('active');
        target.parents('.tab').addClass('active');
        tab_contents.removeClass('active');
        $(href).addClass('active');
    });
//头部移动端下拉菜单
    $("#mobile-lock").click(function(){
        $(this) .toggleClass("active");
    });
//移动端列表点击展开
    $('.tab-content .title').click(function () {
        var caret_blue=$(this).find('.caret-blue');
        if(caret_blue.hasClass('top')){
            caret_blue.removeClass('top').addClass('bottom');
        }else{
            caret_blue.removeClass('bottom').addClass('top');
        }
        $(this).next('.tab-pane').toggleClass('active');
    });
//产品介绍移动端列表点击展开
    $('.product-sort .sort-name').click(function () {
        var caret_blue=$(this).find('.caret-blue');
        if(caret_blue.hasClass('top')){
            caret_blue.removeClass('top').addClass('bottom');
        }else{
            caret_blue.removeClass('bottom').addClass('top');
        }
        $(this).next('.product-list').toggleClass('active');
    });
    //关于我们页面左侧导航收起展开
    $('.main-nav .first-node.father').click(function () {
        $(this).toggleClass('active');
        var li_active=$(this).siblings('.active');
        li_active.removeClass('active');
    });
    $('.main-nav .first-node .nav>li').click(function (e) {
        e.stopPropagation();
    });
    //顶部导航固定
    $(window).scroll(function() {
        var top_bg=$('.top-bg'),
            top_bg_fix=$('.top-bg.top-fixed'),
            winLeft=$(document).scrollLeft(),
            widWidth=$(window).width();
        $(document).scrollTop() > 54 ? top_bg.addClass('top-fixed') : top_bg.removeClass('top-fixed');
        $(document).scrollTop() > 54 ? $('.banner01').addClass('mt54') : $('.banner01').removeClass('mt54');
        $(document).scrollTop() > 54 ? $('.return-top').parent().removeClass('dn') : $('.return-top').parent().addClass('dn');
        if(widWidth<=1200){
            top_bg_fix.css('left',-winLeft);
        }else{
            top_bg_fix.removeAttr('style');
        }
    });
    //回到顶部
    $('.return-top').click(function () {
        $('body,html').animate({scrollTop:0},200);
        return false;
    });
    //右下角客服图标
    $(window).scroll(function() {
        var scrollTop = $(document).scrollTop(),//滚动条距离浏览器顶部的高度
            winHeight = $(window).height(),//窗口高度
            scrollBtm = $(document).height()-scrollTop-winHeight,//距离底部高度
            service_tool=$('.service-tool');
        var footer_height=$('.page-footer-wrap').height()+$('.regisnow-wrap').outerHeight();
        if(scrollBtm<=footer_height){
            service_tool.css('bottom',footer_height+3-scrollBtm);
        }else{
            service_tool.removeAttr('style');
        }
    });
    $(window).resize(function () {
        var scrollTop = $(document).scrollTop(),//滚动条距离浏览器顶部的高度
            winHeight = $(window).height(),//窗口高度
            scrollBtm = $(document).height()-scrollTop-winHeight,//距离底部高度
            service_tool=$('.service-tool');
        var footer_height=$('.page-footer-wrap').height()+$('.regisnow-wrap').outerHeight();
        if(scrollBtm<=footer_height){
            service_tool.css('bottom',footer_height+3-scrollBtm);
        }else{
            service_tool.removeAttr('style');
        }
    });
    //加入我们页面tab切换
    var join_tabs = $("#my-tab .tab");
    var join_tab_contents = $("#my-tab-content .tab-pane");
    join_tabs.find("a").click(function(e){
        e.preventDefault();
        var target = $(e.currentTarget);
        var href = target.attr('href');
        join_tabs.removeClass('active');
        target.parents('.tab').addClass('active');
        join_tab_contents.removeClass('active');
        $(href).addClass('active');
    });
    //首页轮播
    var dots_wrap=$('.dots-wrap'),
        dot=dots_wrap.find('.dot'),
        banner_list=$('.banner-list'),
        banner_list_img=banner_list.find('li'),
        show_index= 0;
    dots_wrap.css({
        'margin-left':-dots_wrap.width()/2,
        'bottom': 20
    });
    dot.bind('click', function () {
        var dot_num=$(this).index();
        $(this).addClass('active').siblings('.dot').removeClass('active');
        show_index=dot_num;
        showBanner(dot_num);
    });
    function showBanner(n){
        banner_list_img.eq(n).addClass('active').fadeIn(750).siblings("li").fadeOut(750).removeClass('active');
        var bgcolor=banner_list_img.eq(n).data('bgcolor');
        $('.banner01').css('background-color',bgcolor);
    }
    function changeBanner(){
        showBanner(show_index);
        show_index++;
        if(show_index==banner_list_img.length){
            show_index=0;
        }
        dot.eq(show_index-1).addClass('active').siblings('.dot').removeClass('active');
    }
    changeBanner();
    var autoChange=setInterval(changeBanner,6000);
    banner_list.hover(function () {clearInterval(autoChange);}, function () {
        autoChange=setInterval(changeBanner,6000);
    });
    //首页数据中心焦点跳转
    var bg_map=$('.background-map'),
        dics=$('.background-map .dics'),
        map_point=$('.map-point'),
        isRun = true,
        show_index2= 0,
        time = 5000,
        timer,
        point_auto=function(){timer = setTimeout(changeDics,time)};

    function showDics(n){
        dics.eq(n).addClass('hover').siblings(".dics").removeClass('hover');
    }
    function changeDics(){
        timer && clearTimeout(timer);
        if(!isRun){
            return;
        }
        showDics(show_index2);
        show_index2++;
        if(show_index2==dics.length){
            show_index2=0;
        }
        point_auto();
    }
    dics.hover(function () {
        show_index2 = $(this).index('.background-map .dics');
        showDics(show_index2);
        clearTimeout(timer);
        isRun = false;
    }, function () {
        isRun = true;
        point_auto();
    });
    map_point.hover(function () {
        isRun = false;
        dics.removeClass('hover');
        clearTimeout(timer);
    }, function () {
        isRun = true;
        point_auto();
    });
    changeDics();
//U市场滚动
    var page = 1;
    var i = 2; //每版放2个图片
    $("a .next").click(function(){    //绑定click事件
        var content = $(".content");
        var content_list = $(".content-list");
        var v_width = content.width();
        var len = content.find("li").length;
        var page_count = Math.ceil(len / i) ;   //只要不是整数，就往大的方向取最小的整数 
        if( !content_list.is(":animated") ){    //判断“内容展示区域”是否正在处于动画  
            if( page == page_count ){  //已经到最后一个版面了,如果再向后，必须跳转到第一个版面。
                content_list.animate({ left : '0px'}, "slow"); //通过改变left值，跳转到第一个版面 
                page = 1;
            }else{
                content_list.animate({ left : '-='+v_width }, "slow");  //通过改变left值，达到每次换一个版面
                page++;
            }
        }
    });
    $("a .pre").click(function(){    //绑定click事件
        var content = $(".content");
        var content_list = $(".content-list");
        var v_width = content.width();
        var len = content.find("li").length;
        var page_count = Math.ceil(len / i) ;   //只要不是整数，就往大的方向取最小的整数 
        if( !content_list.is(":animated") ){    //判断“内容展示区域”是否正在处于动画  
            if( page == 1 ){  //已经到最后一个版面了,如果再向后，必须跳转到第一个版面。
                content_list.animate({ left : '-='+v_width*(page_count-1) }, "slow");
                page = page_count;
            }else{
                content_list.animate({ left : '+='+v_width }, "slow");  //通过改变left值，达到每次换一个版面
                page--;
            }
        }
    });
    getLoginStatus(function (data) {
        if(data.RetCode == 0) {
            $('.nologin').addClass('logined').removeClass('nologin').find('.user-name').text(data.DataSet[0].UserEmail);
            window.isLogin = true;
            $('.jsRegisterBtn').text('进入控制台');
        }
    });
});
