$(document).ready(function () {
  var form = $('.form_buying_product');
    console.log(form);

    function basketUpdating(prod_id, number, is_delete){
        var data = {};
        data.prod_id = prod_id;
        data.number = number;
        var csrf_token = $('.form_buying_product [name="csrfmiddlewaretoken"]').val();
        data["csrfmiddlewaretoken"] = csrf_token;

        if (is_delete){
            data["is_delete"] = true;
        }
        var url = form.attr("action");
        console.log(data);
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    if (data.products_total_nmb || data.products_total_nmb === 0){
                        $('#basket_total_nmb').text(data.products_total_nmb);
                            console.log(data.products);
                        $('.basket-items ul').html("");
                        $.each(data.products, function (k, v) {
                           $('.basket-items ul').append('<li>'+v.name+', '+v.number+'шт. '+'цена '+v.price_per_item+'грн.  '+
                                '<a class="delete-item" href="" data-prod_id="'+v.id+'">X</a>'+
                                '</li>');
                        })
                    }
                },
                error: function () {
                    console.log("error");
                }
                });
    }

    form.on('submit', function (e) {
        //var x = document.getElementById("demo");
        var x = document.getElementsByClassName("btn btn-success btn-lg");
        console.log("12345")
          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition);
          } else {
            x.innerHTML = "Geolocation is not supported by this browser.";
          }
        function showPosition(position) {
          console.log("Latitude: " + position.coords.latitude +
          "Longitude: " + position.coords.longitude);
        }
        e.preventDefault();
        var number = $(this).find('.item-number').val();
        var prod_id = $(this).attr('data-prod_id');
        var prod_name = $(this).attr('data-name');
        var prod_price = $(this).attr('data-price');
        var prod_token = $(this).find('input').attr('value');
       console.log(number);
       console.log(prod_id);
       console.log(prod_name);
       console.log(prod_price);
       console.log(prod_token);

        basketUpdating(prod_id, number, is_delete=false)

    });

function ShowCart(){
         $('.basket-items').removeClass('d-none')
    }
    $(".basket-container").on('hover', function (e) {
        e.preventDefault();
        ShowCart();
    })
    $(".basket-container").mouseover(function () {
        ShowCart();
    });
    $(".basket-container").mouseout(function () {
        $('.basket-items').addClass('d-none');
    });
    $(document).on('click', '.delete-item', function(e) {
        e.preventDefault();
        prod_id = $(this).data("prod_id");
        number = 0;
        basketUpdating(prod_id, number, is_delete=true)
    });

    function calculatingBasketAmount() {
        var total_order_amount = 0;
        $('.total-product-in-basket-amount').each(function () {
            total_order_amount = total_order_amount + parseFloat($(this).text());
        });
        console.log(total_order_amount);
        $('#total_order_amount').text(total_order_amount.toFixed(2));
    };
    $(document).on('change', ".product-in-basket-number", function () {
        var current_number = $(this).val();
        var current_tr = $(this).closest('tr');
        var current_price = parseFloat(current_tr.find('.product-price').text()).toFixed(2);
        var total_amount = parseFloat(current_number*current_price).toFixed(2);
        current_tr.find('.total-product-in-basket-amount').text(total_amount);
        calculatingBasketAmount();
    });
    calculatingBasketAmount();
});