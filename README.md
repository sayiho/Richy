# Heinrichy
Personal assistant made especially for GNU/Linux because we deserve our own version of siri too!


![alt Heinrichy](https://i.imgur.com/63pl8Ob.png)

Did you ever wanted to have your own assistant, but the only ones available are for Android/iOS/Windows plus you are
worried about privacy?

Well, now you can have '**Heinrichy**' which will help you to live in the terminal, because what's the point of searching the web which can take a while when you can simply just ask Heinrichy?

Heinrichy is python based assistant which can help you with;
- maintaining your schedule
- aswering your questions
- calculating medium-level calculation
- giving you informations about movies on the local drive

## Curent version

The most recent version is _0.27_Alpha which brings:
- Changed config format from py to conf (loading using configparser) for flexibility
- Added ability to turn on/off schedule module, multimedia module and modules that will come in the future
- New module called multimedia which allows to give you more info about movies you have on the local hard drive
- first_timer.py script which checks if you have required packages installed to run Heinrichy


## Installation
After downloading Heinrichy, fill in the config file where the values say 'default' (you can also change some other
values which is optional), run first_timer.py script which will analyse your environment and if it won't
give you any errors, it means you can run Heinrichy by running 'heinrichy_main.py'.

## Basic questions
```
'how are you?'
'schedule'
'is the martian any good?'
'whats 100*42?'
'rhymes to happy'
```

## To-do
- [x] *Search for movies on the hard drive and give info about them*
- [ ] *Wikipedia*
- [ ] *Dictionary*
- [ ] *Show weather*
- [ ] *Improve calculator*
- [ ] *Currency conversion*
- [ ] *Lyrics for chosen song*
- [ ] *Url expander/shortener*
- [ ] *Random fact/jokes/quotes*
- [ ] *News from chosen websites*
- [ ] *Allow to install Heinrichy*
- [ ] *Download subtitles for movies*
- [ ] *Move commands into the database*
- [ ] *Give movie/book/music description*

## Modules 

So far, Heinrichy has those modules;
- Schedule (external) - allows to modify your schedule which will then be displayed in Heinrichy
- Multimedia (internal) - allows to get more information about movies you have on the local drive

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
