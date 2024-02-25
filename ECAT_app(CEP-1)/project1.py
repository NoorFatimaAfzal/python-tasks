user_name=input("Enter your name: ")
password=input("Enter your email: ")
if user_name=="noor" or password=="butt":
    print("Welcome to ECAT test")
    questions = [
    ["Qno.1\nWhich one is not a branch of physical sciences?\nA. chemistry\nB. astronomy\nC. geology\nD. biology"],
    ["Qno.2\nWhich branch of science plays an important role in the development of technology and engineering?\nA. chemistry\nB. physics\nC. geology\nD. biology"],
    ["Qno.3\nThe number of categories in which physical quantities are divided are\nA. one\nB. two\nC. three\nD. four"],
    ["Qno.4\nHow many types of units are in SI?\nA. one\nB. two\nC. three\nD. four"],
    ["Qno.5\nIn scientific notation numbers are expressed in\nA. power of 10\nB. power of 2\nC. reciprocal\nD. decimal"],
    ["Qno.6\nRandom errors can be reduced by taking\nA. average\nB. difference\nC. sum\nD. product"],
    ["Qno.7\nThe uncertainty in a measurement may occur due to\nA.	limitation of an instrument\nB.	natural variation of the object to be measured\nC.	inadequate of technique\nD.	all 	given in a , b and c"],
    ["Qno.8\nPreftix deca represents\nA.	10 Raised to power 1\nB.	10 Raised to power 2\nC.	10 Raised to power 3\nD.	10 Raised to power -1"],
    ["Qno.9\nThe error in measurement may occur due to\nA.	inexperience of a person\nB.	the faulty apparantus\nC.	inappropriate method\nD.	due to all reasons in a, b and c"],
    ["Qno.10\n1024 can be written in scientific notation as\nA.	1.024x103\nB.	2 Raised to power 10\nC.	0.000976\nD.	1/0.00097"]
]
    answers = ["D", "B", "B", "C", "A","A","D","A","D","A"]
    choices = ["select any option (A B C D)", "submit", "skip"]
    question_no = 0
    score = 0
    skipped=0
    while question_no < len(questions):
        for question in questions[question_no:]:
            print(question[0])
            choice = input("YOU HAVE THREE CHOICES\n 1️⃣ Enter your ans (A/B/C/D)\n 2️⃣ type 'submit' to end the test\n 3️⃣ type skip to skip this question: \ntype choice...").upper()
            if choice == answers[question_no]:
                score += 1
            if choice == "SUBMIT":
                print("Your score is:", score)
                print("No of correct answers:", score)
                print("No of skipped questions:", skipped)
                if score>7:
                    print("Congratulations! You are eligible for admission🤩")
                else:
                    print("Sorry! You are not eligible for admission😔")
                quit()
            if choice == "SKIP":
                skipped+=1
                question_no += 1
                break
else:
    print("invalid user name or password! Please try again.") 
  
        
