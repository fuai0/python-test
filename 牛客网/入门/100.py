class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        self.x = self.x + other.x
        self.y = self.y + other.y
        return self


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

c1 = Coordinate(x1, y1)
c2 = Coordinate(x2, y2)

print(c1 + c2)
