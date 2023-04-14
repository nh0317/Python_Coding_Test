from collections import defaultdict

def solution(record):
    uids = defaultdict(str)
    res = []
    for command in record:
        cmd = command.split(" ")[0]
        
        if cmd == "Enter":
            cmd, uid, name = command.split(' ')
            res.append([uid, '님이 들어왔습니다.'])
            uids[uid] = name
            
        elif cmd == "Leave":
            cmd, uid = command.split(' ')
            res.append([uid, '님이 나갔습니다.'])
            
        elif cmd == "Change":
            cmd, uid, name = command.split(' ')
            uids[uid] = name

    answer = []
    for uid, msg in res:
        answer.append(uids[uid]+msg)
        
    
    return answer