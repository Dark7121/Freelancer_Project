const courses = [
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
    {name: 'John Dye', mail: 'John56@gmail.com', referral_count: '300',bonus: '$250'},
];


const rowsPerPage = 10;
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
            <td>${courses[i].name}</td>
            <td>${courses[i].mail}</td>
            <td>${courses[i].referral_count}</td>
            <td>${courses[i].bonus}</td>
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



