$('.owl-carousel').owlCarousel({
    loop: false,
    margin: 5,
    nav: true,
    dots: false,
    autoplay: false,
    // autoplayTimeout: 3000,
    stagePadding: 50,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})