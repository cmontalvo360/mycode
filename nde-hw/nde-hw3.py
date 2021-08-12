def grade(scores):
    letter_grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for score in scores:
        if score > 89:
            letter_grades["A"] += 1
        elif score > 79:
            letter_grades["B"] += 1
        elif score > 69:
            letter_grades["C"] += 1
        elif score > 59:
            letter_grades["D"] += 1
        else:
            letter_grades["F"] += 1
    return letter_grades

grades = [50, 99, 89, 98, 67, 75, 67, 77, 87, 88]

print(grade(grades))
