document.addEventListener("DOMContentLoaded",function(){

    var urlParams = new URLSearchParams(window.location.search);
    var salaIdActual = urlParams.get('sala_id');
    
    var links_sala = document.getElementsByClassName("sala-link");

    Array.from(links_sala).forEach(function(link){

        var linkSalaId =  link.getAttribute("data-sala-id");
        

        if (salaIdActual == linkSalaId){

            link.style.color = "black";
            link.style.fontWeight = "550";
        
        }
    });
})

const rightArrow = document.querySelector(
    ".salas-container .right-arrow svg");

const leftArrow = document.querySelector(
    ".salas-container .left-arrow svg");


const tabsList = document.querySelector(".salas-container ul");

rightArrow.addEventListener("click", () => {
    tabsList.scrollLeft += 400;
})

leftArrow.addEventListener("click", () => {
    tabsList.scrollLeft -= 400;
})


const enlace = document.getElementById('reserva-a');
  // Obtener la URL actual
const urlActual = window.location.href;
  // Agregar el nuevo parámetro de consulta a la URL actual
// const nuevaURL = urlActual + '&codigo_id=1016912325';
  // Establecer la nueva URL como el valor del atributo href del enlace
enlace.setAttribute('href', nuevaURL);