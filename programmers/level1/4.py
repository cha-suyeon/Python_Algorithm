# 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant,completion):
        if p != c:
            return p
    return participant.pop()