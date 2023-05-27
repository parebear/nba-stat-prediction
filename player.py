#Testing with just 1 player for now
def main():
    player = ""

    while (player == ""):
        player = input("Choose a player ")
            
    print("Player chosen was {}".format(player))


if __name__ == "__main__":
   main()
