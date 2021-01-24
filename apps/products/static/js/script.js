$(document).ready(function(){

    var searchBtn = $("#search-btn")
    var searchForm = $("#search-form")

    $(searchBtn).on("click", function(){

        searchForm.submit()

    })

})


function dropdown_prices(){

    var dropdown_content = document.getElementById('precos-fields');

    if(dropdown_content.style.display == 'none'){

        dropdown_content.style.display = 'flex';

    }
    else{

        dropdown_content.style.display = 'none';

    }

}
