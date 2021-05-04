// suppose the `id` attribute of element is `message_container`.
var flashMessage = document.getElementById("flash-message");

setTimeout(function() { 
   flashMessage.style.display = "none"; 
}, 3000);
// Timeout is 3 sec, you can change it