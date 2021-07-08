from random import randint
from time import sleep



money=(int(input("         hello \n       --------\n     row_cost=3 ILS\nHow much money do you have: " )))
x=money//3
print ("you can play: "+str(x)+" rows\n  ---------------\n")
if(x==0):
    print ("bye bye")
else:
    total_winning = 0
    #הגרלת 6 מספרים ע"פ מספר הסיבובים שמאפשר הכסף
    for rounds in range(x):
        list = []
        my_number=[]
        for y in range(6):
            y=(int(input("please choose your lottory number (between 1-37): ")))
            if (x>37 or x<1):
                x = (int(input("sorry invalid number please choose new number :" )))
                my_number = my_number + [y]
            else:
                my_number=my_number + [y]

        print("\nyour lottory numbers are: \n  ---------------\n"+ str(my_number))

        win_numbers=[]
        win=0
        for num in range(6):
            num=randint(1,37)
            win_numbers= win_numbers +[num]
            if(num in my_number):
                win=win+1
            else:
                continue
        print ("\n\nThe winning numbers are: \n  ---------------\n"+str(win_numbers))
        print("\n  ---------------\nyour guess: "+str(win)+ " numbers")
        #חישובי זכיה
        prize=0
        #total_winning=0
        if (win==3):
            prize=prize+10
            print("you won: " +str(prize)+" ILS\n")
        elif(win==4):
            prize = prize + 100
            print("you won: " +str(prize)+" ILS\n")
        elif (win == 4):
            prize = prize + 5000
            print("you won: " +str(prize)+" ILS\n")
        elif (win == 4):
            prize = prize + 1000000
            print("you won: " +str(prize)+" ILS\n")
        else:
            prize = 0
            print("you won: " +str(prize)+" ILS\n")

        total_winning =total_winning+prize
    print("your total winning:" +str(total_winning)+" ILS\n")












