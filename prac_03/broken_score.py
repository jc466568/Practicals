
def main():
    score = float(input("Enter score: "))
    print(determine_achievement(score))


def determine_achievement(score):
    if score < 0:
        return "Invalid score"
    elif score > 100:
        return "Invalid score"
    elif 50 < score < 90:
        return "Pass"
    elif 90 < score < 100:
        return "Excellent"
    else:
        return "Bad"


main()
