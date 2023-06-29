# Unlock Infinite Inspiration: Discover Endless Adventures with our Boredom Buster Bot!

![Bored](https://github.com/paolacalle/boredbot/assets/98432607/73117f75-80cb-4cda-9588-3abb7ff40cb4)

## API Background
The Bored API helps you find things to do when you're bored! Data is collected through a voluntary form. 

    https://www.boredapi.com/about 

## Project Pitch

#### What problem are we solving?

Don't let boredom **rule** your life. **Embrace** the _adventure_, _creativity_, and _growth_ that our Bored Bot offers. 

#### Who/ what does the project interface with (people, other systems, hardware)?
Our implementation interfaces with people, leveraging the power of the Bored API and terminal to provide a holistic and interactive experience.

#### What are the inputs?
The user answers a series of questions, so Bored Bot can curate the perfect activity for them.

#### What are the outputs?
An activity tailored to user's preferences.

#### List the 5 steps to go from input -> output
* First we will filter the data based on the attributes they care about the most: Type, Price Range, Accessibility, Participants.
* User will then provide further information based on the attribute they chose. 
* From here, we provide the user with an initial activity suggestion.
* If user likes the activity, the bot chat closes. If not, we give the user the option to stay or change between categories.
* Once the user picks a suggested activity, we provide them with further information and end the bot chat.
* If the user finds no suggestion or wants to stop, we give them our goodbyes and good luck on their boredom.

#### What's the biggest risk?
* Not having enough time.
* The amount of data we have access to.
    * Since it is through submissions, some ranges/categories are empty.
    * The API documentation does not tell us the amount of submissions/data.

#### How will you know you're successful?
* The program provides good outputs based on user input. 
* The program does not crash and handles unexpected inputs.
* It provides suggestions that match our preferences.

[![Check Style](https://github.com/paolacalle/boredbot/actions/workflows/style.yaml/badge.svg)](https://github.com/paolacalle/boredbot/actions/workflows/style.yaml)
[![Tests](https://github.com/paolacalle/boredbot/actions/workflows/unit_test.yaml/badge.svg)](https://github.com/paolacalle/boredbot/actions/workflows/unit_test.yaml)