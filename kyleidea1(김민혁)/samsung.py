def combination(arr, r):
    res = []
    def backtrack(start,cur):
        if len(cur) == r:
            res.append(cur[:])
            return
        for i in range(start,len(arr)):
            cur.append(arr[i])
            backtrack(i+1,cur)
            cur.pop()
    backtrack(0,[]) # 0번부터
    return res

def combination(arr,r):
    res = []
    
    def backtrack(start,cur):
        if len(cur) == r:
            res.append(cur[:])
            return
        for i in range(start,len(arr)):
            cur.append(arr[i])
            backtrack(i+1,cur)
            cur.pop()
    

def combination(arr,r):
    res = []
    def backtrack(start,cur):
        if len(cur) == r:
            res.append(cur[:])
            return
        for i in range(start,cur):
            cur.append(arr[i])
            backtrack(i+1,cur)
            cur.pop()
    backtrack(0,[])
    return res

def combination(arr,r):
    res = []
    def backtrack(start,cur):
        if len(cur) == r:
            res.append(cur[:])
        for i in range(start,len(arr)):
            cur.append(arr[i])
            backtrack(i+1,cur):
            cur.pop()
    backtrack(0,[])
    