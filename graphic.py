import turtle


class Graphic:
    """
    Contains methods for drawing basic shapes such as straight lines, squares, and text.
    """

    def __init__(self, painter=turtle.Turtle()):
        """
        Construct an instance of the Graphic class.

        :param painter: An instance of the Turtle class to use as a painter to draw the shapes.
        """

        self.painter = painter
        # Tell the turtle to use the max speed.
        self.painter.speed(0)

    def draw_line(self,
                  x1, y1,
                  x2, y2,
                  linewidth=1,
                  linecolor='black'):
        """
        Draw a straight line from the starting point to the endpoint with the specified width and color.

        :param x1: The x-coordinate of the starting point.
        :param y1: The y-coordinate of the starting point.
        :param x2: The x-coordinate of the endpoint.
        :param y2: The y-coordinate of the endpoint.
        :param linewidth: The width of the straight line.
        :param linecolor: The color of the straight line.
        :return: None
        """

        self.painter.color(linecolor)
        self.painter.pensize(linewidth)
        # Lift the pen. Do not write while moving to the starting point.
        self.painter.penup()
        # Move to the starting point without drawing anything along the way.
        self.painter.goto(x1, y1)
        # Put the pen down. Prepare to start drawing.
        self.painter.pendown()
        # With the pen down, draw the line toward the endpoint.
        self.painter.goto(x2, y2)

    def draw_rect(self,
                  x1, y1,
                  x2, y2,
                  linewidth=1,
                  linecolor='black',
                  fillcolor='gray'):
        """
        Draw a rectangle with two diagonal points.
        The caller can specify the line width, line color, and fill color.

        :param x1: The x-coordinate of the first diagonal point.
        :param y1: The y-coordinate of the first diagonal point.
        :param x2: The x-coordinate of the second diagonal point.
        :param y2: The y-coordinate of the second diagonal point.
        :param linewidth: The border thickness of the rectangle.
        :param linecolor: The border color of the rectangle.
        :param fillcolor: The fill color of the rectangle.
        :return: None
        """

        # Set border color.
        self.painter.color(linecolor)
        # Set fill color.
        self.painter.fillcolor(fillcolor)
        # Set border thickness.
        self.painter.pensize(linewidth)
        # Lift the pen. Do not write while moving to the starting point.
        self.painter.penup()
        # Move to the first corner without drawing anything along the way.
        self.painter.goto(x1, y1)
        # Tell the painter to be prepared to fill the color after finishing drawing the borderlines.
        self.painter.begin_fill()
        # Put the pen down. Prepare to start drawing.
        self.painter.pendown()
        # Draw a straight line toward the second corner.
        self.painter.goto(x1, y2)
        # Draw a straight line toward the third corner.
        self.painter.goto(x2, y2)
        # Draw a straight line toward the fouth corner.
        self.painter.goto(x2, y1)
        # Draw a straight line back to the first corner, complete the rectangle.
        self.painter.goto(x1, y1)
        # Fill the rectangle with the fill color.
        self.painter.end_fill()

    def draw_text(self,
                  x, y,
                  text,
                  align='left',
                  fontname='Helvetica',
                  fontsize=16,
                  fonttype='normal',
                  color='black'):
        """
        Draw the text relative to the reference point.
        For the vertical position, this method will draw the text right above the reference point.
        The horizontal position will be chosen according to the value of the parameter 'align'.

        :param x: The x-coordinate of the reference point of the text.
        :param y: The y-coordinate of the reference point of the text.
        :param text: The text to be drawn.
        :param align: Text alignment relative to the reference point; possible values are 'left', 'center', or 'right'.
        :param fontname: The font-face of the text.
        :param fontsize: The font size of the text.
        :param fonttype: The font style of the text.
        :param color: The color of the text.
        :return: None
        """

        # Set the color.
        self.painter.color(color)
        self.painter.fillcolor(color)
        # Lift the pen. Do not write while moving to the reference point.
        self.painter.penup()
        # Move to the reference point without drawing anything along the way.
        self.painter.goto(x, y)
        # Put the pen down. Prepare to start drawing.
        self.painter.pendown()
        # Draw the text.
        self.painter.write(text, align=align, font=(fontname, fontsize, fonttype))

    def clear(self):
        """
        Clear the screen and re-initialize the painter.

        :return: None
        """

        # Erase everything on the screen.
        self.painter.clear()
        # Tell the turtle to use the max speed.
        self.painter.speed(0)
