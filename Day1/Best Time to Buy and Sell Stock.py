def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        l=[]
        for j in range(len(prices)):
            if prices[i]>=prices[j]:
                i=j
                j+=1
            else:
                diff=prices[i]-prices[j]
                l.append(abs(diff))
                j+=1
        if len(l)==0:
            return 0
        else:
            return max(l)
