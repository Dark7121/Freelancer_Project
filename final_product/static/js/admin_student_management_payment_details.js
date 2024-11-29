const courses = [
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: 'Course Name'},
    {invoice_id: '#16879', date: 'Jan 19, 2023', student_name:'John Dye', bill_amount:'$500',bill: 'View Bill', description: '1:1 Mentorship'},
];


const rowsPerPage = 10;
let currentPage = 1;

function renderTable() {
    const tableBody = document.querySelector('#paymentTable tbody');
    tableBody.innerHTML = '';

    const start = (currentPage - 1) * rowsPerPage;
    const end = Math.min(start + rowsPerPage, courses.length);

    for (let i = start; i < end; i++) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${courses[i].invoice_id}</td>
            <td>${courses[i].date}</td>
            <td>${courses[i].student_name}</td>
            <td>${courses[i].bill_amount}</td>
            <td class="status"><p class="green-status">${courses[i].bill}</p></td>
            <td>${courses[i].description}</td>
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
            <td><p>-</p></td>
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



