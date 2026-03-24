def get_successful_students(students_list, passing_score=60):
    succes_students= {}
    for i in students_list:
        name= i["name"]
        scores = i["scores"]
        grades = scores.items()

        if min(grades) >= passing_score:
            succes_students[name] = sum(grades) / len(grades)
    return succes_students


