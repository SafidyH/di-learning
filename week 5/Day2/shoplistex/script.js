let shoppingList = [];

function addItem() {
  const inputField = document.getElementById("itemInput");
  const newItem = inputField.value.trim();

  if (newItem !== "") {
    shoppingList.push(newItem);
    inputField.value = "";
    displayList();
  }
}

function clearAll() {
  shoppingList = [];
  displayList();
}

function displayList() {
  const rootDiv = document.getElementById("root");
  rootDiv.innerHTML = "";

  const listUl = document.createElement("ul");
  for (const item of shoppingList) {
    const listItem = document.createElement("li");
    listItem.textContent = item;
    listUl.appendChild(listItem);
  }

  rootDiv.appendChild(listUl);
}

const form = document.createElement("form");
const inputField = document.createElement("input");
inputField.type = "text";
inputField.id = "itemInput";
const addItemBtn = document.createElement("button");
addItemBtn.textContent = "Add Item";
addItemBtn.addEventListener("click", addItem);
const clearAllBtn = document.createElement("button");
clearAllBtn.textContent = "Clear All";
clearAllBtn.addEventListener("click", clearAll);

form.appendChild(inputField);
form.appendChild(addItemBtn);
form.appendChild(clearAllBtn);

const rootDiv = document.getElementById("root");
rootDiv.appendChild(form);