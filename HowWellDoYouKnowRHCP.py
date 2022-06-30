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
    
    choice = input("choose a key by it's associated number: ")
       
    quit(choice)


    if (counter < 2 or int(choice) < 1 or int(choice) > (counter-1)):
        print("invalid")
    else:
        key = choices[f"{choice}"]
        print(f"The information for your choice is: {PeanutButterCup[key]}")

def play_song(Songs, song):
    while(Songs)

        quit_message()

        attempt = input("What is the next line?")

        quit(attempt)
    
    print("You've reached the end of the lyrics, try again")

Songs = {
        "Californication x Red Hot Chilli Peppers" : "",
        "Other side x Red Hot Chilli Peppers": ""
    }

playing = True
print("Try to guess the lyric's next line of one of the following classic songs!\n")

while(playing):
    next_line = play_song(Songs, choose_song(Songs))
    

