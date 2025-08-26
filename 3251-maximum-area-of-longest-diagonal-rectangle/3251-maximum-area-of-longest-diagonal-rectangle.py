class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        Max = 0
        result = 0
        for l, w in dimensions:
            d = sqrt(l * l + w * w)

            if d > Max:
                Max = d
                result = l * w
            elif d == Max:
                result = max(result, l * w)
        return result

        