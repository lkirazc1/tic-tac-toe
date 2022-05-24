import random

#if row is finished
def row_complete(alist, start_square):
    if start_square in alist:
        if start_square + 1 in alist:
            if start_square + 2 in alist:
                return True
    return False

#if column is finished

def column_complete(alist, start_square):
    if start_square in alist:
        if start_square + 3 in alist:
            if start_square + 6 in alist:
                return True
    return False


#if diagonal is finished
def diagonal_complete(alist):
    if 3 in alist and 5 in alist and 7 in alist:
        return True
    if 1 in alist and 5 in alist and 9 in alist:
        return True
    return False


#return if anybody won yet
def return_number(alist, alist2):
    for test_list, score_complete in [(alist, 10), (alist2, -10)]:
        if row_complete(test_list, 1) or row_complete(test_list, 4) or row_complete(test_list, 7):
            return score_complete
        if column_complete(test_list, 1) or column_complete(test_list, 2) or column_complete(test_list, 3):
            return score_complete
        if diagonal_complete(test_list):
            return score_complete
    return 0

#return a tuple of the next best move for o's and the score
def get_next_move(o_list, x_list, is_o_turn):
    current_score = return_number(o_list, x_list)
    if current_score == 10:
        #print("O wins")
        return (10, 0)
    elif current_score == -10:
        #print("X wins")
        return (-10, 0)
    elif len(o_list) > 4:
        #print("tie")
        return (0, 0)
        
    
    elif is_o_turn:
        #get max
        max_move = 0
        #pick something smaller than -10 because -10 is the lowest possible value
        max_score = -123
        for o_move in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if o_move in o_list or o_move in x_list:
                continue
            
            #print("Trying O move", o_move)
            (best_score, best_move) = get_next_move(o_list + [o_move], x_list, False)   
            if (best_score) > max_score:
                max_score = best_score
                max_move = o_move
                if best_score == 10:
                    break
        #print("Level ", len(o_list) + len(x_list), " O ", max_move, " score ", max_score)
        return (max_score, max_move)
    elif not is_o_turn:
        #get min
        min_move = 0
        #pick something bigger than 10 because 10 is the highest possible value
        min_score = 100
        for x_move in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            if x_move in o_list or x_move in x_list:
                continue
            
            #print("Trying X move", x_move)
            (worst_score, worst_move) = get_next_move(o_list, x_list + [x_move], True)   
            if (worst_score) < min_score:
                min_score = worst_score
                min_move = x_move
                if worst_score == -10:
                    break
        #print("Level ", len(o_list) + len(x_list), " X ", min_move, " score ", min_score)
        return (min_score, min_move)            





def print_board(alist, alist2):
    board = ""
    #print board
    for number in [1,2,3]:
        if number in alist:
            board += "o"
            if number != 3:
                board += "|" 
        elif number in alist2:
            board += "x"
            if number != 3:
                board += "|"
        else:
            board += " "
            if number != 3:
                board += "|"
    print(board)
    print("-+-+-")
    #print board second line
    board = ""
    for number in [4, 5, 6]:
        if number in alist:
            board += "o"
            if number != 6:
                board += "|"
        elif number in alist2:
            board += "x"
            if number != 6:
                board += "|"
        else:
            board += " "
            if number != 6:
                board += "|"
    print(board)
    print("-+-+-")
    
    
    #print board third line
    
    
    board = ""
    for number in [7, 8, 9]:
        if number in alist:
            board += "o"
            if number != 9:
                board += "|"
        elif number in alist2:
            board += "x"
            if number != 9:
                board += "|"
        else:
            board += " "
            if number != 9:
                board += "|"
    print(board)

                


    
#intro

print("Tic-tac-toe")

print("By Lucas Kirazci")

#choices of play
p1_guesses = []
p2_guesses = []
computer_guesses = []
choices = input("Do you want to play two person, vs computer easy, or vs computer hard: ")

while choices not in ["two person", "computer easy", "computer hard"]:
    
    choices = input("That is not an option. Please enter again. ")



if choices == "computer easy":
    print("The layout is like this: ")
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")
    print("Enter like the top left is 1 and the top right is 3. Enter numerical order like on a book. ")
    name1 = input("Enter your name: ")
    place = input("Do you want to be first or second? ")
    while place not in ["first", "second"]:
        place = input("That is not an option. Please enter again. ")

    
    
    if place == "first":
            
         while True:   
            
            print_board(p1_guesses, computer_guesses)
            
            
            p1g = input(name1 + ", enter a coordinate: ")
            while p1g not in ["1","2","3","4","5","6","7","8","9"]:
                p1g = input("Enter again, that is not an option. ")
            p1g = int(p1g)
            
            #check if in other guess
            for bob in p1_guesses:
                while p1g == bob:
                    p1g = input("You already chose that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option, please enter again.")
                    p1g = int(p1g)
            for bob in computer_guesses:
                while p1g == bob:
                    p1g = input("The computer already did that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option, please enter again.")
                    p1g = int(p1g)
                    #check if won
            
            
            p1_guesses.append(p1g)
            
            
            if return_number(p1_guesses, computer_guesses) == 10:
                print(name1 + " wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == -10:
                print("Computer wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == 0 and len(p1_guesses) > 4:
                print("It is a tie. ")
                break
            

         

                    
        
            computer_guess = random.randint(1,9)
            while computer_guess in p1_guesses or computer_guess in computer_guesses:
                computer_guess = random.randint(1,9)
            computer_guesses.append(computer_guess)
        
        
            if return_number(p1_guesses, computer_guesses) == 10:
                print(name1 + " wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == -10:
                print("Computer wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == 0 and len(p1_guesses) > 4:
                print("It is a tie. ")
                break


            
            



    if place == "second":
        
        while True:
            
    
                        
            
            computer_guess = random.randint(1,9)
            while computer_guess in p1_guesses or computer_guess in computer_guesses:
                computer_guess = random.randint(1,9)
            computer_guesses.append(computer_guess)
            
            
            
            if return_number(p1_guesses, computer_guesses) == 10:
                print(name1 + " wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == -10:
                print("Computer wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == 0 and len(computer_guesses) > 4:
                print("It is a tie. ")
                break
            
            
            
            print_board(computer_guesses, p1_guesses) 
            
           
            p1g = input(name1 + ", enter a coordinate: ")
            while p1g not in ["1","2","3","4","5","6","7","8","9"]:
                p1g = input("Enter again, that is not an option. ")
            p1g = int(p1g)
            
            #check if in other guess
            for bob in p1_guesses:
                while p1g == bob:
                    p1g = input("You already chose that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option. Please enter again: ")
                    p1g = int(p1g)
            for bob in computer_guesses:
                while p1g == bob:
                    p1g = input("The computer already did that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option. Please enter again: ")
                    p1g = int(p1g)
                    #check if won
        
            
            p1_guesses.append(p1g)
            
            if return_number(p1_guesses, computer_guesses) == 10:
                print(name1 + " wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == -10:
                print("Computer wins!")
                break

            

if choices == "two person":
    print("The layout is like this: ")
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")
    print("Enter like the top left is 1 and the top right is 3. Enter numerical order like on a book. ")
    name1 = input("Player 1, enter your name: ")
    name2 = input("Player 2, enter your name: ")
    while True:
        
                        
        print_board(p1_guesses, p2_guesses)                
        #get user to guess
        
        p1g = input(name1 + ", enter a coordinate: ")
        while p1g not in ["1","2","3","4","5","6","7","8","9"]:
            p1g = input("Enter again, that is not an option. ")
        p1g = int(p1g)
        
        #check if in other guess
        for bob in p1_guesses:
            while p1g == bob:
                p1g = input("You already chose that. Enter again. ")
                while p1g not in ["1","2","3","4","5","6","7","8","9"]:
                    p1g = input("Enter again, that is not an option. ")
                p1g = int(p1g)
        for bob in p2_guesses:
            while p1g == bob:
                p1g = input(name2 + " already did that. Enter again. ")
                while p1g not in ["1","2","3","4","5","6","7","8","9"]:
                    p1g = input("Enter again, that is not an option. ")
                p1g = int(p1g)
        #check if won
        
        p1_guesses.append(p1g)

        if return_number(p1_guesses, p2_guesses) == 10:
            print(name1 + " wins!")
            break
        elif return_number(p1_guesses, p2_guesses) == -10:
            print(name2 + " wins!")
            break
        elif return_number(p1_guesses, p2_guesses) == 0 and len(p1_guesses) > 4:
            print("It is a tie. ")
            break
        

        print_board(p1_guesses, p2_guesses)



        
        p2g = input(name2 + ", enter a coordinate: ")
        while p2g not in ["1","2","3","4","5","6","7","8","9"]:
            p2g = input("Enter again, that is not an option. ")
        p2g = int(p2g)
        #check if rows 
            
        for bob in p2_guesses:
            while p2g == bob:
                p2g = input("You already guessed that. Enter again. ")
                while p2g not in ['1','2','3','4','5','6','7','8','9']:
                    p2g = input("That is not an option. Please enter again: ")
        for bob in p1_guesses:
            while p2g == bob:
                p2g = input(name1 + " already guessed that. Enter again. ")
                while p2g not in ['1','2','3','4','5','6','7','8','9']:
                    p2g = input("That is not an option. Please enter again: ")
                p2g = int(p2g)
        p2_guesses.append(p2g)
        
        if return_number(p1_guesses, computer_guesses) == 10:
            print(name1 + " wins!")
            break
        elif return_number(p1_guesses, computer_guesses) == -10:
            print(name2 + " wins!")
            break

      


if choices == "computer hard":       
    print("The layout is like this: ")
    print("1|2|3")
    print("-+-+-")
    print("4|5|6")
    print("-+-+-")
    print("7|8|9")
    print("Enter like the top left is 1 and the top right is 3. Enter numerical order like on a book. ")
    name1 = input("Enter your name: ")
    place = input("Do you want to be first or second? ")
    while place not in ["first", "second"]:
        place = input("That is not an option. Please enter again. ")
    
    if place == "second":
        while True:
        

                    
        
        
            computer_guess = get_next_move(computer_guesses, p1_guesses, True)[1]
            print("Computer move", computer_guess)
            computer_guesses.append(computer_guess)
            
            
            if return_number(p1_guesses, computer_guesses) == 10:
                print(name1 + " wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == -10:
                print("Computer wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == 0 and len(computer_guesses) > 4:
                print("It is a tie. ")
                break
            
            print_board(computer_guesses, p1_guesses)
           
            p1g = input(name1 + ", enter a coordinate: ")
            while p1g not in ["1","2","3","4","5","6","7","8","9"]:
                p1g = input("Enter again, that is not an option. ")
            p1g = int(p1g)
            
            #check if in other guess
            for bob in p1_guesses:
                while p1g == bob:
                    p1g = input("You already chose that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option. Please enter again: ")
                    p1g = int(p1g)
            for bob in computer_guesses:
                while p1g == bob:
                    p1g = input("The computer already did that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option. Please enter again: ")
                    p1g = int(p1g)
                    #check if won
        
            
            p1_guesses.append(p1g)
            
            if return_number(p1_guesses, computer_guesses) == 10:
                print(name1 + " wins!")
                break
            elif return_number(p1_guesses, computer_guesses) == -10:
                print("Computer wins!")
                break
                
                
                
    if place == "first":
        while True:
        
            print_board(p1_guesses, computer_guesses)
                
                
                
            p1g = input(name1 + ", enter a coordinate: ")
            while p1g not in ["1","2","3","4","5","6","7","8","9"]:
                p1g = input("Enter again, that is not an option. ")
            p1g = int(p1g)
            
            #check if in other guess
            for bob in p1_guesses:
                while p1g == bob:
                    p1g = input("You already chose that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option. Please enter again: ")
                    p1g = int(p1g)
            for bob in computer_guesses:
                while p1g == bob:
                    p1g = input("The computer already did that. Enter again. ")
                    while p1g not in ['1','2','3','4','5','6','7','8','9']:
                        p1g = input("That is not an option. Please enter again: ")
                    p1g = int(p1g)
            p1_guesses.append(p1g)
            
            
            #check if won
            
            
            
            if return_number(computer_guesses, p1_guesses) == 10:
                print(name1 + " wins!")
                break
            elif return_number(computer_guesses, p1_guesses) == -10:
                print("Computer wins!")
                break
            elif len(p1_guesses) > 4:
                print("It is a tie. ")
                break
                
            

            computer_guess = get_next_move(p1_guesses, computer_guesses, False)[1]
            print("Computer move", computer_guess)
            computer_guesses.append(computer_guess)
        
            if return_number(computer_guesses, p1_guesses) == 10:
                print("Computer wins!")
                break
            elif return_number(computer_guesses, p1_guesses) == -10:
                print(name1 + " wins!")
                break   
        
            
        
        
        
        
        
        
