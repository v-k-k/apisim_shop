 	$(document).ready(function(){
    $('.slider').bxSlider({
    	auto:true,
    	speed:300,
    	controls:false,
    	responsive:true,
    	slideWidth:1280,
    	shrinkItems:false,
    	adaptiveHeight:true,
    	touchEnabled:true,
    	pager:false,
    });
// Модальное окно

// открыть по кнопке
$('#get_cons_btn').click(function() { 
    $("body>*:not(.pop-up)").css("filter","blur(5px");
    $('.pop-up').fadeIn(1000);
});

// закрыть на крестик
    $('.close_pop-up').click(function() { 
    $('.pop-up').fadeOut();
    $("body>*:not(.pop-up)").css("filter","none");
    
});

// закрыть по клику вне окна
$(document).mouseup(function (e) { 
    var popup = $('.form');
    if (e.target!=popup[0]&&popup.has(e.target).length === 0){
        $('.pop-up').fadeOut();
        $("body>*:not(.pop-up)").css("filter","none");
        
    }
}); 

//header//
// $(window).scroll((function(){
//     if($(window).scrollTop()>1){
//         $(".page-header").addClass("fixed");
//         $(".logo__img-container").addClass("none");
//         $(".toggler").addClass("block");
//         $(".navigation").addClass("none");

//     } else{
//         $(".page-header").removeClass("fixed");
//         $(".logo__img-container").removeClass("none");
//         $(".toggler").removeClass("block");
//         $(".navigation").removeClass("none");
//     }

// }))
 // });

 	//$(document).ready(function () {
   // var form = $('#form_buying_product');
    //console.log(form);
    //form.on('submit', function (e) {
    //    e.preventDefault();
    //    console.log('gygy');
    //    var nmb = $('#number').val();
    //    console.log(nmb);
     //   var submit_btn = $('#submit_btn');
     //   var prod_id = submit_btn.data("prod_id");
     //   var prod_name = submit_btn.data("name");
     //   var prod_price = submit_btn.data("price");
     //   console.log(prod_id);
      //  console.log(prod_name);
      //  console.log(prod_price);
   // });
//


})