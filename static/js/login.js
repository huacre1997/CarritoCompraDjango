$(function () {
    $("#btnLogin").on("click",function(){
        $.confirm({
            title: 'Login',
            content: 'URL:login',
            buttons: {
                okButton: {
                     text: 'ok',
                     action: function () {
                     }
                 }
             },
             onContentReady: function () {
                 // when content is fetched & rendered in DOM
         
                    this.buttons.okButton.hide();
                  
             },
            // onContentReady: function () {
            //     // bind to events
            
            // }
        });
        });

 
    
});