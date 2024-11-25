let groceryList = [];

function addItem() {
  let itemDescription = document.getElementById("new-item").value;
  let itemQuantity = document.getElementById("new-quantity").value;

  if (itemDescription && itemQuantity) {
    groceryList.push({ description: itemDescription, quantity: itemQuantity });

    let list = document.getElementById("grocery-list");
    list.innerHTML = "";

    for (let i = 0; i < groceryList.length; i++) {
      list.innerHTML +=
        "<li>" +
        groceryList[i].description +
        " - " +
        groceryList[i].quantity +
        "</li>";
    }

    // reset input fields
    document.getElementById("new-item").value = "";
    document.getElementById("new-quantity").value = "1";
  }
}
