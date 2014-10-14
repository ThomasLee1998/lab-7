#x=1

#while (x < 300):
 #   print x
  #  x= x + 2
    


#MyList = [5,3,"yo","dog","cat",6,7,8,9,10]
#index=0
#while(index < len(MyList)):
 #   print MyList[index]
  #  index=index+1
  
  
import random
rand= random.randint(0,50)
player= -1
attempts=1
print "please guess a number between 0 and 50"
while (player !=rand):
      player = int(raw_input())
      if player < rand:
          print " higher"
      if player > rand:
          print "lower"
      attempts= attempts+1 
print "you win"
print "i took you" + str(attempts)+ " attempts" 
    

