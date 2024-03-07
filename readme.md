# MTG - Deckbuilder

This is MTG - Deckbuilder! A full-stack web app that allows you to look up cards so you can create and save your own custom deck. 

## Table of contents

- [MTG - Deckbuilder](#mtg---deckbuilder)
  - [Table of contents](#table-of-contents)
    - [Why?](#why)
    - [Screenshot](#screenshot)
    - [Built with](#built-with)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Database Setup](#database-setup)
  - [Running the Application](#running-the-application)

### Why?
My wife and her siblings and I all play Magic the gathering at home. I create all the decks for everyone to use and update the decks too. It didn't take long for me to start forgetting which cards ended up in which deck. Rather than look through 6 100 cards deck, I decided to create MTG - Deckbuilder! MTG - Deckbuilder allows me to create a deck by looking up and add cards to my deck with the Magic the gathering API. I then can come back and look at my deck or decks anytime I want since all this info is stored in a database. 

### Screenshot

![Overlook of project](static/images/mtgUpdateHomeStatic.png) 
(static/images/cardSearch.png)



### Built with

- Semantic HTML5 markup
- CSS custom properties
- Javascript
- Python
- PostgreSQL
- MTG API: https://docs.magicthegathering.io/

## Prerequisites
- Python 3.x
- PostgreSQL

## Setup

1. Clone the repository from the Github repo:https://github.com/asacripanti/MTGdeckbuilder/tree/capstone , make sure to clone from the capstone branch.
2. Open your terminal, navigate to where you want the project to be nested. 
3. Type the following steps in your terminal window.
4. Set up a virtual environment: `python -m venv venv`
5. Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On Unix or MacOS: `source venv/bin/activate`
6. Install dependencies: `pip install -r requirements.txt`

## Database Setup

1. Create a PostgreSQL database: `createdb myapp_db`
2. Run migrations: `flask db upgrade`

## Running the Application

1. Open your terminal window and navigate to where the project is located. 
2. Make sure you have your virtual environment running(review step 5 in setup) and run the follwing command in your terminal `flask run`
3. Copy the url provided from the terminal window and paste it into your internet browser. (url should look something like this: http://127.0.0.1:5000)




