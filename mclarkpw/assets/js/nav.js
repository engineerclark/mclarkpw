$(document).ready(function() {
    var $nav = $('nav');
    var originalPosition = $nav.offset().top;
    
    function isDocked() {
        return $nav.hasClass('docked');    
    }
    
    function onScroll() {
        var offset = $nav.offset();
        if(!isDocked() && (offset.top - $(window).scrollTop()) < 0) {
            $nav.addClass('docked');    
        }
        else if(isDocked() && $(window).scrollTop() <= originalPosition) {
            $nav.removeClass('docked');
        }
    }
    
    $(window).scroll(onScroll);
});