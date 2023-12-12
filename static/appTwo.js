document.addEventListener('DOMContentLoaded', function () {
    const cardImg = document.querySelectorAll('.cardImg')
    const searchDisplay = document.querySelector('.searchDisplay');
    const testDeck = document.querySelector('.testDeck');
    const searchResults = document.querySelector('.searchResults');


    // cardImg.addEventListener('click', function(event) {
    //     if (event.target.classList.contains('cardImg')) {
    //         console.log('Clicked!');
    //     }
    // });

    testDeck.addEventListener('click', function () {
        window.location.href = 'http://127.0.0.1:5000/deck';
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