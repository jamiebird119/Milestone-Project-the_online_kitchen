$(document).ready(function () {
  $("select").material_select();
});

function add_ingredients() {
  var el = $(".ingredients");
  el.append(`
				<input
          id="ingredient"
          name="ingredient"
          type="text"
          class="validate added_ingredient"
        />
				
			`);

  var el_2 = $(".quantity");
  el_2.append(`<input
          id="ingredient_quantity"
          type="text"
          class="validate added_quantity"
          name="ingredient_quantity"
        />
				`);
    var button = $("#additional");
    button.append(`<div class="col s12 added"><a class="btn-floating btn-large waves-effect waves-light red"
				onclick="remove_ingredients()">
                <i class="material-icons">remove</i>
                </a></div>
                `);
            
}

function remove_ingredients() {
  var el = $(".added_ingredient").last();
  var el_2 = $(".added_quantity").last();
  var button = $(".added").last();
  el.remove();
  el_2.remove();
  button.remove();
}

