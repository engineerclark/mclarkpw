$(document).ready(function() {
    var $nav = $('nav');
    var $mc = $('.maincontent');
    var originalPosition = $nav.offset().top;
    var originalHeight = $nav.outerHeight();
    
    function dock() {
        $nav.addClass('docked');
    }
    
    function undock() {
        $nav.removeClass('docked');       
    }
    
    function isDocked() {
        return $nav.hasClass('docked');    
    }
    
    function onScroll() {
        var offset = $nav.offset();
        if(!isDocked() && (offset.top - $(window).scrollTop()) < 0) {
            dock();
        }
        else if(isDocked() && $(window).scrollTop() <= originalPosition) {
            undock();
        }
    }
    
    $(window).scroll(onScroll);
    onScroll();
});