$(document).ready(function(){
        $('select').material_select();
});

function add_ingredients(){
    var el = $("#additional_ingredients");
    if (el.is(':empty')){
    el.append(`<div class="row added">
			<div class="input-field col s5">
				<input
          id="ingredient_2"
          name="ingredient_2"
          type="text"
          class="validate"
        />
				<label for="ingredient_name">Ingredient Name</label>
			</div>

			<div class="input-field col s5">
				<input
          id="ingredient_quantity_2"
          type="text"
          class="validate"
          name="ingredient_quantity_2"
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
    else{
                    id = $("#additional_ingredients .validate:last").attr('id')
                    split_id = id.split("_")
                    count = parseInt(split_id[2])
                    console.log(count)
                    count += 1;
                    el.append(`<div class="row added">
			<div class="input-field col s5">
				<input
          id="ingredient_name_${count}"
          name="ingredient_name_${count}"
          type="text"
          class="validate"
        />
				<label for="ingredient_name">Ingredient Name</label>
			</div>

			<div class="input-field col s5">
				<input
          id="ingredient_quantity_${count}"
          type="text"
          class="validate"
          name="ingredient_quantity_${count}"
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
    };

}
function remove_ingredients(){
    var el = $('.added').last()
    el.remove();}