$(document).ready(function () {
    $('.space-work').slick({
        dots: true,
        infinite: true,
        adaptiveHeiht: true,
        speed: 500,
        slidesToShow: 3,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 2,
                    infinite: false,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 1,
                }
            },
            
        ]
    });

    $('.about-master').slick({
        dots: true,
        infinite: true,
        speed: 500,
        slidesToShow: 1,
        adaptiveHeiht: true
    });
    
    const nav = $('#nav').offset().top;
    $(window).scroll(function () {
        const scrolled = $(this).scrollTop();
        if (scrolled > nav) {
            $('#header').addClass('nav-fixed')
        } else if (scrolled < nav) {
            $('#header').removeClass('nav-fixed')
        }
    })

    $('.p2').flowtype({
        fontRatio : 18
    });
    $('.p3').flowtype({
        fontRatio : 12
    });
    $('.p4').flowtype({
        fontRatio : 20
    })
})


