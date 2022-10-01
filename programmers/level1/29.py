a = ["marina", "josipa", "nikola", "vinko", "filipa"]
b = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant,completion):
        if p != c:
            return p
    print(participant)
    return participant.pop()


print(solution(a,b))