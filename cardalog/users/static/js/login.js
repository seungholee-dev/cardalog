
// Reset the Modal when it closes
$('#authModal').on('hide.bs.modal', function () {
    $(this).find()
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

    // Initial visibility set ups for Login / SignUp Modals
    $("#signUpModal").hide();
    $("#resetModal").hide();

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

    $("#resetButton").click(function (e) {
        $("#resetButton").text("Return to Login");
    })
});
