from time import sleep

#campaign's price in ILS per day
Facebook_campaign = 100
Instagram_campaign = 50

price1=int(input("How long do you wants the Facebook campaign will run? "))
price1=price1*Facebook_campaign
price2=int(input("How long do you wants the Instagram campaign will run? "))
price2=price2*Instagram_campaign
sleep(2)
summery=price1+price2
summery_with_TAX=(str((summery*1.17)) + " ILS\n")
print("\nthe summery is:  "+ str(summery_with_TAX))
Marketing_Budget=(int(input("please put your Marketing Budget: ")))


if(str(Marketing_Budget))>=(str(summery_with_TAX)):
    print("\nsuccessful")
else:
    print("\nplease add "+ str(int(summery*1.17-Marketing_Budget)) +" ILS to your Marketing Budget")

















#print("Instagram_campaign: "+str(Instagram_campaign))

