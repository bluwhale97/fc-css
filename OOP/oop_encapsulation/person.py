#클래스 만들기 (정의)
class Person:
    # 생성자(constructor)
    def __init__(self, name, age, money):
        self.name = name
        self.age = age
        self.money = money
        # instance member(변수)들이다.
        # 생성자는 어떤 객체가 메모리에 생성될때, 반드시 한번 호출된다.

    # 소멸자 : 객체가 메모리에서 사라질때 반드시 한번 호출하고 사라진다.
    # 파이썬에서는 갈비지 컬렉터가 있어 사용할 일이 거의 없다
    def __del__(self):
        pass

    # instance method
    def get_money(self, amount):
        self.money += amount

    def lose_money(self, amount):
        self.money += amount

    def get_old(self):
        self.age += 1

    def print_money(self):
        print("{} has {} ".format(self.name, self.money))
    
    # 메시지 패싱 (message passing)
    def give_money(self, other, amount):
        self.money -= amount        
        # 다른객체와 상호작용할 때
        # 다른 객체의 데이터를 조작, 수정해야 할때
        # 반드시 그 객체가 가지고 있는 함수를 호출해서 데이터를 수정한다.
        other.get_money(amount)

#객체 생성 (instance == 객체)
yang = Person("taehwan", 18, 1000)
kim = Person("paul", 19, 3000)

yang.give_money(kim, 500)
yang.print_money()
kim.print_money()

