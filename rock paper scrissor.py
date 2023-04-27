import random
ls=['rock','paper','scrissor']
c_c=random.choice(ls)
v_c=input()
v_c.lower()

if c_c==v_c:
    print("you won")
else:
    print('you lost,try again')
