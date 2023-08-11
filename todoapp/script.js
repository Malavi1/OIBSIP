const inputBox = document.getElementById("input-box");
const unChecked = document.getElementById("unchecked");
function saveTask() {
  if (inputBox.value === "") {
    alert("You must add something");
  } else {
    let li = document.createElement("li");
    li.innerHTML = inputBox.value;
    unChecked.appendChild(li);
    let span = document.createElement("span");
    span.innerHTML = "\u00d7";
    li.appendChild(span);
  }
  inputBox.value = "";
}
