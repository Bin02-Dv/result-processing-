// Get the modal and buttons
var modal = document.getElementById("myModal");
var openModalBtn = document.getElementById("openModalBtn");
var closeModalBtn = document.getElementById("closeModalBtn");
// var form = document.getElementById("myForm");

// Open the modal
openModalBtn.addEventListener("click", function () {
    modal.style.display = "block";
});

// Close the modal
closeModalBtn.addEventListener("click", function () {
    modal.style.display = "none";
});

// Close the modal when clicking outside the modal content
window.addEventListener("click", function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
});

// Submit form (you can add your form submission logic here)
// form.addEventListener("submit", function (event) {
//     event.preventDefault();
//     alert("Class Information submitted Successfully!");
//     modal.style.display = "none";
// });






