const pageBody = document.getElementById("body");

const darkModeButton = document.getElementById("DarkModeButton");
const lightModeButton = document.getElementById("LightModeButton");
const highContrastButton = document.getElementById("HighContrastButton");
const mediumContrastButton = document.getElementById("MediumContrastButton");
const defaultContrastButton = document.getElementById("DefaultContrastButton");

function ToggleDarkMode() {
  pageBody.classList.remove("light")
  pageBody.classList.add("dark");
  darkModeButton.classList.remove('outlined-button');
  lightModeButton.classList.add('outlined-button');
  SetCookie("color_mode", "dark");
}

function ToggleLightMode() {
  pageBody.classList.remove("dark")
  pageBody.classList.add("light");
  darkModeButton.classList.add('outlined-button');
  lightModeButton.classList.remove('outlined-button');
  SetCookie("color_mode", "light");
}

function ToggleHighContrast() {
  pageBody.classList.add("hc");
  pageBody.classList.remove("mc")
  mediumContrastButton.classList.add('outlined-button');
  defaultContrastButton.classList.add('outlined-button');
  highContrastButton.classList.remove('outlined-button');
  SetCookie("contrast_mode", "high");
}
function ToggleDefaultContrast() {
  pageBody.classList.remove("hc")
  pageBody.classList.remove("mc")
  highContrastButton.classList.add('outlined-button');
  mediumContrastButton.classList.add('outlined-button');
  defaultContrastButton.classList.remove('outlined-button');
  SetCookie("contrast_mode", "default");
}

function ToggleMediumContrast() {
  pageBody.classList.remove("hc")
  pageBody.classList.add("mc");
  highContrastButton.classList.add('outlined-button');
  mediumContrastButton.classList.remove('outlined-button');
  defaultContrastButton.classList.add('outlined-button');
  SetCookie("contrast_mode", "medium");
}

// Apply settings
if(GetCookie("color_mode") === "light") ToggleLightMode()
if(GetCookie("color_mode") === "dark") ToggleDarkMode()
if(GetCookie("contrast_mode") === "high") ToggleHighContrast()
if(GetCookie("contrast_mode") === "medium") ToggleMediumContrast()
if(GetCookie("contrast_mode") === "default") ToggleDefaultContrast()
