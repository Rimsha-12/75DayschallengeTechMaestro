def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s+=str(i)
        s=int(s)
        s=s+1
        s=str(s)
        l=[]
        for i in s:
            l.append(i)
        return l