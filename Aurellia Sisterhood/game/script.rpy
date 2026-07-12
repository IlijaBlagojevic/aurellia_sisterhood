
#Includes
include "UI/phone.rpy"
include "UI/ui.rpy"

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define igrac = Character("[iname]")
define p = Character("???")
default iname = "Paul"
define Jane = Character("Jane")


# The game starts here.

label start:
    

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.



    $ iname = renpy.input("Unesi ime: ", default="Paul", length=15, allow="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ").strip()
    if iname == "":
        $ iname = "Paul"

    play music "audio/IgracPesma.mp3" fadein 2.0

    "For many students, university life is a constant struggle between ambition and survival."
    
    "Empty wallets, overdue assignments, and uncertain futures become part of everyday life."
    "Yet even in the darkest moments, opportunity has a way of appearing in unexpected places."
    "All it takes is the courage to take the first step. Whether that step leads to salvation..."
    "or something else entirely, is a story only the brave will discover."

    scene bg soba
    with fade
    show screen floating_phone_button

    igrac "The rain tapped softly against my apartment window."
    igrac "Not that it mattered."
    igrac "It wasn't like I had anywhere else to be."
    igrac "I stared at the notification on my laptop."
    igrac "Fuck... not again."
    "Academic Warning."
    igrac "Three failed courses."
    igrac "Just one barely passed."
    igrac "If I continue with this tempo, it will take me years until I finish college."
    igrac "One professor had stopped pretending I could still turn things around. Another simply wrote, {b} See me after class{\b} I never did."
    "He leaned back on his chair with look of despair in his face."
    igrac "Sons of a bitches."
    igrac "I fucking hate every single one of them."
    igrac "When I first got accepted into university, everyone said these would be the best years of my life."
    igrac "yeah, that was a good joke."
    igrac "Every semester started the same way."
    igrac "This time I'll stay ahead."
    igrac "This time I'll study every day."
    igrac "This time I'll stop procrastinating."
    igrac "And every semester ended exactly the same."
    igrac "Late assignments."
    igrac "Missed lectures."
    igrac "Failed exams."
    igrac "I dont know if I am stupid or not."
    igrac "Some people just seemed born knowing how to keep everything together."
    igrac "Classes, part time jobs, relationships."
    igrac "Meanwhile I struggle with everything."
    igrac "My room reflects my life perfectly."
    igrac "I dont dare to look myself up in the mirror."
    igrac "I opened my wallet."
    igrac "Fly had flew of it."
    igrac "Just few coins inside."
    igrac "I dont have enough for groceries."
    igrac "Definitely not enough for next month's rent."
    igrac "The scholarship I'd counted on was gone the moment my grades dropped."
    igrac "My parents couldn't keep sending money forever."
    igrac "Honestly..."
    igrac "They probably thought I was doing much better than I actually was."
    igrac "I couldn't bring myself to tell them the truth."
    igrac "So... I need a job."
    igrac "Somethig simple."
    igrac "Cashier, Warehouse worker, Delivery driver, Night shifts, Didn't matter anymore."
    "He opened a job listing website and started scrolling."
    "Restaurant."
    "Rejected."
    "Retail."
    "Rejected."
    "Retail."
    "Expirience requied."
    "Office assistant."
    "Already filled."
    scene black
    with fade

    $renpy.notify("Hours passed.")
    "..."
    scene bg soba
    with fade

    igrac "AHHHHHH Jesus."
    igrac "Every posting wanted someone with experience."
    igrac "Or qualifications,or availability that clashed perfectly with my lectures."
    igrac "hahahaha."
    igrac "Really funny."
    igrac "You need expirience to get a job."
    igrac "But you need job to get expirience."
    igrac "I'll keep scrolling anyway."
    "Then..."
    "One thing stod up."
    igrac "Aurellia Sisterhood."
    igrac "Empowering women through financial independence and community leadership."
    igrac "Looking for motivated administrative assistants to support our growing organization."
    igrac "Flexible hours."
    igrac "Competitive pay."
    igrac "No prior experience required."
    
    igrac "...That sounds almost too good."
    "The company logo was elegant."
    "The website looked polished."
    "Testimonials filled the page."
    "Smiling faces."
    "Stories of success. Women talking about changing their lives. Everything looked... surprisingly professional."
    igrac "...well."
    igrac "It's not like I have better optinions."
    "I pulled out my phone and called it."

    scene bg phone
    with fade

    p "Hello! You've reached {b} Aurellia Sisterhood {/b}. My name is Jane. How may I help you today?"
    igrac "Hi... I saw your job listing online. I'm interested in applying."
    Jane "Wonderful. We always appreciate motivated applicants. May I have your name?"
    igrac "yeah, it's [iname]."
    Jane "Thank you, [iname]. We'd like to invite you to a brief orientation and registration meeting. It won't take long."
    igrac "Sounds good. Where should I go?"
    Jane "Our office is on the third floor of the Aurora Business Center. Please arrive tomorrow at 10:00 a.m. and bring a photo ID."
    igrac "Is there anything else I should prepare?"
    Jane "Just yourself and an open mind. We'll explain everything once you arrive."
    igrac "...Alright. I'll be there."
    Jane "Excellent. We look forward to meeting you, [iname]. Have a wonderful day."
    igrac "You too."
    "*Click*"

    scene bg soba
    with fade

    igrac "I can't belive it went so smooth."
    igrac "I sure am a lucky guy afterall."
    igrac "She sounded so hot over phone... Just like those girls that work at HotLine."
    igrac "I better head to bed now, I want to have energy for tomorrow."

    scene black
    with fade
    $renpy.notify("Sleeping...")

    ""

    scene bg alarm
    with fade

    play sound "audio/Alarm.mp3" fadein 2.0

    ""

    igrac "Oh shit, I better hurry up!"
    
    scene bg soba
    with fade

    stop sound
    igrac "ughmmmm."

    scene bg toalet1
    with fade
    play sound "audio/shower.mp3"
    "I woke up, went to bathroom and took cold shower."
    "I can feel this day will be good."
    stop sound fadeout 2.0

    scene bg soba
    with fade

    ""
    "It's time to go..."

    "You can open map by clicking on your phone."
    




    



    # This ends the game.

    
