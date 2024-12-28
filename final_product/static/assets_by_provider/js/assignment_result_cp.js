// sidebar dropdown

document.querySelectorAll(".menu-button1").forEach((button) => {
  button.addEventListener("click", () => {
    button.classList.toggle("active");
    const dropdownContent = button.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
});

function goBack() {
  window.history.back();
}

// graph line

document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM fully loaded and parsed");

  document.querySelectorAll(".dropdown-content a").forEach(function (link) {
    link.addEventListener("click", function (event) {
      console.log("Selected:", event.target.textContent);
      // You can add functionality here to update the chart based on the selection
    });
  });
});
