class Line:
    def init(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.vect = [dx - x, dy - y]
        self.a = ((dy - y) / (dx - x))
        self.b = (y - (self.a*x))

    def mathvect(self, line):
        self.vect1 = [line.x - self.x, line.y - self.y]
        self.vect2 = [line.dx - self.x, line.dy - self.y]
    def mathl(self):
        self.l1 = (self.vect[0] * self.vect1[1]) - (self.vect1[0] * self.vect[1])
        self.l2 = (self.vect[0] * self.vect2[1]) - (self.vect[1] * self.vect2[0])
    def mathL(self):
        self.L = self.l1 * self.l2
        return (self.L < 0)

def mathlines(line1, line2):
    line2.mathvect(line1)
    line2.mathl()
    a = line2.mathL()
    line1.mathvect(line2)
    line1.mathl()
    if (line1.mathL()) and a:
        return True
    else:
        return False

if mathlines(line1, line2):
    x = ((line2.b - line1.b) / (line1.a - line2.a))
    y = ((line1.a*x) + line1.b)
    dot = [x, y]
    print(dot)
