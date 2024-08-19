from typing import List

def solution(v: List[str]) -> str:
    ans=""
    v=sorted(v)
    first=v[0]
    last=v[-1]
    for i in range(min(len(first),len(last))):
        if(first[i]!=last[i]):
            return ans
        ans+=first[i]
    return ans

if __name__ == "__main__":
    print(solution(["flower", "flight", "flow"]))
