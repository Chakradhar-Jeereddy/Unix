#Love calculator
#Score for "true love"
#use functions lower(), count(),str()

m_name = input("enter your full name: ")
l_name = input("enter your friend's name: ")

name = (m_name+l_name).lower()
true=0+name.count('t')+name.count('r')+name.count('u')+name.count('e')
love=0+name.count('l')+name.count('o')+name.count('v')+name.count('e')

percent = str(true)+str(love)
if(int(percent)<10 or int(percent)>90):
    print(f"The match is {percent}%, very immense relation.")
elif(int(percent)==40 and int(percent)==50):
    print(f"The match is {percent}%, you're all right together.")
else:
    print(f"The match is {percent}%")
