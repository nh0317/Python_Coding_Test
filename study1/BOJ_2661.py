import sys
import itertools

input = sys.stdin.readline

has_answer = False


def make_sequence(sequence):
    global has_answer
    if len(sequence) == N and not has_answer:
        print(sequence)
        has_answer = True
        return
    elif has_answer:
        return

    for i in range(1, 4):
        if promising(sequence + str(i)):
            # print("pass",sequence+str(i))
            make_sequence(sequence + str(i))
            if has_answer:
                return


def promising(sequence):
    n = len(sequence)
    if n == 1:
        return True
    for i in range(1, (n // 2) + 1):
        if sequence[-i:] == sequence[-2 * i:-i]:
            return False
    return True


N = int(input())
make_sequence("")
