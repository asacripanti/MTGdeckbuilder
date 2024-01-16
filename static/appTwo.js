document.addEventListener('DOMContentLoaded', function () {
    const deckLinks = document.querySelectorAll('.deck-link');
    const cardImgsSearch = document.querySelectorAll('.cardImgSearch')
    const deleteButtons = document.querySelectorAll('.deleteDeckBtn');
    const newDeckSubmitBtn = document.querySelector('.newDeckSubmitBtn');
    const deckForm = document.querySelector('.deckForm');
  
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

    if(newDeckSubmitBtn){
            newDeckSubmitBtn.addEventListener('mouseover', function() {
            deckForm.style.borderColor = '#00FA9A';
        });
    
            newDeckSubmitBtn.addEventListener('mouseout', function() {
            deckForm.style.borderColor = 'white'; // Reset the border color
        });
    }



    cardImgsSearch.forEach(function (cardImgSearch) {
        cardImgSearch.addEventListener('click', function (event) {
            if (event.target.classList.contains('cardImgSearch')) {
                // const detailApiUrl = `https://api.magicthegathering.io/v1/cards?name=${cardName}`;
                const cardName = cardImgSearch.alt;
                const cardType = cardImgSearch.dataset.type;
                const cardColor = cardImgSearch.dataset.color;
                const cmc = parseInt(cardImgSearch.dataset.cmc);
                const imgUrl = cardImgSearch.src;
               
                cardImgSearch.classList.add('cardAdded');

                const cardObject = {
                    name: cardName,
                    type: cardType,
                    colors: cardColor,
                    cmc: cmc,
                    img: imgUrl

                }

                deck.push(cardObject);
                
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








