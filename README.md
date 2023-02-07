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

1. Add two numbers
2. Multiply two numbers
3. Square a numbers
4. Cube a number
5. Concatenate two strings
6. Concatenate three strings without spaces
7. Get the 13th letter in a given phrase
8. Get the Nth letter in a given phrase
9. Sing '10 bottles of beer on the wall'
10. Sing 'N bottles of beer on the wall'
11. For '99 bottles of beer on the wall,' handle the 2, 1, and 0 cases
12. For '99 bottles of beer on the wall,' handle the zero, one, and no cases
13. What day of the week a month starts on
14. What day of the week a date is and the day name
15. Whether as given month/year has a Friday the Thirteenth
16. How many Friday Thirteenths in a given year
