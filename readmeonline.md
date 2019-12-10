# Python Tech Tag

Gitlab repo mit Materialien für das Python Workshop am Freitag, dem 13. Dezember 2019, Tech-Tag des jetzigen adveisor Jahrgangs.
Das Workshop wird zweisprachig gehalten; das bedeutet ihr dürft sowohl Deutsch als auch Englisch in der Kommunikation mit den Tutoren benutzen.
Der Einfachheit halber werden wir ab jetzt in diesen Unterlagen ausschließlich Englisch benutzen. 

**English part starts here, German can be used when asking tutors.**

Just before you get to working on the challenge, I will state my 3 main goals with this workshop:

> 1. Teach you the very basics of Python, the Linux Shell and Git, in a manner that is approachable for total beginners;
> 2. Make it such that you can complete the tutorial independently at your work station in 90 minutes, only asking us questions when you need help;
> 3. Whet your apetite for more reading on your own and offer possible hints at how Python could be useful for your project work at adveisor.

##  Why Python? Why Python for adveisor?
Python is a *very* high level language, which offers you an often faster and more human-experience centric development process than traditional, compiled languages.
Python is also the language of choice in many, many different fields in the industry and is *used by a lot of people with no STEM background*.
Python is a fun and quite versatile place to start your journey into programming and eventually unlocking the **secrets of the Universe**.

adveisor, on the other hand, is a place where you explore and get to know **yourself** (and the world -- heck, there people from like *25+ countries* taking part in it). And since Python enables you to use the full, raw power of **any computer anywhere**, I think it is a perfect tool to have on your hands when going out with such high goals in mind.

Just so you also get to know a bit about me and the motivation behind me ending up holding this workshop:

I was involved with adveisor for the past 2 years back-to-back and saw basically every facet of it first-hand. I want to give back in a way and with something that I felt was missing when I was an *adveisee* myself a couple years ago, so I figured an English-Language programming treasure hunt game with a Christmas Theme is just the way to do it.

So without further ado, let's get going.

## How this workshop works

> 1. This is a programming treasure hunt game with a Christmas Theme.
>
> 2. There will be rewards.
>
> 3. Everything you need is in this repo. Pop us questions when having a hard time figuring something out on your own.

There will be 6 problems in total. You cannot progress to the next one unless you finished the previous problem.
You should be able to finish in 90 minutes and you will have to submit your solution at the end.
The workshop has been designed as individual work, but you can work with your peers if you feel like it.
Attached with each challenge you will find a cheat sheet. Google and the Internet in general are your best pals right now. 

# Challenges
Each challenge has its own separate folder, each folder contains Python (_.py_) files, cheat sheets and more. Navigate using the command line.

Quick refresher:
1. _ls_ - lists contents of current folder.
2. _cd "folderName"_ - switches into folder called _folderName_.
3. Use the tab key to auto-complete.
4. Use _python "program name"_ to run a python script.

## First challenge.
**Basic arithmetics**
##### 1. Swap 2 numbers without using a third variable.

As this instruction states, you have to write an algorithm that switches two numbers between them, each originally stored in one variable, without introducing any other new variable.

> _For example:_
>
> a, b = 2,5
> should become:
> a, b = 5,2

Write your code in _numberSwitch.py_. 

##### 2. Santa rocketship fuel problem.

Santa has become stranded at the edge of the Solar System while delivering presents to other planets! To accurately calculate his position in space, safely align his warp drive, and return to Earth in time to save Christmas, he needs you and his Elves to bring him measurements from fifty stars.

The Elves quickly load you into a spacecraft and prepare to launch, but they first need to determine the amount of fuel required.

Fuel required to launch a given module is based on the module's mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

> _For example:_
>
> For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
> For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
> For a mass of 1969, the fuel required is 654.
> For a mass of 100756, the fuel required is 33583.
> The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add
together all the fuel values.

What is the sum of the fuel requirements for all of the modules on your spacecraft?

Write your code in _rocketship.py_ and use _rocketshipInput.txt_ as your program input to compute the final answer. __Remember this final answer for later.__

_Thanks to https://adventofcode.com/2019/day/1 for this problem!_


## Second challenge.
**Sorting algorithm**

##### 1. Write a Python program which sorts a list using Insertion Sort.
See: https://en.wikipedia.org/wiki/Insertion_sort

Write your code in _insertionSort.py_ and use _sortInput.txt_ as your program input to compute the final answer.

__Add this final answer as the new, last word to the given word lists in the next challenge.__

## Third challenge.
**String processing**

##### 1. Write a Python program to check if some given words are anagrams.

Write your code in _anagram.py_ and use _anagramList.txt_ (__don't forget to add the sorted list from the second challenge as the last word to the list, on a new line__) as your program input to compute the final answer. 

##### 2. Write a Python program to check if different given words are made up from the same characters (by rotating only letters from the same character set).

Write your code in _charRotation.py_ and use _charRotationInput.txt_ as your program input to compute the final answer. 

##### 3. Save your answers from the last two questions on different lines in _hashOriginal.txt_

##### 4. Run _hashGenerator.py_ from us which takes as input _hashOriginal.txt_ and generates a new, mysterious string --- a HASH.

__Remember this final answer for later.__

## Fourth challenge.
**Data Structures**

##### 1. Build a Python data structure with the results you found so far -- result of rocketship problem from Challenge 1 and hash from Challenge 3.

Write your code in _dataStructures.py_. 

##### 2. Build a Python class _Elf_ in the same file as above: _dataStructures.py_.
Instantiate an Elf called Oscar.

## Fifth challenge.
**Keys**

##### 1. Run _python dataStructures.py Oscar.command("liftoff")_ in the terminal to progress to the next leg of your journey.

Save the output of this in _keys.txt_

##### 2. The Elves have lost the second and final key needed for liftoff in the html body of https://fratiloiu.com/python.

Find the key in the html body of the page, add it as a second line to _keys.txt_ and run _crackKey.py_ with this list as its input.
Take the ecrypted message and add your name at its end without a space, save this in _messageName.txt_ and proceed to exercise 6.

## Sixth challenge.
**Almost there!**

##### 1. Write a Python script that generates a hash from the contents of _messageName.txt_.
##### 2. Make github fork, clone, add your reply, commit, pull request with your email adress as a commit comment.
##### 3. Feedback comes in by email.
##### 4. Submit your work as described above and get your Lebkuchen.

# Useful links:
1. https://www.onlinegdb.com/online_python_interpreter
2. https://www.python.org/shell/
3. https://www.pythonanywhere.com/