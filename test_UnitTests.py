
def WhoAmI():
    return('sd3965')
x=WhoAmI()
print(x)
        

def getBondPrice(y, face, couponRate, m, ppy=1):
    r = y / ppy              
    n = m * ppy              
    C = face * couponRate / ppy  
    bondPrice = 0
    for t in range(1, n + 1):
        bondPrice += C / ((1 + r) ** t)
    bondPrice += face / ((1 + r) ** n)
    return bondPrice

getBondPrice(0.03,20000000,0.04,10)


def getBondDuration(y, face, couponRate, m, ppy=1):
    r = y / ppy
    n = m * ppy
    C = face * couponRate / ppy
    price = 0
    weighted_sum = 0

    for t in range(1, n + 1):
        cf = C
        if t == n:
            cf = C + face
        pv = cf / ((1 + r) ** t)
        price += pv
        weighted_sum += (t / ppy) * pv  

    bondDuration = weighted_sum / price
    return bondDuration

getBondDuration(0.03,20000000,0.04,10)


def getBondPrice_E(face, couponRate, m, yc):
    C = face * couponRate
    bondPrice = 0
    discount_factor = 1

    for t, rate in enumerate(yc, start=1):
        discount_factor *= (1 + rate)
        cf = C
        if t == m:
            cf = C + face

        bondPrice += cf / discount_factor

    return bondPrice
getBondPrice_E(20000000,.04,5,[.010,.015,.020,.025,.030])


def getBondPrice_Z(face, couponRate, times, yc):
    C = face * couponRate
    bondPrice = 0

    for t, rate in zip(times, yc):

        if t == times[-1]:   
            cf = C + face
        else:
            cf = C

        bondPrice += cf / ((1 + rate) ** t)

    return bondPrice
getBondPrice_Z(2000000,.04,[1,1.5,3,4,7],[.010,.015,.020,.025,.030])

    

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


print(FizzBuzz(1, 15))
