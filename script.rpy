# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color = "#d60f44")
define i = Character("vinith", color="#3507a0")

image casual1 = im.Scale("1.png", 1920,1080)
image causal2  = im.Scale("2.png", 1920,1080)
image casual3 = im.Scale("3.png", 1920,1080)
image casual4 = im.Scale("4.png", 710, 1000)

image mansion = im.Scale("mansion_front_evening.png", 1920, 1080)
image entrance = im.Scale("interior_entrance_evening.png", 1920,1080)
image room = im.Scale("bedroom01_evening.png", 1920,1080)
image kitchen = im.Scale("mkitchen_day.png", 1920,1080)
image back yard  = im.Scale("backyard_evening.png", 1920,1080)
image hall = im.Scale("mroom_day.png", 1920,1080)
image elen = im.Scale("Miki_A_Miko_Smile.png", 710, 1000)

# The game starts here.

label start:
    call variables
    $ GameRunning = True
    while GameRunning:
 
    return

label variables:
    $INVENTORY[0]=Items("apple", 1, 1, 0, 0)
    return
