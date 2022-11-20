class Game:
    def __init__(self):
        print('Welcome In Full Game .... ^_^')
        print('chooshe Your Game For Our Collection')
        print('Press[1] : Play Event_Odd Game')
        print('Press[2] : Play Sum Average Game')
        print('Press[3] : Play Multiplication Table Game')

        self.choices()


    def choices(self):
        while True:
            user_choice = input('Enter Your Choice : ')

            try :
                user_choice = int(user_choice)   
                if user_choice == 1:
                    self.Even_Odd_Game()

                elif user_choice == 2 :
                    self.Sum_Average_Game()

                elif user_choice == 3 :
                    self.Multiplication_Game()

                else :
                    print('Please Choose Between 1 , 2 or 3')
            except ValueError:
                print('Please Enter A Valid Number ')
            
    def Even_Odd_Game(self):
        print('Welcome In The Even_Odd Game')
        print('Please Enter A Number ... And I Will Tell You if it Even Or Odd')
        print('If You Wanna Close The Game Enter X ')

        while True:
            number = input('Enter A Number : ')
            if number == 'x':
                print('Colsing The Game')
                print('Thanks ...')
                break
            try:
                number = int(number)
                if number % 2 == 0 :
                    print('Even Number ')
                else :
                    print('Odd Number')
            except ValueError:
                print('Please Enter A Valid Number ')
            print('------------------------------------')
    def Sum_Average_Game(self):
        print('This Game Will Take Several Number And Print The Average Of Them')
        count = int(input('How Many Number Would You Like To Sum : '))
        current_count = 0
        summ = 0

        while current_count < count:
            number = float(input('Enter The Number : '))
            summ += number
            current_count += 1

        print('Summ of All Numbers = ' , summ)
        print('Average Of All Numbers = ' , summ/count)


    def Multiplication_Game(self):
        print('Welcome In Multiplication App')
        print('Please Enter The First Number And The Lase Number Of The Multiplication Table')

        start = int(input('Enter The First Number Of The Table : '))
        end = int(input('Enter The last Number Of The Table : '))
        for x in range(start,end+1):
            for y in range(1,13):
                print(x, 'X' , y , '=' , x*y)
            print('------------------------')
            
        
    

game1 = Game()

        
