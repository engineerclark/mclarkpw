/******************************
 *  Simple portfolio operation
 *      Display project preview when gallery thumbnail is clicked
 */


var Portfolio = new (function(){
    var $element = null;
    
    function scrollToPreview() {
        $('html,body').animate({scrollTop: $element.offset().top},'slow');    
    }
    function showPreview(id) {
        var selector = ".project[data-projectid='"+id+"']";
        $element.find('.project').hide();
        var $p = $element.find(selector);
        $p.show();
    }
    function getDefaultId() {
        return $element.find('.project').first().attr('data-projectid');
    }
    function showDefault() {
        showPreview(getDefaultId());
    }
    function onThumbClick(event) {
        event.stopPropagation();
        event.preventDefault();
        var $thumb = $(event.target);
        showPreview($thumb.attr('data-projectid'));    
        scrollToPreview();
    }
    function init(projects) {
        $element = $(projects);
        $element.find('.thumbnail a').click(onThumbClick);
        showDefault();
    }
    this.Init = init;
})();