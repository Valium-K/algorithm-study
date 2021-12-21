def solution(phone_book):
    phone_book_set = set(phone_book)
    min_len = len(min(phone_book, key=lambda x: len(x)))

    for phone_num in phone_book:
        for i in range(min_len, len(phone_num)):
            if phone_num[:i] in phone_book_set:
                return False

    return True