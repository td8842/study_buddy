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
image bg night = "gui/night_city.jpg"
image bg living = "gui/living_room.jpg"  
image bg bedroom = "gui/bedroom.jpg"

default is_playing_music = True
default midnight_path_d1 = False

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

    python:
        times[SESSION_TIME] = min(times[SESSION_TIME], times[STUDY_TIME])
        times[STUDY_TIME] -= times[SESSION_TIME]
        times[BREAK_TIME] = min(times[BREAK_TIME], times[STUDY_TIME])
        times[STUDY_TIME] -= times[BREAK_TIME]

    while times[SESSION_TIME] > 0:
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

    # if session completed, exit the game
    if times[STUDY_TIME] == 0:
        traveller "Congrats in conpleting your study session"
        play audio studied
        return

    traveller "Remaining study time: [int(times[STUDY_TIME]/60)] minutes"

    'Ding, ding~\nThe sweet sound of the alarm pierces the silence.'
    r 'TIIIMES UPPPP!!!!!'

    
    # different path depends on the day
    if midnight_path_d1:
        jump day1_midnight
    else:
        jump day1_evening

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

    jump day1_midnight2

label day1_midnight:
    traveller "It's midnight now"
    jump day2

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
    Fade()
    pause 2.0

    jump day2
label day2:
    traveller "It's day 2 now"
