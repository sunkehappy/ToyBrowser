class Color:
    def __init__(self, r=0, g=0, b=0, a=1, hex_str=None):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        if hex_str:
            self.init_with_hex_str(hex_str)

    def init_with_hex_str(self, hex_str):
        if hex_str.startswith("#"):
            hex_str = hex_str[1:]
        elif hex_str.startswith("0x") or hex_str.startswith("0X"):
            hex_str = hex_str[2:]
        self.r = int(hex_str[:2], 16)
        self.g = int(hex_str[2:4], 16)
        self.b = int(hex_str[4:6], 16)

    def __eq__(self, other):
        if other is None:
            return False
        return self.r == other.r and \
            self.g == other.g and \
            self.b == other.b and \
            self.a == other.a

    def __str__(self):
        if self.a != 1:
            return "0x%02X%02X%02X %1f" % (self.r, self.g, self.b, self.a)
        else:
            return "0x%02X%02X%02X" % (self.r, self.g, self.b)

    def __repr__(self):
        return self.__str__()
