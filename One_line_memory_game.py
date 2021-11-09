x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
score1=0
score2=0
for i in range (5):
        print(x)
        print('#player 1:')
        a=int(input('choose num1.'))
        b=int(input('choose  num2.'))
        
        
        if a==1 and b==12:
                x[0]='D'
                x[11]='D'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[0]='*'
                x[11]='*'
               
               

        elif a==2 and b==19:
                x[1]='F'
                x[18]='F'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[1]='*'
                x[18]='*'
                

               
        elif a==3 and b==15:
                x[2]='A'
                x[14]='A'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[2]='*'
                x[14]='*'
                

                
        elif a==4 and b==17:
                x[3]='J'
                x[16]='J'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[3]='*'
                x[16]='*'
                
             

        elif a==5 and b==11:
                x[4]='B'
                x[10]='B'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[4]='*'
                x[10]='*'
                
                
            
        elif a==6 and b==20:
                x[5]='G'
                x[19]='G'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[4]='*'
                x[10]='*'
                
                
            
        elif a==7 and b==13:
                x[6]='C'
                x[12]='C'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[6]='*'
                x[12]='*'
                
                
           
        elif a==8 and b==16:
                x[7]='I'
                x[15]='I'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[7]='*'
                x[15]='*'
                
                
                   
        elif a==9 and b==18:
                x[8]='E'
                x[17]='E'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[8]='*'
                x[17]='*'
                
                
                
        elif a==10 and b==14:
                x[9]='H'
                x[13]='H'
                print (x)
                print('true')
                score1=1+score1
                print('player1 score :',score1)
                x[9]='*'
                x[13]='*'
                        
                
        else:
               print('false')
               score1=0+score1
               print('player1 score :',score1)
              
        


        print(x)
        print('#player 2:')
        a=int(input('choose num1.'))
        b=int(input('choose  num2.'))
            
        
        if a==1 and b==12:
                x[0]='D'
                x[11]='D'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[0]='*'
                x[11]='*'
               
               

        elif a==2 and b==19:
                x[1]='F'
                x[18]='F'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[1]='*'
                x[18]='*'
                

               
        elif a==3 and b==15:
                x[2]='A'
                x[14]='A'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[2]='*'
                x[14]='*'
                

                
        elif a==4 and b==17:
                x[3]='J'
                x[16]='J'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[3]='*'
                x[16]='*'
                
             

        elif a==5 and b==11:
                x[4]='B'
                x[10]='B'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[4]='*'
                x[10]='*'
                
                
            
        elif a==6 and b==20:
                x[5]='G'
                x[19]='G'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[5]='*'
                x[19]='*'
                
                
            
        elif a==7 and b==13:
                x[6]='C'
                x[12]='C'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[6]='*'
                x[12]='*'
                
                
           
        elif a==8 and b==16:
                x[7]='I'
                x[15]='I'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[7]='*'
                x[15]='*'
                
                
                   
        elif a==9 and b==18:
                x[8]='E'
                x[17]='E'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[8]='*'
                x[17]='*'
                
                
                
        elif a==10 and b==14:
                x[9]='H'
                x[13]='H'
                print (x)
                print('true')
                score2=1+score2
                print('player2 score :',score2)
                x[9]='*'
                x[13]='*'
                        
                
        else:
               print('false')
               score2=0+score2
               print('player2 score :',score2)

print('player1 score',score1)
print('player2 score',score2)
if score1==score2:
    print(' equal')
elif score1>score2:
        print('player1 is won')
else:
    print('player2 is won')
