def find_parent(parent, x):
    
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    # 부모 찾고
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

def solution(n, computers):
    answer = 0
    parent = [i for i in range(n)]
        
    # 반만 확인해서 union 연산
    for i in range(n):
        for j in range(n):
            
            if computers[i][j] == 1:
                union_parent(parent, i, j)
    
    # 네트워크 개수 확인
    roots = []
    for p in parent:
        roots.append(find_parent(parent, p))
    
    answer = len(set(roots))
        
    
    
    return answer