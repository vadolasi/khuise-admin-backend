//Faz os inputs terem capitalize
var inputs_section = document.getElementById('other_inputs')

var inputs = inputs_section.getElementsByTagName("input");

for (var i=0; i < inputs.length; i++) {

    inputs[i].className += " text-capitalize";
    console.log('ola mundo');

}

function CreateGuid() {  
    function _p8(s) {  
        var p = (Math.random().toString(16)+"000000000").substr(2,8);  
        return s ? "-" + p.substr(0,4) + "-" + p.substr(4,4) : p ;  
    }  
    return _p8() + _p8(true) + _p8(true) + _p8();  
}  

function addTamanho(){

    var id = CreateGuid();

    var container = document.getElementById("container_tamanhos");
    var inputs = document.getElementById("inputs_tamanho").children[0];

    var clone = inputs.cloneNode(true);
    clone.id = id;

    container.prepend(clone);

    var cloneText = clone.innerHTML;
    cloneText = cloneText.replace(/templateId/g, id);
    clone.innerHTML = cloneText;

}

function deletarTamanho(id){

    var tamanho = document.getElementById(id);
    tamanho.remove();

}