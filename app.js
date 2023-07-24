const cardNameInput = document.querySelector('#cardName');
const cardNameButton = document.querySelector('#cardNameButton');
const searchDisplay = document.querySelector('#searchDisplay');
const deckDisplay = document.querySelector('#deckDisplay');
const deleteDeckBtn = document.querySelector('#deleteDeck')
const deckName = document.querySelector('#deckName');
const savedDecksDisplay = document.querySelector('#savedDecksDisplay')
const saveDeckBtn = document.querySelector('#saveDeck')
let currentDeckName = '';

axios.defaults.baseURL = 'https://api.magicthegathering.io/v1';


let decks = {};
let deck = [];

document.addEventListener('DOMContentLoaded', () => {
    const savedDeck = localStorage.getItem('deck');
    const savedDecks = localStorage.getItem('decks');
    if (savedDeck) {
      deck = JSON.parse(savedDeck);
      console.log(deck);
      console.log(decks);
      displayDeck(); // Display the deck after loading it from local storage
    }

    if(savedDecks){
        decks = JSON.parse(savedDecks);
        createDeckIcons(decks);
        console.log(decks);
    }
  });

function getCardByName(){
    const cardName =  cardNameInput.value;

    axios.get(`/cards`, {
        params: {
            name: cardName
        }
    })
    .then(response => {
        const cards = response.data.cards;
        const generalInfo = response.data;

        console.log(generalInfo);
     
        console.log(cards);
        displaySearchResults(cards)
    })
    .catch(error => {
        // Handle any errors
        console.error('Error:', error.message);
      });
}

cardNameButton.addEventListener('click', e => {
    e.preventDefault();
    getCardByName();
  });

  function displaySearchResults(cards){
    searchDisplay.innerHTML = '';

    cards.forEach(card => {
        generateImg(card);
    })
}

function displayDeck(){
    searchDisplay.innerHTML = '';
    deck.forEach(card => {
        generateImg(card)
    })
    
}

function generateImg(card){
    if(card.imageUrl){
        const imageUrl = card.imageUrl;
        const cardImg = document.createElement('IMG')
        cardImg.src = imageUrl;
        searchDisplay.appendChild(cardImg);
       cardImgEvents();
}
}

function cardImgEvents(){
    cardImg.addEventListener('click', () => {
        if(!deck.includes(card)){
            deck.push(card);
            saveDeckToLocalStorage();
          }
          else {
              console.log('Card is in deck already!');
          }
    });   
    console.log('Card IMG URL not available.')
}
    


function removeCardFromDeck(){

}

function saveDeckToLocalStorage(){
    decks[deckName.value] = deck;
    localStorage.setItem('deck', JSON.stringify(deck));
    saveDecksToLocalStorage();
    console.log(decks);
    
}

// function resetDeck(){
//     deck = [];
//     saveDeckToLocalStorage();
//     displayDeck();
// }

function deleteDeck(deckName){
    delete decks[deckName];
    saveDeckToLocalStorage()
    saveDecksToLocalStorage();
    console.log(decks);
}

function pushtoDecks(){
    if (deckName.value!== "") {
        decks[deckName.value] = deck.slice(); // Create a copy of the deck array to avoid reference issues
        saveDecksToLocalStorage(); // Save the updated decks object to local storage
        createDeckIcons(decks); // Refresh the deck icons after adding a new deck
        console.log(decks);
      } else {
        console.log("Please provide a valid deck name.");
      }
}

function saveDecksToLocalStorage() {
    localStorage.setItem("decks", JSON.stringify(decks));      
  }

function createDeckIcons(decks){
  for(const deckName in decks) {
    const deckLogo = document.createElement('IMG');
    deckLogo.classList.add('deckIcon');
    deckLogo.src = 'images/deckLogo.png';
    deckLogo.addEventListener('click', () => loadDeck(deckName));
    savedDecksDisplay.appendChild(deckLogo);
  }
}

function loadDeck(deckName){
    if (decks[deckName]) {
        deck = decks[deckName];
        currentDeckName = deckName;
        displayDeck();
        saveDeckToLocalStorage();
      } else {
        console.log("Deck not found in local storage.");
      }
}

saveDeckBtn.addEventListener('click', pushtoDecks);


deleteDeckBtn.addEventListener('click', () => {
    deleteDeck("");
});


deckDisplay.addEventListener('click', displayDeck);

