class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        full = {} #last day filled
        zeros = [] #list of days where we can dry
        ans = [-1]*len(rains)

        for i,lake in enumerate(rains):
            if lake>0: #raining day
                if lake in full: # we need a dry day between last fill and now
                    last_fill_day = full[lake]

                    #find smallest zero day after last fill day
                    idx = bisect.bisect_right(zeros,last_fill_day)
                    if idx == len(zeros): # No available dry day
                        return []
                    dry_day = zeros[idx]
                    ans[dry_day]=lake  # dry that lake
                    zeros.pop(idx)  #

                full[lake]=i
                ans[i] = -1
            else:
                bisect.insort(zeros,i)
                ans[i]=1
        return ans                