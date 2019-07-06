
// Theme selection will be done server-side
var theme = sessionStorage.getItem("theme");
if (!theme) theme = "white";
function apply_theme() {
  var cssf = {"white": "/cses.css", "dark": "/cses-dark.css"};
  var tcol = {"white": "white", "dark": "#292929"};
  document.getElementById("styles").setAttribute("href", cssf[theme]);
  document.getElementById("theme-color").setAttribute("content", tcol[theme]);
}

apply_theme();
function toggle_theme() {
  if (theme == "white") theme = "dark";
  else theme = "white";
  sessionStorage.setItem("theme", theme);
  apply_theme();
  return false;
}


function check_hash() {
  var hash = window.location.hash.substr(1);
  if (!hash) return;
  var e = document.getElementById(hash);
  if (!e) return;
  var p = e.closest(".closed");
  if (!p) return;
  p.classList.remove("closed");
  e.scrollIntoView();
}
window.onload = function() {
  var captions = document.getElementsByClassName("close-trigger");
  var callback = function(e) {
    e.target.closest(".closeable").classList.toggle('closed');
  }
  for (var i = 0; i < captions.length; i++) {
    captions[i].addEventListener("click", callback);
  }
  check_hash();
}
window.onhashchange = check_hash;
