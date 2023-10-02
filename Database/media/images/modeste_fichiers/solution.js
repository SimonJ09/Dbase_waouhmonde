let spinner2 = '<div class="m-auto my-2 spinner-grow text-primary spinner-loader" role="status"> <span class="sr-only">Loading...</span> </div>';
jQuery(document).ready(function ($) {
    let trie = '';
    var paged = 2;
    let click = 0
    $("body").on('keyup', '#search_solution', function (e) {
        var search = e.target.value
        trie = search
        var data = {
            'action': 'load_solutions_by_ajax',
            'page': 1,
            'security': solution.security,
            'search_solution': search
        };
        $.post(solution.ajaxurl, data, function (response) {
            if ($.trim(response) != '') {

                $('#loadmoresolutions').show();
                $('.solutions-container').html('<span></span>')
                $('.solutions-container').append(response);
                paged = 2
                //page++;
            }
            else {
                paged = 2
                $('.solutions-container').html('<h2 class="text-center">Aucune solution trouvée</span>')
            }
        });

    });

    $("body").on('click', '#loadmoresolutions', function () {
        click++
        $('#loadmoresolutions').attr('disabled', 'disabled')
        //$('.pagination').append(spinner2);
        var data = {
            'action': 'add_solutions_by_ajax',
            'page': paged,
            'security': solution.security,
            'search_solution': trie
        };
        $.post(solution.ajaxurl, data, function (response) {
            if ($.trim(response) != '') {

                $('#loadmoresolutions').removeAttr('disabled')
                //$('.spinner-loader').remove()
                $('.solutions-container').append(response);
                paged++;
            }
            else {

                $('#loadmoresolutions').removeAttr('disabled')
                //$('.spinner-loader').remove()
                $('#loadmoresolutions').hide();
            }
        });

    });


});
