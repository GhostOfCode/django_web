// var slides = document.querySelectorAll('#slides .slide');
// var currentSlide = 0;
// var slideInterval = setInterval(nextSlide,5000);
//
// function nextSlide(){
//     slides[currentSlide].className = 'slide';
//     currentSlide = (currentSlide+1)%slides.length;
//     slides[currentSlide].className = 'slide showing';
// }

$(document).ready(function () {
    var form = $('#form_buying_product');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        var nmb = $('#number').val();
        console.log(nmb);
        var submit_btn = $("#submit_btn");
        var product_id = submit_btn.data("product_id");
        var product_name = submit_btn.data("product_name");
        var product_price = submit_btn.data("product_price");
        console.log(product_name);
        console.log(product_id);
        console.log(product_price);

        $('.basket-items ul').append('<li>' + product_name + ', ' + nmb+' pieces '+' by '  +product_price+' USD   ' +
            '<a class="delete-item" href="">x</a></li>'
        );
    });

    function ShowingBasket() {
        $('.basket-items').toggleClass('d-none');
    };

    $('.basket-container').on('click', function (e) {
        e.preventDefault();
        ShowingBasket();
    });

    $(".basket-container").mouseover(function () {
        ShowingBasket();
    });

    $('.basket-container').mouseout(function () {
        ShowingBasket();
    })

    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        $(this).closest('li').remove();
    })
});