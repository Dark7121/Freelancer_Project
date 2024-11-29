
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

function addSuspendListeners() {
    const buttons2 = document.querySelectorAll(".suspend");
    buttons2.forEach((button, index) => {
        button.addEventListener('click', () => {
            popUpContainer.style.display = "block";
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
};


const createAccountBtn = document.getElementById('createAccountBtn');
const popUpContainer = document.getElementById('popUp-container');
const popUpContainer2 = document.getElementById('add-student-popUp');
const popUpCancelBtn = document.getElementById('popup-cancel-btn');
const popUpCancelBtn2 = document.getElementById('popup-cancel-btn2');
const popUpActiveBtn = document.getElementById('popup-activate-btn');

createAccountBtn.addEventListener('click',()=>{
    popUpContainer2.style.display = "block";
})

popUpCancelBtn.addEventListener('click',()=>{
    popUpContainer.style.display = "none";
})

popUpCancelBtn2.addEventListener('click',()=>{
    popUpContainer2.style.display = "none";
})

popUpActiveBtn.addEventListener('click',()=>{
    popUpContainer2.style.display = "none";
})

document.addEventListener('DOMContentLoaded', (event) => {
    renderTable();
    addSuspendListeners()
});