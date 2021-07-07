class Solution(object):
    def largestAltitude(self, gain):
        self.gain = []
        cnt = highest = 0
         
        for i in range(len(gain)):
            cnt += gain[i]
            if cnt > highest:
                highest = cnt
        
        return highest