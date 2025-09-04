class Solution(object):
    def findClosest(self, x, y, z):
        ydist, xdist = 0,0


        if x > z:
            xdist = x - z
        else:
            xdist = z - x
        if y > z:
            ydist = y - z
        else:
            ydist = z - y
        
        if xdist > ydist:
            return 2
        elif ydist > xdist:
            return 1
        else:
            return 0
        