print("welcome","🙏🙏")
print("lest play kon banega crorpati (KBC)")
print("😻😻","😻😻","😻😻","😻😻","😻😻")
question_list = [
    "1 How many continents are there?",             
    "2 What is the capital of India?",            
    "3 NG mei kaun se course padhaya jaata hai?"    ]
options_list = [
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1]
i=0
a=0
b=1
count=0
while i<len(question_list):
    print(question_list[i])
    j=0
    # c=1
    while j<=len(options_list):
        print(options_list[i][j])
        j+=1
        # c+=1
    ans=["3 Seven","4 Eight","4 Delhi","3 Chennai","1 Software Engineering","2 Counseling"]
    print("you have 1 life line ","5️⃣","0️⃣","--","5️⃣","0️⃣")
    print("do you want life line")
    print("🎤 say" )
    life_line=input("yes or no  ")
    if life_line=="yes":
        if count==0:
            print(ans[i+a])
            print(ans[i+b])
            print("😉😉")
            answer=int(input("enter your answer "))
            if solution_list[i]==answer:
                print("right")
                print("😍😍","✅","😍😍")
                print("congrects")
                print("play forword","🎮🎮")
                count+=1
            else:
                print("wrong","🙀🙀")
                print("😧😧")
                print("game over","😵😵")
                break
        else:
            print("you don't have life line ")
            print("you already used your life line","◀️")
            a=int(input("enter answer "))
            if solution_list[i]==a:
                print("right")
            else:
                print("wrong","🙀🙀")
                print("game over","😵😵")
                print("😧😧")


                break
    elif life_line=="no":
        print("👆👆")
        user=int(input("chose answer from obave options "))
        if solution_list[i]==user:
            print("right")
            print("😍😍")
            print("you win you got 10,000 rupees")
            print("😉😉")
        else:
            print("wrong")
            print("😫😫")
            print("🙀🙀")
            break
    else:
        print("wrong","😫😫")
        print("🥴🥴")
        print("game over","🤦🏻‍♀️","🤦🏻‍♀️","🤦🏻‍♀️")
        print("😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭😭")
        break
    a+=1
    b+=1
    i+=1







