const sidebarItems = document.querySelectorAll(".sidebar-item");
const iframe = document.getElementById("contentFrame");

sidebarItems.forEach(item => {
  item.addEventListener("click", function() {
    // Remove active class from all sidebar items
    sidebarItems.forEach(i => i.classList.remove('active'));
    // Add active class to the clicked sidebar item
    item.classList.add('active');

    // Set iframe source
    const page = item.getAttribute('data-page');
    iframe.src = page;

    // Hide all dropdowns except the clicked one
    sidebarItems.forEach(i => {
      if (i !== item) {
        const dropdownContent = i.querySelector(".dropdown-content");
        const iconArrow = i.querySelector(".icon-arrow");
        if (dropdownContent) dropdownContent.style.display = "none";
        if (iconArrow) {
          iconArrow.classList.remove("up-arrow");
          iconArrow.classList.add("down-arrow");
        }
      }
    });

    // Toggle sidebar and navbar for support-panel
    if (item.id === "support-panel") {
      document.querySelector(".container").classList.add("container-shrink");
      document.querySelector(".teachers-navbar").classList.add("hidden");
      document.querySelector(".sidebar").classList.add("shrink");
    } else {
      document.querySelector(".container").classList.remove("container-shrink");
      document.querySelector(".teachers-navbar").classList.remove("hidden");
      document.querySelector(".sidebar").classList.remove("shrink");
    }
  });
});

// Handle dropdown functionality
const dropdowns = document.querySelectorAll(".dropdown");
dropdowns.forEach(dropdown => {
  dropdown.addEventListener("click", function(event) {
    event.stopPropagation(); // Prevent the click event from bubbling up
    const dropdownContent = this.querySelector(".dropdown-content");
    const iconArrow = this.querySelector(".icon-arrow");
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
      iconArrow.classList.remove("up-arrow");
      iconArrow.classList.add("down-arrow");
    } else {
      dropdownContent.style.display = "block";
      iconArrow.classList.remove("down-arrow");
      iconArrow.classList.add("up-arrow");
    }
    this.classList.toggle("open");
  });
});

// Handle dropdown item clicks
const dropdownItems = document.querySelectorAll(".dropdown-content li");
dropdownItems.forEach(dropdownItem => {
  dropdownItem.addEventListener("click", function(event) {
    event.stopPropagation();
    const page = this.getAttribute("data-page");
    iframe.src = page;

    // Remove active class from all sidebar items except the parent
    sidebarItems.forEach(i => {
      if (!i.contains(this)) {
        i.classList.remove("active");
        const dropdownContent = i.querySelector(".dropdown-content");
        const iconArrow = i.querySelector(".icon-arrow");
        if (dropdownContent) dropdownContent.style.display = "none";
        if (iconArrow) {
          iconArrow.classList.remove("up-arrow");
          iconArrow.classList.add("down-arrow");
        }
      }
    });

    // Add active class to parent list item
    const parentItem = this.closest(".sidebar-item");
    parentItem.classList.add("active");
  });
});

