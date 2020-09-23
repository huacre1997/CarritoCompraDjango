$(document).ready(function () {
    $('.owl-carousel').owlCarousel({
        rewind: true,
        loop: false,
        margin: 10,
        nav: true,
        navText: [],
        dots: false,
        mouseDrag:false,
        stageClass: "d-flex owl-stage mb-4",
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 4
            }
        }
    })
    $(".details").click(function (e) { 
        let url=$(this).attr("href");
        $.ajax({
            type: "GET",
            url: url,
            success: function (response) {
                $("#content").empty()
                $("#content").html($(response).html())
            }
        })        
    });
    $(".filter").click(function (e) { 
        let url=$(this).attr("href");
        console.log(url)
        e.preventDefault()
        $.ajax({
            type: "GET",
            url: url,
            success: function (response) {
                $("#ListView").empty()
                $("#ListView").append($(response).html())
            }
        })        
    });
})
