$(document).ready(function () {
    var container = $('.scroll');
    container.infinitescroll({
    navSelector: '.pagination',
    nextSelector: '.pagination a',
    itemSelector: '.item',
    animate: true,
    bufferPx: 5,
    extraScrollPx: 100,
    loading: {
        msgText: '<p>正在加载...</p>',
        finishedMsg: '没有更多内容了',
        img: '/media/img/ajax-loader.gif',
    },
    },
    function (newElements) {
        $(newElements).find('pre').each(function (i, e) {
        hljs.highlightBlock(e)
        });
    });


});
