define traveller = Character('Traveller')
define study_time = 0
           
define midnight_path_d1 = False # True = midnight

label start: # day 1
    
    python:
        user_name = renpy.input("What's your name?", length=32).strip()

        # promting for user name and study time
        while True:
            try:
                study_time = renpy.input("How long do you want to study for (in minutes)?").strip()
                study_time = int(study_time)
                break
            except:
                "Input error" "please input number"
        
        # alternate path if student study for more than 30m
        if study_time >= 30:
            midnight_path_d1 = True

        # convert to seconds
        study_time = study_time * 60
        
        # for displaying
        study_minutes = int(study_time / 60)
        study_seconds = study_time % 60


    # show bg 
    # show traveller #at right
    # hide traveller
    traveller "Hi [user_name]!"

    # Lore stuff

    traveller "You will study for [int(study_time/60)] minutes"

    while study_time > 0:
        traveller "Remaining time [study_minutes:02]:[study_seconds:02]{w=1}{nw}"#with Dissolve(0)
        python:
            study_time -= 1
            study_minutes = int(study_time / 60)
            study_seconds = study_time % 60

    # stops game from skipping after the timer ends
    python:
        renpy.choice_for_skipping()

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