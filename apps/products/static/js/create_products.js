//Faz os inputs terem capitalize
var inputs_section = document.getElementById('other_inputs')

var inputs = inputs_section.getElementsByTagName("input");

for (var i=0; i < inputs.length; i++) {

    inputs[i].className += " text-capitalize";

}
