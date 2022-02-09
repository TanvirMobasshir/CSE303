def get_data(n):
    marks_list = []
    credit_list = []
    for i in range(n):
        print(f"Enter values for Course {i + 1}:")
        x = float(input(f"\tCredit: "))
        a = float(input(f"\tMarks: "))
        credit_list.append(x)
        marks_list.append(a)
        print()

    return [marks_list, credit_list]


def assign_grade(marks_list):
    grade_list = []

    for i in marks_list:
        if 100 >= i >= 95:
            grade_list.append(['A', 4.0])

        if 94 >= i >= 85:
            grade_list.append(['B', 3.5])

        if 84 >= i >= 70:
            grade_list.append(['C', 3.0])

        if 69 >= i >= 60:
            grade_list.append(['D', 2.5])

        if 59 >= i >= 0:
            grade_list.append(['F', 0.0])

    return grade_list


def display_grades(grade_list):
    j = 1
    for i in grade_list:
        print(f'Course {j}:')
        print(f'\tGrade: {i[0]}, Grade Point: {i[1]}')
        print()
        j += 1


def term_gpa(grade, credit):
    sum_credit = 0
    sum_grade = 0
    for i in credit: sum_credit = sum_credit + i
    for j in range(len(grade)):
        sum_grade = sum_grade + (credit[j] * grade[j][1])

    return str("{:.2f}".format(sum_grade / sum_credit))


if __name__ == "__main__":

    print("Student ID: 2019-2-60-025\n")

    marks = get_data(3)
    grades = assign_grade(marks[0])
    display_grades(grades)
    print()
    print('Term GPA: ' + term_gpa(grades, marks[1]))
