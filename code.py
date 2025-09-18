class Solution:
    def jobSequencing(self, deadline, profit):
        
        maxDeadline=0
        for i in range(len(deadline)):
            maxDeadline=max(maxDeadline, deadline[i])
        
        #scheduler = [-1]*maxDeadline
        scheduler = set()
        for i in range(maxDeadline):
            scheduler.add(i)
            
        input = []
        for i in range(len(deadline)):
            input.append([profit[i],deadline[i]])

        input.sort(reverse=True)

        maxEarn = 0
        maxJob = 0
        for i in range(len(input)):
            x=0
            while input[i][1]-1-x>=0:
                if input[i][1]-1-x in scheduler:
                    scheduler.remove(input[i][1]-1-x)
                    maxEarn +=input[i][0]
                    maxJob += 1
                    break
                x += 1 
            if maxJob == maxDeadline:
                break
        return maxJob, maxEarn
            