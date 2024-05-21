def check_exam(arr1,arr2):
    score = 0
    for right_answer, student_answer in zip(arr1,arr2):
        if right_answer is student_answer:
            score += 4
        elif not (right_answer and student_answer):
            continue
        else:
            score -= 1
    return score if score > 0 else 0
