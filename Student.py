def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "S"
    elif 80 <= avg <= 89:
        return "A"
    elif 65 <= avg <= 79:
        return "B"
    elif 50 <= avg <= 64:
        return "C"
    elif 40 <= avg <= 49:
        return "D"
    else:
        return "F"


def main():
    name = "Vaishnavi"
    dept = "BCA"
    sem = "3rd semester"

    
    m1 = float(92)
    m2 = float(94)
    m3 = float(89)

    avg = (m1 + m2 + m3) / 3
    grade = calculate_grade(avg)

    print("\n----- STUDENT RESULT -----")
    print("Name       :", name)
    print("Department :", dept)
    print("Semester   :", sem)
    print("Average    :", round(avg, 2))
    print("Grade      :", grade)


if __name__ == "__main__":
    main()
