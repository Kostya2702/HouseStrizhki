$(document).ready(function () {
    const nav = $('#nav').offset().top;
    $(window).scroll(function () {
        const scrolled = $(this).scrollTop();
        if (scrolled > nav) {
            $('#header').addClass('nav-fixed')
        } else if (scrolled < nav) {
            $('#header').removeClass('nav-fixed')
        }
    })
})