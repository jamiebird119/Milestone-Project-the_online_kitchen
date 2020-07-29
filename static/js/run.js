// Collapsible nav bar initialiser
$(document).ready(function () {
    $(".sidenav").sidenav();
});

// Select Initialiser
$(document).ready(function () {
    $("select").formSelect();
});

// Function to add ingredient line to add recipe/edit recipe form 
function add_ingredients() {
    var el = $(".additional_ingredients");
    el.append(`
    <div class="row added">
    <div class="input-field col s4 m5 ingredients">
				<input
          id="ingredient"
          name="ingredient"
          type="text"
          class="validate added_ingredient"
        />
    </div>
    <div class="input-field col s4 m5 ingredients">    
        <input
          id="ingredient_quantity"
          type="text"
          class="validate added_quantity"
          name="ingredient_quantity"
        />
    </div>
    <div class="col s1">
	<a class="btn-floating btn-small waves-effect waves-light red"
				onclick="remove_ingredients($(this))">
                <i class="material-icons">remove</i>
                </a></div></div>
                `);
}

// Function to remove selected ingredient line from add recipe/edit recipe form
function remove_ingredients(el) {
    var element = el.parent("div").parent(".added");
    element.remove();
}

// Hover effect on recipe
$("a h5").mouseenter(function () {
    $(this).addClass("underline");
});
$("a h5").mouseleave(function () {
    $(this).removeClass("underline");
});
