default traveller = Character('Traveller')

# data list and list index for functions
default times = [0,0,0] 
define STUDY_TIME = 0
define SESSION_TIME = 1
define BREAK_TIME = 2

# character and background definitions
default r = Character("Ryley")
default unknown = Character("???")
default you = Character("You")

image bg afternoon = "gui/afternoon.jpg"
image bg living = "gui/living_room.jpg"  
image bg bedroom = "gui/bedroom.jpg"

default alternate_path = False

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
    if alternate_path:
        jump day1_night2
    else:
        jump day1_evening
    return

label day1_evening:
    traveller "It's the evening now"
    call countdown
    jump day1_night1
    return

label day1_night1:
    traveller "It's midnight now"
    call countdown
    jump day2
    return

label day1_night2:
    traveller "It's midnight now"
    call countdown
    jump day2
    return

label day2:
    traveller "It's day 2 now"
    call countdown

    while times[STUDY_TIME] > 0:
        call countdown
    return

label countdown:
    python:
        times[SESSION_TIME] = min(times[SESSION_TIME], times[STUDY_TIME])
        times[STUDY_TIME] -= times[SESSION_TIME]
        times[BREAK_TIME] = min(times[BREAK_TIME], times[STUDY_TIME])
        times[STUDY_TIME] -= times[BREAK_TIME]

        tmp_session_time = times[SESSION_TIME]
        tmp_break_time = times[BREAK_TIME]
        session_minutes = int(tmp_session_time / 60)
        session_seconds = tmp_session_time % 60
        break_minutes = int(tmp_break_time / 60)
        break_seconds = tmp_break_time % 60

    while tmp_session_time > 0:
        # display message, wait 1 second, then skip
        traveller "Remaining session time [session_minutes:02]:[session_seconds:02]{w=1}{nw}"
        python:
            tmp_session_time -= 1
            session_minutes = int(tmp_session_time / 60)
            session_seconds = tmp_session_time % 60

    while tmp_break_time > 0:
        traveller "Remaining break time [break_minutes:02]:[break_seconds:02]{w=1}{nw}"
        python:
            tmp_break_time -= 1
            break_minutes = int(tmp_break_time / 60)
            break_seconds = tmp_break_time % 60

    # stops game from skipping after the timer ends
    python:
        renpy.choice_for_skipping()
    return