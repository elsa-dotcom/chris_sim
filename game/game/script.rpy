# The script of the game goes in this file.

# Declare characters used by this game.
define m = Character("Me")
define mom = Character ("Mom")
define c = Character("Chris")
define unknown = Character ("???")
define tv = Character("TV Guy")
define e = Character ("Ellie")
define s = Character ("Sophie")
define d = Character ("Derek")
define maid = Character ("Jenna")
define friend = Character("Friend")
define q = Character("Queen")
define k = Character("King")
define n = Character ("Natalie")
define p = Character ("Patricia")
define ch = Character ("Guard Chris Hemsworth")
define cpr = Character("Chef Chris Pratt")
define q = Character ("Queen Gwynne Pine")
define k = Character("King Robert Pine")

# Initialize variables
default karma = 0
default liking_prince = 0
default liking_guard = 0
default liking_chef = 0
default firstdate = "no"
default has_poison = False
default date = 0
default meeting1 = "neutral"
default dinner = 0


# The game starts here.
label start:

    scene livingroom

    "As I'm peacefully reading a magazine, my mom enters."
    show mom

    mom "Darling! I've got some exciting news! You can sign up for the Selection!"
    "The selection is a competition where 35 girls compete against each other to win the heart of a handsome prince."
    mom "You want to sign up, right...?"

    menu:

        "Do you want to sign up for the Selection?"
        "Yes":
            jump yes1

        "No":
            jump no1

    label yes1:

    m "Yes of course I want to sign up! Give me the papers!"
    jump continuation

    label no1:

    m "Actually mom, I don't want to sign up."
    mom "Really..? Oh well, that's okay then."

    "End of game"
    "nice try"
    return

    label continuation:

    scene blackout

    "My mom and I were filling in the sheets for the Selection together and tomorrow we will be taking pictures."
    $ player_name = renpy.input("As part of that, I had to write my first name, which is..")
    if player_name == "":
        $ player_name="kento"
    $ player_surname = renpy.input("And my surname, which is..")
    if player_surname == "":
        $ player_surname="yamazaki"

    "The pictures will be part of my application."
    "The odds of me making it into the competition are really low."
    "35 girls in the whole country, and basically everybody applies."
    "And then out of those 35, only one stays."
    "It's going to be tough."

    scene bedroom
    with fade

    menu:
        "Now, what should I wear?"
        "Dress":
            jump dress

        "Jeans":
            jump jeans

        "Pajamas":
            jump pajamas

    label dress:
        $ clothing = "dress"
        "I'll definitely wear a dress! I'll look amazing!"
        jump makeup

    label jeans:
        $ clothing = "jeans"
        "I'll definitely wear jeans. Not too casual, and not too fancy."
        jump makeup

    label pajamas:
        $ clothing = "pajamas"
        "They should choose me for my personality! Not if I'm wearing a dress or not!"
        jump makeup

    label makeup:

    menu:
        "Hmm.. How much makeup should I wear though..?"
        "None":
            jump nomakeup

        "A little":
            jump mediummakeup

        "A lot":
            jump alotmakeup

    label nomakeup:
        $ makeup = "none"
        "Why should I wear any? I'm beautiful just the way I am!"
        jump pictureday

    label mediummakeup:
        $ makeup = "alittle"
        "I'll have a bit."
        jump pictureday

    label alotmakeup:
        $ makeup = "alot"
        "I'll go full on! It's a special event after all."
        jump pictureday

    label pictureday:

    "Now I'm ready to go take some pictures!"
    scene photoshoot
    with fade

    "I enter the photoshoot room and get ready for the picture."
    show mom

    if clothing == "pajamas":
        mom "Couldn't you have worn something else..?"
        m "I don't care if I'm wearing pajamas - I'll win anyways!"
        jump photoshoot

    else:
        mom "You look great honey."
        m "Thanks mom!"
        scene photoshoot
        jump photoshoot

    label photoshoot:

    unknown "NExT!"
    "I step up to the camera guy, and before I know it I'm done."
    show mom

    mom "You looked fine in that picture."
    mom "Now, lets go home."
    scene blackout

    "We were told that after a week, they'd annnounce the selected on TV."
    "It had been a week now, and my whole family was in front of the TV, ready to see if I got selected or not."
    scene tv

    tv "It has been a long week for some of us!"
    tv "But now, we will finally announce the selected."

    tv "One, Britt Gregory."
    tv "Two, Hanna Somerland"

    "And it goes on and on. I have lost all hope at this point."
    
    if clothing == "pajamas":
        jump lost1
    elif clothing == "jeans" and makeup == "none":
        jump lost1
    elif clothing == "jeans" and makeup == "alot":
        jump lost1
    elif clothing == "dress":
        jump won1
    elif clothing == "jeans" and makeup == "alittle":
        jump won1

    label lost1:
        tv "And, thirty five, Agnes Ulbert."

        "No. I didn't make it."
        "I guess that's better after all.."
        
        menu:
            "Accept it with grace.":
                "It wasn't meant to be."
                return
            
            "Throw a tantrum.":
                m "EXCUSE ME?!"
                "I stand up and throw the remote at the TV."
                m "THIS IS RIGGED! DO YOU KNOW WHO I AM?"
                mom "Honey, please stop screaming..."
                m "NO! I HATE THIS COUNTRY! I HATE PRINCE CHRIS!"
                "I storm out of the room, knocking over a vase."
                "End of game"
                "You are now viral on youtube for being crazy. (someone in your family filmed you)"
                return

    label won1:

        "Eventually....."

        tv "Thirty two, %(player_name)s %(player_surname)s."
        scene blackout

        "I made it."
        "I can't believe it."
        "That means that tomorrow someone from the palace will come visit."
        
        scene bedroom
        with fade
        "KNOCK KNOCK!"
        show man

        unknown "Hello, you must be %(player_name)s %(player_surname)s."
        unknown "I'm here to get your body measurements and tell you some rules."
                
        unknown "When you are part of the Selection, it's forbidden to see other guys."
        unknown "You'll also immediately be disqualified if you sabotage other girls."
        
        menu:
            unknown "Do you understand or do you want me to repeat them?"
            "Understood.":
                jump done
            "Repeat please.":
                jump again

        label again:
            unknown "Okay so,"
            unknown "When you are part of the Selection, it's forbidden to see other guys."
            unknown "You'll also immediately be disqualified if you sabotage other girls."
            jump done
            
        label done:
            unknown "Good. Now get packing."

        scene blackout
        "It's early in the morning. I'm in the car on my way to the airport."
        
        scene plane
        "On the plane, I'm sitting by the window, and next to me are two other girls."
        
        menu:
            "Say something.":
                jump say
            "Stay quiet.":
                jump quiet
            
        label say:
            $ friend = "ellie"
            m "Hey guys, are you part of the Selection too?"
            "Even though I know the answer, I ask so that I have something to say."
            show ellie at right
            unknown "Yeah! What's your name?"
            m "I'm %(player_name)s."
            e "Cool! I'm Ellie and this is Sophie!"
            show sophie at left
            s "Hi."
            e "We were just talking about Prince Chris."
            menu:
                e "What do you like the most about him?"
                "His eyes":
                    jump eyes

                "His abs":
                    jump abs

                "His smile":
                    jump smile

                    label eyes:
                        m "His eyes probably."
                        e "Right!! They're so sea blue and just so... mesmerizing!"
                        m "Yeah exactly!"
                    jump continue1

                    label abs:
                        m "I just really like his.. abs."
                        "Ellie and Sophie laugh."
                        s "Who can disagree with that."
                    jump continue1

                    label smile:
                        m "His smile, definitely."
                        s "Yes. I love it too."
                        e "I actually like his eyes better. Is that weird."
                        s "Yes definitely."
                        "Ellie and I laugh."
                    jump continue1

                    label continue1:
                        "For the rest of the plane ride the three of us just talk."
                        "I'm glad I decided to speak to them."
                        jump entering

        label quiet:
            "I decide not to talk to them."
            jump entering


    label entering:
        $ karma = 0
        
        scene blackout
        "Before I knew it, I was at the castle."
        scene royalhall

        if friend == "ellie":
            show ellie at right
            show sophie at left
            e "Wow it's so pretty!!"
            s "It really is.."
            scene royalhall
        else:
            "I look around in the beautiful enterence hall..."

        "All 35 girls are all gathered here and it's quite crowded."
        "Suddenly, the voice of a lady is heard through the hall from a speaker."

        unknown "Hello ladies!"
        unknown "Welcome to the royal palace!"
        unknown "The plans for this evening are as follows."
        unknown "You will go with your stylist and pick a dress."
        unknown "After that, you will go to your room and meet your maid."
        unknown "And finally, you'll have dinner in the royal dining room."
        show man
        unknown "hey. I'm your stylist."
        "!!"
        "It's the guy from yesterday."
        d "I figured I should introduce myself. I'm Derek."
        d "Now come with me, let's choose a nice dress for you."
        scene changingroom
        with fade

        menu:
            d "So, which one would you like?"
            "The red cocktail dress":
                jump redcocktail
            "The yellow maxi dress":
                jump yellowmaxi
            "The black lace dress":
                jump blacklace

        label redcocktail:
            $ dress = "red"
            m "I'd like the red cocktail dress please."
            d "Nice choice."
            jump continue2

        label yellowmaxi:
            $ dress = "yellow"
            m "I'd like the yellow maxi dress please."
            jump continue2

        label blacklace:
            $ dress = "black"
            m "I'd like the black lace please."
            "Derek smirks."
            d "Alrightie."
            jump continue2

    label continue2:
        scene blackout
        "After I chose a dress, I met my maid, Jenna."
        scene room
        with fade
        show maid
        
        menu:
            maid "Do you want me to escort you? Or can you find it yourself?"
            "Escort me please!":
                jump escort
            "I'll find it myself, thanks.":
                jump noescort

        label escort:
            m "Escort me please!"
            maid "Okay, this way!"
            scene diningroom
            "Jenna left me in the dining room and I was looking around, amazed."
            $ meeting = "notearly"
            jump dining

        label noescort:
            m "It's fine, I'll find it!"
            maid "Alright!"
            scene royalhall
            "I walk down the hallway and I think I went the wrong way because.."
            m "!!"
            show cp
            c "Oh, hello there."
            "It's the prince. He's standing right in front of me."
            c "Are you lost?"
            m "I think so.."
            c "That's alright, I'll show you the way."
            scene diningroom
            "The prince led me halfway to the dining hall because he wasn't allowed to show his face there."
            "Even though we walked really quietly and awkwardly, I can't believe I met the prince."
            $ meeting = "early"
            jump dining

        label dining:
            scene diningroom

            if friend == "ellie":
                e "%(player_name)s!"
                show ellie at right
                show sophie at left
                e "Let's sit together!"
                m "Of course!"
                "We sit together and stare at the delicious food ahead of us."
                jump dinner1

            else:
                "I see the girls from the plane, if only I had befriended them.."
                "But it's fine I can befriend someone else - tonight is the chance!"
                "I see an empty seat next to a girl with glasses."

                menu:
                    "Should I sit there and befriend her?"

                    "Yes! Befriend her!":
                        jump natalie

                    "Sit somewhere else.":
                        jump nonatalie

                label natalie:
                        $ friend = "natalie"
                        "I decide to befriend her."
                        "I sit down next to her."
                        m "Hi my name is %(player_name)s, what's yours?"
                        show natalie
                        n "Hi, I'm Natalie."
                        "Nobody seems to have started to eat, so we wait and talk together."
                        m "So uh.. How was your flight?"
                        n "It was good. I felt kinda long though. I couldn't sleep"
                        m "Oh, how come..?"
                        n "We'll I'm nervous and excited obviously! Aren't you?"
                        "She didn't sound cocky or anything, she sounded very polite. She seems very sweet."
                        m "Yeah of course."
                        jump dinner1

                label nonatalie:
                        $ friend = "no1"
                        "I decide to sit somewhere else and let people come to me."
                        "I'm so alone."
                        jump dinner1

            label dinner1:

            if dress == "black":
                "After a while, I spot, in the far distance, a man, looking rather sharp."
                scene diningroom
                show ch at right

                "In my opinion, he looks.."
                menu:
                    "Very handsome.":
                        jump q1

                    "Ok. I'm faithful to my prince!":
                        jump q2

                label q1:
                    $ karma -= 1
                    "I gave the dude a flirtatious wink and he strode over."
                    scene diningroom
                    show ch
                    unknown "Well hello, how are you doing on such a fine evening?"
                    "I giggle."
                    m "Good thank you very much. If you don't mind me asking, what is your name?"
                    ch "Hemsworth, Miss. Chris Hemsworth."
                    "!! He has the same first name as the Prince!"
                    ch "And you?"
                    m "I'm %(player_name)s."
                    ch "That's quite a splendid name if I say so myself."
                    "I can't help but blush."
                    ch "Well, nice meeting you Miss %(player_name)s, I'm afraid I have to get back to my duty."
                    ch "I really do hope we meet again sometime."
                    scene diningroom
                    "What.. Just happened..?"
                    jump q3

                    label q3:
                        if friend == "ellie":
                            show ellie at right
                            show sophie at left
                            e "He totally wanted you!"
                            e "He was soooo hot I'm kind of jealous!"
                            m "I laugh and cant help but glance at him again."
                            s "But we're competing for the prince! Not him!"
                            e "All I said was that he was hot! I obviously won't pursue him!"
                            "Eventually our talking got cut off by a high pitched female voice."
                            jump q4

                        if friend == "natalie":
                            n "omg he was so cute."
                            m "I know right!"
                            n "I feel kinda guilty, I mean we're competing for the Prince."
                            m "I mean yeah, but the competition has barely begun."
                            "Eventually our talking got cut off by a high pitched female voice."
                            jump q4

                label q2:
                    "I quickly looked away and ignored his attempt to talk to me."
                    scene diningroom

            else:
                "Eventually, a high pitched voice fills the dining room."
                jump q4

            label q4:
                unknown "Hello ladies! It seems we've all gathered!"
                "It's the the same voice from before !"
                unknown "Nice to meet you all. My name is Patricia."
                p "But don't get too attached, some of you might even leave tomorrow."
                "Patricia looks around the hall with an eerie smile."
                p "Anyways, dig in! And you can practice your table manners for tomorrow."

                if friend == "ellie":
                    "What does she mean practice for tomorrow..? What's happening then?"
                    "And why would some of us leave so early..?"
                    m "What is she talking about..?"
                    e "Oh you didn't know..? The king, queen and prince are eating dinner with us!"
                    m "You're kidding!"

                    s "Well it wont be as bad as actually talking to the prince tomorrow. I dunno if I'm ready yet!"

                    if meeting == "early":
                        "Wait, I haven't told them that I already saw him.."
                        m "You know, I actually saw the prince on my way here..."
                        e "What?!!"
                        m "Yah! I was lost and he showed me the way.."
                        s "Did he ask your name? Did you talk..?"
                        m "No"
                        "I felt kind of stupid. I didn't even say thank you when he left."
                        m "I didn't really make a great first impression."
                        e "At least you look stunning. That's always something!"
                        "The three of us laugh and enjoy the rest of the dinner."
                        jump postdinner1

                    else:
                        m "We're already meeting the prince? That's so early.."
                        e "Yeah well I mean that's kind of the point of the Selection, why wait?"
                        m "Good point."
                        "The three of us laugh and enjoy the rest of dinner."
                        jump postdinner1

                if friend == "natalie":
                    "What does she mean practice for tomorrow..? What's happening then?"
                    "And why would some of us leave so early..?"
                    m "Wait, what is she talking about? What's happening tomorrow?"
                    n "I was about to ask the same thing.."
                    "Some girls next to us were talking about how nervous they were for dinner with the king and queen. Oh. So that's what she meant."
                    "Natalie seemed to have heard it to cause we looked at each other in scared faces."
                    n "Oh no.. I'm not ready for that just yet!"
                    m "Same! I'm going to feel so self conscious in front of the royals!"
                    "The girls blabbered on about meeting the prince tomorrow."
                    "So that's what she meant by being sent home so early, cause you'd have talked to the prince and if he didn't like you, he'd send you home."
                    "Natalie seemed to have heard that too cause..."
                    n "Meeting the prince though... I'm sooooo nervous."

                    if meeting == "early":
                        "Wait, I haven't told her that I already saw him.."
                        m "You know, I actually saw the prince on my way here..."
                        n "Wait really? What was he like?"
                        m "I don't know yet, he showed me the way cause I got lost."
                        n "That's nice of him. He seems like a gentleman"
                        m "Yah he was... but..."
                        "I felt kind of stupid. I didn't even say thank you when he left."
                        m "I didn't really make a great first impression."
                        n "I'm sure it was fine! What makes you say that?"
                        m "Well, I was kind of quiet that's all."
                        n "But you're not supposed to meet him until tomorrow, and he knows that."
                        m "I guess."
                        "For the rest of dinner the two of us talk about Prince Chris."
                        jump postdinner1

                    else:
                        m "I wonder what he's like in person"
                        n "Yeah! I bet you he's really kind and polite."
                        m "Nothing less from a prince."
                        "For the rest of dinner the two of us talk about Prince Chris."
                        jump postdinner1

                else:
                    "I wonder what she means by practice for tomorrow."
                    "And also, why would anyone leave so soon..?"
                    "I wish I had someone to ask..."
                    "I enjoy dinner by myself and then leave and go up to my room alone."
                    jump postdinner1


            label postdinner1:

            scene room
            show maid

            maid "Hello! Welcome back Miss %(player_surname)s! How was dinner?"

            menu:

                "It was.."

                "Very tasty!":
                    jump t1

                "It was fine.":
                    jump t2

                "It was lonely..":
                    jump t3

            label t1:
                maid "That's good! It looked very good."
                m "Did you not eat any of it..?"
                maid "No miss! I have my own food. Anyways, you're meeting the prince tomorrow so you have to sleep now!"

                if friend == "no1" and meeting == "notearly":
                    m "I'm meeting the prince tomorrow?!"
                    maid "Yes! Haven't you heard?"
                    m "no..."
                    maid "Well you are! So you need your beauty sleep!"
                    scene blackout
                    "Jenna helped me get to bed and I fell asleep in an instant."
                    jump day1

                else:
                    m "Oh yes... the prince.."
                    maid "Okay! Come on now Miss! You need your beauty sleep for tomorrow!"
                    scene blackout
                    "Jenna helped me get to bed and I fell asleep in an instant."
                    jump day1

            label t2:
                maid "Good. Now you need to sleep cause you're meeting the prince tomorrow."
                if friend == "no1" and meeting == "notearly":
                    m "I'm meeting the prince tomorrow?!"
                    maid "Yes! Haven't you heard?"
                    m "no..."
                    maid "Well you are! So you need your beauty sleep!"
                    scene blackout
                    "Jenna helped me get to bed and I fell asleep in an instant."
                    jump day1

                else:
                    m "Oh yes... the prince.."
                    maid "Okay! Come on now Miss! You need your beauty sleep for tomorrow!"
                    scene blackout
                    "Jenna helped me get to bed and I fell asleep in an instant."
                    jump day1

            label t3:
                maid "lonely..? How come? Did you not have anyone to sit with?"

                if friend == "no1":
                    "I shook my head."
                    maid "Well, it's still early on. You'll find someone eventually!"
                    maid "Anyways, you have to sleep now, you need energy for tomorrow, since you're meeting the prince!"
                    jump t4

                else:
                    m "I did, I just.."

                    menu:
                        "Miss home.":
                            jump tt1

                        "Everyone is alone and we're all competitors.":
                            jump tt2

                    label tt1:
                        maid "It'll get better the longer you stay. Trust me."
                        maid "I think all you need is some sleep now. Especially since you're meeting the prince tomorrow."
                        jump t4

                    label tt2:
                        maid "Just focus on yourself and the prince and make friends without getting too paranoid."
                        maid "Just cause you're fighting for the same thing doesn't mean you're enemies."
                        m "I guess.."
                        maid "All you need is some sleep. Especially since you're meeting the prince tomorrow."
                        jump t4

            label t4:
                if friend == "no1" and meeting == "notearly":
                    m "I'm meeting the prince tomorrow?!"
                    maid "Yes! Haven't you heard?"
                    m "no..."
                    maid "Well you are! So you need your beauty sleep!"
                    scene blackout
                    "Jenna helped me get to bed and I fell asleep in an instant."
                    jump day1

                else:
                    m "Oh yes... the prince.."
                    maid "Okay! Come on now Miss! You need your beauty sleep for tomorrow!"
                    scene blackout
                    "Jenna helped me get to bed and I fell asleep in an instant."
                    jump day1

            label day1:
                scene room
                show maid
                maid "Good morning Miss %(player_surname)s!"
                m "Morning..."
                maid "Wake up now..! You need to go down and eat breakfast cause afterwards you're meeting the prince!"

                if friend == "ellie":
                    scene blackout
                    "I meet up with Ellie and Sophie during breakfast and we talk about our maids and how nervous we are to meet the prince."
                    "After breakfast, the three of us wait in the girl's common room."
                    "It's a room dedicated to the 35 girls staying at the royale palace. We can stay here when we have nothing else to do."
                    scene cr
                    "Patricia is calling out names and the person goes into a room and talks to Chris for a bit."
                    p "Ellie Samuels!"
                    show ellie
                    e "Wish me luck guys!"
                    scene cr
                    "Ellie left and it was just Sophie and I."
                    scene blackout
                    "Eventually Ellie came back, Sophie went and out of us three, I was the only one left."

                    scene cr
                    show ellie at right
                    show sophie at left

                    e "I'm telling you, it's not that bad! He was really sweet!"
                    s "Yeah, he's a real gentleman."
                    p "%(player_name)s %(player_surname)s."
                    e "See you soon!"
                    jump cp1

                if friend == "natalie":
                    scene blackout
                    "I met up with Natalie and ate breakfast with her."
                    "After breakfast we went to the girl's common room."
                    "It's a room dedicated to the 35 girls staying at the royale palace. We can stay here when we have nothing else to do."
                    scene cr
                    "Patricia is calling out names and the person goes into a room and talks to Chris for a bit."
                    p "Ellie Samuels!"
                    "A cute girl jumps up to her feet and walks into the room."
                    m "Are you nervous?"
                    n "Yup. Very. You?"

                    menu:

                        "Of course!":
                            jump tt3

                        "Not really":
                            jump tt4

                    label tt3:

                        jump yourturn

                    label tt4:

                        n "lucky!"

                        jump yourturn

                    label yourturn:
                        scene blackout
                        "Eventually Natalie got called up, and between us, I still had to go."
                        scene cr
                        show natalie
                        n "He was really nice. I don't think you have to worry."
                        p "%(player_name)s %(player_surname)s."
                        n "Good luck!"
                        jump cp1

                else:
                    scene blackout
                    "I sat and ate alone."
                    "After breakfast I went to the girls common room."
                    "It's a room dedicated to the 35 girls staying at the royale palace. We can stay there when we have nothing else to do."
                    scene cr
                    "Patricia is calling out names, and the person goes into a room and talks to Chris for a while."
                    "I noticed that some people stay there for ages, others not so long."
                    "After a very long time Patricia finally called my name."
                    p "%(player_name)s %(player_surname)s."
                    "I stood up and walked into the room."
                    jump cp1

    label cp1:
        scene talkingroom
        with fade
   
        if meeting == "early" and dress == "red":
            c "Oh hello again. You found your way today then?"
            show cptalking

            menu:

                "Yes! All by myself.":
                    jump qq1

                "Mhm..":
                    jump qq2

                "I guess so. Or I might've accidentally stumbled in here.":
                    jump qq1

            label qq1:
                scene talkingroom
                show cphappy2

                c "Is that so? Well it's nice seeing you again. And.."

                scene talkingroom
                show cptalking

                c "I'm sorry I didn't really talk to you yesterday. I was just... so... blinded by your beauty."
                "I can't help but blush."

                menu:
                    "Thank you.":
                        jump qq3

                    "You didn't look so bad either.":
                        jump qq4

                    "Thank you Mr cliche!!":
                        jump qq5

                label qq3:
                    $ meeting1 = "verygood"
                    scene  talkingroom
                    show cphappy

                    "So tell me about yourself."

                    jump qt1

                label qq4:
                    $ meeting1 = "verygood"
                    scene talkingroom
                    show cphappy2

                    c "Well isn't that flattering!"

                    scene talkingroom
                    show cphappy

                    c "Anyways, tell me about yourself."

                    jump qt1

                label qq5:
                    $ meeting1 = "verygood"
                    scene talkingroom
                    show cphappy2

                    c "It might be cliche but it's true! And I wouldn't lie to you!"

                    "I blush again."

                    scene talkingroom
                    show cphappy

                    "Well tell me about yourself."

                    jump qt1

            label qq2:
                $ meeting1 = "okay"
                c "That's good. We didn't talk much yesterday. Tell me about yourself."
                jump qt1


        if meeting == "early" and not dress == "red":

            c "Oh hello again. You found your way today then?"
            show cptalking

            menu:

                "Yes! All by myself.":
                    jump qq11

                "Mhm..":
                    jump qq22

                "I guess so. Or I might've accidentally stumbled in here.":
                    jump qq11

            label qq11:
                scene talkingroom
                show cphappy2

                c "Is that so? Well it's nice seeing you again."

                scene talkingroom
                show cptalking

                c "And since we didn't really talk yesterday, let's talk now."
                c "Tell me something about you."

                jump qt1

            label qq22:
                $ meeting1 = "okay"
                c "That's good. We didn't talk much yesterday. Tell me about yourself."

                jump qt1

        else:

            c "Hello, you must be %(player_name)s."
            show cptalking

            menu:

                "How did you know?":
                    jump rt1

                "Yes. And you must be Prince Chris?":
                    jump rt2

            label rt1:
                scene talkingroom
                show cphappy2

                c "Well I remember of course! How could I forget after seeing your beautiful face as one of the selected?"
                "I blush."

                menu:
                    "Thank you.":
                        jump rt3

                    "That's very sweet of you to say.":
                        jump rt3

                label rt3:
                    $ meeting1 = "okay"
                    c "you're welcome."
                    c "Anyways %(player_name)s, tell me about yourself."
                    jump qt1

            label rt2:
                $ meeting1 = "verygood"
                scene talkingroom
                show cphappy

                c "Nope! I'm actually Prince Henry."
                m "Oh no. I shouldn't be here then."
                c "Yeah, you really shouldn't. You're breaking Selection rules."
                m "Well not necessarily. I'm just talking to prince Henry."
                c "I thought you already had strong romantic feelings for Prince Henry. Cause he's so handsome."

                menu:

                    "Can't disagree with that.":
                        jump rt4

                    "Oh yes, I totally fall for someone cause of their looks.":
                        jump rt5

                label rt4:
                    c "Right!"
                    scene talkingroom
                    show cphappy2
                    c "anyways, tell me about yourself."
                    jump qt1

                label rt5:
                    c "Woowww, hard to get are you?"
                    "I giggle."
                    scene talkingroom
                    show cphappy2
                    c "Anyways tell me about yourself."

                    jump qt1

        label qt1:

        menu:

            "Well... I love cooking and I love eating.":
                jump p1

            "I love hanging out with friends!":
                jump p2

            "Fortnite 4 lyfe yo.":
                jump p3

            "I'm rich.":
                jump p4

            "There's not much to say to be honest.":
                jump p5

        label p1:

            scene talkingroom
            show cphappy

            c "So you love food?"
            m "Obviously! Don't you?"
            c "Of course I do."

            if meeting1 == "verygood":

                c "How about I take you out for lunch tomorrow? I'll let you eat my favorite food."
                "Did he just ask me out to a date?"

                menu:
                    "I'd like that.":
                        jump pp1

                    "I have other plans.":
                        jump pp2

                label pp1:
                    m "I'd like that very much. But I'll be very disappointed if it's bad food."
                    c "Then I promise I won't disappoint you."
                    $ firstdate = "yes"
                    jump ppp1

                label pp2:
                    scene talkingroom
                    show disagree
                    c "oh what.. okay.."
                    c "Anyways it seems it's time for you to leave. Bye"
                    m "Bye!"
                    $ meeting1 = "verybad"
                    jump done1

            else:
                c "I mean, who doesn't love food?"
                m "True."
                jump ppp1

        label p2:

            c "Ah right. Have you found any here yet?"

            if friend == "no1" and meeting1 == "verygood":

                "I shook my head."
                scene talkingroom
                show cpmysterious
                c "Oh well, I'm sure you'll find someone, cause you'll definitely have time to."
                "What's that supposed to mean? Is he saying I won't leave early..?"
                m "Thanks."

                jump ppp1

            if friend == "no1" and not meeting1 == "verygood":
                "I shook my head."
                c "Oh well. I mean this competition is temporary anyways."
                m "Yeah."
                jump ppp1

            if not friend == "no1" and meeting1 == "verygood":
                m "Yeah."
                c "I'm not surprised. You're super sweet."
                "Awh he's so nice."
                m "Awh thanks!"
                c "It's the truth!"
                jump ppp1

            else:
                m "Yah."
                c "That's good."
                jump ppp1

        label p3:
            scene talkingroom
            show cpmysterious
            c "Oh.. you're one of those."
            m "Yeah!"
            c "OH. It seems the session is over. Nice meeting you. Bye."
            m "Bye!"
            $ meeting1 = "verybad"
            jump done1

        label p4:

            if meeting1 == "verygood":
                c "That's all you've got to say?"
                m "Yes."
                c "Well that doesn't help me!"
                "I laugh."
                c "Me marrying you doesn't depend on you being rich or not!"
                m "Well what if I say I'm not rich in money, but in something else."
                c "Oh and what's that?"
                m "I wont sayyyy you'll have to find out."
                c "How about I take you out for lunch tomorrow, and find out then?"

                menu:
                    "I'd like that.":
                        jump pp11

                    "I have other plans.":
                        jump pp21

                label pp11:
                    m "Oh yes I'd love that."
                    c "Good! Then it's a date."
                    $ firstdate = "yes"
                    jump ppp1

                label pp21:

                    scene talkingroom
                    show disagree

                    c "oh what.. okay.."
                    c "Anyways it seems it's time for you to leave. Bye"
                    m "Bye!"
                    $ meeting1 = "verybad"
                    jump done1

            else:

                scene talkingroom
                show cpmysterious

                c "You're.. Rich?"
                m "Yes."
                c "That's all you have to say..?"
                m "Yes."
                c "Oh I see. Oh.. It turns out session is over. Bye."
                m "Bye!"
                $ meeting1 = "verybad"
                jump done1

        label p5:

            if meeting1 == "verygood":

                c "You can't think of anything?"
                m "Nope. Not a thing. You already know everything."

                if meeting == "early" and dress == "red":
                    c "What? That you get lost easily and that you look stunning in a red dress?"
                    jump p51

                if meeting == "early" and not dress == "red":
                    c "What? That you get lost easily?"
                    jump p51

                else:
                    c "What? That your name is %(player_name)s?"
                    jump p51

                label p51:
                    "I laugh."
                    m "Exactly."
                    c "Well there must be something else. Since you're so secretive how about I take you to lunch tomorrow?"

                    menu:
                        "I'd like that.":
                            jump pp12

                        "I have other plans.":
                            jump pp22

                    label pp12:
                        m "I'd like that very much."
                        c "Good. Then it's a date!"
                        $ firstdate = "yes"
                        jump ppp1

                    label pp22:
                        scene talkingroom
                        show disagree
                        c "oh what.. okay.."
                        c "Anyways it seems it's time for you to leave. Bye"
                        m "Bye!"
                        $ meeting1 = "verybad"
                        jump done1

            else:
                c "Oh.. well, since we've run out of things to talk about, you may go."
                m "Oh okay, bye!"
                c "Bye."
                $ meeting1 = "verybad"
                jump done1

        label ppp1:
                scene talkingroom
                show cpmysterious
                c "So..."
                c "Ah sorry, I just realised we're out of time..."
                if meeting == "verybad":
                        m "Oh, I hope I get to see you again"
                        c "We'll see..."
                else:
                        c "I had a nice time with you. I hope I get to see more of you %(player_name)s."
                jump done1

        label done1:
                scene cr
                with fade

                if friend == "ellie":
                        "I sit back down next to Ellie and Sophie"
                        show ellie at right
                        show sophie at left
                        e "How did it go? Isn't he dreamy!"
                        if meeting == "verybad":
                                m "It went amazing! He is, I can't wait to speak to him again."
                        else:
                                m "I'm not sure, but he was lovely."

                if friend == "natalie":
                        "I sit back down next to Natalie"
                        show natalie
                        n "How did it go?"
                        if meeting == "verybad":
                                m "It went amazing! He is, I can't wait to speak to him again."
                        else:
                                m "I'm not sure, but he was lovely."
                else:
                        "I sit back down in the common room."


                scene cr
                "The last few girls get called in to speak with Chris, and when they're done Patricia tells us to wait while Chris decides who gets to stay."
                "It's tense in the common room."
                p "Okay girls! It's time."
                p "Unfortunately, 8 girls will be sent home today. If you hear your name, you will be escorted back to your room and asked to pack up your stuff."
                "Patricia starts listing names..."
                p "Britt Gregory..."
                "Patricia keeps going. Girls start crying and running out of the common room."
                "Finally, she gets to the last name..."

                if meeting == "verybad":
                        p "And finally, %(player_name)s %(player_surname)s."
                        "My heart sinks in my chest."

                        if friend == "ellie":
                                "Me? Really? And Ellie and Sophie get to stay???"
                                show ellie at right
                                show sophie at left
                                e "Oh... I'm so sorry %(player_name)s..."
                                s "This sucks"

                                menu:
                                    "Accept fate":
                                        "I leave sadly."
                                        "I guess it is time to pack my things."
                                        scene blackout
                                        "End of game"
                                        "try to be more charming next time"
                                        return
                                    "Throw a tantrum!!!":
                                        m "NO! ABSOLUTELY NOT!"
                                        scene cr
                                        "I flip a table."
                                        m "PRINCE CHRIS HAS NO TASTE! I AM WAY BETTER THAN ELLIE AND SOPHIE?!"
                                        p "Guards! Remove her!"
                                        "Two guards drag me out while I bite their ankles."
                                        scene blackout
                                        "End of game"
                                        "try to be more charming next time"
                                        return

                        if friend == "natalie":
                                "Me? Really? And Natalie gets to stay???"
                                show natalie
                                n "Oh... I'm so sorry %(player_name)s..."

                                menu:
                                    "Accept fate":
                                        "I leave sadly."
                                        "I guess it is time to pack my things."
                                        scene blackout
                                        "End of game"
                                        "try to be more charming next time"
                                        return
                                    "Throw a tantrum!!!":
                                        m "NO! ABSOLUTELY NOT!"
                                        scene cr
                                        "I flip a table."
                                        m "PRINCE CHRIS HAS NO TASTE! I AM WAY BETTER THAN NATALIE!"
                                        p "Guards! Remove her!"
                                        "Two guards drag me out while I bite their ankles."
                                        scene blackout
                                        "End of game"
                                        "try to be more charming next time"
                                        return

                        else:
                                "Me? Really?"

                                menu:
                                    "Accept fate":
                                        "I leave sadly."
                                        "I guess it is time to pack my things."
                                        scene blackout
                                        "End of game"
                                        "try to be more charming next time"
                                        return
                                    "Throw a tantrum!!!":
                                        m "NO! ABSOLUTELY NOT!"
                                        scene cr
                                        "I flip a table."
                                        m "PRINCE CHRIS HAS NO TASTE! I AM THE BEST ONE HERE!"
                                        p "Guards! Remove her!"
                                        "Two guards drag me out while I bite their ankles."
                                        scene blackout
                                        "End of game"
                                        "try to be more charming next time"
                                        return

                else:
                        p "And finally, Agnes Ulbert..."
                        "I didn't get asked to leave?"

                        if friend == "ellie":
                                show ellie at right
                                show sophie at left
                                e "This is amazing! We can all stay!"
                                s "Yay!!!"

                        if friend == "natalie":
                                show natalie
                                n "This is amazing! We can both stay!"

    scene blackout
    "Everyone who is allowed to stay goes for lunch before returning to their rooms until dinner to recover from the stress."

    scene room
    show maid
    maid "Miss %(player_surname)s! I am so happy that you got to stay!"
    m "Thank you Jenna, me too!"
    maid "I will let you recover from your date. Derek prepared an elegant dress for your royal dinner tonight, I have laid it out on the bed for you."
    
    scene blackout
    "I read and have a nap, and then get ready for the royal dinner."

    scene diningroom
    with fade

    "The atmosphere in the dining room is tense."

    if friend == "ellie":
        show ellie at right
        show sophie at left
        e "Omg, the Queen looks so scary!"
        s "Shhh! She'll hear you."
        hide ellie
        hide sophie

    elif friend == "natalie":
        show natalie
        n "I read a book on royal etiquette yesterday. Just follow my lead."
        hide natalie

    else:
        "I sit alone. At least no one can steal my bread roll."

    "Trumpets blare."
    unknown "All rise for King Robert and Queen Gwynne!"

    show kq at left
    show cp at right

    "The Royals enter."

    if firstdate == "yes":
        "Prince Chris catches my eye as he sits down."
        "He gives me a subtle wink."
        "Other girls look in my direction with jealousy."
    else:
        "Prince Chris looks around the room."

    "We all sit down."
    scene diningroom
    "The soup is served. It looks green and suspicious."

    menu:
        "What do I do first?"

        "Tuck the napkin into my collar like a bib.":
            $ dinner -= 1
            "I shove the napkin into my dress so I don't spill."
            "The Queen stares at me. Her eyes narrow."
            q "How... rustic."
            "I see Chris cringe slightly."

        "Place the napkin elegantly on my lap.":
            $ dinner += 1
            "I unfold the napkin and place it on my lap."
            "The Queen nods approvingly."
            if friend == "natalie":
                n "Nice form."

    "Everyone is staring at the soup."

    menu:
        "Start eating immediately. I'm starving!":
            $ dinner -= 1
            "I grab my spoon and slurp the soup."
            "SLURP."
            "The entire room goes silent."
            q "We usually wait for the host to start, my dear."
            "I choke on a crouton out of embarrassment."

        "Wait for the Queen to pick up her spoon.":
            $ dinner += 1
            "I wait patiently."
            "The Queen lifts her spoon. Then we all begin."

    "The main course arrives. Roast chicken."

    menu:
        "Pick it up with my hands.":
            $ dinner -= 2
            "I grab the chicken leg and take a massive bite."
            m "Mmm, tastes like victory."
            "The Queen looks like she is about to faint."
            c "Uh... %(player_name)s?"
            "It seems that was not the move."

        "Use the knife and fork.":
            $ dinner += 1
            "I carefully cut the meat."

    "The dinner feels like it lasted for hours. Patricia watches us like a hawk from the corner."

    if dinner < 2:
        "I think I made a bad impression on the parents..."
        "Chris looks a bit disappointed."
    else:
        "I think I survived the Royal Dinner!"
        "Chris looks pleased."

    "Finally, we are dismissed."
    
    scene blackout
    "It has been a long day."
    scene room
    with fade
    
    "I'm in my pajamas, but I feel restless."
    
    menu:
        "Go to sleep":
            jump day2_morning
        "Sneak out to the garden":
            jump night_garden

    label night_garden:
        "I quietly put my shoes on and sneak outside."
        scene night_garden
        with fade
        "The air is cool and smells of roses."
        
        if dress == "black":
            "A shadow is following me..."
            show ch
            ch "Miss %(player_surname)s. Out past curfew?"
            
            menu:
                "I couldn't sleep.":
                    ch "Understandable. it's been a busy day for you."
                    ch "What drew you to the gardens?"

                    menu:
                        "I was hoping to run into a strong man to protect me.":
                            $ karma -= 1
                            $ liking_guard += 1
                            ch "You're playing a dangerous game."
                            m "You look dangerous, Mr. Hemsworth. I like danger."
                            ch "Is that so?"
                            "He takes a step closer, and lowers his voice."
                            ch "You should be careful what you wish for."
                            "He smirks, and disappears into the shadows."

                        "I just love flowers.":
                            ch "Don't we all."
                            "He smiles, and disappears into the shadows."
                
                "I'll walk back to my room...":
                    ch "Stay safe."
                    "He disappears into the shadows."
                    jump day2_morning

            hide ch

        "I walk further and see someone sitting on a bench."
        show cpmysterious at center
        
        "It's Prince Chris."
        c "Oh! You startled me."
        
        if firstdate == "yes":
            c "I was just thinking about our date tomorrow. I'm looking forward to it."
            
            menu:
                "Me too! I can't wait either.":
                    $ liking_prince += 1
                    c "You look lovely in the moonlight."
                    "I blush."
                    m "Thank you, so do you!"
                    "He smiles."
                    hide cpmysterious
                    show cphappy at center
                    c "Okay, you should go back to your room now! You're far too cute to be out after curfew!"
                    hide cphappy
                    "I walk back to my room and finally go to sleep."
                    scene blackout
                    with fade

                "I bet you say that to all the girls.":
                    c "Only the special ones."
                    m "You think I'm special?"
                    hide cpmysterious
                    show cphappy at center
                    c "Why do you think I haven't scolded you for being out after curfew?" 
                    "I blush."
                    c "Speaking of, you should really go back to your room now before the Queen tells you off!"
                    hide cphappy
                    "I walk back to my room and finally go to sleep."
                    scene blackout
                    with fade
                
                "I want you right now.":
                    if liking_prince > 1:
                        c "Woah there... let's save some mystery for tomorrow."
                        "He smiles, but steps back."
                        c "See you then..."
                        hide cpmysterious
                        "Maybe that was a bit too forward..."
                        "I walk back to my room and finally go to sleep."
                        scene blackout
                        with fade

                    else:
                        c "Uhh... that's a bit much. I think I should go inside."
                        $ liking_prince -= 1
                        hide cpmysterious
                        "He looked uncomfortable."
                        "Maybe that was a bit too forward..."
                        "I walk back to my room and finally go to sleep."
                        scene blackout 
                        with fade

        else:
            c "You shouldn't be out here."
            menu:
                "Sorry! I'll go back.":
                    c "Goodnight."
                    hide cpmysterious
                    "I walk back to my room and finally go to sleep."
                    scene blackout 
                    with fade

                "Come on, live a little.":
                    c "Rules are rules. Goodnight."
                    $ liking_prince -= 1
                    hide cpmysterious
                    "Oops, he didn't seem too pleased..."
                    "I walk back to my room and finally go to sleep."
                    scene blackout 
                    with fade

        jump day2_morning



    label day2_morning:

        scene room
        "Jenna wakes me up again for breakfast."

        scene diningroom
        
        if friend == "ellie":
            "I sit down with Ellie and Sophie." 

            show ellie at right
            show sophie at left

            if firstdate == "yes":
                "Surprisingly at dinner yesterday, I didn't tell them about my date with Prince Chris today. I tell them."
                e "No way! I have a date with the Prince today too!"

            else:
                e "I forgot to tell you guys! I have a date with the Prince today!"
                s "No way, me too!"

            "Jealousy bubbles up inside me."

            menu:
                "Be happy for them":
                    "I smile through the pain."
                    jump breakfast_done

                "Poison them":
                    "I must eliminate the competition."
                    jump kitchen_scene

        elif friend == "natalie":
            "I sit down next to Natalie." 

            show natalie

            if firstdate == "yes":
                "Surprisingly at dinner yesterday, I didn't tell her about my date with Prince Chris today. I tell her."
                n "No way! I have a date with the Prince today too!"
            else:
                n "I forgot to tell you yesterday, I have a date with the Prince today!"

            "Jealousy bubbles up inside me."

            menu:
                "Be happy for her":
                    "I smile through the pain."
                    jump breakfast_done

                "Poison her":
                    "I must eliminate the competition."
                    jump kitchen_scene
            
        else:
            "I eat alone."
            jump breakfast_done


    label kitchen_scene:
        scene kitchen
        "I sneak into the kitchen, it smells delicious in here."
        "Out of nowhere, someone leaps out in front of me."
        
        show cpr2
        cpr "Buonjiorno! Welcome to my kingdom!"
        m "Who are you?"
        cpr "It's me, Chef Chris! But you can call me... anytime."
        "He winks."
        "He... doesn't look like a chef."
        
        menu:
            "Flirt with the Chef":
                $ karma -= 1
                $ liking_chef += 1
                m "You're the tastiest thing in this kitchen."
                cpr "Stop it, or I'll make a treat out of you!"
                "He winks again and I giggle."
            
            "Just ask for help":
                m "I need a favor."
                cpr "What can I do for you?"

        m "I need something... to give someone a little stomach ache. Just for a few hours."
        cpr "A stomach ache? That is not very nice."
        
        menu:
            "It's for me. I know it's weird but... I love stomach aches.":
                cpr "Okay, you're weird. But take this, it works fast."
                $ has_poison = True
            
            "I need to eliminate my rivals.":
                if liking_chef > 0:
                    cpr "Ah, you're spicy. I like it. Take this."
                    $ has_poison = True
                else:
                    cpr "What? No! Go away!"
                    $ has_poison = False


        scene diningroom
        "I return to the table."
        
        if has_poison:

            if friend == "ellie":
                "I slip the extract into Ellie's juice when she's not looking."
                if karma < -1:
                    show sophie at left
                    s "What do you think you're doing?"
                    "Sophie points at the vial in my hand."
                    show ellie at right
                    e "What? Were you trying to poison me?"
                    "They both stare at me."
                    m "I..."
                    e "I want to report you but I don't want to win that way."
                    e "Stay away from me."
                    s "And me."
                    scene diningroom
                    "The girls leave me on my own. I guess I don't have any friends here anymore."
                    $ friend = "no1"
                    jump breakfast_done

                else:
                    show ellie 
                    e "Hmmm... this juice doesn't taste so good..."
                    "Ellie runs out of the dining room. Victory!"
                    hide ellie
                    show sophie
                    s "Poor Ellie, I hope she's okay!"
                    jump breakfast_done


            elif friend == "natalie":
                "I slip the extract into Natalie's juice when she's not looking."
                if karma < -1:
                    "Suddenly, Patricia walks in."
                    show patricia at left
                    p "What are you doing?!"
                    "She points at the vial in my hand."
                    show natalie at left
                    n "What??? Were you trying to poison me?"
                    "The dining room falls silent and all the girls stare at me."
                    p "This is against the rules, and you know that. HOME!!!"
                    scene blackout
                    "End of game"
                    "Better luck next time"
                    return

                else:
                    show natalie
                    n "Hmmm... this juice doesn't taste so good..."
                    "Natalie runs out of the dining room. Victory!"
                    jump breakfast_done

        else:
            "I couldn't get the poison. I just eat my toast angrily."
            jump breakfast_done



    label breakfast_done:

        scene room
        if firstdate == "yes":
            "I head back to my room to prepare for my date later with Prince Chris."
            jump second_date

        else:
            if has_poison:
                "I spend the rest of the day looking at the ceiling"
                if friend == "ellie":
                    "At least Ellie can't go on her date anymore..."
                elif friend == "natalie":
                    "At least Natalie can't go on her date anymore..."

            else:
                "I spend the rest of the day looking at the ceiling while other girls have dates."
                "This sucks. I must make a better impression next time I see him."

            return



    label second_date:

        scene blackout

        "After getting ready, and reading for a bit, I head downstairs for lunch with the Prince."

        scene diningroom
        with fade
        
        show cphappy
        c "I'm so glad you could make it, %(player_name)s."
        
        menu:

            "You're so hot.":
                $ date += 1
                "The Prince blushes."
                c "You don't look so bad yourself either..."

            "Let's eat.":
                c "Straight to business. I like that."
        
        "We sit down. The atmosphere is romantic."
        "The dining room got cut off from the other girls, so that the Prince and I could have some privacy."
        "We have lunch and chat about random things. After we've eaten, he's more serious."

        hide cphappy
        show cpmysterious
        c "So, how are you finding life at the castle?"
        
        menu:

            "It's overwhelming but amazing.":
                $ date += 1
                c "I can imagine. I'm here to support you."
            
            "I don't love it - I want more freedom.":
                $ date -= 1
                c "Ah, I see..."
                c "Maybe you're not cut out for this lifestyle."

            "It's... fine.":
                c "Maybe you'll have more to say if you stay longer."


        c "Are the staff nice to you?"

        if liking_guard > 1:

            if liking_chef > 1:

                menu:

                    "Yes, guard Hemsworth has been particularly endearing...":
                        $ date -= 1
                        c "Oh..."
                        "Prince Chris looks jealous."
                        c "I really hope that's not going to impact our time together."
                        "He now looks stern. I feel scolded."
                        "Just be careful %(player_name)s. You know what happens if you see other men."
            
                    "Yes, the chef was really quite charming...":
                        $ date -= 1
                        c "Oh..."
                        "Prince Chris looks jealous."
                        c "I really hope that's not going to impact our time together."
                        "He now looks stern. I feel scolded."
                        "Just be careful %(player_name)s. You know what happens if you see other men."

                    "The maid's been great.":
                        $ date += 1
                        c "I can imagine. I'm here to support you."

                    "It's been fine. Nothing spectacular.":
                        c "Oh.. Well hopefully that will change. I'll have a chat with them."
            else:

                menu:

                    "Yes, guard Hemsworth has been particularly endearing...":
                        $ date -= 1
                        c "Oh..."
                        "Prince Chris looks jealous."
                        c "I really hope that's not going to impact our time together."
                        "He now looks stern. I feel scolded."
                        "Just be careful %(player_name)s. You know what happens if you see other men."
            
                    "The maid's been great.":
                        $ date += 1
                        c "I can imagine. I'm here to support you."

                    "It's been fine. Nothing spectacular.":
                        c "Oh.. Well hopefully that will change. I'll have a chat with them."


        elif liking_chef > 1:

            menu:

                "Yes, the chef was really quite charming...":
                    $ date -= 1
                    c "Oh..."
                    "Prince Chris looks jealous."
                    c "I really hope that's not going to impact our time together."
                    "He now looks stern. I feel scolded."
                    "Just be careful %(player_name)s. You know what happens if you see other men."

                "The maid's been great.":
                    $ date += 1
                    c "I can imagine. I'm here to support you."

                "It's been fine. Nothing spectacular.":
                    c "Oh.. Well hopefully that will change. I'll have a chat with them."

        else:

            m "Yes, my maid has been lovely to me."
            $ date += 2
            c "That's very nice to hear."
 

        if date > 2:
            c "I feel like I can really talk to you %(player_name)s."
            c "In fact... I think I'm starting to fall for you."
            "He reaches for my hand and stares into my eyes."
            "My heart skips a beat."
            c "I want to see you again for another date tomorrow. I'll plan something active this time so wear some sports gear."
            "I nod. Too nervous to speak."

        if date >= 0:

            c "I had a nice lunch with you today %(player_name)s."
            c "I'll see you around the palace."

        if else:

            c "I have a lot to think about after this lunch..."
            c "You may want to start packing."
            scene blackout
            "I go back to my room, devastated."
            "End of game"
            "better luck next time"
            return
            
        scene blackout
        "I go back to my room, heart fluttering."
        return

