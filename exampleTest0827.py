def correct_sentence(text, symbol):
    if text.count(symbol) < 2:
        return None
    first = text.find(symbol)
    return text.find(symbol, first + 1)


# print(correct_sentence("hi", " "))

v = list(range(10))

# for i in v:
#     print(i)


print(" ".join([str(i) for i in v]))


words = ["Hello", "hi", "Yes", "right", "no"]
new_words = []

list1 = [1, 2, 3]

for i in list1:
    for j in list1:
        print(i * j, end=" ")
print("\n")
# print("NEW WORDS", new_words)

test = [i*j for j in list1 for i in list1]
print("testing", test)
test2 = [i * j for i in list1 for j in list1]
print("testing2", test2)
# new_words2 = [ word for word in words if len(word) > 3 ]
# # new_words3 = [word for ]
# print("new words2", new_words2)

func = lambda x : x + 1
print(func(3))

what = list(map(lambda x: x ** 2, range(6)))
print(what)

from functools import reduce
print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))
print(reduce(lambda x, y: y + x, [0, 1, 2, 3, 4]))
print(reduce(lambda x, y: x + y, "abcde"))
print(reduce(lambda x, y: y + x, "abcde"))


def missing_participant(participant, completion):
    hash = {}
    print("hash", hash)
    for i in participant:
        if i in hash:
            hash[i] += 1
            # print("hash2: ", hash)
        else:
            hash[i] = 1
            # print("hash[{}]".format(i), hash[i])
    for i in completion:
        if hash[i] == 1:
            del hash[i]
        else:
            hash[i] -= 1
    answer = list(hash.keys())[0]
    return answer


print(missing_participant(["leo", "kiki", "eden"], ["eden", "kiki"]))


def phone_number_has(phone_book):
    answer = True
    finish = False
    phone_book = sorted(phone_book, key=len)
    print("sorted", phone_book)
    print(len(phone_book))
    for i in range(0, len(phone_book)):
        if finish:
            break
        current = phone_book[i]
        print("current", current)
        for j in range(i + 1, len(phone_book)):
            comp = phone_book[j]
            if len(current) < len(comp) and current == comp[0:len(current)]:
                answer= False
                finish = True
                break
    return answer


print(phone_number_has(["119", "97674223", "1195524421"]))
print(phone_number_has(["123", "456", "789"]))


def top_height(heights):
    answer = [0 for _ in range(len(heights))]
    for i in reversed(range(len(heights))):
        print("reversed(range(len(heights)))", (range(len(heights))))
        cur = 0
        for j in range(i):
            print("range(i)", range(i))
            print("heights[i], heights[j]", heights[i], heights[j])
            if heights[i] < heights[j]:
                cur = j + 1
        answer[i] = cur

    return answer


print(top_height([1, 5, 3, 6, 7, 6, 5]))


def appeach(s):
    result = []
    if len(s) == 1:
        return 1

    for i in range(1, (len(s) // 2) + 1):
        b = ''
        cnt = 1
        tmp = s[:i]

        for j in range(i, len(s) , i):
            if tmp == s[j:i+j]:
                cnt += 1
            else:
                if cnt != 1:
                    b = b + str(cnt) + tmp
                else:
                    b = b + tmp
                tmp = s[j: j + i]
                cnt = 1

        if cnt != 1:
            b = b + str(cnt) + tmp
        else:
            b = b + tmp

        result.append(len(b))
    return min(result)


print(appeach("aabbaccc"))


def ternary(number):
    result = []
    sum = 0

    while number != 0:
        result.append(number % 3)
        number = number // 3

    for i in range(len(result)):
        sum = sum + ((3 ** (len(result) - i - 1)) * result[i])

    return sum


print("TERNARY: ", ternary(45))


from collections import defaultdict


def shopping_gem(gems):
    begin, end = 0, 0
    all_kind_length = len(set(gems))
    now_dict = defaultdict(int)
    ans_list = []

    while begin < len(gems):
        now_size = len(now_dict.keys())
        if now_size < all_kind_length and end < len(gems):
            now_dict[gems[end]] += 1
            end += 1
        else:
            while all_kind_length <= len(now_dict.keys()) and begin < end:
                now_size = len(now_dict.keys())
                now_dict[gems[begin]] -= 1
                if now_dict == all_kind_length:
                    ans_list.append([begin + 1, end])
                begin += 1

            else:
                now_dict[gems[begin]] -= 1
                if now_dict[gems[begin]] == 0:
                    now_dict.pop(gems[begin])
                begin += 1

    return sorted(ans_list, key=lambda x: (x[1] - x[0], x [0]))[0]


def day_of_year(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    my_sum = b
    while True:
        a = a - 1
        if a < 1:
            break
        b = months[a]
        my_sum += b

    answer = days[(my_sum - 1) % 7]
    return answer


print(day_of_year(5, 24))


import heapq


# 숫자들을 더해서 K를 넘지 않는 조합 만들기
def scoville(scoville, K):
    answer = 0
    heap = []
    for h in scoville:
        heapq.heappush(heap, h)
    while True:
        current = heapq.heappop(heap)
        if len(heap) < 1 and current < K:
            answer = -1
            break
        if current >= K:
            break
        else:
            answer += 1
            next_node = heapq.heappop(heap)
            heapq.heappush(heap, current + next_node * 2)
    return answer


sc = [1, 2, 3, 9, 10, 12]
k = 7
print(scoville(sc, k))


from collections import deque

def printer_proriety(priorities, location):
    answer = 0
    priorities = deque(priorities)
    m = max(priorities)

    while True:
        v = priorities.popleft()
        if m == v:
            answer += 1
            if location == 0:
                break
            else:
                priorities.append(v)
                if location == 0:
                    location = len(priorities) - 1
                else:
                    location -= 1

    return answer
