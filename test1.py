# print("Red Apple\rPine")
#
# # url = "http://naver.com"
# url = "http://google.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# print("my_str", my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(password)
#
#
# subway = ["유재석", "조세호", "박명수"]
#
# subway.append("하하")
# subway.insert(1, "정형돈")
# print("subway", subway)


# for waiting_no in [0, 1, 2, 3, 4]:
# for waiting_no in range(5):
#     print("대기번호: {0}".format(waiting_no))


# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")
#
# customer2 = "아이언맨"
# person = "Unknown"
#
# while person != customer2:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")

absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))