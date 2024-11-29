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

// sidebar
function toggleMenu(element) {
  var submenu = element.querySelector("ul");
  submenu.style.display =
    submenu.style.display === "none" || submenu.style.display === ""
      ? "block"
      : "none";
}
