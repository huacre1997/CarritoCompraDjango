$(document).ready(function () {
  
      $( function() {
         function runEffect() {
           var selectedEffect = "blind"
      
           var options = {};
      
           $( "#effect" ).toggle( selectedEffect, options, 500 );
         };
      
    
         function runEffect1() {
            var options = {};
            $( "#effect2" ).toggle( "drop", options, 500 );
            
          };
          function runEffect3() {
            var options = {};
            $( "#effect3" ).toggle( "drop", options, 500 );
            
          };
          function slideEffectOptionUser() {
            var selectedEffect = "blind"
      
           var options = {};
      
           $( "#showOptionUsers" ).toggle( selectedEffect, options, 500 );
            
          };
       function shaker(){
         var options = {
            easing:"linear"
         };

         $( "#carrIcon" ).effect( "bounce",options,500 );         

       }
         $( "#carr" ).on( "click", function() {
           runEffect();
           runEffect1();
            runEffect3()
         });
         $( "#userOptions" ).on( "click", function() {
           slideEffectOptionUser()
        });
         $( "#carrIcon" ).hover(  function() {
            shaker()
          });
       
       } );
   })

