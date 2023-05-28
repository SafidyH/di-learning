function removeColor() {
    const colorSelect = document.getElementById("colorSelect");
    const selectedColorIndex = colorSelect.selectedIndex;
    colorSelect.remove(selectedColorIndex);
  }

  const removeBtn = document.getElementById("removeBtn");
  removeBtn.addEventListener("click", removeColor);