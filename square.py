class Square:
    """
    Square:
            x
            y
            side
            color
            draw(canvas)
    """

    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """Draw itself into canvas"""
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color

