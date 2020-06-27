while True:
   print"=========MAIN MENU========== "
   print"             GAME CATEGORIES               "
   print"1)GENIE QUIZ"
   print"2)CRYPTO SCRAMBLE"
   print"3)EXIT"
   choice=input("Enter Your Choice :")

   if choice==1:
      print"==========GENIE QUIZ============"
      print"                  Play The Game                       "
      print"                                                             "
      print"----------------INSTRUCTIONS------------------"
      print"1.Think of a number between 1-63"
      print"2.Answer the questions correctly and carefully "
      print"3.Let's see whether You are a genius or it's the Genie the true genius"
      print"                                                              "
      while True:
         computer=0
         player=0
         category=1
         if category==1:
            l1=[[1,3,5,7,9,11,13,15],[17,19,21,23,25,27,29,31],[33,35,37,39,41,43,45,47],[49,51,53,55,57,59,61,63]]

            l2=[[2,3,6,7,10,11,14,15],[18,19,22,23,26,27,30,31],[34,35,38,39,42,43,46,47],[50,51,54,55,58,59,62,63]]
        
            l3=[[4,5,6,7,12,13,14,15],[20,21,22,23,28,29,30,31],[36,37,38,39,44,45,46,47],[52,53,54,55,60,61,62,63]]
        
            l4=[[8,9,10,11,12,13,14,15],[24,25,26,27,28,29,30,31],[40,41,42,43,44,45,46,47],[56,57,58,59,60,61,62,63]]

            l5=[[16,17,18,19,20,21,22,23],[24,25,26,27,28,29,30,31],[48,49,50,51,52,53,54,55],[56,57,58,59,60,61,62,63]]

            l6=[[32,33,34,35,36,37,38,39],[40,41,42,43,44,45,46,47],[48,49,50,51,52,53,54,55],[56,57,58,59,60,61,62,63]]
            x=0
            s=0
            for i in range(0,len(l1)):
               for j in range(0,len( l1[i])) :
                  print l1[i][j],
               print
         print"is your number in any one of the above rows?"
         eli=raw_input("enter yes/no")
         if eli=="yes":
            s=l1[0][0]
         else:
            s=s+0
         x=x+s
         for k in range(0,len(l2)):
            for l in range(0,len(l2[k])):
               print l2[k][l],
            print
         print "is your number in anyone of the above rows?"
         bo=raw_input("enter yes/no?")
         if bo=="yes":
            s=l2[0][0]
         else:
            s=0
         x=x+s
         for m in range  (0,len(l3)):
            for n in range(0,len(l3[m])):
               print l3[m][n],
            print
         print"is your number in any of the above rows"
         ga=raw_input("enter yes or no")
         if ga=="yes":
            s=l3[0][0]
         else:
            s=0
         x=x+s
         for o in range(0,len(l4)):
            for p in range (0,len(l4[o])):
               print l4[o][p],
            print
         print"is your number in any of the above rows"
         ma=raw_input("enter yes/no")
         if ma=="yes":
            s=l4[0][0]
         else:
            s=0
         x=x+s
         for q in range(0,len(l5)):
            for r in range(0,len(l5[q])):
               print l5[q][r],
            print
         print"is your number in any of the above rows"
         em=raw_input("enter yes or no")
         if em=="yes":
            s=l5[0][0]
         else:
            s=0
         x=x+s
         for s in range (0,len(l6)):
            for t in range(0,len(l6[s])):
               print l6[s][t],
            print
         print"is your number in the any of the above row"
         io=raw_input("enter yes or no ")
         if io=="yes":
            s=l6[0][0]
         else:
            s=0
         x=x+s
         print x
         guess=raw_input("Did i guess your number right?")
         if guess=="yes":
            print "Never challenge a genie"
         else:
            print "There is something wrong with you"
         chan=raw_input( "Do u want to take the challenge again?")
         if chan=="yes":
            continue
         else:
            print"-------------end---------------"
            break
         
   print"=================================================================================================="
   if choice==2:
      print"-------------------CRYPTO SCRAMBLE ------------------------"
      while True:
         print"1)Play The Game"
         print"2)Instructions "
         print"3)Score Board "
         category=input("enter your choice:")
         if category==1:
            l=["Q)Vehicle first priority is fish","Q)No way out: old friend","Q)Sudden hurried movement is price paid for sending a letter without the cents of giving in. ","Q)Feeling happy is a reason against temporary shelter. ","Q)Uses phone line to establish connection, or song of dedication between small candy-coated chocolates ","Q)Greatest amount possible is variable, I find, between two mothers ","Q)Sea organism is walked by pirate's captives, weighs 1000 kg. "]
            l1=[ ]
            player=0
            computer=0
            n=7
            import random
            for i in range(n):
               question=random.choice(l)
               print question
               if question== "Q)Vehicle first priority is fish" :
                  print"a)rtaew "
                  print"b)omsaln "
                  print"c)rpac"
                  print"d)I don't know"
                  answer=raw_input("enter your choice:")
                  if answer=="a":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"In this case, the answer would be rpac, which unscrambled, gives carp. A car is a substitute for vehicle. The phrase ""first priority"" indicates that the first letter from the word priority should be used ('p'). In this case, the last word in the clue ('fish') provides the meaning of the word. Thus we have car + p = carp. "
                     else:
                        print"'rpac',is the right answer"
                     player=player+0
                     computer=computer+10
                  elif answer=="b":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"In this case, the answer would be rpac, which unscrambled, gives carp. A car is a substitute for vehicle. The phrase ""first priority"" indicates that the first letter from the word priority should be used ('p'). In this case, the last word in the clue ('fish') provides the meaning of the word. Thus we have car + p = carp."
                     else:
                        print"Right Answer : rpac"
                     player=player+0
                     computer=computer+10
                  elif answer=="c":
                     print "right answer"
                     player=player+10
                     computer=computer+0
                  elif answer=="d":
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"In this case, the answer would be rpac, which unscrambled, gives carp. A car is a substitute for vehicle. The phrase ""first priority"" indicates that the first letter from the word priority should be used ('p'). In this case, the last word in the clue ('fish') provides the meaning of the word. Thus we have car + p = carp. "
                     else:
                        print"Right Answer : rpac"
                     player=player+0
                     computer=computer+10
               elif question=="Q)No way out: old friend":
                  print"a)Tmetlasea"
                  print"b)Rppteda"
                  print"c)Kctsu"
                  print"d)I don't know "
                  answer=raw_input("enter your choice:")
                  if answer=="a":
                     print"right answer"
                     player=player+10
                     computer=computer+0
                  elif answer=="b":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give STALEMATE. When in stalemate (as in the game of chess), there is no move that can be made without putting oneself in check. Something which is old is stale. Mate is slang for friend. "
                     else:
                        print"Right Answer : Tmetlasea"
                     player+=0
                     computer+=10
                  elif answer=="c":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give STALEMATE. When in stalemate (as in the game of chess), there is no move that can be made without putting oneself in check. Something which is old is stale. Mate is slang for friend. "
                     else:
                        print"Right Answer : Tmetlasea"
                     player+=0
                     computer+=10
                  elif answer=="d":
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give STALEMATE. When in stalemate (as in the game of chess), there is no move that can be made without putting oneself in check. Something which is old is stale. Mate is slang for friend. "
                     else:
                        print"Right Answer : Tmetlasea"
                     player+=0
                     computer+=10
               elif question=="Q)Sudden hurried movement is price paid for sending a letter without the cents of giving in. ":
                  print"a)Usrh"
                  print"b)eotapsg"
                  print"c)Eptdsmea"
                  print"d)I don't know"
                  answer=raw_input("enter your choice:")
                  if answer=="a":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give STAMPEDE. A stampede is a sudden hurried movement. A stamp is the price paid for sending a letter. To give in is to cede. The letter 'c' with a slash through it is used to denote cents. The letter c removed from cede leaves 'ede'. "
                     else:
                        print"Eptdsmea"
                     player+=0
                     computer+=10
                  elif answer=="b":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give STAMPEDE. A stampede is a sudden hurried movement. A stamp is the price paid for sending a letter. To give in is to cede. The letter 'c' with a slash through it is used to denote cents. The letter c removed from cede leaves 'ede'. "
                     else:
                        print"Right Answer : Eptdsmea"
                     player+=0
                     computer+=10
                  elif answer=="c":
                     print "right answer"
                     player+=10
                     computer+=0
                  else :
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give STAMPEDE. A stampede is a sudden hurried movement. A stamp is the price paid for sending a letter. To give in is to cede. The letter 'c' with a slash through it is used to denote cents. The letter c removed from cede leaves 'ede'. "
                     else:
                        print"Right Answer : Eptdsmea"
                     player+=0
                     computer+=10
               elif question=="Q)Feeling happy is a reason against temporary shelter. ":
                  print"a) Lmhesoes"
                  print"b)Noetctn"
                  print"c)Sbsuifll"
                  print"d)I don't know"
                  answer=raw_input("enter your choice:")
                  if answer=="a":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give CONTENT. Content can be described as feeling happy. A reason against something is the 'con' (as opposed to the 'pro'). A tent is a temporary shelter"
                     else:
                        print"Right Answer : Noetctn"
                     player+=0
                     computer+=10
                  elif answer=="b":
                     print"right answer"
                     player+=10
                     computer+=0
                  elif answer=="c":
                     print "wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give CONTENT. Content can be described as feeling happy. A reason against something is the 'con' (as opposed to the 'pro'). A tent is a temporary shelter"
                     else:
                        print"Right Answer : Noetctn"
                     player+=0
                     computer+=10
                  elif answer=="d":
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give CONTENT. Content can be described as feeling happy. A reason against something is the 'con' (as opposed to the 'pro'). A tent is a temporary shelter"
                     else:
                        print"Right Answer : Noetctn"
                        player+=0
                        computer+=10
               elif question=="Q)Uses phone line to establish connection, or song of dedication between small candy-coated chocolates ":
                  print"a)Demmo"
                  print"b)Nacorme"
                  print"c)Owo"
                  print"d)I don't know"
                  answer=raw_input("enter your choice")
                  if answer=="a":
                     print"right answer"
                     player+=10
                     computer+=0
                  elif answer=="b":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give MODEM. An ode is a song of dedication. M & M's are a brand of small candy-coated chocolates. "
                     else:
                        print"Right Answer : Demmo"
                     player+=0
                     computer+=10
                  elif answer=="c":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give MODEM. An ode is a song of dedication. M & M's are a brand of small candy-coated chocolates. "
                     else:
                        print"Right Answer : Demmo"
                     player+=0
                     computer+=10
                  elif answer=="d":
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give MODEM. An ode is a song of dedication. M & M's are a brand of small candy-coated chocolates. "
                     else:
                        print"Right Answer : Demmo"
                     player+=0
                     computer+=10
               elif question=="Q)Greatest amount possible is variable, I find, between two mothers ":
                  print"a)Nlamrtea "
                  print"b)Ymmom "
                  print"c)Auximmm"
                  print"d)I don't know "
                  answer=raw_input("enter your choice:")
                  if answer=="a":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give MAXIMUM. The maximum is the greatest amount possible. A common letter denoted as the variable in an equation is 'x'. Following that the clue simply gives us the letter 'i'. Both of these are found, in that order, between two mothers: 'ma' and 'mum'. "
                     else:
                        print"Right Answer : Auximmm"
                     player+=0
                     computer+=10
                  elif answer=="b":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give MAXIMUM. The maximum is the greatest amount possible. A common letter denoted as the variable in an equation is 'x'. Following that the clue simply gives us the letter 'i'. Both of these are found, in that order, between two mothers: 'ma' and 'mum'. "
                     else:
                        print"Right Answer : Auximmm"
                     player+=0
                     computer+=10
                  elif answer=="c":
                     print"right answer"
                     player+=10
                     computer+=0
                  else:
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give MAXIMUM. The maximum is the greatest amount possible. A common letter denoted as the variable in an equation is 'x'. Following that the clue simply gives us the letter 'i'. Both of these are found, in that order, between two mothers: 'ma' and 'mum'. "
                     else:
                        print"Right Answer : Auximmm"
                     player+=0
                     computer+=10
               elif question=="Q)Sea organism is walked by pirate's captives, weighs 1000 kg. ":
                  print"a)Naklntpo "
                  print"b)Nteon"
                  print"c)Gaale"
                  print"d)I don't know "
                  answer=raw_input("enter your choice:")
                  if answer=="a":
                     print"right answer"
                     player+=10
                     computer+=0
                  elif answer=="b":
                     print"wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give PLANKTON. Plankton is a sea organism. A plank is a board of wood which is traditionally walked by pirate's captives (hence the expression""walk the plank""). Something which weighs 1000 kg is a ton. "
                     else:
                        print"Right Answer : Naklntpo"
                     player+=0
                     computer+=10
                  elif answer=="c":
                     print "wrong answer"
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Naklntpo : Unscrambles to give PLANKTON. Plankton is a sea organism. A plank is a board of wood which is traditionally walked by pirate's captives (hence the expression""walk the plank""). Something which weighs 1000 kg is a ton. "
                     else:
                        print"Right Answer : Naklntpo"
                     player+=0
                     computer+=10
                  else:
                     print "want to look at how to solve it ?"
                     look=raw_input("enter yes/no:")
                     if look=="yes":
                        print"Unscrambles to give PLANKTON. Plankton is a sea organism. A plank is a board of wood which is traditionally walked by pirate's captives (hence the expression""walk the plank""). Something which weighs 1000 kg is a ton. "
                     else:
                        print"Right Answer : Naklntpo"
                     player+=0
                     computer+=10
               n=n-1
               l.remove(question)
            print"------------------------------------------END-----------------------------------------------"
         if category==2:
            print"===========INSTRUCTIONS=============="
            print"\aEach question consists of four options "
            print"\aEvery option is a jumbled word "
            print"\aEvery question is a crypted question which has clues in it"
            print"\aLet's see who wins the challenge"
         if category==3:
            def scoreboard(computer,player):
               print"--------------------SCORE---------------------"
               print"Player's total score is :",player
               print"Computer's total score is :",computer
               if computer>player:
                  return"computer won"
               else:
                  return"you won"
               
            print scoreboard(computer,player)
         playing=raw_input("Type 'yes' to 'continue'  or 'no' to 'end' ")
         print"Type 'no' :"
         print"\aTo look into the scoreboard : |Type 3|  --> scoreboard"
         print"\aTo Exit the game :Type 'no' --> |Type 3| --> Exit"
         if playing=="yes":
            continue
         else:
            break
   if choice==3:
      break 

            
      
      
   
               
            

        
        
        
        
        
    
    
        
        

    
        
        
    
        
    
    

            

        
        
    
        

      

