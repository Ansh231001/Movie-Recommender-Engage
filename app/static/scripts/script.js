// JS FOR CAROUSEL 

$('.owl-carousel').owlCarousel({
    loop: true,
    margin: 10,
    nav: true,
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        //NUMBER OF ITEMS BASED ON SCREEN WIDTH
        //0,300,600,1000 WIDTH IN PIXELS

        0: {
            items: 1   
        },
        300 : {
            items: 2
        },
        600: {
            items: 3
        },
        1000: {
            items: 5
        }
    }
})



