import random
import time

def question_genaerator():
    #generate two random number
    a = random.randint(1,9)
    b = random.randint(1,9)

    #random opratore
    operatore_list = ["+","-","*"]
    selected_operator = random.choice(operatore_list)

    print(f"{a} {selected_operator} {b} = ?")

    if selected_operator == "+":
        return a+b
    elif selected_operator == "-":
        return a-b
    else:
        return a*b
    
question_number_limit = 5
question_number = 0

score = 0
time_limit = 10
# create while loop

while question_number < question_number_limit:
    # step 1 generate a random questio
    result = str(question_genaerator())
    staet_time = time.time()
    # step 2 get user answer
    user_answer = input("enter your answer: ")
    end_time = time.time()
    time_diff = end_time - staet_time
    # step 3 check the answer ad time
    if time_diff < time_limit:
        if result == user_answer:
            score +=1
            print(f"perfect, score {score}")
        else:
            print("Sorry, your answer is wrong")
    else:
        print(f"Time is out please answer on time {time_limit}")
    
    question_number +=1
    print(f"FINAL RESULT Score: {score} the number of question: {question_number_limit}")
    


