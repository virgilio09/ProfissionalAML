$(document).ready(function(){
    // -------------------- #backtotop ----------------------------
    jQuery("#backtotop").click(function () {
        jQuery("body,html").animate({
            scrollTop: 0
        }, 600);
    });
    jQuery(window).scroll(function () {
        if (jQuery(window).scrollTop() > 150) {
            jQuery("#backtotop").addClass("visible");
        } else {
            jQuery("#backtotop").removeClass("visible");
        }
    });

    // ---------------------- dashboard ----------------------------
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');
    
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    
});