# tdd-py
Test-driven Python

Make sure you have [Python3 installed](https://docs.python-guide.org/starting/install3/osx/), 
and download [PyCharm](https://www.jetbrains.com/pycharm/) from JetBrains.

Open the project in PyCharm.

* add a build configuration for Python, using the project directory as the script path
* add a pytest configuration using the same path

Right-click on the tests folder and select "Run 'pytest in tests' "

From the command line, use 'python3 -m pytest'

Tests will run in the terminal in PyCharm.

Once you have a test working, figure out two ways to break it by changing the code (not the test)

Work them in this order: maths, stringy, songs, dates.
Tests for:

Add two numbers
Multiply two numbers
Square a numbers
Cube a number
Concatenate two strings
Concatenate three strings without spaces
Get the 13th letter in a given phrase
Get the Nth letter in a given phrase
Sing '10 bottles of beer on the wall'
Sing 'N bottles of beer on the wall'
For '99 bottles of beer on the wall,' handle the 2, 1, and 0 cases
For '99 bottles of beer on the wall,' handle the zero, one, and no cases
What day of the week a month starts on
What day of the week a date is and the day name
Whether as given month/year has a Friday the Thirteenth
How many Friday Thirteenths in a given year
