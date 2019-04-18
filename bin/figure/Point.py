class Point:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        pass

    def __str__(self):
        return '{"x": ' + str(self.get_x()) + ', "y": ' + str(self.get_y()) + '}'

    def set_x(self, inx):
        self.x = inx

    def set_y(self, iny):
        self.y = iny

    def set_z(self, inz):
        self.z = inz

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_point(self):
        return {'x':self.get_x(), 'y':self.get_y()}
