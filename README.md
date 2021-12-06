# Barchart_Project
This program is a part of the 01219114 Computer Programming 1 course. This program is a program for drawing bar charts.
You can import data from a file or you can input text and numbers to create a bar chart.

## Overview and features
The main program will ask user that you want to draw a bar chart using data from a text file or draw a barchart using manually provided data, then it will draw bar chart and their titles.

## The program contain with 3 options.
1. Draw a barchart using data from a text file
2. Draw a barchart using manually provided data
3. Exit 
 
## The program's designs
`Graphics class` : It's a class that allows to draw basic shapes on the screen, such as squares, straight lines, and letters. The Turtle class is passed to the Graphic constructor to be used as a tool for drawing shapes.

`BarChartManager class`: This class controls the overall program functions such as arranging screen size and coordinates,instructing the user to enter data into the program and controlling the process of reading and writing files.

`Bar class` : It’s a class for drawing a single data bar of a bar chart. This class calls methods in Class Graphic to draw a square and letters. It receives all the calculated information from class BarChart
and uses that information to draw components of the data bar.

`BarChart class` : It’s a class that controls the drawing of every component of a bar chart. This class takes all the detailed information of a bar chart and processes it to determine the optimal size and position of every component. This includes the title, axes, paddings, gaps, and every data bar.

And here is class diagram of the program.

![barchart-class-diagram](docs/barchart-class-diagram.png)

## Code structure
* [main.py](main.py) : This file used to run main program 
* [graphic.py](graphic.py) : This file contains the `Graphic` class.
* [barchart_manager.py](barchart_manager.py) : This file contains the `BarChartManager` class.
* [barchart.py](barchart.py) : This file contains the `BarChart` class.
* [bar.py](bar.py) : This file contains the `Bar` class.
* [draw_text.py](_sandbox/draw_text.py) : This file used for setting font sizes,style and also set the position of the texts.
