// navbar 

// window.onscroll = function() {scrollFunction()};

// function scrollFunction() {
//     if(document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
//         document.getElementById("navbar").style.backgroundColor = 'blue';
//     }else{
//         document.getElementById("navbar").style.position = 'initial';
      
//     }
// }

// #backtotop
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
