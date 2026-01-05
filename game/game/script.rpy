# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

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
define ch = Character ("Chris Hemsworth")

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

     "I'll definately wear a dress! I'll look amazing!"

    jump makeup

    label jeans:
     $ clothing = "jeans"

     "I'll definately wear jeans. It'll not be too casual, and not too fancy."

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

    elif clothing == "dress":

        mom "You look great honey."

        m "Thanks mom!"

        scene photoshoot

        jump photoshoot

    elif clothing == "jeans":

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

        return

    label won1:

        "Eventually....."

        tv "Thirty two, %(player_name)s %(player_surname)s."

        scene blackout

        "I made it."

        "I can't believe it."

        "That means that tomorrow someone from the palace will come visit."

        "Apparently they'll inform me about some things.."

        "Then they'll tell me when to leave!"

        scene bedroom
        with fade

        "KNOCK KNOCK!"

        show man

        unknown "Hello, you must be %(player_name)s %(player_surname)s."

        unknown "I'm here to get your body measurements and tell you some rules."

        m "Alright."

        scene bedroom

        "The man measures my body, and then he tells me some rules."

        show man

        unknown "It's vital for you to know these rules, so listen carefully."

        unknown "When you are part of the Selection, it's forbidden to see other guys."

        unknown "You'll also immediately be disqualified if you sabotage other girls."

        unknown "And of course, you can apply your own manners for the rest, such as just being genuinly polite."

        menu:

            unknown "Do you understand or do you want me to repeat them?"

            "Understood.":

                jump done

            "Repeat please.":

                jump again

        label again:

            unknown "Okay so,"

            unknown "When you are part of the Selection, it's forbidden to see other guys."

            unknown "You will immediately disqualified if you sabotage other girls."

            unknown "And of course, you can apply your own manners for the rest, such as just being genuinly polite."

        label done:

            unknown "Good."

        unknown "Now that you're all done, you can prepare to pack - you're leaving tomorrow morning."

        m "Okay! Thank you!"

        scene bedroom

        "I better start packing then!"

        scene blackout

        "It's early in the morning. I've said good bye to my family, and I'm in the car on my way to the airport."

        "I wonder if I'll make friends whilst I'm there.."

        scene plane

        "On the plane, I'm sitting by the window, and next to me are two other girls who are part of the Selection."


        menu:

            "I wonder if I should say something... It would be nice to know someone."

            "Say something.":

                jump say

            "Stay Quiet.":

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

                        m "His smile, definately."

                        s "Yes. I love it too."

                        e "I actually like his eyes better. Is that weird."

                        s "Yes definately."

                        "Ellie and I laugh."

                    jump continue1

                    label continue1:

                        "For the rest of the plane ride the three of us just talk."

                        "I'm glad I decided to speak to them."

                        jump entering

        label quiet:

            "I decide not to talk to them and just silently listen to music for the rest of the plane ride."

            jump entering

        label entering:

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

            d "Nice choice. I've heard the prince likes that."

            jump continue2

        label yellowmaxi:

            $ dress = "yellow"

            m "I'd like the yellow maxi dress please."

            d "Okay."

            jump continue2

        label blacklace:

            $ dress = "black"

            m "I'd like the black lace please."

            "Derek smirks."

            d "Alrightie."

            jump continue2

    label continue2:

        scene blackout

        "After I chose a dress, I got to go to my room and met my maid."

        scene room
        with fade

        m "Hello..?"

        unknown "Finally!"

        show maid

        maid "Hello, you must be Miss %(player_surname)s! I'm Jenna!"

        m "Nice to meet you Jenna."

        "Jenna curtsied, and then she told me she'd prepare me for the dinner."

        scene blackout

        "I took a bath and I put on the dress that I chose earlier."

        scene room
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
        show cptalking

        if meeting == "early" and dress == "red":

            c "Oh hello again. You found your way today then?"

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

                c "How about I take you out for dinner tomorrow night? I'll let you eat my favorite food."

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

                c "Oh well, I'm sure you'll find someone, cause you'll definately have time to."

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

                c "How about I take you out for dinner tomorrow night, and find out then?"

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

                    c "Well there must be something else. Since you're so secretive how about I take you to dinner tomorrow?"

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

                        if friend == "natalie":

                                "Me? Really? And Natalie gets to stay???"

                                show natalie

                                n "Oh... I'm so sorry %(player_name)s..."

                        else:

                                "Me? Really?"

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
