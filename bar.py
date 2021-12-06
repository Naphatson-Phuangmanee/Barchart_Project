from graphic import Graphic


class Bar:
    """
    This class represents the data bar.
    It receives all the calculated information from class BarChart
    and uses that information to draw components of the data bar straight away.
    """

    def __init__(self, left, bottom, width, height, label, value, graphic=Graphic()):
        """
        Construct an instance of the Bar class.

        :param left: The x-coordinate at the left end of the bar.
        :param bottom: The y-coordinate at the bottom end of the bar.
        :param width: The width of the bar.
        :param height: The height of the bar.
        :param label: The label of the data point.
        :param value: The numeric value of the data point.
        :param graphic: An instance of the Graphic class responsible for drawing all the basic shapes.
        """

        self.graphic = graphic
        self.left = left
        self.bottom = bottom
        # The x-coordinate at the right end of the bar.
        self.right = self.left + width
        # The y-coordinate at the top end of the bar.
        self.top = self.bottom + height
        self.width = width
        self.height = height
        self.value = value
        self.label = label

    def draw(self):
        """
        Draw the data bar and its associated information.

        :return: None
        """

        # Calculate the x-coordinate at the midpoint of the data bar.
        horizontal_midpoint = self.left + self.width / 2
        # Draw a rectangle as the data bar itself.
        self.graphic.draw_rect(self.left, self.bottom,
                               self.right, self.top,
                               linecolor='#00330D',
                               fillcolor='#004D13')
        # Draw the numeric value above the data bar.
        self.graphic.draw_text(self.right, self.top + 5,
                               f'{self.value:,}',
                               align='right',
                               color='#660011')
        # Draw the label beneath the data bar.
        self.graphic.draw_text(horizontal_midpoint, self.bottom - 40,
                               self.label,
                               align='center',
                               color='#003D99')
