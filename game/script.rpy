define traveller = Character('Traveller')
           
label start:
    
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
        
        # convert to seconds
        
        study_time = study_time * 60
        
        study_minutes = int(study_time / 60)
        study_seconds = study_time % 60


    # show bg 
    # show traveller #at right
    traveller "Hi [user_name]!"
    traveller "You will study for [int(study_time/60)] minutes"

    while study_time > 0:
        traveller "Remaining time [study_minutes:02]:[study_seconds:02]{w=1}{nw}"#with Dissolve(0)
        python:
            study_time -= 1
            study_minutes = int(study_time / 60)
            study_seconds = study_time % 60
    
    hide traveller