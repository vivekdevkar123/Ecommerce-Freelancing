$('.owl-carousel').owlCarousel({
    loop: false,
    margin: 8,
    nav: true,
    dots: false,
    autoplay: false,
    // stagePadding: 0,
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