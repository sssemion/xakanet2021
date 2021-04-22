$(function(){
    $('.delete-server').on("click", function(){
        start_url = "/ajax/server/delete";
        server_id = $(this).val();
        url = start_url + "/" + server_id
        console.log(url);
        $.ajax({
                    url: url,
                    method: 'post',
                    dataType: 'json',

                    success: function(data) {
                        $.jGrowl('', {'header': 'Successfully deleted'});
                        window.location.href = "/";
                    },

                    error: function(data) {
                        $.jGrowl(data.responseJSON["message"], {'header': 'Error'});
                }
            });

    })
});