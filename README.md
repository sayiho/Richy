# Richy [![Build Status](https://travis-ci.org/MichPCX/Heinrichy.svg?branch=master)](https://travis-ci.org/MichPCX/Richy) [![Python Language](https://camo.githubusercontent.com/b5335e67163d72a456a4ea4345e58b7eb497c884/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c616e67756167652d507974686f6e2d7265642e737667)](https://github.com/MichPCX/Richy) [![Python 2.7, 3.4, 3.5](https://img.shields.io/pypi/pyversions/icon_font_to_png.svg)](https://github.com/MichPCX/Richy)
Personal assistant made especially for GNU/Linux because we deserve our own version of siri too!

Did you ever wanted to have your own assistant, but the only ones available are for Android/iOS/Windows plus you are
worried about privacy?

Well, now you can have '**Richy**' which will help you to live in the terminal, because what's the point of searching the web (which can take a while by the way) when you can simply just ask Richy?

Richy is open-source python-based assistant which can help you with;
- maintaining your schedule,
- aswering your questions,
- calculating medium-level calculation,
- giving you informations about your movies library or any movie you want

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

## Installation
After downloading Richy, just move the folder .richy to /home/{your username}/ and start setup.py. Thats all!
When you will run Richy for the first time, you will be able also to modify config.

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

## Why Richy?
Name 'Richy' is a modification after the name of famous physicist [Heinrich Friedrich Weber](https://en.wikipedia.org/wiki/Heinrich_F._Weber) which was Albert Einstein's initial doctoral
advisor. As Heinrich was helping Albert Einstein, Richy will help you with day-to-day questions and tasks.
It was made especially for GNU/Linux as members of Linux Master Race also need an assistant, however with few
code modifications, the code should work on Microsoft Windows or MacOS. I've decided to create Richy after
I came across an article where the author was trying to live in the terminal and only use the terminal without any GUI for
30 days. This is nearly impossible without any preparation which is why I created Richy, I wanted to do
nearly everything in the command line without the need for any user interface.

## How can I help?
If you have any ideas on how Richy could be improved or if you found some interesting
script that could be used as module to Richy, just email me; michpcx@protonmail.ch. Also, if you found some
bugs in the code or you have more efficient way of performing a task, just create new issue in the [issue tracker](https://github.com/MichPCX/Richy/issues).

*By michpcx, michpcx@protonmail.ch*
