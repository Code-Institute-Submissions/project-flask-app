$(document).ready(function() {
    $('.sidenav').sidenav();

    countCategoryText = 0;
    countCategoryNumber = 0;
    countCategoryBoolean = 0;
    countCasePicture = 0;
    countCaseVideo = 0;


    $('#btnAddprojectCategoryText').click(function() {
        let newDivText = $('<div class="input-field col s12"><input placeholder="text" maxlength="40" id="new_category" type="text" class="validate" name="textcategory' + countCategoryText + '"><label for="new_category">Category title (text)</label></div>');
        $('#formWrapper').append(newDivText);
        countCategoryText += 1
    });

    $('#btnAddprojectCategoryNumber').click(function() {
        let newDivNumber = $('<div class="input-field col s12"><input maxlength="40" placeholder="text" id="new_category" type="text" class="validate" name="numbercategory' + countCategoryNumber + '"><label for="new_category">Category title (number)</label></div>');
        $('#formWrapper').append(newDivNumber);
        countCategoryNumber += 1
    });

    $('#btnAddprojectCategoryBoolean').click(function() {
        let newDivBoolean = $('<div class="input-field col s12"><input maxlength="40" placeholder="text" id="new_category" type="text" class="validate" name="booleancategory' + countCategoryBoolean + '"><label for="new_category">Category title (boolean)</label></div>');
        $('#formWrapper').append(newDivBoolean);
        countCategoryBoolean += 1
    });

    $('.btnRemoveprojectCategory').click(function() {
        $(this).closest('div').remove()
    });
    $('#btnAddcasePicture').click(function() {
        let newDivPicture = $('<div class="input-field col s12"><input placeholder="image URL should start with' + " 'http' " + '(Get nice images from pexels.com :D )" id="new_picture" type="text" class="validate" name="image' + countCasePicture + '"><label for="new_picture">Add picture url</label></div>');
        $('#caseForm').append(newDivPicture);
        countCasePicture += 1
    });
    $('#btnAddcaseVideo').click(function() {
        let newDivVideo = $('<div class="input-field col s12"><input placeholder="video URL should start with' + " 'http' " + '(Get nice videos from Youtube ... duhh! :P )" id="new_video" type="text" class="validate" name="video' + countCaseVideo + '"><label for="new_video">Add video url</label></div>');
        $('#caseForm').append(newDivVideo);
        countCaseVideo += 1
    });

    $('.carousel.carousel-slider').carousel({
        fullWidth: true
    });
});
