$(document).ready(function () {
    $.ajaxSetup({
        headers: {"X-CSRFToken": $.cookie('csrftoken')}
    });

    function basketAmount() {
        var total_order_amount = 0;
        $(".total_product_in_basket_amount").each(function () {
            total_order_amount += parseFloat($(this).text());
        });
        $("#total_order_amount").text(parseFloat(total_order_amount).toFixed(2));

    }


    function updateCart(product_id, count, url) {

        var data = {};
        data.product_id = product_id;
        data.count = count;
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                if (data.count_error) {

                    alert("Неверное число заказанных товаров!");
                }
                else {
                    $(".basket-items ul").empty();

                    $("#basket_total_count").text(' (' + data.products_total_count + ')');
                    $.each(data.products_in_basket, function (k, v) {
                        console.log(v);
                        $(".basket-items ul").append('<li>' + v.name + ' '
                            + v.count + ' шт.' + 'по ' + v.price + 'rub       ' +
                            '<a href="#" class="delete-item" data-action="' + url + '" data-product_id="' + v.id + '">x</a></li>')
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
            var url = form.attr('action');

            updateCart(product_id, count, url)


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
        url = $(this).data("action");
        updateCart(product_id, count, url)
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

