class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        res=[]
        for i in range(0,len(hours)):
            if hours[i]>=target:
                res.append(i)
        return len(res)
        