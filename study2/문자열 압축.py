def solution(s):
    minn = len(s)

    for i in range(1, len(s) // 2 + 1):
        zips = ""
        ori = ""
        cnt = 1
        start = 0
        while start < len(s):
            if start + i <= len(s) and ori[-i:] == s[start:start + i]:
                cnt += 1
            else:
                if cnt > 1:
                    zips += str(cnt)
                    cnt = 1
                zips += ori[-i:]

            if start + i <= len(s):
                ori += s[start:start + i]
            start += i

        # 마지막에 대한 예외 처리
        last_idx = len(s) % i if len(s) % i != 0 else i
        end = str(cnt) + s[-last_idx:] if cnt > 1 else s[-last_idx:]
        zips += end

        minn = min(minn, len(zips))

    return minn