document.addEventListener("DOMContentLoaded", () => {
  const bankNameInput = document.getElementById("bank-name");
  const accountHolderNameInput = document.getElementById("account-holder-name");
  const branchCodeInput = document.getElementById("branch-code");
  const accountNumberInput = document.getElementById("account-number");
  const cardName = document.getElementById("card-name");
  const cardNumber = document.getElementById("card-number");

  accountHolderNameInput.addEventListener("input", () => {
    cardName.textContent = accountHolderNameInput.value || "Hasan";
  });

  accountNumberInput.addEventListener("input", () => {
    cardNumber.textContent = accountNumberInput.value || "1200 01452 54215";
  });
});
