//const container = document.getElementById("container");

/*
from : https://www.tutorjoes.in/JS_tutorial/dynamic_circular_progress_bar_in_javascript
*/
window.onload = function() {
                var container = document.getElementById('container');
                alert(container);

                console.log("élément récupéré : "+container)
                console.log("début du chargement !");

                const courses = [
                  { course: "Préparation votre vidéo...", percent: 100, color: "#DC143C" },
                ];
                /*
                courses.forEach((course) => {
                  container.innerHTML +=`
                  <div class="progress-group">
                  <div class="circular-progress" >
                    ...
                  </div>
                  <label class="text" style="color:${course.color}">${course.course}</label>
                </div>
                  `;
                });*/

                //style="  background: conic-gradient(${course.color} ${3.6 * course.percent}deg, #fff 0deg);"

                const progressGroups = document.querySelectorAll(".progress-group");

                  progressGroups.forEach((progress, index) => {
                    let progressStartValue = 0;
                    let progressStartEnd = courses[index].percent;
                    /*
                    the lower it is, the faster it goes
                    */
                    let speed = 20;
                    let progressTimer = setInterval(() => {
                      progressStartValue++;
                      if (progressStartValue == progressStartEnd) {
                        clearInterval(progressTimer);
                      }
                      progress.querySelector(".circular-progress").style.background = `
                      conic-gradient(${courses[index].color} ${3.6 * progressStartValue}deg, #fff 0deg)`;
})
                      /*useless
                      progress.querySelector(".course-value").innerHTML = progressStartValue + "%";
                    }, speed);*/

                  });


};

