// FlashMessage Dimiss timeout (3secs)
let flashMessage = document.getElementById("flash-message");

setTimeout(function() { 
   flashMessage.style.display = "none"; 
}, 3000);

// Jquery for Login Modal (AJAX)
// With your other jQuery, or in some other script
$('#loginModal').ready(function(){
    console.log('it worked');
    // On form submit, do ajax instead
    $("#login-form").submit(function(e){
        var loginUrl = $(this).attr('action');
        var loginData = $(this).serialize();
        $.post(loginUrl, loginData).done(function(data){

            if (data.status == 'ok'){
            // print "success" on the html somewhere
                console.log(data.status);
                
                // Refresh the page
                window.location.reload();

            // Something is wrong with the credential
            } else {
                console.log(data.status);
                $('#login-error-text').css('visibility', 'visible');
            }
        });
        e.preventDefault(); // This stops page reload
    });
});

// Delete confirm for Global (Used in Set)
function deleteConfirmPopUp() {
    let result = confirm('Are you sure you want to delete?');
    return result;
};

let menu = document.getElementById("main-menu");
// Make main-menu toggle by clicking the profile img
document.getElementById("home-profile-img").addEventListener('click', function (e) {
    if (menu.style.display === "none") {
        menu.style.display = "block";
    } else {
        menu.style.display = "none";
    }
})
