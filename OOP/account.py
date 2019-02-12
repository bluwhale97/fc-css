# 클래스 멤버, 클래스 메서드
# 전역 변수와 전역 함수를 대체

class Account:
    # class member
    # 객체가 하나도 없어도 접근이 가능
    acnt_num = 0

    # class method
    @classmethod
    def get_account_num(cls):
        return cls.acnt_num

    # 대체 생성자(alternative constructor)
    # '<customer>_<balance>' 처럼 데이터가
    # 원하는 바와 다르게 들어왔다고 할때 사용한다.
    @classmethod
    def init_from_string(cls, string):
        cust, bal = string.split('_')
        return cls(cust, int(bal))
    
    # customer : string, balance : number
    def __init__(self, costomer, balance):
        self.costomer = costomer
        self.balance = balance
        Account.acnt_num += 1

    def deposit(self, amount):
        if amount <= 0:
            return
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("잔고가 부족합니다. \n")
            return False

        self.balance-=amount
        return amount

    # message passing 활용하여 채우기
    def transfer(self, other, amount):
        
        flag = self.withdraw(amount)
        if flag == False:
            print("송금을 실패하였습니다.\n")
            return False

        # messege passing
        other.deposit(amount)
        print("송금되었습니다. \n")
        return True

    def __str__(self):
        return '{} : {}'.format(self.costomer, self.balance)

if __name__ == "__main__":
    acc1 = Account('yang', 4000)
    acc2 = Account('kim', 2000)

    acc1.transfer(acc2,1000)
    print(acc1)
    print(acc2)

    print(Account.get_account_num())