from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []
    dic = defaultdict()
    amounts = defaultdict()

    # dic : parent를 저장
    # key = enroll, value = referral(parent)
    # amounts : 해당 사람이 번 금액을 저장
    for i in range(len(enroll)):
        dic[enroll[i]] = referral[i]
        amounts[enroll[i]] = 0

    for i in range(len(seller)):
        # 현재 seller가 번 돈을 저장
        p = seller[i]
        a = amount[i] * 100
        amounts[p] += a

        # 부모가 없을 때까지
        while dic[p] != "-":
            # 현재 번 돈에서 10%를 빼고, parent에게 준다.
            amounts[p] -= int(a * 0.1)
            p = dic[p]  # 부모 찾기
            amounts[p] += int(a * 0.1)

            # 자식에게 받은 금액
            a = int(0.1 * a)

            # 0이면 올려주지 않아도 된다!
            # 시간 초과 원인
            if a == 0:
                break
        amounts[p] -= int(a * 0.1)

    # 금액만 리스트로 반환
    answer = list(amounts.values())
    return answer