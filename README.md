# Heinrichy [![Build Status](https://travis-ci.org/MichPCX/Heinrichy.svg?branch=master)](https://travis-ci.org/MichPCX/Heinrichy) [![Python 2.7, 3.4, 3.5](https://img.shields.io/pypi/pyversions/icon_font_to_png.svg)](https://github.com/MichPCX/Heinrichy)
Personal assistant made especially for GNU/Linux because we deserve our own version of siri too!


[![asciicast](https://asciinema.org/a/81946.png)](https://asciinema.org/a/81946)

Did you ever wanted to have your own assistant, but the only ones available are for Android/iOS/Windows plus you are
worried about privacy?

Well, now you can have '**Heinrichy**' which will help you to live in the terminal, because what's the point of searching the web (which can take a while by the way) when you can simply just ask Heinrichy?

Heinrichy is open-source python-based assistant which can help you with;
- maintaining your schedule,
- aswering your questions,
- calculating medium-level calculation,
- giving you informations about your movies library or any movie you want

## Curent version

The most recent version _0.38Alpha brings:

-Added colorama instead of class with colours as colorama has wider range of options.

-New data.json file which has all the local commands for Heinrichy.

-Changed how Heinrichy shows schedule so it is updated every time it wants to show it.

## Installation
After downloading Heinrichy, fill in the config file where the values say 'default' (you can also change some other
values which is optional), run first_timer.py script which will analyse your environment and if it won't
give you any errors, it means you can run Heinrichy by running 'heinrichy_main.py'.

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
- [x] *Currency conversion*
- [x] *Random jokes*
- [x] *Dictionary*
- [ ] *Wikipedia*
- [ ] *Show weather*
- [ ] *Random fact/quotes*
- [ ] *Improve calculator*
- [ ] *Lyrics for chosen song*
- [ ] *Url expander/shortener*
- [ ] *News from chosen websites*
- [ ] *Allow to install Heinrichy*
- [ ] *Download subtitles for movies*
- [ ] *Give tvshow/book/music description*

## Modules

Prebuilded modules which you can find in Heinrichy;
- Schedule (external) - allows to modify your schedule which will then be displayed in Heinrichy ('schedule')
- Multimedia (internal) - allows to get more information about movies you have on the local drive ('movie help')

And many more modules and features coming soon!

## Why Heinrichy?
Name 'Heinrichy' is a modification after the name of famous physicist [Heinrich Friedrich Weber](https://en.wikipedia.org/wiki/Heinrich_F._Weber) which was Albert Einstein's initial doctoral
advisor. As Heinrichy was helping Albert Einstein, Heinrichy will help you with day-to-day questions and tasks.
It was made especially for GNU/Linux as members of Linux Master Race also need an assistant, however with few
code modifications, the code should work on Microsoft Windows or MacOS. I've decided to create Heinrichy after
I came across an article where the author was trying to live in the terminal and only use the terminal without any GUI for
30 days. This is nearly impossible without any preparation which is why I created Heinrichy, I wanted to do
nearly everything in the command line without the need for any user interface.

## How can I help?
If you have any ideas on how Heinrichy could be improved or if you found some interesting
script that could be used as module to Heinrichy, just email me; michpcx@protonmail.ch. Also, if you found some
bugs in the code or you have more efficient way of performing a task, just create new issue in the [issue tracker](https://github.com/MichPCX/Heinrichy/issues).

*By michpcx, michpcx@protonmail.ch*
