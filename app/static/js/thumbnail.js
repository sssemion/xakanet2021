var original_image;
var points;
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            original_image = e.target.result;
            $("#preload").attr("src", original_image);
            $(".photo-filename").text($("#photoField").val().split('\\').pop().split('/').pop());
            $("#croppie-toggler").attr("disabled", false);
        }

        reader.readAsDataURL(input.files[0]);
    }
}

$(function(){
    $("#photoField").change(function() {
        readURL(this);
    });
});