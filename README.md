# Richy [![Build Status](https://travis-ci.org/MichPCX/Richy.svg?branch=master)](https://travis-ci.org/MichPCX/Richy) [![Python Language](https://i.imgur.com/0Ao4FpW.png)](https://github.com/MichPCX/Richy) [![Python 2.7, 3.4, 3.5](https://i.imgur.com/kpTitBA.png)](https://github.com/MichPCX/Richy) [![OS Linux](https://i.imgur.com/CqiDOdy.png)](https://github.com/MichPCX/Richy)

<p align="center"><img src="https://i.imgur.com/fb5cHtB.png" alt="Linux" /></p>

Personal assistant made especially for GNU/Linux because we deserve our own version of siri too!

Do you use WolframAlpha often or you need a quick answer for simple question? Just use **Richy**.

**Richy** is open-source python-based assistant which can help you with;
- aswering your (simple) questions,
- maintaining your schedule,
- calculating medium-level calculation,
- giving you informations about your movies library or any movie you want

## Why Richy?
Once I found myself looking for answers on WolframAlpha every single day and as I loved (and still do!) using the terminal, I decided to make Richy. Richy will help you with day-to-day questions and tasks.
It was made especially for GNU/Linux as users of Linux also need answers.

## Installation
To get Richy, just follow following steps;
- Download Richy,
- Move the folder .richy to /home/{your username}/
- Run ```python setup.py install``` and you are ready to go!

When running Richy for the first time, you will have the choice to edit config.

## How to use it?
After installation you can use richy in two modes; internal and external;

-internal, - simply type ```richy``` which will open up its main screen where you can see your schedule and ask questions from there!

-external - you can simply run ```richy {your question here}``` for example ```richy whats 2+2?``` and richy will give you the answer you are looking for without starting the actual richy command prompt. 

## Curent version

The most recent version of Richy is 0.45 which brings:

 - Changed name "Heinrichy" to just "Richy" which makes it simpler and easier to remember.
 - Code has been optimized for stability
 - Richy has entered Beta phrase
 - Added ability to install Richy using setup.py script
 - Richy config and modules has been moved to /home/$USER/.richy
 - Added ability to change the size of terminal in config which will also change the main "Richy" text to fit the size of terminal that has been chosen.
 - Added ability to use colour to display version of Richy if you choose to.
 - Created logo_printer.py script which holds the functions for printing out the logo.
 - Added better exception handling
 - Added script which will allow to edit config on first startup
 - Added wikipedia summary (can be used as 'wiki the hobbit')
 
## Example questions
```
'schedule'
'whats 100*42?'
'tell me a joke'
'26 pounds to kg'
'rhymes with coder'
'dictionary vehicle'
'scrabble programming'
'US $900 2005'
'december 30, 1990 plus 10000 days'
```

## Modules

To add functionality to Richy, the script uses modules to add new functions to it so you can easily write your own modules. Prebuilded modules that come with Richy;
- Schedule - allows to modify your schedule which will then be displayed in Richy ('schedule')
- Multimedia - allows to get more information about movies you have on the local drive and movies you want to watch ('movie help')

## To-do
- [ ] *Show weather*
- [ ] *Random fact/quotes*
- [ ] *Improve calculator to solve algebra*
- [ ] *Lyrics for chosen song*
- [ ] *Url expander/shortener*
- [ ] *News from chosen websites*
- [ ] *Download subtitles for movies*
- [ ] *Give tvshow/book/music description*

## Support & license
If you found a bug in Richy, use [issue tracker](https://github.com/MichPCX/Richy/issues) to let me know. 

Also if you need to contact me directly, email me on *michpcx@protonmail.ch*.

**Warning**; Richy comes under [General Public License v3](https://github.com/MichPCX/Richy/blob/master/License.md). Please note that Richy is still in beta so you are using it for your own risk. Huge thanks goes to the user [subdiff](https://github.com/subdiff/Modern_Tux) for providing modernised version of linux logo.
