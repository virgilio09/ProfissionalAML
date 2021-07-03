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
    
    
    // preenchimento ciadde e estado home
    carregar_json('Estado');
    function carregar_json(id, cidade_id){
        var html = '';

        $.getJSON('https://gist.githubusercontent.com/letanure/3012978/raw/36fc21d9e2fc45c078e0e0e07cce3c81965db8f9/estados-cidades.json', function(data){
            html += '<option>Selecionar '+ id +'</option>';
            // console.log(data);
            if(id == 'Estado' && cidade_id == null){
                for(var i = 0; i < data.estados.length; i++){
                    html += '<option value='+ data.estados[i].sigla +'>'+ data.estados[i].nome+'</option>';
                }
            }else{
                for(var i = 0; i < data.estados.length; i++){
                    if(data.estados[i].sigla == cidade_id){
                        for(var j = 0; j < data.estados[i].cidades.length; j++){
                            html += '<option value='+ data.estados[i].sigla +'>'+data.estados[i].cidades[j]+ '</option>';
                        }
                    }
                }
            }

            $('#'+id).html(html);
        });
        
    }

    $(document).on('change', '#Estado', function(){
        var cidade_id = $(this).val();
        $(this).css('font-weight', '600');
        if(cidade_id != null){
            carregar_json('Cidade', cidade_id);
        }
    });

    $('#Cidade').change(function(){
        $(this).css('font-weight', '600');
    });

    $('#category').change(function(){
        $(this).css('font-weight', '600');
    });

});