$(document).ready(function () {
    var form = $('#form_buying_product');
    form.on('submit', function (e) {
            e.preventDefault();
            var count = $('#count').val();
            var submit_btn = $('#submit_btn');
            var product_id = submit_btn.data('product_id');
            var product_name = submit_btn.data('name');
            var product_price = submit_btn.data('price');
        }
    )
});

//TODO: https://www.youtube.com/watch?v=c2Q9wj9ju3Y