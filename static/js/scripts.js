$(document).ready(function () {


    var form = $('#form_buying_product');
    form.on('submit', function (e) {
            e.preventDefault();
            var count = $('#count').val();
            var submit_btn = $('#submit-btn');
            var product_id = submit_btn.data("product-id");
            var product_name = submit_btn.data("name");
            var product_price = submit_btn.data("price");


            var data = {};
            data.product_id = product_id;
            data.count = count;
            data.csrfmiddlewaretoken = $('#form_buying_product').find('[name="csrfmiddlewaretoken"]').val();
            var url = form.attr('action');
            $.ajax({
                url: url,
                type: 'POST',
                data: data,
                cache: true,
                success: function (data) {
                    console.log("OK");
                    console.log(data.products_total_count);

                    $(".basket-items ul").empty();

                    $("#basket_total_count").text(' (' + data.products_total_count + ')');
                    $.each(data.products, function (k, v) {
                        $(".basket-items ul").append('<li>' + v.name + ' '
                            + v.count + ' шт.' + 'по ' + v.price_per_item + 'rub       ' +
                            '<a href="#" class="delete-item">x</a></li>')
                    })
                }
            });


        }
    );


    $('.basket-container').mouseover(function (e) {
        $('.basket-items').removeClass('hidden');
    });
    $('.basket-container').mouseout(function (e) {
        $('.basket-items').addClass('hidden');
    });

    // $(document).on('click', '.delete-item', function (e) {
    //     e.preventDefault();
    //     $(this).closest('li').remove();
    // })
});

