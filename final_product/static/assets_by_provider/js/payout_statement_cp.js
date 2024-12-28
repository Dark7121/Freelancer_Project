document.getElementById("export-btn").addEventListener("click", function () {
  const fileName = "example.txt"; // Specify the file name here
  const fileContent = "This is a sample file content."; // Specify the file content here

  const blob = new Blob([fileContent], { type: "text/plain" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = fileName;
  document.body.appendChild(a);
  a.click();

  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});

// after payment link
const data = [
  {
    sno: 1,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 2,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 3,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 4,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 5,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 6,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 7,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 8,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 9,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 10,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 11,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sno: 12,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial intelligence",
    enrollments: "5 users",
    perShare: "$50",
    amount: "$35",
  },
];

const rowsPerPage = 6;
let currentPage = 1;

const tableBody = document.getElementById("tableBody");
const resultsCount = document.getElementById("resultsCount");
const pageSelect = document.getElementById("pageSelect");
const pageInfo = document.getElementById("pageInfo");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

function renderTable(page) {
  tableBody.innerHTML = "";
  const start = (page - 1) * rowsPerPage;
  const end = start + rowsPerPage;
  const paginatedItems = data.slice(start, end);

  paginatedItems.forEach((item) => {
    const row = `
      <tr>
        <td>${item.sno}</td>
        <td>${item.invoiceNo}</td>
        <td>${item.name}</td>
        <td>${item.month}</td>
        <td>${item.courseName}</td>
        <td>${item.enrollments}</td>
        <td>${item.perShare}</td>
        <td>${item.amount}</td>
    <td><button class="view-proof-btn" onclick="viewProof(${item.sno})">View proof</button></td>
        <td><button class="view-bill-btn" onclick="viewBill(${item.sno})">View bill</button></td>
      </tr>
    `;
    tableBody.innerHTML += row;
  });

  resultsCount.textContent = `${data.length} Results`;
  pageInfo.textContent = `of ${Math.ceil(data.length / rowsPerPage)} pages`;

  updatePagination();
}

function updatePagination() {
  pageSelect.innerHTML = "";
  const totalPages = Math.ceil(data.length / rowsPerPage);
  for (let i = 1; i <= totalPages; i++) {
    const option = document.createElement("option");
    option.value = i;
    option.textContent = i;
    pageSelect.appendChild(option);
  }
  pageSelect.value = currentPage;
}

function viewProof(sno) {
  alert(`View proof for S.No ${sno}`);
}

function viewBill(sno) {
  alert(`View bill for S.No ${sno}`);
}

prevBtn.addEventListener("click", () => {
  if (currentPage > 1) {
    currentPage--;
    renderTable(currentPage);
  }
});

nextBtn.addEventListener("click", () => {
  const totalPages = Math.ceil(data.length / rowsPerPage);
  if (currentPage < totalPages) {
    currentPage++;
    renderTable(currentPage);
  }
});

pageSelect.addEventListener("change", (e) => {
  currentPage = parseInt(e.target.value, 10);
  renderTable(currentPage);
});

// Initial render
renderTable(currentPage);

// Pending Payments

const data2 = [
  {
    sNo: 1,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 2,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 3,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 4,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 5,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 6,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 7,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 8,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 9,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 10,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 11,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 12,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 13,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 14,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
  {
    sNo: 15,
    invoiceNo: "#16879",
    name: "John Dye",
    month: "Mar, 2023",
    courseName: "Artificial Intelligence",
    enrollments: "500 users",
    perShare: "$50",
    amount: "$35",
  },
];

let currentPage2 = 1;
const rowsPerPage2 = 13;

function displayTable(page) {
  const tableBody = document.getElementById("table-body2");
  tableBody.innerHTML = "";
  const start = (page - 1) * rowsPerPage2;
  const end = start + rowsPerPage2;
  const paginatedItems = data2.slice(start, end);

  paginatedItems.forEach((item) => {
    const row = `<tr>
                      <td>${item.sNo}</td>
                      <td>${item.invoiceNo}</td>
                      <td>${item.name}</td>
                      <td>${item.month}</td>
                      <td>${item.courseName}</td>
                      <td>${item.enrollments}</td>
                      <td>${item.perShare}</td>
                      <td>${item.amount}</td>
                   </tr>`;
    tableBody.innerHTML += row;
  });

  document.getElementById(
    "results-info2"
  ).innerText = ` ${data2.length} Results`;
}

function prevPage() {
  if (currentPage2 > 1) {
    currentPage2--;
    displayTable(currentPage2);
  }
}

function nextPage() {
  if (currentPage2 * rowsPerPage2 < data2.length) {
    currentPage2++;
    displayTable(currentPage2);
  }
}

window.onload = () => {
  displayTable(currentPage2);
};
