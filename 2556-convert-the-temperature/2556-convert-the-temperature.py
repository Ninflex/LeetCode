class Solution(object):
    def convertTemperature(self, celsius):
        ans = []
        fahr = celsius * 1.80 + 32.00
        kelvin = celsius + 273.15
        ans.append(kelvin)
        ans.append(fahr)
        return ans
        