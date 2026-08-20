class solution:
    def merge(self,intervals):
        intervals.sort()
        ans=[]
        for interval in intervals:
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                ans[-1][1]=max(ans[-1][1],interval[1])
        return ans