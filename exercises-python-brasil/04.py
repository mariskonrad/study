# Faça um programa que peça as 4 notas bimestrais e mostre a média.

def get_grades(grade1, grade2, grade3, grade4):
    average = int(grade1) + int(grade2) + int(grade3) + int(grade4) // 4
    return ("The avarage grade is: {}" .format(average))

def get_input():
    grade = input("Digite a nota: ")
    return grade

grades = get_grades(get_input(), get_input(), get_input(), get_input())
