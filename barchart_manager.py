import csv
import turtle

from barchart import BarChart


class BarChartManager:
    """
    This class controls the overall program functions
    such as arranging screen size and coordinates,
    instructing the user to enter data into the program,
    and controlling the process of reading and writing files.
    """

    def __init__(self, screen_width, screen_height):
        """
        Construct an instance of the BarChartManager class.

        :param screen_width: The width of the drawable area.
        :param screen_height: The height of the drawable area.
        """

        self.screen = turtle.Screen()
        # Set the size of the main window.
        self.screen.setup(screen_width, screen_height)
        # Move the origin of the screen's coordinate system to the bottom-left corner of the window.
        self.screen.setworldcoordinates(0, 0, screen_width, screen_height)

    def close(self):
        """
        Clear the resources managed by this instance of BarChartManager.
        """

        # Shut the turtlegraphics window.
        self.screen.bye()

    def draw_barchart(self, title, data):
        """
        This is a utility method for drawing a bar chart that fits into the window.
        This method receives a text title and a data dictionary
        and draws a bar chart that fills the drawable area.

        :param title: The title of the bar chart.
        :param data: The dictionary containing all the data points.
        :return: None
        """
        print('Please wait while the program is drawing the barchart...')
        barchart = BarChart(
            title,
            data,
            self.screen.window_width(),
            self.screen.window_height()
        )
        barchart.draw()
        print('Finished drawing the barchart.')

    def draw_barchart_using_sample_data(self):
        """
        Draws a bar chart using an embedded sample data set.
        """

        title = 'Population of Six Largest Cities in Southeast Asia'
        data = {
            'Bandung': 7_065_000,
            'Bangkok': 17_066_000,
            'Ho Chi Minh City': 13_312_000,
            'Jakarta': 34_540_000,
            'Kuala Lumpur': 8_285_000,
            'Manila': 23_088_000,
        }
        self.draw_barchart(title, data)

    def draw_barchart_using_data_from_file(self):
        """
        Draws a bar chart using data loaded from a CSV file.
        """

        loc = input('Enter a file location to load the data: ')
        title = 'UNTITLED'
        data = {}
        with open(loc, 'r', newline='') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if len(row) == 2:
                    if row[0] == '[CHARTTITLE]':
                        title = row[1]
                    else:
                        data[row[0]] = float(row[1])
        self.draw_barchart(title, data)

    def draw_barchart_using_data_from_user_input(self):
        """
        Draws a bar chart using data manually entered by the user.

        This method receives a title and data points from the user.
        It asks the user to enter a file path to save the data
        and then display a bar chart according to that data set.
        """

        title = input('Enter the title of the barchart: ')
        data = {}
        i = 0
        while True:
            i += 1
            label = input(f'Enter the label of data #{i}: ')
            value = float(input(f'Enter the value of data #{i}: '))
            # Add the data point to the data dictionary.
            data[label] = value
            command = input('Please enter n (next) or q (quit): ')
            if command != 'n':
                break
        loc = input('Enter a file location to save the data: ')
        with open(loc, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['[CHARTTITLE]', title])
            for label, value in data.items():
                writer.writerow([label, value])
        print(f'Successfully saved data into file {loc}')
        self.draw_barchart(title, data)
