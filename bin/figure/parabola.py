from figure.figure import Figure
from figure.Point import Point


class Parabola(Figure):
    def __init__(self):
        Figure.__init__(self)

    def calculate(self):
        x = int(self.start)
        return_list = []
        while x <= int(self.end):
            y = int(self.a) * pow(int(x), 2) + int(self.b) * int(x) + int(self.c)
            #print(str(x) + " : " + str(y))
            return_list.append(Point(x, y).get_point())
            x += int(self.step)
        return return_list

    def print_all_json(self):
        jsonStr = "{" + self.view_to_Json('a', self.get_a())
        jsonStr = jsonStr + ", " + self.view_to_Json('b', self.get_b())
        jsonStr = jsonStr + ", " + self.view_to_Json('c', self.get_c())
        jsonStr = jsonStr + ", " + self.view_to_Json('start', self.get_start_range())
        jsonStr = jsonStr + ", " + self.view_to_Json('stop', self.get_end_range())
        jsonStr = jsonStr + ", " + self.view_to_Json('step', self.get_range_step()) + "}"
        return jsonStr

    def view_to_json(self, parameter, value):
        return '"' + str(parameter) + '" :' + str(value)

