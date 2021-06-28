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
    var rmBtn = $('.rm-btn')
    
    $(searchBtn).on('click', function() {
        searchForm.submit();
    });

    $(rmBtn).on('click', function(e) {

        e.preventDefault();

        var delLink = $(this).attr('href');
        
        bootbox.confirm({
            message: "Você realmente deseja remover esse serviço?",
            buttons: {
                confirm: {
                    label: 'Sim',
                    className: 'btn'
                },
                cancel: {
                    label: 'Cancelar',
                    className: 'btn'
                }
            },
            callback: function (result) {
                if(result) {
                    window.location.href = delLink;
                }
            }
        });

    });

    
});