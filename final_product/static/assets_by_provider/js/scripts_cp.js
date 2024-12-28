// const ctx = document.getElementById("revenueChart").getContext("2d");
// const revenueChart = new Chart(ctx, {
//   type: "line",
//   data: {
//     labels: ["Apr 01", "Apr 07", "Apr 10", "Apr 20", "Apr 31"],
//     datasets: [
//       {
//         label: "Revenue",
//         data: [40000, 51749, 45000, 50000, 47000],
//         borderColor: "rgba(0, 200, 83, 1)",
//         backgroundColor: "rgba(0, 200, 83, 0.1)",
//         fill: true,
//         tension: 0.4,
//       },
//     ],
//   },
//   options: {
//     responsive: true,
//     scales: {
//       y: {
//         beginAtZero: true,
//         max: 100000,
//       },
//     },
//   },
// });

//  After Payout and course overview
document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("modal");
  const closeButton = document.querySelector(".close-button");
  const invoiceLinks = document.querySelectorAll(".invoice-link");

  invoiceLinks.forEach((link) => {
    link.addEventListener("click", (event) => {
      event.preventDefault();

      const row = link.closest("tr");
      const sno = row.querySelector("td:first-child").textContent;
      const invoice = row.querySelector("td:nth-child(2)").textContent;
      const user = row.querySelector("td:nth-child(3)").textContent;
      const enrollments = row.querySelector("td:nth-child(6)").textContent;
      const enrollmentNo = row.getAttribute("data-enrollment-no").split(",");
      const perShare = row.querySelector("td:nth-child(7)").textContent;
      const amount = row.querySelector("td:nth-child(8)").textContent;

      document.getElementById("modal-sno").textContent = sno;
      document.getElementById("modal-invoice").textContent = invoice;
      document.getElementById("modal-user").textContent = user;
      document.getElementById("modal-enrollments").textContent = enrollments;

      const modalEnrollmentNo = document.getElementById("modal-enrollment-no");
      modalEnrollmentNo.innerHTML = "";
      enrollmentNo.forEach((item) => {
        const [code, date] = item.split(" ");
        const p = document.createElement("p");
        p.textContent = `${code} ${date}`;
        modalEnrollmentNo.appendChild(p);
      });

      document.getElementById("modal-per-share").textContent = perShare;
      document.getElementById("modal-amount").textContent = amount;

      modal.style.display = "block";
    });
  });

  closeButton.addEventListener("click", () => {
    modal.style.display = "none";
  });

  window.addEventListener("click", (event) => {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  });
});
