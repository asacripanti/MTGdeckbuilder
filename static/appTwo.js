document.addEventListener('DOMContentLoaded', function () {
    const cardImgs = document.querySelectorAll('.cardImg')
    const searchDisplay = document.querySelector('.searchDisplay');
    const testDeck = document.querySelector('.testDeck');
    const searchResults = document.querySelector('.searchResults');
    
    const deck = [];

    cardImgs.forEach(function (cardImg) {
        cardImg.addEventListener('click', function (event) {
            if (event.target.classList.contains('cardImg')) {
                // const detailApiUrl = `https://api.magicthegathering.io/v1/cards?name=${cardName}`;
                const cardName = cardImg.alt;
                const cardType = cardImg.dataset.type;
                const cardColor = cardImg.dataset.color;
                const cmc = parseInt(cardImg.dataset.cmc);
                const imgUrl = cardImg.src;

                const cardObject = {
                    name: cardName,
                    type: cardType,
                    colors: cardColor,
                    cmc: cmc,
                    img: imgUrl

                }

                deck.push(cardObject);
                console.log('Clicked!');
                console.log(deck);


                fetch('/add_card', {
                    method: 'POST',
                    headers: {
                      'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(cardObject),
                  })
                    .then(response => response.json())
                    .then(data => {
                      console.log(data.message); // Log the server response message
                    })
                    .catch(error => {
                      console.error('Error:', error);
                    });
                
    
            }
        });
    });
});








