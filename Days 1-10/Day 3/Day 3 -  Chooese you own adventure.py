print("Welcome to my choose your own adventure! ")

print('''           .-.
           [.-''-.,
           |  //`~\)
           (<| 0\0|>_
           ";\  _"/ \\_ _,
          __\|'._/_  \ '='-,
         /\ \    || )_///_\>>
        (  '._ T |\ | _/),-'
         '.   '._.-' /'/ |
         | '._   _.'`-.._/
           ,\ / '-' |/
         [_/\-----j
    _.--.__[_.--'_\__
   /         `--'    '---._
  /  '---.  -'. .'  _.--   '.
  \_      '--.___ _;.-o     /
    '.__ ___/______.__8----''')

left_or_right = (input("You arrive at a pathway that splits do you choose left or right? ")).lower()

if left_or_right == "left":
    swim_or_wait = (input("You come to a river do you swim or wait? ")).lower()
    if swim_or_wait == "wait":
        print("You waiting allowed for a small boat to arrive that lead you to the otherside and you come to a section with multiple doors.")
        door = (input("Which door do you pick? ")).lower()
        if door == "blue":
            print("There was a monster stampede that ran you over. Game Over.")
        elif door == "red":
            print("You meet an angry dragon that burns you. Game Over.")
        elif door == "yellow":
            print("You have found the Genie that will grant you wishes! You've won!")
        else:
            print("Game Over.")
    else:
        print("You were attacked by hungery crocs on your swim. Game Over.")

else:
    print("Your path lead to a hole that you fell into. Game Over.")