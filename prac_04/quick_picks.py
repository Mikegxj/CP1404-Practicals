import random
NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program"""
    number_quick_picks = int(input("How many qick picks you wish to generate?: "))
    while number_quick_picks < 0:
        print("number of quick picks cannot be 0!")
        number_quick_picks = int(input("How many qick picks you wish to generate?: "))

    for i in range(number_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM,MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()

