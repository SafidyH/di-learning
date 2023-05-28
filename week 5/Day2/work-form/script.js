const form = document.getElementById("myForm");
    console.log(form);

    const firstNameInput = document.getElementById("fname");
    const lastNameInput = document.getElementById("lname");
    console.log(firstNameInput);
    console.log(lastNameInput);

    const submitButton = document.getElementById("submit");
    submitButton.addEventListener("click", function(event) {
      event.preventDefault();

      const firstNameValue = firstNameInput.value;
      const lastNameValue = lastNameInput.value;

      if (firstNameValue.trim() !== "" && lastNameValue.trim() !== "") {
        const usersAnswerList = document.querySelector(".usersAnswer");

        const firstNameItem = document.createElement("li");
        firstNameItem.textContent = firstNameValue;

        const lastNameItem = document.createElement("li");
        lastNameItem.textContent = lastNameValue;

        usersAnswerList.appendChild(firstNameItem);
        usersAnswerList.appendChild(lastNameItem);
      }
    });