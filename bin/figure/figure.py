from figure.Point import Point


class Figure:
    a = b = c = 0
    start = -1
    end = 1
    step = 1

    def __init__(self):
        pass

    def set_a(self, a=0):
        self.a = a

    def get_a(self):
        return self.a

    def set_b(self, b=0):
        self.b = b

    def get_b(self):
        return self.bt

    def set_c(self, c=0):
        self.c = c

    def get_c(self):
        return self.c

    def set_start_range(self, start=-1):
        self.start = start

    def get_start_range(self):
        return self.start

    def set_range_step(self, step=1):
        try:
            if step == 0:
                raise Exception("Step can not be 0.")
            else:
                self.step = step
        except Exception as e:
            print(str(e) + " Step set to 1")
            self.step = 1

    def get_range_step(self):
        return self.step

    def set_end_range(self, end=1):
        self.end = end

    def get_end_range(self):
        return self.end

    def calculate(self):
        sets = []
        sets.append(Point())
        return sets

    def set_all(self, dict):
        self.set_a(dict.get('a'))
        self.set_b(dict.get('b'))
        self.set_c(dict.get('c'))
        self.set_start_range(dict.get('start'))
        self.set_end_range(dict.get('stop'))
        self.set_range_step(dict.get('step'))