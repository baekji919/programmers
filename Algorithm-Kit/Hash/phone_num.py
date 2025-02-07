def solution(phone_book):
    phone_book.sort()
    print(phone_book)

    # 방법 1 - 효율성 검사 떨어짐
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False
            elif phone_book[j].startswith(phone_book[i]):
                return False

    # 방법 2
    for i in range(len(phone_book) -1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))