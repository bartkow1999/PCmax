# PCmax
This repository presents Tabu search algorithm implementation to solve PCmax problem.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Code examples](#code-examples)
* [Contact](#contact)

## General info
The project was made in **November 2019**.

## Technologies
Python 3.6 or newer

## Setup
Clone this repository using git bash:
```
git clone https://github.com/bartosztkowalski/PCmax.git
```
Run using ***python*** or open in dedicated IDE (e.g. PyCharm)
```
python TABU_MASTER.py
```

## Code Examples
The program processes the .txt file, which must be attached in the main project folder.

.Txt file format:
```
<int> <- the number of processors
<int> <- number of tasks
<int> - length of the first task
<int>
...
<int> - length of the last task
```

Example:
```
10
200
337
505
605
...
1
1918
```

To perform the processing, line 182 of the code must be modified. Replace <file name> with the file name in the root directory:
``with open ('<relative file path>') as plik:``
for example:
``with open('m10n200.txt') as plik:``

The result of the program is:
```
<list containing lists of assigned tasks for each processor>
processing execution time: <float> (in seconds)
<list of summed times on every processor>
Best result: <int> | optimum for a given problem: <int>
```
Example:
```
[[1375, 925, 915, 881, 806, 795, 767, 723, 669, 555, 505, 440, 363, 337, 290, 243, 149, 115, 91, 55], [1819, 946, 887, 848, 792, 782, 731, 675, 560, 532, 505, 454, 385, 302, 260, 178, 118, 111, 71, 43], [2650, 908, 875, 847, 785, 759, 709, 645, 534, 424, 354, 335, 316, 278, 191, 140, 103, 90, 55, 1], [955, 946, 911, 895, 851, 798, 781, 705, 637, 564, 532, 508, 499, 406, 285, 246, 170, 125, 109, 76], [1827, 949, 931, 852, 802, 783, 722, 660, 613, 551, 419, 349, 313, 308, 271, 205, 157, 115, 103, 69], [2129, 989, 888, 828, 774, 764, 694, 613, 554, 521, 477, 400, 384, 275, 241, 160, 114, 105, 71, 18], [984, 976, 950, 892, 825, 791, 751, 705, 692, 605, 542, 505, 415, 325, 290, 260, 173, 145, 106, 67], [1918, 970, 895, 858, 813, 755, 705, 692, 550, 519, 470, 410, 327, 307, 266, 180, 145, 117, 71, 31], [2848, 905, 861, 819, 786, 741, 587, 531, 495, 416, 368, 340, 314, 275, 255, 167, 144, 81, 55, 11], [992, 979, 933, 903, 843, 788, 765, 711, 641, 564, 537, 503, 483, 381, 318, 228, 172, 127, 66, 65]]
[10999, 10999, 10999, 10999, 10999, 10999, 10999, 10999, 10999, 10999]
Czas: 0.6640439033508301
Najlepszy wynik: 10999 | Optimuum: 10999
```