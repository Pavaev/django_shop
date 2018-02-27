$(document).ready(function () {


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

                $(".basket-items ul").empty();

                $("#basket_total_count").text(' (' + data.products_total_count + ')');
                $.each(data.products, function (k, v) {
                    $(".basket-items ul").append('<li>' + v.name + ' '
                        + v.count + ' шт.' + 'по ' + v.price_per_item + 'rub       ' +
                        '<a href="#" class="delete-item" data-product_id="' + v.id + '">x</a></li>')
                });
                if (data.total_amout > 0) {
                    $(".basket-items ul").append('<div class="navbar-total-amout">Итого:' + data.total_amout + 'rub</div>');
                }
                else {
                    $(".basket-items ul").append('Корзина пуста')
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
    })
});

