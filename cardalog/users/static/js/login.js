function onClickRegister() {
}

// Jquery for Login Modal (AJAX)
$('#authModal').ready(function(){
    console.log('it worked');
    // On form submit, do ajax instead
    $("#login-form").submit(function(e){
        var loginUrl = $(this).attr('action');
        var loginData = $(this).serialize();
        console.log(loginData)
        $.post(loginUrl, loginData).done(function(data){
            if (data.status == 'ok'){
                // print "success" on the html somewhere
                console.log(data.status);
                
                // Refresh the page
                window.location.reload();
            // Something iss wrong with the credential
            } else {
                console.log(data.status);
                $('#login-error-text').css('visibility', 'visible');
            }
        });
        e.preventDefault(); // This stops page reload
    });
});

