// graph
const ctx = document.getElementById("myChart").getContext("2d");
const myChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: ["A", "B", "C", "D", "E", "F", "G"],
    datasets: [
      {
        label: "Lorem",
        data: [12000, 19000, 3000, 5000, 20000, 30000, 45000],
        borderColor: "rgba(255, 99, 132, 1)",
        backgroundColor: "rgba(255, 99, 132, 0.2)",
        fill: false,
        tension: 0.4,
      },
      {
        label: "Lorem",
        data: [10000, 15000, 25000, 35000, 22000, 29000, 40000],
        borderColor: "rgba(54, 162, 235, 1)",
        backgroundColor: "rgba(54, 162, 235, 0.2)",
        fill: false,
        tension: 0.4,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          callback: function (value) {
            return value >= 1000 ? value / 1000 + "k" : value;
          },
        },
      },
    },
  },
});

// pie chart
const ctx1 = document.getElementById("myPieChart").getContext("2d");
const myPieChart = new Chart(ctx1, {
  type: "pie",
  data: {
    labels: ["Option A", "Option B", "Option C", "Option D"],
    datasets: [
      {
        data: [29, 35, 14, 22],
        backgroundColor: [
          "rgba(255, 99, 132, 1)", // Option A
          "rgba(54, 162, 235, 1)", // Option B
          "rgba(75, 192, 192, 1)", // Option C
          "rgba(255, 205, 86, 1)", // Option D
        ],
        borderWidth: 1,
      },
    ],
  },
  options: {
    plugins: {
      legend: {
        display: false,
      },
    },
  },
});

// Generate labels dynamically
const labels = [
  { color: "rgba(255, 99, 132, 1)", text: "Option A: 29%" },
  { color: "rgba(54, 162, 235, 1)", text: "Option B: 35%" },
  { color: "rgba(75, 192, 192, 1)", text: "Option C: 14%" },
  { color: "rgba(255, 205, 86, 1)", text: "Option D: 22%" },
];

const labelsContainer = document.getElementById("chartLabels");
labels.forEach((label) => {
  const p = document.createElement("p");
  p.style.color = label.color;
  p.textContent = label.text;
  labelsContainer.appendChild(p);
});

// quiz marks

document.addEventListener("DOMContentLoaded", function () {
  var modal = document.getElementById("my-customResultModal");
  var span = document.getElementsByClassName("my-custom-close")[0];
  var resultDetails = document.getElementById("my-customResultDetails");

  // Filter dropdown
  var filterButton = document.querySelector(".my-filter-button");
  var filterDropdown = document.querySelector(".my-filter-dropdown");

  filterButton.addEventListener("click", function (event) {
    event.stopPropagation();
    filterDropdown.style.display =
      filterDropdown.style.display === "block" ? "none" : "block";
  });

  window.onclick = function (event) {
    if (
      !event.target.matches(".my-filter-button") &&
      !event.target.matches(".filter-icon")
    ) {
      if (filterDropdown.style.display === "block") {
        filterDropdown.style.display = "none";
      }
    }
  };

  // Sorting function
  document
    .querySelectorAll(".my-filter-dropdown a")
    .forEach(function (element) {
      element.addEventListener("click", function (event) {
        event.preventDefault();
        var sortType = this.getAttribute("data-sort");
        sortTable(sortType);
      });
    });

  function sortTable(sortType) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.querySelector(".my-custom-table tbody");
    switching = true;

    while (switching) {
      switching = false;
      rows = table.rows;

      for (i = 0; i < rows.length - 1; i++) {
        shouldSwitch = false;

        x = rows[i].getElementsByTagName("TD")[1];
        y = rows[i + 1].getElementsByTagName("TD")[1];

        if (
          sortType === "marks-asc" &&
          parseInt(x.innerHTML.split("/")[0]) >
            parseInt(y.innerHTML.split("/")[0])
        ) {
          shouldSwitch = true;
          break;
        } else if (
          sortType === "marks-desc" &&
          parseInt(x.innerHTML.split("/")[0]) <
            parseInt(y.innerHTML.split("/")[0])
        ) {
          shouldSwitch = true;
          break;
        }

        x = rows[i].getElementsByTagName("TD")[3];
        y = rows[i + 1].getElementsByTagName("TD")[3];

        if (
          sortType === "date-latest" &&
          new Date(x.innerHTML) < new Date(y.innerHTML)
        ) {
          shouldSwitch = true;
          break;
        } else if (
          sortType === "date-oldest" &&
          new Date(x.innerHTML) > new Date(y.innerHTML)
        ) {
          shouldSwitch = true;
          break;
        }
      }

      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
      }
    }
  }
});
