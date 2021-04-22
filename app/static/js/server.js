$(function(){
    $('input[name=server]').click(function(){
        start_url = "/ajax/server/activate";
        server_id = $(this).val();
        url = start_url + '/' + server_id;
        $.ajax({
                    url: url,
                    method: 'post',
                    dataType: 'json',

                    success: function(data) {
                        $.jGrowl('', {'header': 'Successfully activated'});
                    },

                    error: function(data) {
                        $.jGrowl(data.responseJSON["message"], {'header': 'Error'});
                }
            });
    });
});