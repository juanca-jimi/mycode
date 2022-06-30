def quit_message():
    print("To quit, enter \"q\"")

def quit(flag):
    if flag == "q":
        quit()

def choose_song(Songs):
    counter = 1
    print("choose a song")
    choices = {}

    for song in Songs.keys():
        print(f"{counter}. {song}")
        choices[f"{counter}"] = song
        counter += 1

    quit_message()
    
    choice = input("choose a song by it's associated number: ")
       
    quit(choice)


    if (counter < 2 or not choice.isDigit() or int(choice) < 1 or int(choice) > (counter-1)):
        print("invalid. try again.")
        choose_song(Songs)
    else:
        key = choices[f"{choice}"]
        print(f"You chose {key}")

def play_song(Songs, song):
    n_lines = len(Songs[song].splitlines())
    
    stopping_point = Random.randomint(1, n_lines)
    
    current_line = 0;

    while(current_line < stopping_point):
        print(Songs[song].splitlines)

    

Songs = {
        "Californication x Red Hot Chilli Peppers" : "",
        "Other side x Red Hot Chilli Peppers": ""
    }

playing = True
print("Try to guess the lyric's next line of one of the following classic songs!\n")

while(playing):
    
    correct_next_line  = play_song(Songs, choose_song(Songs))
    
    quit_message()

    attempt = input("What is the next line?")

    quit(attempt)

    print("Correct! You win") if correct_next_line.lower() == attempt.lower() else print("Better luck next time!")
    

