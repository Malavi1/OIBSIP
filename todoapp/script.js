const inputBox = document.getElementById("input-box");
const unChecked = document.getElementById("unchecked");
const checked = document.getElementById("checked");

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

unChecked.addEventListener(
  "click",
  function (e) {
    if (e.target.tagName === "LI") {
      e.target.classList.toggle("checked");

      let li = document.createElement("li");
      li.innerHTML = e.target.textContent;
      checked.appendChild(li);
    } else if (e.target.tagName === "SPAN") {
      e.target.parentElement.remove();
    }
  },
  false
);
