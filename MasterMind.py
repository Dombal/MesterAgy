from random import randint


def player_guess( C ):
    nofcolours=0
    while nofcolours < 4 :
        guess_input=input("\033[1;37;40m Choose 4 colours!")
        guess=[]
        nofcolours=0
        for i in range(len(guess_input)):
            if (guess_input[i] in C) and not (guess_input[i] in guess) : 
                nofcolours += 1
                guess.append(guess_input[i])
            if nofcolours==4:
                break
        if nofcolours < 4 :
            print("Not enough good colours. Repeat!")

    return guess


def check (L, M):
    white_counter=0
    black_counter=0   
    for i in range(4):
        for j in range (4):
            if L[j] == M[i]:
                if j==i:
                    black_counter=black_counter+1
                else:
                    white_counter=white_counter+1
    return [black_counter, white_counter]

def colour_line( M ) :

    line = " "
    for i in range(4) :
        if M[i] == "P":
            line += '\033[1;35;45m     '
        elif M[i] == "R":
            line += '\033[1;31;41m     '
        elif M[i] == "G":
            line += '\033[1;32;42m     '
        elif M[i] == "Y":
            line += '\033[1;33;43m     '
        elif M[i] == "B":
            line += '\033[1;34;44m     '
        elif M[i] == "W":
            line += '\033[1;37;47m     '
        else:
            break
    return line


    

def plot (tc, guess, bc, wc): 
    circles= 'o' * wc
    print(str(tc+1) + ".   " + colour_line(guess) +  "\033[0;37;40m      " + 'O'*wc + 'X'*bc )


    
colours_draw=[ "R", "G", "W", "P" , "B", "Y"] 
colours=[ "R", "G", "W", "P" , "B", "Y"] 

hidden_colours=[]
for i in range(4):
    hide=randint(0,5-i)
    hidden_colours.append(colours_draw[hide])
    colours_draw.remove(colours_draw[hide])


print ("Welcome to our game! This game is the computer form of the popular board game called Master Mind.")
print ("Rules: The  computer will hide 4 colours to 4 spot, none of the colour is repeated. The player's task is to guess the hidden colours. If  colour is matched, but the spot isn't good, the computer will sign 'O'. If the spot is good as well the sign will be 'X'. The player has 10 turns to guess it. Have a good luck!")    
print("Colours: R = Red;  G = Green; W= White; P = Purple; B = Blue; Y = Yellow;")
print("I hid the colours! Guess it!")

nofturns=10      

for turn in range(nofturns):
    guess_colours = player_guess( colours )
    aux=check(hidden_colours,guess_colours)
    plot(turn, guess_colours, aux[0], aux[1])
    if aux[0] == 4:
        print("Congratulations! You won.")
        break
    if turn == nofturns-1  :
        print ("Unfortunately, You lost!")
        print("The good answer is:")
        plot(-1, hidden_colours, 4, 0)

