class Range:
    def __init__(self, pointLower, pointUpper):
        if pointUpper < pointLower:
            raise TypeError('上端よりおおきい下端は設定できません')

        self.pointLower = pointLower
        self.pointUpper = pointUpper

    # def __hash__():

    def __eq__(self, other):
        return self.pointLower == other.pointLower and self.pointUpper == other.pointUpper

    # def __ne__(self, other):
    #     return True

    def __str__(self):
        return "[{0},{1}]".format(self.pointLower, self.pointUpper)

    def __contains__(self, other):
        if isinstance(other, Range):
            return self.pointLower <= other.pointLower and other.pointUpper <= self.pointUpper
        
        return self.pointLower <= other and other <= self.pointUpper
