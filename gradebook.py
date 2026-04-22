def letter_grade(score):
    if not isinstance(score,(int, float)):
        raise TypeError("Score must be a float or integer")
    
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "c"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_passing(score):
    if not isinstance(score,(int, float)):
        raise TypeError("Score must be a float or integer")
    return score >= 60


def average(scores):
    return round(sum(scores) / len(scores), 2)


def curved_score(score, bonus):
    pass 

