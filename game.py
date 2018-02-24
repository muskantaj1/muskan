import random
cs=0
ps=0
count=0
s=("rock","paper","scissor")
r=random.randint(0,2)
c=s[r]
q=input("press p to play")
while count<=10:
       count=count+1
       if q=="p":
        i=input("enter your choice")
        print("player chose,i","comp chose,c")
       if i=="rock":
        if c=="rock":
           print("it is a tie")
           print("ur score is, ps","comp score is,cs")
        elif c=="scissor":
            print("u won")
            ps=ps+1
            print("ur score is, ps","comp score is,cs")
        else:
           print("comp won")
           cs=cs+1
           print("ur score is, ps","comp score is,cs")
      if i=="scissor":
       if c=="scissor":
           print("it is a tie")
           print("ur score is, ps","comp score is,cs")
       elif c=="rock":
            print("comp won")
            cs=cs+1
            print("ur score is, ps","comp score is,cs")
       else:
           print("u won")
           ps=ps+1
           print("ur score is, ps","comp score is,cs")
      if i=="paper":
       if c=="paper":
          print("it is a tie")
          print("ur score is, ps","comp score is,cs")
      elif c=="scissor":
            print("comp won")
            cs=cs+1
            print("ur score is, ps","comp score is,cs")
      else:
           print("u won")
           ps=ps+1
           print("ur score is, ps","comp score is,cs")
            

            

               
          
               
        
