def solution(my_string, overwrite_string, s):
    num = s + len(overwrite_string)
    answer = my_string[0:s]+overwrite_string+my_string[num:]
    return answer