// $('a.page-scroll').bind('click', function(event) {
//     var $anchor = $(this);
//     $('html, body').stop().animate({
//         scrollTop: $($anchor.attr('href')).offset().top
//     }, 1500, 'easeInOutExpo');
//     event.preventDefault();
// });
//
$(document).ready(function () {

    $(document).on("scroll", function(){
        //Method 1: Using addClass and removeClass
        if ($(document).scrollTop() > 50) {

            $('.navbar-default').addClass('navbar-shrink').stop()
        } else {
            $('.navbar-default').removeClass('navbar-shrink');
        }
        //Method 2: Using toggleClass

       // $(".navbar-default").toggleClass("navbar-shrink", $(this).scrollTop() > 50)
    });
});

$(function() {
    $('a.page-scroll').bind('click', function(event) {
        event.preventDefault();
        var $target = $(this.hash),
            target = this.hash;
        $('html, body').stop().animate({
            scrollTop: $target.offset().top
        }, 1000, function(){

        });
    });
});


//
// $(function() {
//     $('a.page-scroll').bind('click', function(event) {
//         var $anchor = $(this);
//         $('html, body').stop().animate({
//             scrollTop: $($anchor.attr('href')).offset().top
//         }, 1500, 'easeInOutExpo');
//         event.preventDefault();
//     });
// });

// // Highlight the top nav as scrolling occurs
// $('body').scrollspy({
//     target: '.navbar-fixed-top'
// })
//
// // Closes the Responsive Menu on Menu Item Click
// $('.navbar-collapse ul li a').click(function() {
//     $('.navbar-toggle:visible').click();
// });