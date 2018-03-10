$(document).ready(function () {


    function basketAmount() {
        var total_order_amount = 0;
        $(".total_product_in_basket_amount").each(function () {
            total_order_amount += parseFloat($(this).text());
        });
        $("#total_order_amount").text(parseFloat(total_order_amount).toFixed(2));

    }


    function updateBasket(product_id, count, is_delete) {

        var data = {};
        data.product_id = product_id;
        data.count = count;
        data.csrfmiddlewaretoken = $('#form_buying_product').find('[name="csrfmiddlewaretoken"]').val();
        data.is_delete = is_delete;


        var url = form.attr('action');
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {

                if (data.count_error.length) {
                    console.log(data);
                    alert("Неверное число заказанных товаров!");
                }
                else {
                    $(".basket-items ul").empty();

                    $("#basket_total_count").text(' (' + data.products_total_count + ')');
                    $.each(data.products, function (k, v) {
                        $(".basket-items ul").append('<li>' + v.name + ' '
                            + v.count + ' шт.' + 'по ' + v.price_per_item + 'rub       ' +
                            '<a href="#" class="delete-item" data-product_id="' + v.id + '">x</a></li>')
                    });
                    if (data.total_amount > 0) {
                        $(".basket-items ul").append('<div class="navbar-total-amount">Итого:' + data.total_amount + 'rub</div>');
                    }
                    else {
                        $(".basket-items ul").append('Корзина пуста')
                    }
                }
            }
        });

    }

    var form = $('#form_buying_product');
    form.on('submit', function (e) {
            e.preventDefault();
            var count = $('#count').val();
            var submit_btn = $('#submit-btn');
            var product_id = submit_btn.data("product-id");


            updateBasket(product_id, count, is_delete = false)


        }
    );


    $('.basket-container').mouseover(function (e) {
        $('.basket-items').removeClass('hidden');
    });
    $('.basket-container').mouseout(function (e) {
        $('.basket-items').addClass('hidden');
    });

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        product_id = $(this).data("product_id");
        count = 0;
        updateBasket(product_id, count, is_delete = true)
    });

    basketAmount();

    $(document).on("change", ".product-in-basket-count", function () {
        var current_count = $(this).val();
        var current_tr = $(this).closest("tr");
        var current_price = current_tr.find(".product-price").text();
        var total_amount = parseFloat(current_count * current_price).toFixed(2);
        current_tr.find(".total_product_in_basket_amount").text(total_amount);
        basketAmount();
    });
});

