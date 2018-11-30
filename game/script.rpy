﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## Canada Characters

## Japan Characters
define yuuki = Character("Ohno Yuuki")
define ayako = Character("Sato Ayako")
define jap_mom   = Character("Mom")
define jap_dad   = Character("Dad")

## Pakistan Characters
define aasim   = Character("Aasim")
define brother   = Character("Brother")
define pak_main   = Character("You")


# The game starts here.

# story_a = set in Canada
# story_b = set in Japan
# story_c = set in Pakistan

# TODO: Add BGM for each of the routes


label start:
    "Where would you like travel to?"

    menu:
        "Canada":
            jump story_a

        "Japan":
            jump story_b

        "Pakistan":
            jump story_c

label end:
    "Play Again?"

    menu:
        "Yes ... Return to Menu":
            jump start

        "Maybe another time":
            return



label story_a:
        "Canada Story in Progress"

        menu:
            "Return to Selection Menu":
                jump start

###################### Japan Story Start
label story_b:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    show okaasan happy at left
    show otousan happy at right

    jap_mom "You decided to spend your prime in Tokyo and you're telling me that you can't find any halfway decent eligible bachelors?"

    "I'm having my weekly lunch break phone call with my parents, who live (and raised me in) the countryside."

    "It's been several months since I'd started at my schoolteacher position in Tokyo. My parents haven't gotten over that their 'daughter' is in The Big City, in 'her' twenties, and yet, obstinately single. They mean well, but... sometimes their advice is a tad misguided."

    "For one thing, although I live in an overcrowded city, it's not exactly easy for me to find 'halfway decent eligible' guys interested in me because, well, I'm a guy too."

    jap_mom "Your father and I are only getting older. We only have so many years left to see our grandchildren before we make our exit."

    "It's funny she'd say that, because I'd been thinking of getting sterilized... I don't know that I never want biological children, but Japanese law won't recognize my gender identity unless I become 'unable to reproduce'."

    jap_mom "Yuuki-chan, are you listening? Tell your parents they won't die before seeing their grandchildren."

    scene bg room

    menu:
        "How do I respond?"

        "Tell Mom and Dad you'll try your best.":
            jump story_b_reassure

        "Tell Mom and Dad you'd rather not lie to them.":
            jump story_b_not_lie

        "Say you weren't listening.":
            jump story_b_werent_listening

label story_b_reassure:
    yuuki "{a=http://lang-8.com/725244/journals/199182171541683591437838792131877435706}{i}Ganbarimasu.{/i}{/a}"

    jap_mom "That's our Yuuki!"

    yuuki "The thing is—"

    jump story_b_end_of_call

label story_b_not_lie:
    yuuki "I'd rather not lie to you..."

    jap_mom "Then find a boyfriend sooner rather than later!"

    yuuki "It's really not that easy..."

    jump story_b_end_of_call

label story_b_werent_listening:
    yuuki "Sorry, I'm a bit out of it."

    jap_mom "What're we going to do with you? Your parents are going to die of a broken heart."

    jump story_b_end_of_call

label story_b_end_of_call:
    # Play sound of classroom bell

    yuuki "Ah, sorry. It seems like the lunch break is over. We'll talk again next week, yeah?"

    jap_dad "Yeah."

    jap_mom "We're always missing you around. Love you!"

    yuuki "Love you."

    # Play sound of call disconnecting

    hide okaasan
    hide otousan

    "I sigh in mild relief. Another uneventful conversation with my parents, another day I remain in their good graces as their only and darling daughter. I keep telling myself that one day, one of these days, I'll tell them about my gender troubles and happenings, but there's never seems like a 'right' time."

    "Students shuffle into the classroom, as lethargic as you'd expect high schoolers to be on a Monday afternoon."

    yuuki "Alright, everyone. Let's settle in and start our review session for the test later this week."

    "At the reminder of the upcoming test, the students straighten themselves in their seats a little and put effort into being (or seeming?) alert and attentive."

    "At the start of the school year, during the first couple days of my teaching career, I was a little taken aback that I, someone who'd only so recently been on the other side of the classroom, was being heralded as an 'authority'."

    "Now, though, I found myself teasing with my power when I could. The atmosphere change in the classroom at the mention of a test hasn't gotten old, yet."

    # chalkboard sounds

    "{i}PRODUCT RULE and QUOTIENT RULE{/i}, I write out on the chalkboard."

    yuuki "To differentiate products and quotients we have the Product Rule and the Quotient Rule."

    yuuki "If the two functions f(x) and g(x) are differentiable (i.e. the derivative exist) then the product is differentiable and {font=fonts/Inconsolata-Regular.ttf}(fg)' = f'g + fg'{/font}."

    "My body becomes more relaxed as I continue writing on the chalkboard and reading my own handwriting aloud."

    "Math's always comforted me, with its no-nonsense language and problems. In contrast to having to figure out how to conversations with my parents that didn't leave me feeling like I'd somehow betrayed them, calculus problems were a pleasure."

    # more chalkboard sounds

    "A couple of hours pass like this, and then I've found myself dismissing my last class of the day."

    show bg hallway with dissolve

    "As a new faculty member, I haven't yet been asked to sponsor any after-school club, so I go home a little earlier than other teachers."

    "I make my way through the school hallways, idly trying to recall if I have any unexpired food left in the fridge."

    "I pass by Sato Ayako-sensei's classroom, where I find her hunched over at her desk, looking somewhat deep in thought. Sato-sensei is interesting—she's kept trying to make acquaintances with me, despite my reserved nature. Well, 'my reserved nature' isn't quite right..."

    "I wouldn't think of myself as reserved, but, ever since I started transitioning, I found myself unsure of where I fit into society and how to proceed with developing new interpersonal relationships."

    "I look cisgender enough that I don't have to worry about confused stares, but I worry about becoming 'exposed' if I were to let those unfamiliar with my history get close to me. There's no way of knowing how they'd react."

    "Still, it'd be nice to have a friend in an unfamiliar city..."

    menu:
        "What should I do?"

        "Poke my head in the door and say hi to Sato-sensei.":
            $ convo_with_sato = True
            jump story_b_head_poke

        "Continue home.":
            $ convo_with_sato = False
            jump story_b_continue_home

label story_b_head_poke:

    "I decide it can't hurt to say hi to Sato-sensei, so I poke my head in the door to do so."

    yuuki "Sato-sensei! How are you?"

    show ayako happy

    ayako "I'm well. How are you, Ohno-sensei?"

    menu:
        "How do I respond?"

        "Tell her I'm also well.":
            jump story_b_do_well

        "Tell her about my troubles with my parents.":
            jump story_b_troubles_with_parents

label story_b_do_well:
    yuuki "I'm doing well. You seem deep in thought—what're you working on?"

    ayako "Ah, it's nothing big. It's just that I'm realizing that I'll be spending the holidays alone."

    "I wonder if she's telling me this as a subtle hint to invite her out for the holidays. I wouldn't mind hanging out with Sato-sensei, but it's hard to feel 'right' hanging out with anyone while being a very closeted trans man. I worry about giving off the wrong messages and getting into an uncomfortable situation."

    yuuki "Well, getting some well-deserved peace and quiet to yourself sounds like an excellent vacation."

    "Sato-sensei smiled, but doesn't seem convinced."

    ayako "I'll try to remind myself of that."

    "She turns her attention from me to some papers on her desk."

    ayako "I have some paperwork to fill out, so we should catch up later."

    "I nod and walk back into the hallway."

    jump story_b_continue_home

label story_b_troubles_with_parents:
    yuuki "I'm mostly doing well, the most complicated thing in my life is that I'm having some drama with my parents."

    ayako "Oh no! What's going on?"

    yuuki "It's nothing big! They just keep pushing me to get a girlfriend; they don't like how much of a loner I seem to be."

    "I cringe slightly at my use of 'girlfriend', when my parents would probably faint if they'd heard I had one."

    ayako "You {i}are{/i} a bit of a loner. Maybe a girlfriend would get you to go out more!"

    yuuki "Yeah, maybe."

    "I wonder if I'd be able to find a partner who'd push me out of the protective shell I've formed for myself—I sure hope I do."

    "Sato-sensei averts her glance from me to her desk."

    ayako "Actually, I have no holiday plans right now, aside from that I need to do some shopping for my family members."

    "Without meaning to, I tense my body."

    ayako "Would you like to come along with me?"

    "Sato-sensei is a nice person, and I'm sure I'd have a great time with her but without thinking I immediately respond:"

    yuuki "Sorry, I've already done my holiday shopping and my upcoming schedule is a bit hectic, right now."

    "Sato-sensei immediately puts her hands up, palms toward me, signalling for me not to feel bad about my rejection."

    ayako "I completely understand. I have some paperwork to fill out, so we should catch up more later."

    "I nod and walk back into the hallway."

    jump story_b_continue_home

label story_b_continue_home:
    show bg train with dissolve

    # moving train sounds

    if convo_with_sato:
        "I'm on the train home, leaning against the window and thinking back to my conversations with my parents and with Sato-sensei."

    else:
        "I'm on the train home, leaning against the window and thinking back to my conversation with my parents."

    "I've been thinking about this a lot: I'm happier than I've ever been, living my life as a man rather than as a woman. However, I'm also more isolated than I've ever been. It's hard to figure out what face to put on toward different people in my life."

    "I look through my Twitter feed, hoping to find some meme or another that'll make me laugh."

    "Instead, I come across a tweet from Ebina City Council member Tsuruhashi Masumi, in response to Asahi Shimbun's report on an attitude survey regarding same sex marriage:"

    "'If abnormal people increase, human beings will become extinct. … Homosexuality is abnormal. Media should be more responsible than to report abnormal activities.'"

    "'{a=https://www.tofugu.com/japan/conformity-in-japan/}The nail that sticks out gets hammered down{\a},' as the saying goes."

    "Would I be regarded as a 'homosexual' in Tsuruhashi-san's eyes, when I identify as a man and am interested in women? Probably, I think, resolving not to further dwell on the subject."

    "I look out the window and watch the city pass by. I let myself fall asleep, telling myself to be content with what I have. As long as I don't make too much of a splash around me, I'll be fine."

    hide bg train with dissolve

    # This ends the game.

    jump end
###################### Japan Story End

label story_c:
    show bedroom with dissolve
    "Wake Up"

    menu:
        "Stay in bed a little longer?":
            jump story_c_in_bed
        "Morning Prayer?":
            jump story_c_morning_routine

label story_c_in_bed:
    show bedroom with dissolve
    "You reach over and grab your phone"

    menu:
        "News?":
            jump story_c_news
        "Binder!":
            jump story_c_binder

label story_c_morning_routine:
    show bedroom with dissolve
    "Your rustling wakes up Aasim"

    "You kiss him on the cheek and roll out of bed. You pick up the ring from the bedside table"

    aasim "Can I get you chai?"

    pak_main "I'm okay"

    "You look at the time. You're late!!"

    jump story_c_late


label story_c_news:
    show news with dissolve
    "Article: Once ostracized now Pakistan: Transgender people are running for Parliament"

    "Hmmm.... maybe I should vote this year. When are Elections again?"

    "Opens Calendar App"

    #Calendar App Opening screen switch
    show calendar1 with dissolve
    "Today's Date: July 13th, 2018"
    "Election Day: July 25th, 2018"
    "Dr. Ralhan comes for shots: July 28th, 2018"

    menu:
        "Keep looking at your Calendar?":
            jump story_c_calendar
        "Binder!":
            jump story_c_binder

label story_c_calendar:
    show calendar2 with dissolve
    "Right ... Hajj ... "

    "Hopefully Allah can change the thinking of the Saudi Government in my lifetime"

    "You look over at the clock for the time. You're late!!"

    jump story_c_late


label story_c_binder:
    show tinder with dissolve
    "Left, Left, Lef....oooo...."

    "nope. jk. He's too pendu"

    "nothing good today"

    menu:
        "Keep Swiping?":
            jump story_c_binder_repeating
        "News!":
            jump story_c_news

label story_c_binder_repeating:
    show tinder with dissolve
    "Left, Left, Left"

    "Still nothing good today"

    menu:
        "Keep Swiping?":
            jump story_c_binder_repeating
        "News!":
            jump story_c_news

label story_c_late:
    show makeup with dissolve
    "You run to the bathroom and shart putting on your make up"

    "You wear the salwar kameez you bought last weekend and head out. You wave hello to the chowkidar and head down the road"

    menu:
        "Take the back roads. Less People means less stares":
            jump story_c_back_road
        "Theres safety in being in public":
            jump story_c_main_road

label story_c_back_road:
    show backroad with dissolve
    "You walk through some alleys. On your way, you say hello to some children, give 100 rupees to the woman on the street corner (even though you know it goes straight to the guru - 100 rupees for a blessing isnt too bad of a deal), and skip over some puddles"
    "Nothing too out of the ordinary"
    jump story_c_arrived

label story_c_main_road:
    show mainroad with dissolve
    "Hey! Beautiful gay!"
    "You look at the standing niama (police officer or mother's brother"
    "He burns away, 'Family always has your back', you say sarcastically under your breath"
    "Hmm... maybe you should call your brother today. Although it is his responsiblity"
    jump story_c_arrived

label story_c_arrived:
    show office with dissolve
    " 'Government of Pakistan' ... You're Here"
    "You hand the security guard your I.D. He looks you up and down and looks like he’s about to raise an eyebrow. But he doesn’t. You’re let in without exchanging a word"
    "Normal day at work. Paper pushing, phone checking, some staring"
    "Who actually cares about other people’s takes"

    show clock3pm with dissolve
    "The clock hits 3pm. Time to check out and you're feeling lazy"
    menu:
        "Rikshaw":
            jump story_c_rikshaw
        "Uber":
            jump story_c_uber

label story_c_rikshaw:
    show rickshaw with dissolve
    "You walk to the street corner and flag one down. He takes you home and takes you home and you pay in 20 rupees. He says thank you"
    "No words other than that"


label story_c_uber:
    show uberpak with dissolve
    "You walk outside and she pick you up. You say thank you and get out"
    "No words other than that"

label story_c_home:
    "You stroll into your home and take a seat on the couch"

    menu:
        "Turn on the T.V.":
            jump story_c_tv
        "Call your brother":
            jump story_c_brother


label story_c_tv:
    show marvia with dissolve
    "Its Marvia Malik on Kohenoon News. She's talking about village gange that killed two men suspected of being gay"

    menu:
        "Switch to Drama Network":
            jump story_c_tv_drama
        "Call your brother":
            jump story_c_brother

label story_c_tv_drama:
    show drama with dissolve
    "How can a saas be so cruel? You think to yourself."
    "You enjoy your lazy day. You watch T.V. till its time to prep dinner. You wash your dishes, do your night prayers, and head to bed."
    #Story is finished

    jump end


label story_c_brother:
    show bhai with dissolve
    pak_main "Its been a week! You don't have to check up on your little sister?"
    brother "I'm sorry"
    pak_main "Fine. I guess I should be the one chekcin gup on you. You're okay?"
    brother "Yeah, fine"
    pak_main "How's Kareem?"
    brother "We broke up?"
    pak_main "Oh ... Are you okay? Do you want to talk about it?"
    brother "I'm fine, but I don't feel like talking"
    pak_main "He wont tell anyone, will he?"
    brother "He's not tryna to kill me"
    pak_main "Okay. OKay. What can I do?"
    brother "Nothing right now. ... I'm fine ... Chalo, I'll call you this weekend. I'm a little busy right now"
    pak_main "Bye"
    #Screen change

    "'How did I get it better than him?' You think to yourself"
    "Might as well watch some TV"
    jump story_c_tv_drama

### End of Code
