var page= 2;
let spinner = '<div class="m-auto my-2 spinner-grow text-primary spinner-loader" role="status"> <span class="sr-only">Loading...</span> </div>';
jQuery( document ).ready(function( $ ) {
    $( "body" ).on('click', '#loadmoreposts' ,function() {
        //$('.blogposts-container').append(spinner);
        $('#loadmoreposts').attr('disabled', 'disabled')
        var data= {
            'action' : 'load_posts_by_ajax',
            'page': page,
            'security': blog.security

        };

        $.post(blog.ajaxurl, data, function(response) {
            if($.trim(response) != '') {
                console.log('reponse', response)
                $('#loadmoreposts').removeAttr('disabled')
                //$('.spinner-loader').remove()
                $('.blogposts-container').append(response);
                page++;
            }
            else {
                $('#loadmoreposts').removeAttr('disabled')
                //$('.spinner-loader').remove()
                $('#loadmoreposts').hide();
            }
        });
    });
    
    
  });
