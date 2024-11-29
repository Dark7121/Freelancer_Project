const courses2 = [
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
    {student_name: 'John Dye', email:"john@gmail.com", date: 'Jan 19,2024 ', result: '30/60', action:"Add Comment"},
];

const rowsPerPage2 = 7;
let currentPage2 = 1;
let sortedCourses2 = [...courses2];

function renderTable2() {
    const tableBody = document.querySelector('#referralTable2 tbody');
    tableBody.innerHTML = '';

    const start2 = (currentPage2 - 1) * rowsPerPage2;
    const end2 = Math.min(start2 + rowsPerPage2, sortedCourses2.length);

    for (let i = start2; i < end2; i++) {
        const row2 = document.createElement('tr');
        row2.innerHTML = `
            <td>${sortedCourses2[i].student_name}</td>
            <td>${sortedCourses2[i].email}</td>
            <td>${sortedCourses2[i].date}</td>
            <td>${sortedCourses2[i].result}</td>
            <td>
                <div class="p_container">
                    <p class="green_status">${sortedCourses2[i].action}</p>
                </div>
            </td>
        `;
        tableBody.appendChild(row2);
    }

    // Add empty rows if fewer than rowsPerPage are present
    for (let i = end2; i < start2 + rowsPerPage2; i++) {
        const row2 = document.createElement('tr');
        row2.innerHTML = `
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td><div class="p_container">-</div></td>
        `;
        tableBody.appendChild(row2);
    }

    const totalPages2 = Math.ceil(sortedCourses2.length / rowsPerPage2);
    const pageSelect2 = document.getElementById('pageSelect2');
    pageSelect2.innerHTML = ''; // Clear existing options

    for (let i = 1; i <= totalPages2; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        pageSelect2.appendChild(option);
    }

    pageSelect2.value = currentPage2; // Set the current page
    document.getElementById('totalCourses').innerText = `Total Course Enrollments: ${sortedCourses2.length}`;
    document.getElementById('currentPage2').innerText = `Page ${currentPage2} of ${totalPages2}`;
}

function nextPage2() {
    const totalPages2 = Math.ceil(sortedCourses2.length / rowsPerPage2);
    if (currentPage2 < totalPages2) {
   result: '30/60',      currentPage2++;
}}

function prevPage2() {
    if (currentPage2 > 1) {
        currentPage2--;
        renderTable2();
    }
}

function changePage2() {
    const pageSelect2 = document.getElementById('pageSelect2');
    currentPage2 = parseInt(pageSelect2.value);
    renderTable2();
}

window.onload = function() {
    renderTable2();
};
