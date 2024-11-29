const ctx = document.getElementById("revenueChart").getContext("2d");
const revenueData = {
  labels: ["Apr 01", "Apr 10", "Apr 20", "Apr 31"],
  datasets: [
    {
      label: "Revenue",
      data: [
        45000, 47000, 50000, 52000, 48000, 47000, 51749, 49000, 46000, 52000,
        50000, 53000, 47000, 48000, 49000, 47000, 45000, 46000, 48000, 49000,
        47000, 45000, 46000, 48000, 49000, 47000, 45000, 46000, 48000, 49000,
        47000,
      ],
      borderColor: "green",
      fill: false,
      pointHoverRadius: 7,
      pointHoverBackgroundColor: "black",
      pointHoverBorderColor: "black",
      pointHoverBorderWidth: 2,
      pointRadius: 3,
    },
  ],
};

const revenueChart = new Chart(ctx, {
  type: "line",
  data: revenueData,
  options: {
    responsive: true,
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: function (value) {
            if (value === 0) return "0";
            if (value >= 1000000) return value / 1000000 + "m";
            if (value >= 1000) return value / 1000 + "k";
            return value;
          },
        },
      },
      x: {
        grid: {
          display: false,
        },
      },
    },
    plugins: {
      tooltip: {
        callbacks: {
          label: function (context) {
            return `${context.raw} on ${context.label}`;
          },
        },
      },
      legend: {
        display: false,
      },
    },
    elements: {
      line: {
        tension: 0.4,
      },
    },
  },
});

// Tasks
document.addEventListener("DOMContentLoaded", (event) => {
  const popupButton = document.getElementById("createPostBtn");
  const popup = document.getElementById("popup");
  const closeButton = document.querySelector(".close1");

  popupButton.addEventListener("click", () => {
    popup.style.display = "flex";
  });

  closeButton.addEventListener("click", () => {
    popup.style.display = "none";
  });

  window.addEventListener("click", (event) => {
    if (event.target === popup) {
      popup.style.display = "none";
    }
  });
});

// script.js community

document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("modal2");
  const closeBtn = document.querySelector(".close22");
  const discussionTitle = document.getElementById("discussion-title22");
  const discussionText = document.getElementById("discussion-text22");

  document.querySelectorAll(".dis-cuss .click-open").forEach((row) => {
    row.addEventListener("click", () => {
      const id = row.getAttribute("data-id");
      discussionTitle.textContent = `Discussion ${id}`;
      modal.style.display = "block";
    });
  });

  closeBtn.onclick = () => {
    modal.style.display = "none";
  };

  window.onclick = (event) => {
    if (event.target === modal) {
      modal.style.display = "none";
    }
  };

  const likeLink = document.querySelector(".like-link");
  const dislikeLink = document.querySelector(".dislike-link");
  const shareLink = document.querySelector(".share-link");

  likeLink.addEventListener("click", (e) => {
    e.preventDefault();
    likeLink.classList.toggle("active");
    dislikeLink.classList.remove("active");
  });

  dislikeLink.addEventListener("click", (e) => {
    e.preventDefault();
    dislikeLink.classList.toggle("active");
    likeLink.classList.remove("active");
  });

  shareLink.addEventListener("click", (e) => {
    e.preventDefault();
    if (navigator.share) {
      navigator
        .share({
          title: "Share Discussion",
          text: "Check out this discussion!",
          url: window.location.href,
        })
        .then(() => console.log("Successful share"))
        .catch((error) => console.log("Error sharing", error));
    } else {
      alert("Share functionality not supported in this browser.");
    }
  });
});

// payout statement popup modal

document.addEventListener("DOMContentLoaded", (event) => {
  // Get the modal
  var modal = document.getElementById("modal");

  // Get the <span> element that closes the modal
  var span = document.getElementsByClassName("close-btn")[0];

  // When the user clicks on any table cell, open the modal
  document
    .querySelectorAll(
      ".dashboard-payout-tablee th, .dashboard-payout-tablee td"
    )
    .forEach((cell) => {
      cell.addEventListener("click", () => {
        modal.style.display = "block";
      });
    });

  // When the user clicks on <span> (x), close the modal
  span.onclick = function () {
    modal.style.display = "none";
  };

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function (event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  };
});

// sidebar
function toggleMenu(element) {
  var submenu = element.querySelector("ul");
  submenu.style.display =
    submenu.style.display === "none" || submenu.style.display === ""
      ? "block"
      : "none";
}
