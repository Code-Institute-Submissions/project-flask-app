$(document).ready(function() {
    $('.sidenav').sidenav();

    countCategory=0
    $('#btnAddTopicCategory').click(function() {
        let newDiv = $('<div class="row"><div class="input-field col s12"><input placeholder="text" id="new_category" type="text" class="validate" name="category'+countCategory+'"><label for="new_category">Category</label></div></div>');
        $('#formWrapper').append(newDiv);
        countCategory+=1
    });

});
