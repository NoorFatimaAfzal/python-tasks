questions = [
    ["Which one is not a branch of physical sciences?\nA. chemistry\nB. astronomy\nC. geology\nD. biology"],
    ["Which branch of science plays an important role in the development of technology and engineering?A. chemistry\nB. physics\nC. geology\nD. biology"],
    ["The number of categories in which physical quantities are divided are\nA. one\nB. two\nC. three\nA. one\nB. two\nC. three\nD. four"],
    ["How many types of units are in SI?\nA. one\nB. two\nC. three\nD. four"],
    ["In scientific notation numbers are expressed in\nA. power of 10\nB. power of 2\nC. reciprocal\nD. decimal"]
]
answers = ["D", "B", "B", "C", "A"]
choices = [["select any option(A B C D)\tor\tsubmit\tor\tskip"]]
question_no = 0
score = 0

for i in range(len(questions)):
    for question in questions[i]:
        print(question)
        print(choices[0])
        choice = input("Enter your choice: ").upper()
        if choice == answers[question_no]:
            score += 1
        if choice == "SUBMIT":
            break
        question_no += 1

print("Your score is:", score)
