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

## Curent version

The most recent version 0.45_Beta brings:

 - Changed name "Heinrichy" to just "Richy" which makes it simpler and easier to remember.
 - Code has been optimized for stability
 - Richy has entered Beta phrase and left Alpha as it works quite well without giving any errors
 - Added ability to install Richy using setup.py script (you can then just run 'richy what day is it' and richy will give you the answer.
 - Richy config and modules has been moved to /home/$USER/.richy
 - Added ability to change the size of terminal in config which will change the main "Richy" text to fit the size of terminal that has been chosen.
 - Added ability to colour in version of Richy if you choose to dispaly it.
 - Created logo_printer.py script which holds the functions for printing out the logo.
 - Added better exception handling
 - Created script which will run the first time Richy is being run to modify the config, so the user can input his/hers name etc.
 - Added wikipedia summary (can be used as 'wiki the hobbit' for example)

## How to use it?
After installation, you can simply run 'richy {your question here}' for example 'richy whats 2+2?' and richy will give you the answer. Or you could always just type in 'richy' which will open up its main screen where you can see your schedule and ask questions from there!

## Basic questions
```
'schedule'
'whats 100*42?'
'tell me a joke'
'26 pounds to kg'
'rhymes with coder'
'dictionary vehicle'
'scrabble programming'
'US $900 2005' (inflation)
'december 30, 1990 plus 10000 days'
```

## To-do
- [x] *Search for movies on the hard drive and give info about them*
- [x] *Move commands into the file*
- [x] *Allow to install Richy*
- [x] *Currency conversion*
- [x] *Random jokes*
- [x] *Dictionary*
- [x] *Wikipedia*
- [ ] *Show weather*
- [ ] *Random fact/quotes*
- [ ] *Improve calculator*
- [ ] *Lyrics for chosen song*
- [ ] *Url expander/shortener*
- [ ] *News from chosen websites*
- [ ] *Download subtitles for movies*
- [ ] *Give tvshow/book/music description*

## Modules

Prebuilded modules which you can find in Richy;
- Schedule (external) - allows to modify your schedule which will then be displayed in Richy ('schedule')
- Multimedia (internal) - allows to get more information about movies you have on the local drive ('movie help')

And many more modules and features coming soon!

## How can I help?
If you have any ideas on how Richy could be improved or if you found some interesting
script that could be used as module to Richy, just email me; michpcx@protonmail.ch. Also, if you found some
bugs in the code or you have more efficient way of performing a task, just create new issue in the [issue tracker](https://github.com/MichPCX/Richy/issues).

*By michpcx, michpcx@protonmail.ch*
