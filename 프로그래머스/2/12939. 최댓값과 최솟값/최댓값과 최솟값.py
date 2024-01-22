def solution(s):
    numbers = [ int(n) for n in s.split(' ')]
    answer = str(min(numbers)) +' ' + str(max(numbers))
    return answer