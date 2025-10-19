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
image bg night = "gui/night_city.jpg"
image bg living = "gui/living_room.jpg"  
image bg bedroom = "gui/bedroom.jpg"

default alternate_path = False

#sound effects
default audio.studied = "audio/studied.mp3" 

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
    play sound studied
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
    'I jump in my seat, and whip around\ntowards the sound of the voice.\nNot from the door, but from the window?!'
    you '!!! I told you to stop jumpscaring me!\n Seriously, my heart cant take it anymore!'

    'Thats my childhood friend, my study buddy Ryley.'
    r 'So, what are we studying today, hmmm?'
    'Ryley kicks their shoes off from the outside and climbs through the window.'

    '...and ends up on the floor.'

    you 'What the! You knocked over my ultra special study pencil case!'

    'Ryley scrambles around picking everything back up.'
    r 'Noo! Not your ultra special study pencil case!!'
    'I laugh and help clean up. Before we know it,\nthe room is back to its pristine studying condition.'

    you 'Dont worry about it too much. Youre okay too, right?'
    'Ryley brightens up, clearly really happy about something.'
    r 'Yeah!! Not a scratch!! Dont worry~'
    'I smile, relieved everythings in order.\nHehe. And now--'
    you 'Study time!! Grab your pencils, take a seat. lets lock in!!'
    
    # bg: study desk

    'Ryley plops down on the bed behind me, not a book in sight.'

    'How how how, does Ryley get by without studying!!!\nMaybe Ive got a thing or two to learn.'

    r 'Hmm, today Im thinking [int(times[STUDY_TIME]/60)] minutes.'
    'I get everything into position and get ready, picking up my pen. Its time to lock in.'
    r 'Ill set a timer, kay? Ill tell you when youre done. Good luck~!'

    # bg changes to night

    call countdown

    # if session completed, exit the game
    if times[STUDY_TIME] == 0:
        traveller "Congrats in conpleting your study session"
        play audio studied
        return
   
    traveller "Remaining study time: [int(times[STUDY_TIME]/60)] minutes"

    'Ding, ding~\nThe sweet sound of the alarm pierces the silence.'
    r 'TIIIMES UPPPP!!!!!'

    
    # different path depends on the day
    if alternate_path:
        jump day1_midnight1
    else:
        jump day1_evening
    return

label day1_evening:
    r 'See? Youre done in no time!!'
    'Though it felt like I just sat down, apparently the timer thinks otherwise.'
    you 'Huh?! Already? But I just started.'
    'I look at my desk. I realize I already finished what I sat down to do.\nHuh, time does move fast when youre locked in.'
    r 'Cmon, let’s do something before dinner. Im tired of sitting around!'
    'The light pours through the window, illuminating the room with gold.'
    you 'Well, we still have some time before dinner wanna play a game?'
    'Ryley pulls out their phone with an evil glint in their eyes.'
    r 'Wanna play some Clash Royale?'
    'I pull mine out too with a grin. Itll be a breath of fresh air after the studying.'
    # play sfx clash royale opening
    you 'Youre on.'

    call countdown

    jump day1_midnight2
    return

label day1_midnight1:
    'Ryley starts shaking my chair before I can even put my pencil down.'
    you 'Okay, okay!! Im done studying.'
    'Its so dark outside now, the moon high in the sky.\nGosh, how long was I out for.'
    'My stomach grumbles and thunders through the room!\n I look down sheepishly.'
    'You hungry? Come come, lets go out to eat!!\nWe can stretch our legs for a bit too!'
    you 'I could go for some ramen.'
    'Normally Id just make some instant noodles,\nbut itd be nice to head out for a little bit.'
    r 'Midnight ramen always hit different. lets gooooo!'

    show bg night
    'Sometimes, I get pretty carried away while\nstudying and end up sitting for hours.'
    'No matter how long though, Ryley always waits for me despite never studying themself\nIm glad to have a friend like–'

    'I hear the worlds loudest slurp next to me,\nbelonging to none other than Ryley.'
    r 'So good! \nI could eat 9 more bowls.'
    you 'Hey, let me have my moment! Were overdue for some exposition!'
    'I sigh happily.\nAfter every study session, Ryley and I hang out for a while- \nit almost makes the hours worth it.'
    you 'Do you think you can even afford that many bowls?'
    'Ryley rubs their head sheepishly.'
    r 'Hey, its not like Im dead broke, okay?!'
    'Ryley sets down their bowl and leans back, satisfied.'
    'Sometimes, I get pretty carried away while\nstudying and end up sitting for hours.'
    'No matter how long though,\nRyley always waits for me despite never studying themself.\nIm glad to have a friend like-'

    r 'So [user_name], hows your academic comeback going?\nHave you rewritten all your notes yet?'
    you 'As if thats a bad idea!!\nAnyway, I think its going all right.\nI just need to continue doing this for a while.'
    'The chef comes by and picks up Ryleys bowl.\n Nothing left in there, not even a drop of broth.'
    r 'Thank you for the meal~!'
    'Ryley leaves cash for the chef to take,\nand turns to the window to stare at the neon lights outside.'
    'Yknow, youve been pushing yourself pretty hard lately.'
    'Im caught off a little. Why so serious!'
    you 'Yeah, but youre helping a lot lately, you know.\nYoure kinda keeping me sane out here.'
    'Ryley turns to me and laughs, clapping their hands together.'
    r 'Im glad!! You got this, [user_name]~\nwe can keep having lotsa fun after studying each time too.'
    'Its true- I have been studying a lot more lately,\nand it really has been draining.'

    show bg night

    you 'Thanks. Im grateful.That was pretty deep of you too, Ryley.'
    'Ryley winks and puts their finger up to their lips\nin a shushing shape.'
    'Dont tell anyone, kay? Youll ruin my rep.'
    'We both laugh, and keep chatting until the store closes.'

    jump day2
    return

label day1_midnight2:
    'Its so dark outside now, the moon high in the sky.\nGosh, how long did we play for?!'
    'My stomach grumbles and thunders through the room!\n I look down sheepishly.'
    'You hungry? Come come, lets go out to eat!!\nWe can stretch our legs for a bit too!'
    you 'I could go for some ramen.'
    'Normally Id just make some instant noodles, but itd be nice to head out for a little bit.'
    r 'Night time ramen always hit different! lets gooooo!!!'

    show bg night
    pause 2.0
    'Sometimes, I get pretty carried away while studying and end up sitting for hours.'
    'No matter how long though, Ryley always waits for me despite never studying themself.\nIm glad to have a friend like--'
    # play slurp sfx
    'sluuuuurrrrp'
    'I hear the worlds loudest slurp next to me, belonging to none other than Ryley.'
    r 'So good, \nI could eat 9 more bowls..!'
    you 'Hey, let me have my moment! Were overdue for some exposition!'
    'I sigh happily.\nAfter every study session, Ryley and I hang out for a while. It almost makes the studying worth it.'
    you 'Do you think you can even afford that many bowls?'
    'Ryley rubs their head sheepishly.'
    r 'Hey, its not like Im dead broke, okay?!'
    'Ryley sets down their bowl and leans back, satisfied.'
    r 'So [user_name], hows your academic comeback going?\nHave you rewritten all your notes yet?'
    you 'As if thats a bad idea!!\nAnyway, I think its going all right. I just need to continue doing this for a while.'
    'The chef comes by and picks up Ryleys bowl. nothing left in there, not even a drop of broth.'
    r 'Thank you for the meal~!'
    'We keep chatting until the store closes.'
    pause 2.0


    jump day2
    return

label day2:
    traveller "It's day 2 now"
    'Its a Tuesday morning, when…'
    'A devious creature spills onto the floor.\nThrough my window.\nAnd knocks over my ultra special study pencil case.'
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