import csv
from Calculation_Functions import calculate_average, determine_grade

def read_csv(filename):
    with open(filename, newline='') as csvfile:
        return list(csv.DictReader(csvfile))

def main():
    students = read_csv('Students.csv')
    results = read_csv('Student_Results.csv')

    for student in students:
        student_id = student['ID']
        student_name = student['Name']
        result = next((r for r in results if r['ID'] == student_id), None)
        if result:
            scores = [int(result['Math']), int(result['Science']), int(result['English'])]
            average = calculate_average(scores)
            grade = determine_grade(average)
            print(f"{student_name} - Average: {average}, Grade: {grade}")
        else:
            print(f"No results found for {student_name}")

if __name__ == "__main__":
    main()
