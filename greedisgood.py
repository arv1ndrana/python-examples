def score(dice):

    roll_string = "".join(str(roll) for roll in dice)
    one = two = three = four = five = six = 0
    score = 0

    one = roll_string.count("1")
    two = roll_string.count("2")
    three = roll_string.count("3")
    four = roll_string.count("4")
    five = roll_string.count("5")
    six = roll_string.count("6")

    if one >= 3:
        score += 1000
        one -= 3
    elif five >= 3:
        score += 500
        five -= 3
    elif six >= 3:
        score += 600
    elif four >= 3:
        score += 400
    elif three >= 3:
        score += 300
    elif two >= 3:
        score += 200

    if one < 3:
        score += 100 * one
    if five < 3:
        score += 50 * five

    return score
