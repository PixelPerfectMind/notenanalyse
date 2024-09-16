const pageBody = document.getElementById("body");

const darkModeButton = document.getElementById("DarkModeButton");
const lightModeButton = document.getElementById("LightModeButton");
const highContrastButton = document.getElementById("HighContrastButton");
const mediumContrastButton = document.getElementById("MediumContrastButton");
const defaultColorModeButton = document.getElementById("DefaultColorModeButton");

function ToggleDarkMode() {
  pageBody.classList.remove("light")
  pageBody.classList.add("dark");
  darkModeButton.classList.remove('outlined-button');
  lightModeButton.classList.add('outlined-button');

  Save();
}
function ToggleLightMode() {
  pageBody.classList.remove("dark")
  pageBody.classList.add("light");
  darkModeButton.classList.add('outlined-button');
  lightModeButton.classList.remove('outlined-button');

  Save();
}

function ToggleHighContrast() {
  pageBody.classList.add("hc");
  pageBody.classList.remove("mc")
  mediumContrastButton.classList.add('outlined-button');
  defaultColorModeButton.classList.add('outlined-button');
  highContrastButton.classList.remove('outlined-button');

  Save();
}
function ToggleDefaultContrast() {
  pageBody.classList.remove("hc")
  pageBody.classList.remove("mc")
  highContrastButton.classList.add('outlined-button');
  mediumContrastButton.classList.add('outlined-button');
  defaultColorModeButton.classList.remove('outlined-button');

  Save();
}

function ToggleMediumContrast() {
  pageBody.classList.remove("hc")
  pageBody.classList.add("mc");
  highContrastButton.classList.add('outlined-button');
  mediumContrastButton.classList.remove('outlined-button');
  defaultColorModeButton.classList.add('outlined-button');

  Save();
}

function Save() {
  if (pageBody.classList.contains('dark')) SetCookie("color_mode", "dark");
  else SetCookie("color_mode", "light");

  if (pageBody.classList.contains('hc')) SetCookie("contrast_mode", "hc");
  if (pageBody.classList.contains('mc')) SetCookie("contrast_mode", "mc");
}