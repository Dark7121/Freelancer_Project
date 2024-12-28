const courses2 = [
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16807',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16997',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16937',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16897',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16867',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16787',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16947',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16987',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16837',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16997',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16917',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16797',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16887',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16857',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16957',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16877',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16947',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16787',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16767',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16777',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16817',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
    {code_name:'#16717',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', student_name: 'John Dye', email:"john@gmail.com", bill_amount:"₹500" , status: 'View Bill'},
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
            <td>${sortedCourses2[i].code_name}</td>
            <td>${sortedCourses2[i].valid_from}</td>
            <td>${sortedCourses2[i].valid_to}</td>
            <td>${sortedCourses2[i].student_name}</td>
            <td>${sortedCourses2[i].email}</td>
            <td>${sortedCourses2[i].bill_amount}</td>
            <td>
                <div class="p_container">
                    <p class="green_status">${sortedCourses2[i].status}</p>
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
        currentPage2++;
        renderTable2();
    }
}

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


function sortTable() {
    const sortSelect = document.getElementById('sortSelect').value;
    var select = document.getElementById('sortSelect');
            var value = select.value;
            console.log('Selected value:', value);
    if (sortSelect === 'voucher') {
        sortedCourses2.sort((a, b) => a.code_name.localeCompare(b.code_name));
    } else {
        sortedCourses2 = [...courses2]; // Reset to original order if "Default" is selected
    }
    currentPage2 = 1; // Reset to first page
    renderTable2();
}

document.querySelector('.custom-select').addEventListener('change', function() {
    console.log(this.value); // Do something with the selected value
});
