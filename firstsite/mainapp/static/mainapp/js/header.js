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

    var obj   = $('.back');
	var shade = obj.find('.city-back-shade');
	var tmt   = false;
	$(window).on('scroll resize', function() {
		//if (tmt) clearTimeout(tmt);
		//tmt = setTimeout(function() {
		if ($(window).width() > 1023) {
			var wHeight   = $(window).height();
			var scrollTop = $(window).scrollTop();
			var opacity   = Math.min(0.9, scrollTop / wHeight);
			shade.css('opacity', opacity);
		}
		//}, 50);
	}).resize();
    
    // Плавная прокрутка

    const anchors = document.querySelectorAll('a[href*="#"]')

    for (let anchor of anchors) {
        anchor.addEventListener("click", function(event) {
            event.preventDefault();
            const blockID = anchor.getAttribute('href')
            document.querySelector('' + blockID).scrollIntoView({
                behavior: "smooth",
                block: "start"
            })
        })
    }

    // 
});



