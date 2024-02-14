questions=[["Which one is not a branch of physical sciences?"],
           ["Which branch of science plays an important role in the development of technology and engineering?"],
           ["The number of categories in which physical quantities are divided are"],
           ["How many types of units are in SI?"],
           ["In scientific notation numbers are expressed in"]]
options=[["A.chemistry","B.astronomy","C.geology","D.biology"],
         ["A.chemistry","B.physics","C.geology","D.biology"],
         ["A.one","B.two","C.three","D.four"],
         ["A.one","B.two","C.three","D.four"],
         ["A.powe of 10","B.power of 2","C.reciprocal","D.decimal"]]
answers=["D","B","B","C","A"]
choices=[["submit"],["skip"]]
question_no=0
score=0
for i in range(len(questions)):
    for question in questions[i]:
        print(question)
        for option in options[question_no]:
            print(option)
            ans=input("select any option(A B C D)").upper()
            if ans==answers[question_no]:
                score+=1
                break
            choice1=input("Skip ? y/n").lower()
            if choice1=="y":
                break
            choice2=input("Submit ? y/n").lower()
            if choice2=="y":
                break
        question_no+=1

            
    # user_ans=input("select any option").upper()
    




























# question_no=0
# score=0
# user_answers=[]
# for question in questions:
#     print(question)
#     for option in options[question_no]:
#         print(option)
#     user_ans=input("select any option").upper()
#     user_answers.append(user_ans)
#     if user_ans==user_answers[question_no]:
#         score+=1
#     question_no+=1
# print(score)