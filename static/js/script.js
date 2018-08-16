$(document).ready(function() {
    $('.sidenav').sidenav();

    countCategory=0
    $('#btnAddprojectCategory').click(function() {
        let newDiv = $('<div class="input-field col s12"><input placeholder="text" id="new_category" type="text" class="validate" name="category'+countCategory+'"><label for="new_category">Category</label></div>');
        $('#formWrapper').append(newDiv);
        countCategory+=1
    });
    
    $('.btnRemoveprojectCategory').click(function() {
        $(this).closest('div').remove()
    })
});
