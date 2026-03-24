def get_successful_students(students_list, passing_score=60):
    succes_students= {}
    for i in students_list:
        name= i["name"]
        scores = i["scores"]
        grades = scores.values()

        if min(grades) >= passing_score:
            succes_students[name] = sum(grades) / len(grades)
    return succes_students

students_math_results = [
{"name": "Олександр", "scores": {"Calculus": 85,
"Algebra": 90, "Discrete Math": 78}},
{"name": "Марія", "scores": {"Calculus": 65, "Algebra":
55, "Discrete Math": 70}},
{"name": "Іван", "scores": {"Calculus": 92, "Algebra": 88,
"Discrete Math": 95}},
{"name": "Анна", "scores": {"Calculus": 45, "Algebra": 60,
"Discrete Math": 50}}
]

print(f'The successful students are:')
for name, grade in get_successful_students(students_math_results).items():
    print(f'{name} - grade {grade}')