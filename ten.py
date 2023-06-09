class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.pose = "A"

    def start(self):
        if self.pose == "A":
            self.pose = "B"
            return 0
        if self.pose == "B":
            self.pose = "C"
            return 1
        if self.pose == "C":
            self.pose = "A"
            return 3
        if self.pose == "F":
            self.pose = "A"
            return 8
        raise MealyError("start")

    def stay(self):
        if self.pose == "F":
            self.pose = "B"
            return 7
        if self.pose == "D":
            self.pose = "E"
            return 4
        if self.pose == "E":
            self.pose = "F"
            return 5
        if self.pose == "G":
            self.pose = "A"
            return 9
        raise MealyError("stay")

    def order(self):
        if self.pose == "C":
            self.pose = "D"
            return 2
        if self.pose == "F":
            self.pose = "G"
            return 6
        raise MealyError("order")


def main():
    return StateMachine


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o1 = main()
    raises(lambda: o1.stay(), MealyError)
    raises(lambda:  o1.order(), MealyError)
    assert


