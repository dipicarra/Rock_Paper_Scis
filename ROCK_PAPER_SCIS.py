# ROCK PAPER SCISSORS
# YOU CAN CONTACT ME @ https://discord.com/users/976932346550972477

# THIS IS V2 OF A CS PROJECT
# BY ROMEU

plays = ["r", "p", "s"] # THE PLAYS ALLOWED IN THE GAME
a = True
while a:
    # --- INTRO ---

    print(""" 
    How to play :
    To play ROCK - write 'r'
    To play PAPER - write 'p'")
    To play SCISSORS - write 's")
    That's it have fun! <3
    """)

    # --- INITIALIZATION ---

    p1 = str(input("PLAYER 1 - PLAY : "))
    p2 = str(input("PLAYER 2 - PLAY : "))

    # --- VERIFICATION ---
    if p1 in plays and p2 in plays:
        if p1 == p2:
            print("PLAYER 1 AND 2 - DRAW")
        elif p1 == "r" and p2 == "p":
            print("PLAYER 2 - WINS")
        elif p1 == "r" and p2 == "s":
            print("PLAYER 1 - WINS")
        elif p1 == "p" and p2 == "r":
            print("PLAYER 1 - WINS")
        elif p1 == "p" and p2 == "s":
            print("PLAYER 2 - WINS")
        elif p1 == "s" and p2 == "r":
            print("PLAYER 2 - WINS")
        elif p1 == "s" and p2 == "p":
            print("PLAYER 1 - WINS")
    else:
        print("""
        Please use the allowed plays:
        - Rock - "w" 
        - Paper - "p"
        - Scissors - "s"
        """)

    # --- LOOP BREAKER ---
    cp = str(input("WOULD YOU LIKE TO CONTINUE PLAYING? (y/n): "))
    if cp == "y":
        a == True
    else:
        break