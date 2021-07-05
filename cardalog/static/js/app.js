// FlashMessage Dimiss timeout (3secs)
let flashMessage = document.getElementById("flash-message");

setTimeout(function() { 
   flashMessage.style.display = "none"; 
}, 3000);

// Delete confirm for Set
function deleteConfirmPopUp() {
    let result = confirm('Are you sure you want to delete?');
    return result;
};

let menu = document.getElementById("main-menu");
// Make main-menu toggle by clicking the profile img
document.getElementById("home-profile-img").addEventListener('click', function (e) {
    if (menu.style.display === "none") {
        menu.style.display = "block";
        // button.innerHTML = "Show Menu";
    } else {
        menu.style.display = "none";
        // button.innerHTML = "Hide Menu";
    }
})