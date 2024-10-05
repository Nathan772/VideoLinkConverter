
/*
from : https://www.tutorjoes.in/JS_tutorial/dynamic_circular_progress_bar_in_javascript
*/


/*window.onload = function() {
                var container = document.getElementById('container');
};*/
//wait for container
window.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#container').addEventListener('click', () => {
    console.log('You clicked me!')
    });


                var container = document.getElementById('container');
                //alert(container);
                console.log("élément récupéré : "+container)
                console.log("début du chargement !");

                /* C'est color qui gère la couleur du cercle de chargement de vidéo
                percent indique le moment d'arrêt
                course, lorsqu'il est associé à la bonne balise dans le html, indique
                le pourcentage d'avancement (mais il ne sera
                pas utilisé ici car on ne le connait pas)
                */
                const courses = [
                  { course: "preparationVideo", percent: 100, color: "#DC143C" },

                ];

                let isLoading = true;
                const progressGroups = document.querySelectorAll(".progress-group");

                progressGroups.forEach((progress, index) => {


                          //console.log("passage dans chargement ...")


                          let progressStartValue = 0;
                          let progressStartEnd = courses[index].percent;
                          /*
                          the lower it is, the faster it goes
                          */
                          let speed = 10;


                            //peut être qu'un progressTimer n'est pas réutilisable
                            let progressTimer = setInterval(() => {

                              //for(let i= 0;i<5;i++){

                                progressStartValue++;
                                if (progressStartValue == progressStartEnd) {
                                  // this part forbids to redo a new circle turn ??
                                  clearInterval(progressTimer);
                                  console.log("la valeur de progressStart value "+progressStartValue);
                                }
                                //console.log("la valeur de i :"+i)
                                progress.querySelector(".circular-progress").style.background = `
                                conic-gradient(${courses[index].color} ${3.6 * progressStartValue}deg, #fff 0deg)`;


                                //console.log("la valeur de i :"+i)
                                progress.querySelector(".circular-progress").innerHTML = progressStartValue + "%";

                                //progress.querySelector(".circular-progress").style.background = `
                                                              //conic-gradient("#FFFFFF" ${3.6 * progressStartValue}deg, #fff 0deg)`;
                                /*
                                bloque l'affichage de la barre à une faible valeur*/
                                /*if(i < 5){
                                  progressStartValue=50;
                                }*/
                                //console.log("la valeur de i :"+i)
                              //} //linked to for

                                 }, speed);







                        });

                        console.log("on sort de l'affichage de la barre de chargement ");


});

