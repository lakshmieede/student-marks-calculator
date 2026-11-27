def calculate_composite(a, b, c):
    return round(a*0.2 + b*0.3 + c*0.5, 2)

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    return "F"

a = 80
b = 90
c = 70

total = calculate_composite(a, b, c)

print("Total:", total)
print("Grade:", calculate_grade(total))
