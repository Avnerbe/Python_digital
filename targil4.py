print("now we will calculate your markting:\nprices:\ntommato:3nis\ncucumber:2nis\nkola:5nis\nchicken:20nis per kg")
tomato=int(input("how many tomato do you want?"))
cucumber=int(input("how many cucumber do you want?"))
kola=int(input("how many kola do you want?"))
chicken=int(input("how many chicken do you want?"))
sum1=tomato*3
sum2=cucumber*2
sum3=kola*5
sum4=chicken*20
summery=sum1+sum2+sum3+sum4
print("total price="+str(summery)+" nis")
print("total price="+str("%.2f" % (summery*1.17))+"  nis with tax")






