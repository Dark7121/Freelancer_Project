const courses2 = [
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
    {code_name:'#16907',valid_from:'Dec 10,2023', valid_to: 'Jan 19,2024 ', no_of_voucher: '219', edit: 'Edit', view:"View", stop:"Stop" , status: 'Active'},
];

const rowsPerPage2 = 5;
let currentPage2 = 1;

function renderTable2() {
    const tableBody = document.querySelector('#referralTable2 tbody');
    tableBody.innerHTML = '';

    const start2 = (currentPage2 - 1) * rowsPerPage2;
    const end2 = Math.min(start2 + rowsPerPage2, courses2.length);

    for (let i = start2; i < end2; i++) {
        const row2 = document.createElement('tr');
        row2.innerHTML = `
            <td>${courses2[i].code_name}</td>
            <td>${courses2[i].valid_from}</td>
            <td>${courses2[i].valid_to}</td>
            <td>${courses2[i].no_of_voucher}</td>
            <td>
                <div class="eps_btn_container">
                    <button class="eps_btn">${courses2[i].edit}</button>
                    <button class="eps_btn">${courses2[i].view}</button>
                    <button class="eps_btn">${courses2[i].stop}</button>
                </div>
            </td>
            <td>
                <div class="p_container">
                    <p class="green_status">${courses2[i].status}</p>
                </div>
            </td>
        `;

        row2.onclick = function() {
            goToCoursePage();
        };
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
        `;
        tableBody.appendChild(row2);
    }

    const totalPages2 = Math.ceil(courses2.length / rowsPerPage2);
    const pageSelect2 = document.getElementById('pageSelect2');
    pageSelect2.innerHTML = ''; // Clear existing options

    for (let i = 1; i <= totalPages2; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.textContent = i;
        pageSelect2.appendChild(option);
    }

    pageSelect2.value = currentPage2; // Set the current page

    document.getElementById('currentPage2').innerText = `Page ${currentPage2} of ${totalPages2}`;
}

function nextPage2() {
    const totalPages2 = Math.ceil(courses2.length / rowsPerPage2);
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

