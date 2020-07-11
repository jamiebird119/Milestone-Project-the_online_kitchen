$(document).ready(function(){
        $('select').material_select();
});

function add_ingredients(){
    var el = $("#additional_ingredients");
    el.append(`<div class="row added">
			<div class="input-field col s5">
				<input
          id="ingredient[]"
          name="ingredient[]"
          type="text"
          class="validate"
        />
				<label for="ingredient">Ingredient Name</label>
			</div>

			<div class="input-field col s5">
				<input
          id="ingredient_quantity[]"
          type="text"
          class="validate"
          name="ingredient_quantity[]"
        />
				<label for="ingredient_quantity">Ingredient Quantity</label>
			</div>
            <div class="col s2"> 
            <a class="btn-floating btn-large waves-effect waves-light red"
				onclick="remove_ingredients()">
                <i class="material-icons">remove</i>
                </a>
                </div>
                </div>`);
    }
    
}
function remove_ingredients(){
    var el = $('.added').last()
    el.remove();}