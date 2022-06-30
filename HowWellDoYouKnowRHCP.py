import random

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
    song = Songs[song].splitlines()

    n_lines = len(song)
    
    stopping_point = Random.randomint(1, n_lines)
    
    current_line = 0;
    
    while(current_line < stopping_point):
        print(song[current_line])
        current_line += 1

    

Songs = {
        "Californication x Red Hot Chilli Peppers" : "Psychic spies from China try to steal your mind's elation
And little girls from Sweden dream of silver screen quotation
And if you want these kind of dreams it's Californication
It's the edge of the world and all of Western civilization
The sun may rise in the East at least it's settled in a final location
It's understood that Hollywood sells Californication
Pay your surgeon very well to break the spell of aging
Celebrity skin, is this your chin, or is that war you're waging?
First born unicorn
Hardcore soft porn
Dream of Californication
Dream of Californication
Dream of Californication
Dream of Californication
Marry me, girl, be my fairy to the world, be my very own constellation
A teenage bride with a baby inside getting high on information
And buy me a star on the boulevard, it's Californication
Space may be the final frontier but it's made in a Hollywood basement
And Cobain can you hear the spheres singing songs off Station To Station?
And Alderaan's not far away, it's Californication
Born and raised by those who praise control of population
Well, everybody's been there and I don't mean on vacation
First born unicorn
Hardcore soft porn
Dream of Californication
Dream of Californication
Dream of Californication
Dream of Californication
Destruction leads to a very rough road but it also breeds creation
And earthquakes are to a girl's guitar, they're just another good vibration
And tidal waves couldn't save the world from Californication
Pay your surgeon very well to break the spell of aging
Sicker than the rest, there is no test, but this is what you're craving?
First born unicorn
Hardcore soft porn
Dream of Californication
Dream of Californication
Dream of Californication
Dream of Californication",
        "Other side x Red Hot Chilli Peppers": "How long, how long will I slide?
Separate my side, I don't
I don't believe it's bad
Slit my throat it's all I ever
I heard your voice through a photograph
I thought it up and brought up the past
Once you know you can never go back
I gotta take it on the other side
Centuries are what it meant to me
A cemetery where I marry the sea
Stranger things could never change my mind
I gotta take it on the other side
Take it on the other side
Take it on, take it on
How long, how long will I slide?
Separate my side, I don't
I don't believe it's bad
Slit my throat it's all I ever
Pour my life into a paper cup
The ashtray's full and I'm spillin' my guts
She wants to know, am I still a slut?
I've got to take it on the other side
A scarlet starlet and she's in my bed
A candidate for a soul mate bled
Push the trigger and pull the thread
I gotta take it on the other side
Take it on the other side
Take it on
Take it on
How long, how long will I slide?
Separate my side, I don't
I don't believe it's bad
Slit my throat it's all I ever
Turn me on, take me for a hard ride
Burn me out, leave me on the other side
I yell and tell it that it's not my friend
I tear it down, I tear it down
And then it's born again
How long, how long will I slide?
Separate my side, I don't
I don't believe it's bad
Slit my throat it's all I ever
How long, I don't, I don't believe it's bad
Slit my throat it's all I ever"
    }

playing = True
print("Try to guess the lyric's next line of one of the following classic songs!\n")

while(playing):
    
    correct_next_line  = play_song(Songs, choose_song(Songs))
    
    quit_message()

    attempt = input("What is the next line?")

    quit(attempt)

    print(f"The next line is {correct_next_line}")

    print("Correct! You win") if correct_next_line.lower() == attempt.lower() else print("Better luck next time!")
    


