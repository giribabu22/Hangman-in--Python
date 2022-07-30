li = [
        "    +----+",
        "    |     |",
        "    O     |",
        "   /|\\    |",
        "   / \\    |",
        "          |",
        "---------------"
    ];
index_ = 0
x=0
def man():
  global index_,life
  if index_ < len(li):
    print('wrong answer\n you have',life,'chances left')
    life-=1
    index_+=1
    for i2 in range(index_):
      print(li[i2])


def quest(name):
    global x,life
    question=['maybe your name !!','animal give milk !','always in your pocket!','very small thing ','you learning this man ']
    life=6
    s=list()
    for plac in range(len(name)):
        s.append('_')
    i=0
    while i<len(name):
        if x<len(li):
            t2=input(f'{question[rn]}\n enter the letter ')
            if t2 in name and t2 not in s:
                res=name.index(t2)
                s[res]=t2  
                for t3 in s:
                    if t2 in s:print(t3)
                i+=1
            elif t2 not in s:
                x+=1
                for t4 in s:
                    print(t4)
                man()
        else:
            print('game end boss !!!')
            i+=3
            break
    else:
        print('you wine the game the 3000UC~ ')
        maingame()

def maingame():
    global rn
    import random 
    rn=random.randrange(0,5)
    names=['prem','cow','phone','ant','python'] 
    inp=input('if you want to paly the game yes/no :')
    if inp=='yes' or inp== 'y':
        quest(names[rn])
        print(names[rn])
    else:
        print('thank you')
print('wel come \n',)
maingame()