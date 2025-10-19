default traveller = Character('Traveller')
default study_time = 0
default session_time = 0
default break_time = 0
# default times = [0,0,0,0,0,0,0] # data list for functions not implemented
           
default is_playing_music = True
default midnight_path_d1 = False

label start: # day 1
    # initialization
    python:
        user_name = renpy.input("What's your name?", length=32).strip()

        # promting for user name and study time
        while True:
            try:
                study_time = renpy.input("How long do you want to study for (total) (in minutes)?").strip()
                study_time = int(study_time)
            except:
                "Input error" "please input number"
            try:
                session_time = renpy.input("How long do you want a small session to be (in minutes)?").strip()
                session_time = int(session_time)
            except:
                "Input error" "please input number"
            try:
                break_time = renpy.input("How long do you want your break time to be (in minutes)?").strip()
                break_time = int(break_time)
                break
            except:
                "Input error" "please input number"
        
        # alternate path if student study for more than 30m per session
        if session_time >= 30:
            midnight_path_d1 = True

        # convert to seconds
        study_time = study_time * 60
        session_time = session_time * 60
        break_time = break_time * 60
        
        # for displaying
        session_minutes = int(session_time / 60)
        session_seconds = session_time % 60
        break_minutes = int(break_time / 60)
        break_seconds = break_time % 60

    # show bg 
    # show traveller #at right
    # hide traveller
    traveller "Hi [user_name]!"
    # Lore stuff

    traveller "You will study for [int(study_time/60)] minutes"
    traveller "You session time is [int(session_time/60)] minutes"
    traveller "You break time is [int(break_time/60)] minutes"

    python:
        session_time = min(session_time, study_time)
        study_time -= session_time
        break_time = min(break_time, study_time)
        study_time -= break_time

    while session_time > 0:
        traveller "Remaining session time [session_minutes:02]:[session_seconds:02]{w=1}{nw}"
        python:
            session_time -= 1
            session_minutes = int(session_time / 60)
            session_seconds = session_time % 60

    while break_time > 0:
        traveller "Remaining break time [break_minutes:02]:[break_seconds:02]{w=1}{nw}"
        python:
            break_time -= 1
            break_minutes = int(break_time / 60)
            break_seconds = break_time % 60

    # stops game from skipping after the timer ends
    python:
        renpy.choice_for_skipping()

    # if session completed, exit the game
    if study_time == 0:
        traveller "Congrats in conpleting your study session"
        return

    traveller "Remaining study time: [int(study_time/60)] minutes"

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
