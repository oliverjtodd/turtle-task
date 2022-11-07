from turtle import Turtle


class DrawShapes:
    def __init__(self, labels: bool) -> None:
        self.t = Turtle()
        self.labels = labels

    def pentagon(self) -> None:
        """A regular pentagon with a radius of 70"""
        self.t.penup()
        self.t.goto((-400, 0))
        self.t.pendown()
        self.t.circle(radius=70, steps=5)
        if self.labels is True:
            self.t.penup()
            self.t.goto((-400, -20))
            self.t.pendown()
            self.t.write("A regular pentagon with a radius of 70")

    def hexagon(self) -> None:
        """A regular hexagon with a radius of 80"""
        self.t.penup()
        self.t.goto((0, 0))
        self.t.pendown()
        self.t.circle(radius=80, steps=6)
        if self.labels is True:
            self.t.penup()
            self.t.goto((0, -20))
            self.t.pendown()
            self.t.write("A regular hexagon with a radius of 80")

    def polygon(self) -> None:
        """A regular polygon with a radius of 90"""
        self.t.penup()
        self.t.goto((400, 0))
        self.t.pendown()
        self.t.circle(radius=90, steps=17)
        if self.labels is True:
            self.t.penup()
            self.t.goto((400, -20))
            self.t.pendown()
            self.t.write("A regular polygon with a radius of 90")

    def watermark(self) -> None:
        if self.labels is True:
            self.t.penup()
            self.t.goto((0, -70))
            self.t.pendown()
            self.t.write("By Oliver Todd")


s = DrawShapes(labels=True)
s.pentagon()
s.hexagon()
s.polygon()
s.watermark()

input()
