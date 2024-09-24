
import random


def main():
    """Get score and print the result"""
    score = float(input("Enter score: "))
    print(determine_status(score))
    """Generate a random score and determine its status"""
    random_score = random.randint(0,100)
    print(f"Random score:{random_score}")
    print(determine_status(random_score))


def determine_status(score):
    """Determine the status of a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
