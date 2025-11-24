# ---------- CONFIG / VARIABLES ----------

define v = Character("Victor", color="#e0d0c0")
define c = Character("Monster", color="#c0ff80")
define n = Character(None)  # narrator

default hearts = 3
define max_hearts = 3

# Optional: slightly slower text for dramatic effect
# $ preferences.text_cps = 40

# ---------- IMAGES ----------

# BACKGROUNDS
image bg_orkney = "backgrounds/bg_orkney.png"
image bg_lab_night = "backgrounds/bg_lab_night.png"
image bg_lab_night_empty = "backgrounds/bg_lab_empty.png"
image bg_window_casement = "backgrounds/bg_casement.png"
image bg_bedroom = "backgrounds/bg_bedroom.png"
image bg_beach_night = "backgrounds/bg_coastline.png"

# VICTOR SPRITES
image victor neutral = "characters/victor/victor_neutral_open.png"
image victor tired = "characters/victor/victor_tired.png"
image victor concerned = "characters/victor/victor_anxious_closed.png"
image victor worried = "characters/victor/victor_tired.png"
image victor anxious = "characters/victor/victor_anxious_open.png"
image victor panic = "characters/victor/victor_angry_closed.png"
image victor angry = "characters/victor/victor_angry_open.png"
image victor furious = "characters/victor/victor_furious_open.png"
image victor collapsed = "characters/victor/victor_neutral_closed.png" #placeholder

# CREATURE SPRITES
image creature neutral = "characters/monster/monster_neutral_open.png"
image creature grin = "characters/monster/monster_grin.png"
image creature angry = "characters/monster/monster_angry_open.png"
image creature wrath = "characters/monster_despair_closed.png"
image creature despair = "characters/monster/monster_despair_open.png"
image creature shadow = "characters/monster/monster_shadowed_open.png"

# UI HEARTS
image ui_heart_full = "hearts/full_heart.png"
image ui_heart_empty = "hearts/empty_heart.png"

# ---------- HEART HUD SCREEN ----------

screen hud():
    hbox:
        xalign 0.03
        yalign 0.03
        spacing 4
        for i in range(max_hearts):
            if i < hearts:
                add "ui_heart_full":
                    zoom 0.15
            else:
                add "ui_heart_empty":
                    zoom 0.15

# ---------- START LABEL (ORKNEY ONLY) ----------

label start:

    # Reset hearts at the beginning of the Orkney sequence
    $ hearts = 3
    show screen hud
    # SCENE 1 – Orkney establishing, context
    play music  "audio/wind_light.wav" fadein 1.5 loop
    scene bg_orkney
    with fade

    n "Victor Frankenstein had fled far to the north, to one of the remotest of the Orkney islands."
    n "The island was little more than a rock, beaten constantly by the waves and barren of almost all life."
    n "Only a few miserable cottages dotted the shoreline, and a handful of gaunt inhabitants lived off oatmeal and what they could bring from the mainland."

    show victor tired at left
    v "A fitting place to bury myself in work... and in my own horror."

    n "Here he had chosen to continue a task he now dreaded: the making of a second creature."

    # SCENE 2 – Routine / isolation summary (short, mostly narration)
    scene bg_lab_night  # you can swap to day version later if you create one
    with dissolve

    n "He lodged in a small hut, its rooms rough and barely repaired, and turned one of them into a laboratory."
    n "By day he worked among instruments and jars; by evening he walked along the stony beach, listening to the ocean roar at his feet."
    show victor concerned at left
    v "Switzerland feels like another world. This desolate rock is all I deserve."

    # We jump forward in time to when the work is well underway and horrible to him.
    n "As his labours advanced, the work grew more loathsome. Sometimes he could not bring himself to enter the lab for days; at other times, he toiled day and night."
    show victor worried at left
    v "The first time, frenzy blinded me to what I was doing..."
    v "...but now I see every detail clearly, and it sickens me."

    # ---- SCENE 3 – Evening in the lab (start of actual passage, trivia begins after reflections) ----

    scene bg_lab_night
    with fade

    play sound  "audio/rain_heavy_inside.wav" loop
    # (optionally mix rain+wind in your mixer; or just keep one)

    show victor tired at left
    n "One evening, Victor sat alone in his laboratory. The sun had set; the moon was rising out of the sea beyond the window."
    n "The light was too dim for careful work, and he hesitated between resting and forcing himself to continue."

    show victor concerned
    v "If I stop now, I delay the end of this horror."
    v "If I continue, I may set something worse loose on the world."

    # ---- SCENE 4 – Reflection on first creation (Trivia Q1) ----

    n "His thoughts returned to his first experiment, three years before, and to the being he had drawn into existence."
    show victor worried
    v "That single act has filled my life with remorse."

    # TRIVIA 1 – about the first creature & Victor's feeling
    call trivia_1

    # ---- SCENE 5 – Fears about the female & race of devils (Trivia Q2, Q3) ----

    show victor anxious
    n "He looked toward the shape on the table, the half-finished female he laboured to animate."
    v "I know nothing of her mind. She might be more cruel than the first..."
    v "He promised to hide himself from mankind. She never did."
    v "She could reject him, or flee to men, or help him people the world with more like them."

    # TRIVIA 2 – about his fear of their offspring
    call trivia_2

    show victor anxious
    n "He imagined them fleeing Europe, only to breed a race that would make human life fearful and uncertain."
    v "Do I have the right to inflict such a curse on the generations to come?"

    # TRIVIA 3 – about his moral dilemma
    call trivia_3

    show victor worried
    n "He remembered how the creature's arguments had once swayed him, and how its threats had shaken him."
    n "But now, the wickedness of his promise stood before him with terrible clarity."

    # ---- SCENE 6 – Creature at the window ----

    play sound "audio/thunder.wav"
    $ renpy.pause(0.4)

    show victor panic
    n "A shudder ran through him; his heart seemed to fail. Slowly, he looked up toward the window."

    scene bg_window_casement
    with dissolve

    show creature grin at right
    play sound  "audio/steps_heavy.mp3"
    n "In the moonlight, the creature's face pressed against the casement, lips twisted in a ghastly grin."
    n "It had followed him: through forests, caves, and heaths, watching, waiting."

    # ---- SCENE 7 – Bride destroyed ----

    scene bg_lab_night
    show victor furious at left
    show creature grin at right
    with dissolve

    n "As Victor looked at him, the creature's expression showed nothing but malice and treachery."
    v "Another like you... No. Never again."

    play sound  "audio/flesh_tear.mp3"
    $ renpy.pause(0.2)

    n "Seized by a kind of madness, he tore apart the unfinished creature, destroying the work on which the dæmon had set his hopes."

    show creature despair at right
    n "The wretch saw the ruin of his only chance at companionship and howled with a despair that twisted into revenge."

    # Cut to black, then lab without the body
    scene black
    with fade
    $ renpy.pause(0.8)

    scene bg_lab_night_empty
    with fade

    n "When the echo of his cry faded, the laboratory seemed emptier than ever. The table lay bare; shreds of the ruined work had been cleared away."

    # ---- SCENE 8 – Victor vows to stop, goes to bedroom ----

    show victor tired at left
    v "It is done. I will not resume these labours. Not ever."

    scene bg_bedroom
    with dissolve

    play sound  "audio/rain_heavy_outside.wav"
    show victor worried at left
    n "Victor locked the lab behind him and retreated to his small room."
    n "Alone, with no one to break the gloom, his mind filled with the worst imaginings."

    # ---- SCENE 9 – Waiting, footsteps, creature enters (Trivia Q4) ----

    n "Hours passed. He sat by the window, gazing at the sea, its surface almost motionless under the quiet moon."
    n "He heard distant voices of fishermen, carried briefly by the breeze, then swallowed again by silence."

    play sound  "audio/run.mp3"
    n "At last, the sound of oars near the shore reached him. Someone had landed close to the house."

    play sound  "audio/door_creak.mp3"
    n "A soft creaking at the door below made him tremble from head to foot."

    show victor panic
    v "It's him... it must be him... I should call for help—no, I can't move..."

    play sound  "audio/steps_heavy.mp3"
    n "Heavy footsteps approached along the passage. The door to his room opened."

    show creature angry at right
    with dissolve

    c "You have destroyed the work you began. Do you dare break your promise?"
    c "I have followed you across countries, through cold and hunger, to see this hope fulfilled."

    # TRIVIA 4 – about where the creature has followed him (Rhine/England/Scotland)
    call trivia_4

    # ---- SCENE 10 – Threats & wedding-night vow (Trivia Q5, Q6, Q7) ----

    show victor angry at left
    v "Begone. I do break my promise. I will never make another like you."

    show creature wrath at right
    c "Slave. You are my creator, but I am your master. Obey."
    c "You believe yourself miserable? I can make your days so wretched that daylight itself will be hateful to you."

    # TRIVIA 5 – about the creature's new ruling passion (revenge)
    call trivia_5

    c "Shall every man have his wife, and each beast its mate, and I be alone?"
    c "You can tear away my other hopes, but revenge remains—dearer than light or food."

    show victor furious at left
    v "I will not set loose another demon on the earth. Go, and do not poison the air with your words."

    show creature grin at right
    c "Very well. I go. But remember: I shall be with you on your wedding-night."

    # TRIVIA 6 – about what night he names
    call trivia_6

    show victor furious
    v "Villain! Before you sign my death-warrant, be sure you are yourself safe!"

    scene bg_beach_night
    with dissolve

    play sound  "audio/run.mp3"
    n "Victor rushed to the shore in time to see a small boat darting away into the darkness, the creature's form shrinking into the distance."

    # ---- SCENE 11 – Aftermath on the island (no more trivia, just closing) ----

    scene bg_bedroom
    show victor anxious at left
    with fade

    n "Silence returned, but the creature's words echoed in his mind."
    v "Wedding-night... so that is when he will strike."

    n "He paced the room in agitation, imagining a thousand cruel possibilities."
    n "At last, rage sank into a deeper despair, and the night slowly gave way to dawn."

    scene bg_beach_night
    with dissolve

    n "The next day he walked the shore like a restless specter, half wishing to remain on that barren rock forever."
    n "But a letter summoned him away, and before he could depart he had to put his instruments and the last traces of his work in order."

    n "The decision not to resume his labours never wavered. For the first time, the idea of creating another being seemed clearly, absolutely wrong to him."

    # ORKNEY SEQUENCE END
    n "Thus ended Victor's work on the Orkney island—but the creature's threat still clung to him, like a shadow."

    return


# ---------- TRIVIA LABELS (hearts + loop until correct) ----------

label trivia_1:
    # About Victor's feeling after the first creation
    show victor concerned
    n "Thinking back to his first experiment, how did Victor feel about what he had done?"

    menu:
        "He looked back on it with pride.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "The very idea sickens him. Even his memory rebels at that thought."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_1

        "It filled his life with remorse and horror.":
            play sound "audio/correct.mp3"
            show victor worried
            n "He remembered only remorse: the barbarity of the creature, and the guilt that had never faded."
            return

        "He felt indifferent; it was only a scientific result.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "If only it had been that simple. His heart has never been indifferent to the consequences."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_1


label trivia_2:
    # About fear of offspring
    show victor anxious
    n "What future possibility terrified Victor most as he imagined finishing the female?"

    menu:
        "That she would immediately kill him in the lab.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor panic
            n "He feared for many lives, not only his own."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_2

        "That together they would have children and form a race of beings like themselves.":
            play sound "audio/correct.mp3"
            show victor worried
            n "He pictured generations of such beings, making human life precarious and full of terror."
            return

        "That she would be too gentle, and pity mankind.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "Gentleness was not what haunted him. It was the thought of multiplying his mistake."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_2


label trivia_3:
    # About his moral question
    show victor concerned
    n "What question about his own right troubled Victor most?"

    menu:
        "Whether he had the right to disobey the creature.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "It was not obedience that obsessed him; it was what he might do to all mankind."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_3

        "Whether he had the right to bring such a curse on future generations for his own peace.":
            play sound "audio/correct.mp3"
            show victor worried
            n "He imagined ages to come cursing his name as their pest."
            return

        "Whether he had the right to leave the island before finishing his work.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "The island itself was not the true question; the fate of humanity was."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_3


label trivia_4:
    # About where the creature followed him
    show creature angry at right
    n "The creature lists the places he followed Victor through. Which is one of them?"

    menu:
        "Along the shores of the Rhine and over its hills.":
            play sound "audio/correct.mp3"
            show creature neutral
            n "He had crept along the Rhine and over its summits, haunting Victor's journey."
            return

        "Through the deserts of Africa and across the Alps.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious at left
            n "That is not how the creature describes his path."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_4

        "Across the frozen seas of the Arctic before Orkney.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "The Arctic comes later in the story; this is not yet that part of his pursuit."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_4


label trivia_5:
    # About the creature's ruling passion
    show creature wrath at right
    n "The creature says that, though other hopes can be destroyed, one passion remains to him. What is it?"

    menu:
        "Revenge, dearer than light or food.":
            play sound "audio/correct.mp3"
            show creature wrath
            n "Revenge becomes his only sustaining desire."
            return

        "Love, which he hopes to find among men.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious at left
            n "Love was what he once sought, but it has curdled into something darker."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_5

        "Ambition, to rule over mankind.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show creature angry
            n "He does not speak of ruling men—only of making Victor suffer as he has suffered."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_5


label trivia_6:
    # About the wedding-night threat
    show creature grin at right
    n "When the creature finally leaves, what moment does he name as the time he will 'be with' Victor?"

    menu:
        "On Victor's wedding-night.":
            play sound "audio/correct.mp3"
            show victor panic at left
            n "Those words fix a date in Victor's mind, turning joy into a sentence."
            return

        "On the night Victor finishes a new creature.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "Victor has already destroyed his work; the creature's threat is tied to something else."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_6

        "On the night Victor returns to Switzerland.":
            $ hearts -= 1
            play sound "audio/wrong.mp3"
            show victor anxious
            n "The creature chooses something far more personal than a place."
            if hearts <= 0:
                jump game_over_hearts
            jump trivia_6


# ---------- GAME OVER (HEARTS REACHED ZERO) ----------

label game_over_hearts:

    hide screen hud
    scene bg_bedroom
    with fade

    show victor collapsed at center
    play sound "audio/run.mp3"
    $ renpy.pause(0.5)

    n "Victor's thoughts spun out of control. Memories blurred, and the weight of his guilt crushed down on him."
    v "Why can't I recall what has happened? Why does everything slip away from me...?"
    n "His nerves, worn thin by sleepless nights, fear, and solitude, finally gave way."
    n "He collapsed where he stood, swallowed by exhaustion and dread."

    scene black
    with fade

    n "{b}GAME OVER{/b}"
    n "Victor's mind breaks under the strain long before the creature's threat can be fulfilled."

    menu:
        "Return to Main Menu":
            return

        "Restart the Orkney sequence":
            jump start
