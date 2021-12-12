class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flayable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship = FlyableUnit()
# 다중 상속을 받았을 때
# super를 사용하면 먼저 사용한 부모를 호출한다.