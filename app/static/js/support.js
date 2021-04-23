$(function(){
    $('.item-button').on('click', function(){
        data = $(this).val().split(',');
        username = data[0];
        item_id = data[1];
        url = "/ajax/user/" + username + '/give/' + item_id;
        $.ajax({
            url: url,
            method: 'post',
                    dataType: 'json',

                    success: function(data) {
                        $.jGrowl('', {'header': 'Successfully gave'});
                    },

                    error: function(data) {
                        $.jGrowl(data.responseJSON["message"], {'header': 'Error'});
                }
        });
    });

    $('.action-creeper').on('click', function(){
        username = $(this).val();
        url = "/ajax/user/" + username + '/act/creeper';
        $.ajax({
            url: url,
            method: 'post',
                    dataType: 'json',

                    success: function(data) {
                        $.jGrowl('', {'header': 'Successfully acted'});
                    },

                    error: function(data) {
                        $.jGrowl(data.responseJSON["message"], {'header': 'Error'});
                }
        });
    });


    $('.action-web').on('click', function(){
        username = $(this).val();
        url = "/ajax/user/" + username + '/act/web';
        $.ajax({
            url: url,
            method: 'post',
                    dataType: 'json',

                    success: function(data) {
                        $.jGrowl('', {'header': 'Successfully acted'});
                    },

                    error: function(data) {
                        $.jGrowl(data.responseJSON["message"], {'header': 'Error'});
                }
        });
    });

    $('.action-sand').on('click', function(){
        username = $(this).val();
        url = "/ajax/user/" + username + '/act/sand';
        $.ajax({
            url: url,
            method: 'post',
                    dataType: 'json',

                    success: function(data) {
                        $.jGrowl('', {'header': 'Successfully acted'});
                    },

                    error: function(data) {
                        $.jGrowl(data.responseJSON["message"], {'header': 'Error'});
                }
        });
    });

});