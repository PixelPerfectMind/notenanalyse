const pageBody = document.getElementById("body");

function ToggleDarkMode() {
  pageBody.classList.remove("light")
  pageBody.classList.add("dark");
}
function ToggleLightMode() {
  pageBody.classList.remove("dark")
  pageBody.classList.add("light");
}