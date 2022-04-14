class Pumps:
    H0 = a = b = None

    def __init__(self, mark):
        if mark == 'ND10':
            self.H0 = 331.1  # m
            self.a = 0
            self.b = 0.082e-3  # hr2/m5
        elif mark == 'NM1250-260':
            self.H0 = 289.8  # m
            self.a = 0
            self.b = 0.0348e-3  # hr2/m5

    # Н = Н0 + а · Q – b · Q2
    def head(self, Q):
        """
        Return the head of a pump
        :param Q: volume flow, m3/hr
        :return: head, m
        """
        return self.H0 + self.a * Q - self.b * Q ** 2
