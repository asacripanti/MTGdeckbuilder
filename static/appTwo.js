document.addEventListener('DOMContentLoaded', function () {
    const cardImg = document.querySelectorAll('.cardImg')
    const cardDisplay = document.querySelector('.cardDisplay');


    cardDisplay.addEventListener('click', function(event) {
        if (event.target.classList.contains('cardImg')) {
            console.log('Clicked!');
        }
    });

});








// cardImg.forEach(cardImg => {
//     cardImg.addEventListener('click', function(){
//         console.log('Clicked!');
//     })
// })


// cardDisplay.addEventListener('click', function(event) {
//     if (event.target.classList.contains('cardImg')) {
//         console.log('Clicked!');
//     }
// });