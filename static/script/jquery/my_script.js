$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        console.log(12345);
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $('#submit_btn');
        var prod_id = submit_btn.data("prod_id");
        var prod_name = submit_btn.data("name");
        var prod_price = submit_btn.data("price");
        console.log(prod_id);
        console.log(prod_name);
        console.log(prod_price);
    });


        function showingBasket(){
            $('.basket-items').removeClass('d-none');
        }
    $('.basket-container').on('hover', function (e) {
        e.preventDefault();
        showingBasket();
    })
    $('.basket-container').mouseover(
        showingBasket()
    );
    $('.basket-container').mouseout(function () {
        $('.basket-items').addClass('d-none')
    });
})