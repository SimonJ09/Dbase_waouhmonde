var page = 2;
let spinner1 = '<div class="m-auto my-2 spinner-grow text-primary spinner-loader" role="status"> <span class="sr-only">Loading...</span> </div>';
jQuery(document).ready(function ($) {
    $("body").on('click', '#loadmorerealisations', function () {
        //$('.realisations-container').append(spinner1);
        $('#loadmorerealisations').attr('disabled', 'disabled')
        var data = {
            'action': 'load_realisations_by_ajax',
            'page': page,
            'security': realisation.security,
            'type_realisation': $('#loadmorerealisations').attr('data-id')

        };
        //console.log(data.type_realisation);
        $.post(realisation.ajaxurl, data, function (response) {

            if ($.trim(response) != '') {
                $('#loadmorerealisations').removeAttr('disabled')
                //$('.spinner-loader').remove()
                $('.realisations-container').append(response);
                page++;
            }
            else {
                $('#loadmorerealisations').removeAttr('disabled')
                //$('.spinner-loader').remove()
                $('#loadmorerealisations').hide();
            }
        });
    });


});
