

bills = [5,5,10,10,5,20,5,10,5,5]
def lemonadeChange():
    fives = 0
    tens = 0

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives > 1:
                fives -= 1
                tens += 1
            else:
                return False
        elif bill == 20:
            if tens >= 1 and fives >= 1:
                fives -= 1
                tens -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True
"""    collected = []

    for bill in bills:
        if bill == 5:
            collected.append(bill)
            print(collected)
        elif bill == 10:
            if 5 in collected:
                collected.remove(5)
                collected.append(bill)
                print(collected)
            else:
                return False
        elif bill == 20:
            if 10 in collected and 5 in collected:
                collected.remove(5)
                collected.remove(10)
                collected.append(bill)
                print(collected)
            elif collected.count(5)>=3:
                for i in range(3):
                    collected.remove(5)
                collected.append(bill)
                print(collected)
            else:
                return False

            return True"""

print(lemonadeChange())