def WhoAmI():
    return "sd3965"


def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y / ppy
    n = m * ppy
    C = face * couponRate / ppy
    bondPrice = 0.0

    for t in range(1, n + 1):
        bondPrice += C / ((1 + r) ** t)

    bondPrice += face / ((1 + r) ** n)
    return bondPrice


def getBondDuration(y, face, couponRate, m, ppy=1):
    r = y / ppy
    n = m * ppy
    C = face * couponRate / ppy

    price = 0.0
    weighted_sum = 0.0

    for t in range(1, n + 1):
        cf = C + face if t == n else C
        pv = cf / ((1 + r) ** t)
        price += pv
        weighted_sum += (t / ppy) * pv  

    return weighted_sum / price


def getBondPrice_E(face, couponRate, m, yc):
    C = face * couponRate
    bondPrice = 0.0

    for t, rate in enumerate(yc, start=1):
        cf = C + face if t == m else C
        bondPrice += cf / ((1 + rate) ** t)

    return bondPrice


def getBondPrice_Z(face, couponRate, times, yc):
    C = face * couponRate
    bondPrice = 0.0

    for t, rate in zip(times, yc):
        cf = C + face if t == times[-1] else C
        bondPrice += cf / ((1 + rate) ** t)

    return bondPrice


def FizzBuzz(start, finish):
    outlist = []
    for i in range(start, finish + 1):
        if i % 15 == 0:
            outlist.append("FizzBuzz")
        elif i % 3 == 0:
            outlist.append("Fizz")
        elif i % 5 == 0:
            outlist.append("Buzz")
        else:
            outlist.append(i)
    return outlist



if __name__ == "__main__":
    print(WhoAmI())
    print(getBondPrice(0.03, 2000000, 0.04, 10))
    print(getBondPrice(0.03, 2000000, 0.04, 10, 2))
    print(getBondDuration(0.03, 2000000, 0.04, 10))
    print(getBondPrice_E(2000000, 0.04, 5, [0.010, 0.015, 0.020, 0.025, 0.030]))
    print(getBondPrice_Z(2000000, 0.04, [1, 1.5, 3, 4, 7], [0.010, 0.015, 0.020, 0.025, 0.030]))
    print(FizzBuzz(1, 15))