const courses = [
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    {username: "John David - Student", email: '132@gmail.com', view: "View"},
    
];


const rowsPerPage = 10;
let currentPage = 1;

function renderTable() {
    const tableBody = document.querySelector('#activeAccountsTable tbody');
    tableBody.innerHTML = '';

    const start = (currentPage - 1) * rowsPerPage;
    const end = Math.min(start + rowsPerPage, courses.length);

    for (let i = start; i < end; i++) {
        const row = document.createElement('tr');
        row.innerHTML = ` 
            <td>${i + 1}.</td>
            <td>${courses[i].username}</td>
            <td>${courses[i].email}</td>
            <td class="status">
                <button class="green-status">${courses[i].view}</button>
            </td>
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
            <td class="status">-</td>
        `;
        tableBody.appendChild(row);
    }

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


window.onload = function() {
    const pageSelect = document.getElementById('pageSelect');
    const totalPages = Math.ceil(courses.length / rowsPerPage);
    pageSelect.innerHTML = '';

    for (let i = 1; i <= totalPages; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.text = i;
        pageSelect.appendChild(option);
    }

    pageSelect.value = currentPage;
    renderTable();
};
