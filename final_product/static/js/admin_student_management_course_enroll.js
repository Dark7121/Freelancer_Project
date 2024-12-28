const courses = [
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Jan 26, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '70%', enrollment_date: 'Jan 27, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '75%', enrollment_date: 'Jan 28, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '80%', enrollment_date: 'Jan 29, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '85%', enrollment_date: 'Jan 30, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '90%', enrollment_date: 'Jan 31, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '95%', enrollment_date: 'Feb 1, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '100%', enrollment_date: 'Feb 2, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '45%', enrollment_date: 'Feb 3, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '50%', enrollment_date: 'Feb 4, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '55%', enrollment_date: 'Feb 5, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '60%', enrollment_date: 'Feb 6, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
    {name: 'Introduction to Strategic Analysis', completion: '65%', enrollment_date: 'Feb 7, 2023', instructor: 'John Dye'},
];


const rowsPerPage = 10;
let currentPage = 1;

function renderTable() {
    const tableBody = document.querySelector('#courseTable tbody');
    tableBody.innerHTML = '';

    const start = (currentPage - 1) * rowsPerPage;
    const end = Math.min(start + rowsPerPage, courses.length);

    for (let i = start; i < end; i++) {
        const row = document.createElement('tr');
        const completionPercentage = parseInt(courses[i].completion);
        const status = completionPercentage === 100 ? 'Completed' : 'Ongoing';
        const statusClass = status === 'Ongoing' ? 'green-status' : 'purple-status';
        row.innerHTML = `
            <td>${i + 1}</td>
            <td>${courses[i].name}</td>
            <td>${courses[i].completion}</td>
            <td>${courses[i].enrollment_date}</td>
            <td>${courses[i].instructor}</td>
            <td class="status"><p class="${statusClass}">${status}</p></td>
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
            <td class="status"><p>-</p></td>
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



