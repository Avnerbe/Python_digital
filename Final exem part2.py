from random import randint
from time import sleep


#row_cost=3
money=(int(input("How much money do you have: " )))
x=money//3
print ("you can play: "+str(x)+" rounds\n")


#הגרלת 6 מספרים ע"פ מספר הסיבובים שמאפשר הכסף
for term in range(x):
    list = []
    my_num = ["8", "21", "2", "5","6", "11"]
    for win_numbers in range(6):
      num=randint(1,37)
      #ביטול כפילות מספרים
      if(num in list):
          num = randint(1,37)
          #בדיקת זכיה
          if(str(num) in my_num):
              print("winning")
          else:
              #win=0
              #winning =win+0
              print("no win")
          list = list + [num]
      else:
          list = list + [num]

    print(list)













