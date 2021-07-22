# Blackjack / Twenty

# - Program welcomes a user startup
# - Bottom of the screen, two buttons display: "add card" and "Challenge computer" 
#       * 2 boxes + 2 text sprites
# - When "add card" button pressed, a random card is dealt. Its score adds up to the score counter, add any cards at any time
#       * 2 text sprite(bottom)
# - When "challenge computer" button pressed, computer simulation start
#       * 2 text sprite(bottom)

import play
from random import randint

play.set_backdrop('black')
#add card box
add_card_box = play.new_box(
    color='red',
    x=-110, y=-140,
    width=140, height=45,
    border_color='red',
    border_width = 3,
    transparency=90
)

add_card_text = play.new_text(
    words="Add Card",
    x=-110, y=-140,
    font=None, font_size=30,
    color="black",
)

#challenge computer box
chng_computer_box = play.new_box(
    color='red',
    x=110, y=-140,
    width=190, height=45,
    border_color='red',
    border_width = 3,
    transparency=90
)

chng_computer_text = play.new_text(
    words="Challenge Robot",
    x=110, y=-140,
    font=None, font_size=30,
    color="black",
)

#instructions text
instructions = play.new_text(
    words="Try to get 21 POINTS and BEAT the ROBOT",
    x=0, y=230,
    font=None, font_size=50,
    color="red",
)

#scores
users_score = play.new_text(
    words="0",
    x=-110, y=-200,
    font=None, font_size=50,
    color="white"
)

computers_score = play.new_text(
    words="0",
    x=110, y=-200,
    font=None, font_size=50,
    color="white"
)

#users made steps
made_steps = play.new_text(
    words="0",
    x=-100, y=-250,
    font=None, font_size=40,
    color="red"
)

comp_steps = play.new_text(
    words="0",
    x=100, y=-250,
    font=None, font_size=40,
    color="red"
)
#welcome message
welcome = play.new_text(
    words="Welcome to Blackjack",
    x=0, y=0,
    font=None, font_size=50,
    color="red"
)
#lose 
lose = play.new_text(
    words="You Lost",
    x=0, y=0,
    font=None, font_size=40,
    color="red"
)

#win
win = play.new_text(
    words="You Won",
    x=0, y=0,
    font=None, font_size=40,
    color="red"
)

lose.hide()
win.hide()
welcome.hide()

card_images = []
computers_card_images = []

for i in range(11):
    card_image = play.new_image(
        image=str(i+1)+'.png', 
        size=40, 
        x=-120, y=40
    )

    computers_card_image = play.new_image(
        image=str(i+1)+'.png', 
        size=40, 
        x=120, y=40
    )

    card_images.append(card_image)
    card_image.hide()

    computers_card_images.append(computers_card_image)
    computers_card_image.hide()

@play.when_program_starts
def start():
    pass

@add_card_box.when_clicked
async def users_clicked():
    rand_num = randint(1, 11)
    card_images[rand_num - 1].show()

    users_score.words = str(int(users_score.words) + rand_num)
    made_steps.words = str(int(made_steps.words) + 1)

    for n in range(11):
        if card_images[n].is_shown:
            card_images[n].hide()

    card_images[rand_num - 1].show()
    if int(users_score.words) > 20:
        add_card_box.hide()
        add_card_text.hide()
        chng_computer_box.hide()
        chng_computer_text.hide()
        card_images[rand_num - 1].hide()

        made_steps.hide()
        comp_steps.hide()
        computers_score.hide()
        users_score.hide()
        instructions.hide()
        if int(users_score.words) == 21: 
            win.show()
        elif int(users_score.words) > 21:
            lose.show()

@chng_computer_box.when_clicked
async def challenge_clicked():
    #hide buttons
    add_card_box.hide()
    add_card_text.hide()
    chng_computer_box.hide()
    chng_computer_text.hide()

    while int(comp_steps.words) != int(made_steps.words):
        #draw new card
        rand_robot_num = randint(1, 11)
        computers_card_images[rand_robot_num - 1].show()

        #robot's score
        computers_score.words = str(int(computers_score.words) + rand_robot_num)
        #add 1 to comps_steps
        comp_steps.words = str(int(comp_steps.words) + 1)
        
        #wait 1 second
        await play.timer(seconds=1)

        #hide then
        computers_card_images[rand_robot_num - 1].hide()

    #show buttons
    add_card_box.hide()
    add_card_text.hide()
    chng_computer_box.hide()
    chng_computer_text.hide()

    for i in range(11):
        if card_images[i].is_shown:
            card_images[i].hide()
        if computers_card_images[i].is_shown:
             computers_card_images[i].hide()

    made_steps.hide()
    comp_steps.hide()
    computers_score.hide()
    users_score.hide()
    instructions.hide()
    
    if int(computers_score.words) >= 22:
        win.show()
    else:
        if int(computers_score.words) == 21:
            lose.show
        if int(users_score.words) > int(computers_score.words):
            win.show()
        elif int(users_score.words) < int(computers_score.words):
            lose.show()
        else: 
            win.show()
    
@play.repeat_forever
def repeat():
    pass

play.start_program()