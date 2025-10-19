default traveller = Character('Traveller')

default times = [0,0,0,0,0,0,0] # data list for functions, may not be implemented
define STUDY_TIME = 0
define SESSION_TIME = 1
define SESSION_MINUTES = 2
define SESSION_SECONDS = 3
define BREAK_TIME = 4
define BREAK_MINUTES = 5
define BREAK_SECONDS = 6
default r = Character("Ryley")
default unknown = Character("???")
default you = Character("You")
default study_time = 0
default session_time = 0
default break_time = 0
# default times = [0,0,0,0,0,0,0] # data list for functions not implemented
image bg afternoon = "gui/afternoon.jpg"
image bg living = "gui/living_room.jpg"  
image bg bedroom = "gui/bedroom.jpg"
default is_playing_music = True
default midnight_path_d1 = False

label start: # day 1
    # initialization
    python:
        user_name = renpy.input("What's your name?", length=32).strip()

        # promting for user name and study time
        while True:
            try:
                times[STUDY_TIME] = renpy.input("How long do you want to study for (total) (in minutes)?").strip()
                times[STUDY_TIME] = int(times[STUDY_TIME])
            except:
                "Input error" "please input number"
            try:
                times[SESSION_TIME] = renpy.input("How often do you want to have a break (in minutes)?").strip()
                times[SESSION_TIME] = int(times[SESSION_TIME])
            except:
                "Input error" "please input number"
            try:
                times[BREAK_TIME] = renpy.input("How long do you want your break time to be (in minutes)?").strip()
                times[BREAK_TIME] = int(times[BREAK_TIME])
                break
            except:
                "Input error" "please input number"
        
        # alternate path if student study for more than 30m per session
        if times[SESSION_TIME] >= 30:
            midnight_path_d1 = True

        # convert to seconds
        times[STUDY_TIME] = times[STUDY_TIME] * 60
        times[SESSION_TIME] = times[SESSION_TIME] * 60
        times[BREAK_TIME] = times[BREAK_TIME] * 60
        
        # for displaying
        times[SESSION_MINUTES] = int(times[SESSION_TIME] / 60)
        times[SESSION_SECONDS] = times[SESSION_TIME] % 60
        times[BREAK_MINUTES] = int(times[BREAK_TIME] / 60)
        times[BREAK_SECONDS] = times[BREAK_TIME] % 60

    # show bg 
    # show traveller #at right
    # hide traveller
    show bg afternoon
    # show traveller #at right
    # hide traveller
    'The sun begins its descent in the sky as I walk \nhome from school.'
    'The cicadas are crying, and inside, so am I...'
    'I am soooo behind on my classes.'
    # play music
    'Last week, I was 38 minutes short of my\nweekly 40 hours of studying.'
    'The week before that, 41 minutes.'
    'And before that I didnt study at all--'
    'Thats probably not the root of all my problems.'
    show bg living
    pause 2.0
    show bg bedroom
    'The moment Im indoors, the clock starts ticking.'
    'I jump out of my uniform, change into a comfy outfit, \nand sit down on the desk, when--'

    unknown 'Heya, [user_name]!! You ready to study?'
    'I jump in my seat, and whip around towards the sound of the voice…\nNot from the door, but from the window?!'

    traveller "You will study for [int(times[STUDY_TIME]/60)] minutes"
    traveller "You session time is [int(times[SESSION_TIME]/60)] minutes"
    traveller "You break time is [int(times[BREAK_TIME]/60)] minutes"

    call countdown

    # if session completed, exit the game
    if times[STUDY_TIME] == 0:
        traveller "Congrats in conpleting your study session"
        return

    traveller "Remaining study time: [int(times[STUDY_TIME]/60)] minutes"

    # different path depends on the day
    if midnight_path_d1:
        jump day1_midnight
    else:
        jump day1_evening

label day1_evening:
    traveller "It's the evening now"
    jump day2

label day1_midnight:
    traveller "It's midnight now"
    jump day2

label day2:
    traveller "It's day 2 now"

label countdown:
    python:
        times[SESSION_TIME] = min(times[SESSION_TIME], times[STUDY_TIME])
        times[STUDY_TIME] -= times[SESSION_TIME]
        times[BREAK_TIME] = min(times[BREAK_TIME], times[STUDY_TIME])
        times[STUDY_TIME] -= times[BREAK_TIME]

    while times[SESSION_TIME] > 0:
        # display message, wait 1 second, then skip
        traveller "Remaining session time [times[SESSION_MINUTES]:02]:[times[SESSION_SECONDS]:02]{w=1}{nw}"
        python:
            times[SESSION_TIME] -= 1
            times[SESSION_MINUTES] = int(times[SESSION_TIME] / 60)
            times[SESSION_SECONDS] = times[SESSION_TIME] % 60

    while times[BREAK_TIME] > 0:
        traveller "Remaining break time [times[BREAK_MINUTES]:02]:[times[BREAK_SECONDS]:02]{w=1}{nw}"
        python:
            times[BREAK_TIME] -= 1
            times[BREAK_MINUTES] = int(times[BREAK_TIME] / 60)
            times[BREAK_SECONDS] = times[BREAK_TIME] % 60

    # stops game from skipping after the timer ends
    python:
        renpy.choice_for_skipping()