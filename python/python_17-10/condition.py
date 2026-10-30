grade= int(input("Grade:"))#input here takes value  in str but we are working in int so there is a error so we use type castign here
if(grade>=90):
    print("A grade")
elif(grade>=80):
    print("gradeB")
elif(grade>=70):
    print("c grade")
else:
    print("fail")
