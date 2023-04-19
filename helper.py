class myClass:

    def __init__(self, m, c):
        self.m = m
        self.c = c
        self.a = []
        self.b = []

    def reverse(self,x):
        for i in range(len(x) // 2):
            temp = x[i]
            x[i] = x[len(x) - 1 - i]
            x[len(x) - 1 - i] = temp
        return x

    def irreducibility_check(self):
        for i in range(1 << self.m):
            s = bin(i)[2:]
            s = '0' * (self.m - len(s)) + s
            # print(list(s))
            s = list(map(int, list(s)))
            # print(s[1:m])
            if (s[1:self.m] != [0 for i in range(self.m - 1)]):
                chk = [self.c[i] for i in range(self.m + 1)]
                q, r = self.division(chk, s)
                if (r == [0 for i in range(self.m)]):
                    # print(
                    #     "Your polynomial is not irreducible over F_2. Please try again with some irreducible polynomial...")
                    return False

        return True

    def division(self,a, b):
        for t in range(len(b) - 1, -1, -1):
            if (b[t] == 1):
                break
        q = [0 for i in range(self.m)]
        for i in range(len(a) - 1, -1, -1):
            if (a[i] == 1) and (i > (t - 1)):
                for j in range(t + 1):
                    a[i - j] = (a[i - j] + b[t - j]) % 2
                    q[i - t] = 1

        # print(c)
        return q, a[0:self.m]



    def add(self,a, b):
        return [(a[i] + b[i]) % 2 for i in range(self.m)]

    def multiply(self,a, b):
        s = [0 for i in range(2 * self.m - 1)]
        for i in range(2 * self.m - 1):
            for j in range(i + 1):
                if ((j < self.m) and ((i - j) < self.m)):
                    s[i] = (s[i] + a[j] * b[i - j]) % 2
        q, r = self.division(s, self.c)
        # print(c)
        print(r)
        return r

    def gcd(self,a, b):
        for i in range(len(b) - 1, 0, -1):
            if (b[i] == 1):
                q, r = self.division(a, b)
                u, v = self.gcd(b, r)
                v1 = self.multiply(q, v)
                v2 = self.add(u, v1)
                return v, v2
        u = [0 for i in range(self.m)]
        v = [0 for i in range(self.m)]
        u[0] = 1
        # print(c)
        if b[0] == 1:
            return v, u
        else:
            return u, v

    def print_result(self,x):
        temp = ""
        # print(x)
        for i in range(len(x)-1, 0, -1):
            if x[i] == 1:
                if i != 1:
                    temp = temp + "x^" + str(i) + " + "
                else:
                    temp = temp + "x + "
        if x[0] != 0:
            temp += str(x[0])
        else:
            temp = temp.strip(' + ')
        return temp


