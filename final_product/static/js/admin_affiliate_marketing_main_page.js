const activeAccounts =  JSON.parse(document.getElementById('active-accounts-data').textContent);
const suspendedAccounts =  JSON.parse(document.getElementById('suspended-accounts-data').textContent);

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
            <td>${activeAccounts[i].name}</td>
            <td>${activeAccounts[i].email_id}</td>
            <td>${activeAccounts[i].phone_number}</td>
            <td>${activeAccounts[i].date_of_creation}</td>
            <td>${activeAccounts[i].total_enrollment_count}</td>
            <td class="actions">
                <p class="details">${activeAccounts[i].detail}</p>
                <p class="edit">${activeAccounts[i].edit}</p>
                <button class="suspend" data-index="${i}">${activeAccounts[i].suspend}</button>
            </td>
        `;
        tableBody.appendChild(row);
    }

    // Add empty rows if fewer than 10 rows are present
    for (let i = end; i < start + rowsPerPage; i++) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td></td>
            <td class="actions"></td>
        `;
        tableBody.appendChild(row);
    }

    document.getElementById('currentPage').innerText = `Page ${currentPage} of ${Math.ceil(activeAccounts.length / rowsPerPage)}`;
    addSuspendListeners()
}

const rowsPerPage2 = 10;
let currentPage2 = 1;

function renderTable2() {
    
    const tableBody2 = document.querySelector('#suspendedAccountsTable tbody');
    tableBody2.innerHTML = '';

    
    const start2 = (currentPage2 - 1) * rowsPerPage2;
    const end2 = Math.min(start2 + rowsPerPage2, courses2.length);

    
    for (let i = start2; i < end2; i++) {
        const row2 = document.createElement('tr');
        row2.innerHTML = ` 
            <td>${suspendedAccounts[i].name}</td>
            <td>${suspendedAccounts[i].email_id}</td>
            <td>${suspendedAccounts[i].phone_number}</td>
            <td>${suspendedAccounts[i].date_of_creation}</td>
            <td>${suspendedAccounts[i].total_enrollment_count}</td>
            <td class="actions">
                <p class="details">${suspendedAccounts[i].detail}</p>
                <p class="edit">${suspendedAccounts[i].edit}</p>
                <button class="activate" data-index="${i}">${suspendedAccounts[i].activate}</button>
            </td>
        `;
        tableBody2.appendChild(row2);
    }

    // Add empty rows if fewer than 10 rows are present
    for (let i = end2; i < start2 + rowsPerPage2; i++) {
        const row2 = document.createElement('tr');
        row2.innerHTML = `
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td>-</td>
            <td class="actions">-</td>
        `;
        tableBody2.appendChild(row2);
    }
    document.getElementById('currentPage2').innerText = `Page ${currentPage2} of ${Math.ceil(suspendedAccounts.length / rowsPerPage2)}`;
    addActivateListeners();
}


function nextPage() {
    const totalPages = Math.ceil(activeAccounts.length / rowsPerPage);
    if (currentPage < totalPages) {
        currentPage++;
        renderTable();
    }
}
function nextPage2() {
    const totalPages2 = Math.ceil(suspendedAccounts.length / rowsPerPage2);
    if (currentPage2 < totalPages2) {
        currentPage2++;
        renderTable2();
    }
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        renderTable();
    }
}

function prevPage2() {
    if (currentPage2 > 1) {
        currentPage2--;
        renderTable2();
    }
}

function changePage() {
    const pageSelect = document.getElementById('pageSelect');
    currentPage = parseInt(pageSelect.value);
    renderTable();
}

function changePage2() {
    const pageSelect2= document.getElementById('pageSelect2');
    currentPage2 = parseInt(pageSelect2.value);
    renderTable2();
}

function addSuspendListeners() {
    const buttons = document.querySelectorAll(".suspend");
    buttons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const index = event.target.getAttribute('data-index');
            console.log(`Suspend clicked for row index: ${index}`);
            popUpContainer.style.display = "block";
        });
    });
}

function addActivateListeners() {
    const buttons = document.querySelectorAll(".activate");
    buttons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const index = event.target.getAttribute('data-index');
            console.log(`Activate clicked for row index: ${index}`);
            popUpContainer2.style.display = "block";
        });
    });
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

    const pageSelect2 = document.getElementById('pageSelect2');
    const totalPages2 = Math.ceil(courses2.length / rowsPerPage2);
    pageSelect2.innerHTML = '';

    for (let i = 1; i <= totalPages2; i++) {
        const option = document.createElement('option');
        option.value = i;
        option.text = i;
        pageSelect2.appendChild(option);
    }

    pageSelect2.value = currentPage2;
    renderTable2();
};


const suspendBtn = document.getElementById('suspendAccountBtn');
const activateBtn = document.getElementById('activateAccountBtn');
const popUpContainer = document.getElementById('popUp-container');
const popUpContainer2 = document.getElementById('popUp-container2');
const popUpCancelBtn = document.getElementById('popup-cancel-btn');
const popUpCancelBtn2 = document.getElementById('popup-cancel-btn2');

suspendBtn.addEventListener('click',()=>{
    popUpContainer.style.display = "block";
})

activateBtn.addEventListener('click',()=>{
    popUpContainer2.style.display = "block";
})  

popUpCancelBtn.addEventListener('click',()=>{
    popUpContainer.style.display = "none";
})

popUpCancelBtn2.addEventListener('click',()=>{
    popUpContainer2.style.display = "none";
})

document.addEventListener('DOMContentLoaded', (event) => {
    renderTable();
    renderTable2();
    addActivateListeners();
    addSuspendListeners()
});