$(document).ready(function () {
  
      $( function() {
         // run the currently selected effect
         function runEffect() {
           // get effect type from
           var selectedEffect = "blind"
      
           // Most effect types need no options passed by default
           var options = {};
           // some effects have required parameters
         //   if ( selectedEffect === "scale" ) {
         //     options = { percent: 50 };
         //   } else if ( selectedEffect === "transfer" ) {
         //     options = { to: "#button", className: "ui-effects-transfer" };
         //   } else if ( selectedEffect === "size" ) {
         //     options = { to: { width: 200, height: 60 } };
         //   }
      
           // Run the effect
           $( "#effect" ).toggle( selectedEffect, options, 500 );
         };
      
         // Callback function to bring a hidden box back
         function callback() {
           setTimeout(function() {
             $( "#effect2" ).removeAttr( "style" ).hide().fadeIn();
           }, 1000 );
         };
      
         function runEffect1() {
            var options = {};
            $( "#effect2" ).toggle( "drop", options, 500 );
            
          };
          function runEffect3() {
            var options = {};
            $( "#effect3" ).toggle( "drop", options, 500 );
            
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
         $( "#carrIcon" ).hover(  function() {
            shaker()
          });
       
       } );
   })

