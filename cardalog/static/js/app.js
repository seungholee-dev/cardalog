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