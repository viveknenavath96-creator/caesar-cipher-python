print("******************************************")
print("Welcome To My Quizz Game......!")
question_bank=[
        {"text":"Which planet is known as the Red Planet?","answer":"B"},
       {"text":"What is the process by which plants convert sunlight, water, and carbon dioxide into oxygen and energy?","answer":"B"},
        {"text":"What is the capital city of Canada?","answer":"C"},
        {"text":"Which planet is commonly referred to as the Red Planet?","answer":"B"},
        {"text":"In what year did the Berlin Wall fall, marking the beginning of the end of the Cold War?","answer":"A"},
        {"text":"What is the name of the largest hot desert in the world?","answer":"C"},
        {"text":"Which acclaimed director directed the 1975 summer blockbuster film 'Jaws'?","answer":"D"},
        {"text":"In which fictional town is the classic novel 'To Kill a Mockingbird' by Harper Lee set?","answer":"B"},
        {"text":"Who was the first Emperor of the Roman Empire?","answer":"C"},
        {"text":"What is the chemical symbol for gold?","answer":"A"},
        {"text":"Who wrote the famous play 'Romeo and Juliet'?","answer":"B"}
]
options=[["A. Venus","B. Mars","C.Jupiter","D.Mercury"],
         ["A.Transpiration","B. Photosynthesis","C.Cellular Respiration","D. Nitrogen Fixation"],
         ["A.Toronto","B.Vancouver","C.Ottawa","D. Montreal"],
         ["A.Venus","B.Mars","C.Jupiter","D.Mercury"],
         ["A.1989","B.1991","C.1987","D.1993"],
         ["A.Gobi Desert","B.Arabian Desert","C.Sahara Desert","D.Kalahari Desert"],
         ["A.Martin Scorsese","B.George Lucas","C.hristopher Nolan","D.Steven Spielberg"],
         ["A.West Egg","B.Maycomb","C.Yoknapatawpha","D.Casterbridge"],
         ["A.Julius Caesar","B.Nero","C.Augustus","D.Marcus Aurelius"],
         ["A.Au","B.Ag","C.Gd","D.Go"],
         ["A.Charles Dickens","B.William Shakespeare","C.Jane Austen","D.Christopher Marlowe"]
]
score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False
    
for question_num in range(len(question_bank)):
    print("***********************************")
    print(question_bank[question_num]["text"])
    for i in options[question_num]:
        print(i)

    guess=input("Enter your answer(A/B/C/D):").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"]) 
    if is_correct:
        print("correct answer")
        score+=1
    else:
        print("incorrect answer")   
        print(f"Your correct answer is {question_bank[question_num]['answer']}") 
    print(f"Your correct is score is {score}/{question_num+1}")
print(f"Your score is {score}")   
print(f"Your percencentage is {(score/len(question_bank))*100}%")    

