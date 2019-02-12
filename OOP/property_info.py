# property 기법: 외부에서 마치 멤버에 바로 접근하는 것처럼 보이지만
# 실제로는 메서드로 접근하는 것

class Person:
    def __init__(self, name, money):
        self.name = name
        self.__money = money

    # getter : 멤버 값을 가져온다.
    @property
    def money(self):
        print("getter exceuted")
        return self.__money

    # setter : 
    @money.setter
    def money(self, amount):
        print("setter executed")
        self.__money = amount

if __name__ == "__main__":
    y = Person('yang', 1000)
    # getter : 멤버를 호출하는 것 처럼 보이지만 실제로는 getter를 호출하는 것이다
    print(y.money)
    # setter 호출
    
    y.money = 5000
    