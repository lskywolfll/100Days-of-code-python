
def welcome():
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

def game():
    road = input("""You're at a cross road. Where do you want to go? Type "left" or "right" \n""")

    if road == "left":
        road_lake = input("""You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n""")
        
        if road_lake == "wait":
            road_island = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n""")
            road_island = road_island.lower()
            if road_island == "yellow":
                print('''
                              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
          Win  _/_______\_
              /___________\
                ''')
                print("You Win!")
            elif road_island == "red":
                print('''
                              (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                ''')
                print("Burned by fire.\n Game Over.")
            elif road_island == "blue":
                print('''
                                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
                ''')
                print("Eaten by beasts.\n Game Over.")
            else:
                print("Game Over.")

        else:
            print("""
*********************************************************************++
      |\
       \`._.-' `--.
        ) o o =[#]#]
        ) _o      -3
       /.' `-.,---'       kOs
             '
*******************************************
            """)
            print("Attacked by trout.\n Game Over.")
    else:
        print('''
     |     '       /  |    |             /  |
     /__      ___ (  /     /__   Y  __  (  _/
     \\--`-'-|`---\\ |     \`--`-'-|`---\\/
      |' _/   ` __/ /       |'__/   ` __/ |
      '._  W    ,--'        '-.   w   ,--/
         |_:_._/              |'_._._/  /
                              |________/

[dead]
        ''')
        print("Fall into a hole.\nGame Over.")

def run():
    welcome()
    game()


if __name__ == "__main__":
    run()