document.addEventListener('DOMContentLoaded', function () {
    const deckLinks = document.querySelectorAll('.deck-link');
    const cardImgs = document.querySelectorAll('.cardImg')
    const deleteButtons = document.querySelectorAll('.deleteBtn');
    const searchDisplay = document.querySelector('.searchDisplay');
    const testDeck = document.querySelector('.testDeck');
    const searchResults = document.querySelector('.searchResults');
    
    const deck = [];

    deckLinks.forEach(function (deckLink) {
        deckLink.addEventListener('click', function (event) {
            event.preventDefault();

            // Extract the deck ID from the data attribute
            const deckId = deckLink.dataset.deckId;

            const url = `/deck/${deckId}`;

            // Navigate to the URL
            window.location.href = url;

            // Now you can use the deckId in your logic
            console.log('Clicked on deck with ID:', deckId);
        });
    });

   
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            // Prevent the click event from propagating to the container
            event.stopPropagation();

            // Add any additional logic for handling the delete button click
        });
    });


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








