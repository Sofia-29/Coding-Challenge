
function change_file_name(fileInputId){
    $(fileInputId).on('change', function(){
        var fileName = $(this).val();
        fileName = fileName.replace('C:\\fakepath\\', "");
        $(this).next('.custom-file-label').html(fileName);
    })
}