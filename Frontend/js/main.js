/* Sección index.html */

let menu = document.querySelector("#menu-icon");
let navbar = document.querySelector(".navbar");

menu.onclick = () => {
  navbar.classList.toggle("active");
};

window.onscroll = () => {
  navbar.classList.remove("active");
};

/* Sección productos.html */

let preveiwContainer = document.querySelector(".products-preview");
let previewBox = preveiwContainer.querySelectorAll(".preview");

document.querySelectorAll(".products-container .product").forEach((product) => {
  product.onclick = () => {
    preveiwContainer.style.display = "flex";
    let name = product.getAttribute("data-name");
    previewBox.forEach((preview) => {
      let target = preview.getAttribute("data-target");
      if (name == target) {
        preview.classList.add("active");
      }
    });
  };
});

previewBox.forEach((close) => {
  close.querySelector(".fa-times").onclick = () => {
    close.classList.remove("active");
    preveiwContainer.style.display = "none";
  };
});

/* Sección inicio sesión */

const username = document.getElementById("username");
const password = document.getElementById("password");
const boton = document.getElementById("password");

boton.addEventListener("click", (e) => {
  e.preventDefault();
  const data = {
    username: Facundo1.value,
    password: Facundo1.value,
  };
  console.log(data);
});
