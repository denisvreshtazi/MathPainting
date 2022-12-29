class Rectangle:
    """
    Rectangle:
            x
            y
            width
            height
            color
            draw(canvas)
    """

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """Draw itself into canvas"""
        canvas.data[self.x: self.x + self.width, self.y: self.y + self.height] = self.color
