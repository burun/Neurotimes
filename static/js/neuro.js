$(document).ready(function() {
    $('.grid').imagesLoaded(function() {
          $('.grid').masonry({
           // options
            itemSelector: '.grid-item',
            columnWidth: ".grid-sizer",
          });
    });

    var container = $('.scroll');
    container.infinitescroll({
    navSelector: '.paginator',
    nextSelector: '.paginator a',
    itemSelector: '.item',
    animate: true,
    bufferPx: 5,
    extraScrollPx: 100,
    loading: {
        msgText: '',
        finishedMsg: $('<div style="text-align: center">没有更多内容了</div>'),
        img: '/media/img/ajax-loader.gif',
    },
    },
    function (newElements) {
        $(newElements).find('pre').each(function (i, e) {
        hljs.highlightBlock(e)
        });
    });

    // Show wechat qrcode on home page
    var image = '<img src="/media/img/qrcode.png">';
    $('#popover').popover({trigger: "hover", content: image, html: true});
});
