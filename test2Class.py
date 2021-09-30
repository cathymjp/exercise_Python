def open_account():
    print("새로운 계좌가 생성되었습니다")


def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


# balance = 0
# balance = deposit(balance, 1000)
# # balance = withdraw(balance, 500)
#
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0}원 이며, 잔액은 {1}원 입니다.".format(commission, balance))
# print(balance)
# print("")
# open_account()


def profile(name, age, main_lang):
    print("이름: {0}\t\t나이: {1}\t\t주 사용 언어: {2}".format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 20, "자바")


# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t\t나이: {1}\t\t주 사용 언어: {2}".format(name, age, main_lang))


profile("유재석")
profile("김태호")


def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name="유재석", main_lang="파이썬", age=20)
profile(age=30, main_lang="C", name="김태호")
