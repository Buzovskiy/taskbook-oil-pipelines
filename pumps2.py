class Pumps:
    H0 = a = b = None

    def __init__(self, liquid):
        if liquid == 'water':
            self.H0 = 283  # m
            self.a = 0
            self.b = 35.4e-6  # hr2/m5
        elif liquid == 'oil':
            self.H0 = 276  # m
            self.a = 0
            self.b = 37.2e-6  # hr2/m5

    def head(self, Q):
        """
        Return the head of a pump
        :param Q: volume flow, m3/hr
        :return: head, m
        """
        return self.H0 + self.a * Q - self.b * Q ** 2
