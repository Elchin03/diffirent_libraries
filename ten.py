class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.pose = "A"

    def mix(self):
        if self.pose == "A":
            self.pose = "B"
            return 0
        if self.pose == "B":
            self.pose = "C"
            return 2
        if self.pose == "E":
            self.pose = "C"
            return 7
        if self.pose == "F":
            self.pose = "G"
            return 8
        raise MealyError("mix")

    def hike(self):
        if self.pose == "A":
            self.pose = "C"
            return 1
        if self.pose == "E":
            self.pose = "F"
            return 6
        if self.pose == "F":
            return 10
        if self.pose == "G":
            self.pose = "H"
            return 11
        raise MealyError("hike")

    def rig(self):
        if self.pose == "C":
            self.pose = "D"
            return 4
        if self.pose == "D":
            self.pose = "E"
            return 5
        if self.pose == "F":
            self.pose = "H"
            return 9
        if self.pose == "B":
            self.pose = "H"
            return 3
        raise MealyError("rig")


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o1 = main()
    raises(lambda: o1.rig(), MealyError)
    assert o1.mix() == 0 and o1.pose == "B"
    raises(lambda: o1.hike(), MealyError)
    assert o1.mix() == 2 and o1.pose == "C"
    raises(lambda: o1.mix(), MealyError)
    raises(lambda: o1.hike(), MealyError)
    assert o1.rig() == 4 and o1.pose == "D"
    raises(lambda: o1.mix(), MealyError)
    raises(lambda: o1.hike(), MealyError)
    assert o1.rig() == 5 and o1.pose == "E"
    raises(lambda: o1.rig(), MealyError)
    assert o1.hike() == 6 and o1.pose == "F"
    assert o1.hike() == 10 and o1.pose == "F"
    assert o1.mix() == 8 and o1.pose == "G"
    raises(lambda: o1.mix(), MealyError)
    raises(lambda: o1.rig(), MealyError)
    assert o1.hike() == 11 and o1.pose == "H"
    raises(lambda: o1.mix(), MealyError)
    raises(lambda: o1.rig(), MealyError)
    raises(lambda: o1.hike(), MealyError)

    o2 = main()
    assert o2.hike() == 1 and o2.pose == "C"
    o2.rig()
    o2.rig()
    assert o2.mix() == 7 and o2.pose == "C"
    o2.rig()
    o2.rig()
    o2.hike()
    assert o2.rig() == 9 and o2.pose == "H"

    o3 = main()
    o3.mix()
    assert o3.rig() == 3 and o3.pose == "H"


test()
