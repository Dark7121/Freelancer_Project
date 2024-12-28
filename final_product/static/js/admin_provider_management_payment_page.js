const courses = [
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
    {ivoice: "#16879", name: 'John Dye', month: "Mar, 2023", course: 'Artificial Intelligence', no_of_enrollment: '500 Users',per_share: '$30',amount: '$35', pay: "Pay"},
];


const rowsPerPage = 6;
let currentPage = 1;

function renderTable() {
    const tableBody = document.querySelector('#referralTable tbody');
    tableBody.innerHTML = '';

    const start = (currentPage - 1) * rowsPerPage;
    const end = Math.min(start + rowsPerPage, courses.length);

    for (let i = start; i < end; i++) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${i + 1}.</td>
            <td>${courses[i].ivoice}</td>
            <td>${courses[i].name}</td>
            <td>${courses[i].month}</td>
            <td>${courses[i].course}</td>
            <td>${courses[i].no_of_enrollment}</td>
            <td>${courses[i].per_share}</td>
            <td>${courses[i].amount}</td>
            <td class="status"><p class="green-status">${courses[i].pay}</p></td>
        `;
        tableBody.appendChild(row);
    }

    // Add empty rows if fewer than 10 rows are present
    for (let i = end; i < start + rowsPerPage; i++) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td class="status">-</td>
        `;
        tableBody.appendChild(row);
    }

    document.getElementById('totalCourses').innerText = `Total Course Enrollments: ${courses.length}`;
    document.getElementById('currentPage').innerText = `Page ${currentPage} of ${Math.ceil(courses.length / rowsPerPage)}`;
}

function nextPage() {
    const totalPages = Math.ceil(courses.length / rowsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        renderTable();
    }
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        renderTable();
    }
}

function changePage() {
    const pageSelect = document.getElementById('pageSelect');
    currentPage = parseInt(pageSelect.value);
    renderTable();
}

window.onload = renderTable;



