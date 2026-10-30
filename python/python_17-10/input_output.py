
#f.write("Hii everyone\nwe arelearning i/o from java\ni like programming in java  ")
'''with open("practise.txt","r+") as f:
    f.write("hii i am gurvansh and currently learning")
    d=f.read()
    new=d.find("learning")
    print(new)'''
with open("practise.txt","r+") as f:
    f.write("hii i am gurvansh and currently learning")
    d=f.read()
    print(d.replace("am","m"))
    