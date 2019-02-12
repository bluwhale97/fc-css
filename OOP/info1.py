# 파이썬에서 정보 은닉을 제공하는 첫 번째 방법
# *파이썬에서는 정보 은닉을 완벽하게 제공하지는 않는다.
# 
# 클래스의 멤버는 실제로는 _ClassName__Member 식으로 저장이 된다
# 고로 클래스 밖에서 위와 같은 방법으로 접근은 가능하지만,
# OOP원칙에 위배되므로 사용하지 않는다.
#
# 

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    def get_age(self):
        return self.__age
if __name__ == "__main__":
    yang = Person('yang',18)

    yang.__age = 200
    print(yang.__age)
    print(yang.get_age())
    