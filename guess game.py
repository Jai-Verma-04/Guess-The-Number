import random

def WrongInput():
    print('Only 1-10 guesses are allowed')
    again=input("Continue again? [Y/N] ")
    if again=='Y' or 'y':
        main()
    else:
        print('Wrong Input, Program Exiting')
            
def main():
    num=random.randint(10,99)
    i=1
    print(num)
    j=int(input('Enter Number of guesses you want from 1-10: '))
    if j>10:
        WrongInput()  
    else:    
        while i<=j:
            inp = int(input('Enter your Guess(only two digit): '))
            if inp >=1 and inp<=100:
                if inp==num:
                    if i==1:
                        end='st'
                        msg="You're a champ"
                    elif i==2:
                        end='nd'
                        msg='Wooho! Nice'
                    elif i==3:
                        end='rd'
                        msg="you can do better"
                    else:
                        end='th'
                        msg=''
                    print(f"Correct Guess\nYou got this in your {i}{end} guess! {msg}")
                    break
                else:
                    print('Wrong Answer!')
            else:
                print('Only enter between correct range')
                continue
            i+=1
    
main()
