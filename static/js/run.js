$(document).ready(function () {
  $("select").material_select();
});


  
function add_ingredients() {
  var el = $(".additional_ingredients");
  el.append(`
    <div class="row added">
    <div class="input-field col s5 quantity">
				<input
          id="ingredient"
          name="ingredient"
          type="text"
          class="validate added_ingredient"
        />
    </div>
    <div class="input-field col s5 quantity">    
        <input
          id="ingredient_quantity"
          type="text"
          class="validate added_quantity"
          name="ingredient_quantity"
        />
    </div>
    <div class="col s2">
	<a class="btn-floating btn-large waves-effect waves-light red"
				onclick="remove_ingredients($(this))">
                <i class="material-icons">remove</i>
                </a></div></div>
                `		);}

  

function remove_ingredients(el) {
 var element = el.parent("div").parent(".added")
  element.remove();
}


