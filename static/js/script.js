$(document).ready(function() {
    $('.sidenav').sidenav();

    countCategoryText=0
    countCategoryNumber=0
    countCategoryBoolean=0
    $('#btnAddprojectCategoryText').click(function() {
        let newDivText = $('<div class="input-field col s12"><input placeholder="text" maxlength="40" id="new_category" type="text" class="validate" name="textcategory'+countCategoryText+'"><label for="new_category">Category title (text)</label></div>');
        $('#formWrapper').append(newDivText);
        countCategoryText+=1
    });
    
    $('#btnAddprojectCategoryNumber').click(function() {
        let newDivNumber = $('<div class="input-field col s12"><input maxlength="40" placeholder="text" id="new_category" type="text" class="validate" name="numbercategory'+countCategoryNumber+'"><label for="new_category">Category title (number)</label></div>');
        $('#formWrapper').append(newDivNumber);
        countCategoryNumber+=1
    });
    
    $('#btnAddprojectCategoryBoolean').click(function() {
        let newDivBoolean = $('<div class="input-field col s12"><input maxlength="40" placeholder="text" id="new_category" type="text" class="validate" name="booleancategory'+countCategoryBoolean+'"><label for="new_category">Category title (boolean)</label></div>');
        $('#formWrapper').append(newDivBoolean);
        countCategoryBoolean+=1
    });
    
    $('.btnRemoveprojectCategory').click(function() {
        $(this).closest('div').remove()
    })
});
