
// Reset the Modal when it closes
$('#authModal').on('hidden.bs.modal', function () {
    // Reset Form data (Text fields)
    $(this).find('form').trigger('reset');
    
    // Reset to Initial visibility set ups for Login / SignUp Modals
    modalInitialSetUp();
})

// Login Modal (AJAX) Login request
$("#authModal").ready(function () {
    // On form submit, do ajax instead
    $("#login-form").submit(function (e) {
        var loginUrl = $(this).attr("action");
        var loginData = $(this).serialize();
        console.log(loginData);
        $.post(loginUrl, loginData).done(function (data) {
            if (data.status == "ok") {
                // print "success" on the html somewhere
                console.log(data.status);

                // Refresh the page
                window.location.reload();
                // Something iss wrong with the credential
            } else {
                console.log(data.status);
                $("#login-error-text").css("visibility", "visible");
            }
        });
        e.preventDefault(); // This stops page reload
    });

    modalInitialSetUp();

    // Toggle Sign up text
    $("#toggleSignUp").click(function (e) {
        $("#loginModal").hide();
        $("#signUpModal").show();
    });

    // Toggle Reset Email text
    $("#toggleReset").click(function (e) {
        $("#loginModal").hide();
        $("#resetModal").show();
    });

    // Reset Email button
    $("#resetForm").submit(function (e) {
        var resetUrl = $(this).attr("action");
        var resetEmail = $(this).serialize();
        // console.log(resetEmail)
        // $.post(resetUrl, resetEmail).done(function (data) {
        //     console.log(data);
        // })
    });
});

// Initial visibility set ups for Login / SignUp Modals
let modalInitialSetUp = () => {
    $('#loginModal').show();
    $("#signUpModal").hide();
    $("#resetModal").hide();
}