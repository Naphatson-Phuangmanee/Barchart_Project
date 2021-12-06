from bar import Bar
from graphic import Graphic


class BarChart:
    """
    Represents all parts of the bar chart.

    This class controls the drawing of every component of a bar chart.
    The constructor takes all the detailed information of a bar chart
    and processes it to determine every component's optimal size and position.

    The components of the bar chart include the title, axes, paddings, gaps, and every data bar.
    """

    def __init__(self, title, data, total_width, total_height, graphic=Graphic()):
        """
        Construct an instance of the BarChart class.

        :param title: The title of the bar chart.
        :param data: The dictionary containing all the data points,
                and each data point is composed of a text label and a number value.
        :param total_width: The total width of the drawable area.
        :param total_height: The total height of the drawable area.
        :param graphic: An instance of the Graphic class responsible for drawing all the basic shapes.
        """

        self.title = title
        self.data = data
        self.total_width = total_width
        self.total_height = total_height
        self.graphic = graphic
        padding_left = 50
        padding_right = 50
        padding_top = 50
        padding_bottom = 60
        # The height of the space at the top of the bar chart reserved for the title.
        title_area_height = 50
        # The distance between the lowest point of the title and the top point of the highest bar.
        title_bottom_and_bar_top_gap = 80
        # The width of the horizontal axis.
        self.chart_width = self.total_width - padding_left - padding_right
        # The x-coordinate at the start of the horizontal axis.
        self.chart_left = padding_left
        # The x-coordinate at the end of the horizontal axis.
        self.chart_right = self.chart_left + self.chart_width
        # The y-coordinate at the top of the vertical axis.
        self.chart_top = self.total_height - padding_top
        # The y-coordinate at the bottom of the vertical axis.
        self.chart_bottom = padding_bottom
        # The y-coordinate at the bottom of the title area.
        self.title_bottom = self.chart_top - title_area_height
        # The maximum possible height of the tallest bar.
        self.bar_max_height = self.title_bottom - title_bottom_and_bar_top_gap - self.chart_bottom
        # List of all instances of class Bar associated with this bar chart,
        # each of which represents the information of 1 data point.
        self.bars = self.__build_bars()

    def __build_bars(self):
        """
        Build the list of instances of the class Bar from the dictionary of data points provided to the constructor.
        Each instance of Bar uniquely represents one data point.

        Each bar will be at the same width and arranged equally spaced along the horizontal axis.
        The height of the tallest bar will be set to the calculated value self.bar_max_height.
        This helps ensure that no bar will interfere with the bar chart's title above.

        :return: List[Bar]
        """

        # The maximum numeric value of all the data points.
        max_value = max(self.data.values())
        # The number of bars, which is determined by the number of data points in the dictionary.
        num_bars = len(self.data)
        # The spacing between each bar along the horizontal axis.
        horizontal_gap = 50 if num_bars <= 5 else 20
        # The width of each bar.
        width = ((self.chart_width - horizontal_gap) / num_bars) - horizontal_gap
        # An empty list to hold new instances of Bar.
        bars = []
        # Loop through each data point in the dictionary
        # and determine the optimum information for creating each new bar.
        for idx, (label, value) in enumerate(self.data.items()):
            # The x-coordinate at the left end of the bar along the horizontal axis,
            # the distance away from the vertical axis.
            left = self.chart_left + horizontal_gap + idx * (width + horizontal_gap)
            # The y-coordinate at the bottom end of the bar, which is exactly on the horizontal axis.
            bottom = self.chart_bottom
            # The height of the bar, in proportion to the maximum value of self.bar_max_height.
            height = value / max_value * self.bar_max_height
            # Create the new instance of the class Bar.
            bar = Bar(left, bottom, width, height, label, value, self.graphic)
            # Add the new bar to the list.
            bars.append(bar)
        return bars

    def __draw_bars(self):
        """
        Display every bar by telling each bar to draw itself.

        :return: None
        """

        for bar in self.bars:
            bar.draw()

    def __draw_title(self):
        """
        Draw the title at the top center of the bar chart,
        right above the virtual horizontal line y = self.title_bottom.

        :return: None
        """

        # Calculate the midpoint of the bar chart along the horizontal axis.
        horizontal_midpoint = self.chart_left + self.chart_width / 2
        # Draw the title in the center alignment,
        # providing (horizontal_midpoint, self.title_bottom) as the reference point.
        self.graphic.draw_text(horizontal_midpoint, self.title_bottom,
                               self.title,
                               align='center',
                               color='#0066FF',
                               fontsize=26,
                               fonttype='bold')

    def __draw_axes(self):
        """
        Draw the vertical and horizontal axes.

        :return: None
        """

        linewidth = 1
        linecolor = '#660011'
        # Draw the horizontal axis.
        self.graphic.draw_line(self.chart_left, self.chart_bottom,
                               self.chart_right, self.chart_bottom,
                               linewidth=linewidth,
                               linecolor=linecolor)
        # Draw the vertical axis.
        self.graphic.draw_line(self.chart_left, self.chart_bottom,
                               self.chart_left, self.chart_top,
                               linewidth=linewidth,
                               linecolor=linecolor)

    def draw(self):
        """
        Draw all components of the bar chart.
        It starts with erasing everything on the screen and then drawing bars, the title, and axes, respectively.

        :return: None
        """

        # Erase everything on the screen.
        self.graphic.clear()
        # Draw the data bars.
        self.__draw_bars()
        # Draw the title.
        self.__draw_title()
        # Draw the axes.
        self.__draw_axes()
