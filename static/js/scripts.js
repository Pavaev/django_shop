$(document).ready(function () {
    var form = $('#form_buying_product');
    form.on('submit', function (e) {
            e.preventDefault();
            var count = $('#count').val();
            var submit_btn = $('#submit-btn');
            var product_id = submit_btn.data("product_id");
            var product_name = submit_btn.data("name");
            var product_price = submit_btn.data("price");

            $('.basket-items ul').append('<li>' + product_name + ', '
                + count + ' шт.' + 'по ' + product_price + 'rub       ' +
                '<a href="#" class="delete-item">x</a></li>')

        }
    );

    function showingBasket() {
        $('.basket-items').removeClass('hidden');

    }


    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        showingBasket()

    });
    $('.basket-container').mouseover(function (e) {
        showingBasket()
    });
    // $('.basket-container').mouseout('click', function (e) {
    //     $('.basket-items').addClass('hidden');
    // });

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })
});

//TODO: https://www.youtube.com/watch?v=c2Q9wj9ju3Y