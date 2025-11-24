# ------------------------------------------------------------
# CONFIG & VARIABLES
# ------------------------------------------------------------

# Optional: make text type out instead of instant (tweak or remove if you don't like it)
define config.default_text_cps = 40  # characters per second

# Characters
define v = Character("Victor", color="#e0d0ff")
define m = Character("Creature", color="#ffb0b0")
define n = Character("Narrator", color = "#ffffff")  # unnamed narrator (just text)
define config.default_text_cps = 30


# Hearts (health / sanity)
default hearts = 3
define max_hearts = 3

# ------------------------------------------------------------
# IMAGES: BACKGROUNDS
# ------------------------------------------------------------

image bg orkney_coast = "images/backgrounds/bg_orkney.png"
image bg lab_night    = "images/backgrounds/bg_lab_night.png"
image bg window       = "images/backgrounds/bg_casement.png"
image bg bedroom      = "images/backgrounds/bg_bedroom.png"
image bg beach_night  = "images/backgrounds/bg_coastline.png"
image bg lab_empty = "images/backgrounds/bg_lab_empty.png"

# ------------------------------------------------------------
# IMAGES: VICTOR SPRITES (OPEN/CLOSED MOUTHS)
# ------------------------------------------------------------

image victor neutral_open      = "images/characters/victor/victor_neutral_open.png"
image victor neutral_closed    = "images/characters/victor/victor_neutral_closed.png"

image victor tired             = "images/characters/victor/victor_tired.png"      # no open/closed

image victor concerned_open    = "images/characters/victor/victor_anxious_open.png"
image victor concerned_closed  = "images/characters/victor/victor_anxious_closed.png"

image victor anxious_open      = "images/characters/victor/victor_anxious_open.png"
image victor anxious_closed    = "images/characters/victor/victor_anxious_closed.png"

image victor panic_open        = "images/characters/victor/victor_anxious_open.png"
image victor panic_closed      = "images/characters/victor/victor_anxious_closed.png"

image victor angry_open        = "images/characters/victor/victor_angry_open.png"
image victor angry_closed      = "images/characters/victor/victor_angry_closed.png"

image victor furious_open      = "images/characters/victor/victor_angry_open.png"
image victor furious_closed    = "images/characters/victor/victor_angry_closed.png"


# ------------------------------------------------------------
# IMAGES: CREATURE SPRITES (OPEN/CLOSED MOUTHS WHERE PROVIDED)
# ------------------------------------------------------------

image creature neutral_open    = "images/characters/monster/monster_neutral_open.png"
image creature neutral_closed  = "images/characters/monster/monstere_neutral_closed.png"

image creature grin            = "images/characters/monster/monstergrin.png"

image creature angry_open      = "images/characters/monster/monster_angry_open.png"
image creature angry_closed    = "images/characters/monster/monster_angry_closed.png"

image creature despair_open    = "images/characters/monster/monster_despair_open.png"
image creature despair_closed  = "images/characters/monster/monster_despair_closed.png"

image creature shadowed_open   = "images/characters/monster/monster_shadowed_open.png"
image creature shadowed_closed = "images/characters/monster/monster_shadowed_closed.png"


# ------------------------------------------------------------
# IMAGES: UI (HEARTS)
# ------------------------------------------------------------

image heart_full  = "hearts/full_heart.png"
image heart_empty = "hearts/empty_heart.png"

# NOTE: If hearts are too big, you can scale them like this:
# image heart_full_small  = im.Scale("images/ui/heart_full.png", 48, 48)
# image heart_empty_small = im.Scale("images/ui/heart_empty.png", 48, 48)
# Then use heart_full_small / heart_empty_small in the HUD instead.


# ------------------------------------------------------------
# AUDIO DEFINITIONS
# (Adjust filenames to match your actual files in /audio)
# ------------------------------------------------------------

define audio.wind         = "audio/windy_heavy.wav"
define audio.rain         = "audio/rain_heavy_outside.wav"
define audio.rain_inside  = "audio/rain_heavy_outside.wav"
define audio.thunder      = "audio/thunder.wav"
define audio.waves        = "audio/waves.mp3"
define audio.door_creak   = "audio/door_creek.mp3"
define audio.footsteps    = "audio/steps_heavy.mp3"
define audio.flesh_tear   = "audio/flesh_tear.mp3"
define audio.correct_sfx  = "audio/correct.mp3"
define audio.wrong_sfx    = "audio/wrong.mp3"

# NOTE: if you only want part of an sfx, you can:
# - trim it in an external audio editor, OR
# - lower the volume and stop it quickly using `queue` / `stop sound`.


# ------------------------------------------------------------
# TRANSFORMS (POSITION / SIZE)
# ------------------------------------------------------------

transform left_side:
    xalign 0.2
    yalign 1.0

transform right_side:
    xalign 0.8
    yalign 1.0

# Example: to custom position or resize a sprite, you can do:
# show victor neutral_open at left_side:
#     zoom 0.9
# or:
# show creature shadowed_open at Position(xalign=0.8, yalign=1.0)


# ------------------------------------------------------------
# HEART HUD SCREEN
# ------------------------------------------------------------

screen heart_hud():
    zorder 100
    frame:
        xalign 0.02
        yalign 0.02
        background None
        hbox:
            spacing 4

            # full hearts
            for i in range(hearts):
                add "heart_full":
                    zoom 0.15

            # empty hearts
            for i in range(max_hearts - hearts):
                add "heart_empty":
                    zoom 0.15


# ------------------------------------------------------------
# TRIVIA HELPER LABEL
# ------------------------------------------------------------

label lose_heart:
    $ hearts -= 1
    play sound audio.wrong_sfx
    if hearts <= 0:
        jump game_over_panic
    return

# ------------------------------------------------------------
# START & MAIN ORKNEY FLOW
# ------------------------------------------------------------

label start:

    # Show HUD for hearts always
    show screen heart_hud

    # Optional ambient sound
    play music audio.wind fadein 1.0

    # Scene 1: Orkney establishing
    scene bg orkney_coast with fade

    n "Victor Frankenstein has fled south and east, then north, until the world itself seems to narrow into rock and sea."
    n "The Orkney Islands are desolate, battered by waves and wind, far from Geneva, far from Switzerland, and even further from the innocence he once imagined he possessed."

    n "Here, on one of the remotest of these islands, he has chosen a barren rock as the scene of his labours."
    n "The soil barely feeds a few miserable cows, and the island’s handful of inhabitants live in poverty, numb to suffering."
    n "To them he is a strange lodger with a small hired hut; to himself, he is a man attempting to correct—or compound—a monstrous error."

    # Move into lab scene (evening)
    jump orkney_lab_evening


# ------------------------------------------------------------
# ORKNEY LAB – EVENING REFLECTION + TRIVIA
# ------------------------------------------------------------

label orkney_lab_evening:

    stop music fadeout 1.0
    play ambient audio.rain_inside

    scene bg lab_night with fade

    show victor tired at left_side
    n "Victor has spent his mornings labouring over the filthy process of constructing a second being, and his evenings pacing the beach, listening to the roar of the waves."
    n "But tonight, he sits in his laboratory, tools idle, eyes unfocused."

    show victor neutral_open at left_side
    v "Three years ago... I was engaged in the same manner."

    show victor neutral_closed at left_side
    n "He remembers the first experiment: the ecstatic frenzy, the feverish anticipation, and then the horror of the creature's awakening."

    show victor concerned_open at left_side
    v "I created a fiend whose barbarity has desolated my heart, and filled it with a remorse that has never left me."

    show victor concerned_closed at left_side
    n "Now he prepares to repeat the experiment—this time with a companion for the being he loathes and fears."

    # --- TRIVIA 1: about his first creation / remorse ---
    call trivia_1

    show victor anxious_open at left_side
    v "Another being... of whose dispositions I am entirely ignorant."

    show victor anxious_closed at left_side
    n "He imagines her ten thousand times more malignant than her mate, delighting in murder and wretchedness."

    show victor neutral_open at left_side
    v "He swore to quit the neighbourhood of man... but she has made no such promise."

    show victor neutral_closed at left_side
    n "Victor realises the compact he made was with one creature only; the second might refuse to vanish into deserts."

    # --- TRIVIA 2: about the compact / promise ---
    call trivia_2

    show victor concerned_open at left_side
    v "They might even hate each other..."
    v "He already loathes his own deformity—would he not recoil still more from it in another form?"

    show victor concerned_closed at left_side
    n "Victor imagines the female turning away from her mate in disgust, drawn instead to the ‘superior beauty’ of humankind."

    show victor anxious_open at left_side
    v "Then he would be again alone… exasperated, deserted by one of his own species."

    show victor anxious_closed at left_side

    # --- TRIVIA 3: about the risk of their offspring ---
    call trivia_3

    show victor panic_open at left_side
    v "A race of devils... children, propagated upon the earth, making human existence precarious and full of terror."

    show victor panic_closed at left_side
    n "For the first time, the full wickedness of his promise bursts upon him."

    show victor anxious_open at left_side
    v "Had I a right, for my own benefit, to inflict this curse upon everlasting generations?"

    show victor anxious_closed at left_side
    n "He shudders to imagine future ages cursing him as their pest, whose selfishness bought peace at the price of the human race."

    # --- TRIVIA 4: about why his fear shifts from the creature’s threats to his own moral responsibility ---
    call trivia_4

    # Move to the window/creature appearance
    jump orkney_creature_at_window


# ------------------------------------------------------------
# CREATURE AT THE WINDOW & BRIDE DESTRUCTION
# ------------------------------------------------------------

label orkney_creature_at_window:

    stop ambient fadeout 1.0
    play ambient audio.wind

    # Victor in lab, looking up
    scene bg lab_night with fade
    show victor panic_closed at left_side

    n "Victor trembles; his heart fails within him."

    scene bg window with dissolve
    play sound audio.thunder
    n "He looks up. By the light of the rising moon, he sees the dæmon at the casement."

    show creature grin at right_side
    n "A ghastly grin wrinkles the creature’s lips as he gazes upon Victor, who sits fulfilling the task allotted him."

    show victor panic_open at left_side
    v "He followed me... through forests, caves, and heaths, and now comes to claim his due."

    show victor panic_closed at left_side

    # Victor’s sensation of madness → destroys bride
    show victor furious_open at left_side
    v "Another like him... I cannot—"

    show victor furious_closed at left_side
    n "His mind reels; with a sensation bordering on madness, Victor thinks of his promise."

    play sound audio.flesh_tear
    scene black with vpunch
    n "Trembling with passion, he tears to pieces the thing on which he was engaged."

    # Cut back to lab with empty gurney background
    scene bg bg_lab_empty with fade
    # (This is your edited lab background with the body removed.)
    show creature despair_open at right_side
    m "—!"

    play sound audio.flesh_tear
    show creature despair_closed at right_side
    n "The wretch sees Victor destroy the creature whose future existence meant his only hope of happiness."

    show creature angry_open at right_side
    m "..."

    show creature angry_closed at right_side
    n "With a howl of devilish despair and revenge, he withdraws."

    play sound audio.footsteps

    # Victor leaves, locks door, goes to bedroom
    jump orkney_bedroom_dread


# ------------------------------------------------------------
# BEDROOM DREAD + DOOR CREEK + CONFRONTATION
# ------------------------------------------------------------

label orkney_bedroom_dread:

    play ambient audio.rain_inside

    scene bg bedroom with fade
    show victor tired at left_side

    n "Victor locks the laboratory door and vows never to resume his labours. Alone in his small room, he finds no comfort."

    n "Hours pass as he sits near the window, gazing at the almost motionless sea under the quiet moon."

    play sound audio.waves
    n "The silence is so profound that the paddling of oars near the shore startles him."

    play sound audio.footsteps
    n "Footsteps, a door creaking softly… he trembles from head to foot, knowing—before he admits it—who approaches."

    play sound audio.door_creak

    show creature shadowed_open at right_side
    m "You have destroyed the work which you began. Do you dare break your promise?"

    show creature shadowed_closed at right_side
    show victor anxious_open at left_side
    v "Begone! I do break my promise. Never will I create another like yourself, equal in deformity and wickedness."

    show victor anxious_closed at left_side

    show creature angry_open at right_side
    m "Slave, I before reasoned with you; you have proved yourself unworthy of my condescension."
    m "Remember that I have power. You are my creator, but I am your master. Obey!"

    show creature angry_closed at right_side

    show victor furious_open at left_side
    v "The hour of my weakness is past, and the period of your power is arrived."
    v "Your threats cannot move me to an act of wickedness. Begone!"

    show victor furious_closed at left_side

    # --- TRIVIA 5: about the nature of their power dynamic / threat ---
    call trivia_5

    show creature despair_open at right_side
    m "Shall each man find a wife for his bosom, and each beast its mate—and I be alone?"
    m "Beware. Revenge remains—dearer than light or food."

    show creature despair_closed at right_side

    show creature shadowed_open at right_side
    m "It is well. I go; but remember—I shall be with you on your wedding-night."

    show creature shadowed_closed at right_side

    show victor furious_open at left_side
    v "Villain! Before you sign my death-warrant, be sure you are yourself safe!"

    show victor furious_closed at left_side
    n "Victor lunges, but the creature eludes him and flees."

    play sound audio.footsteps
    play sound audio.door_creak

    scene bg beach_night with fade
    play sound audio.waves
    n "In moments, Victor sees a small boat shoot across the waters with arrowy swiftness, vanishing amidst the waves."

    jump orkney_after_confrontation


# ------------------------------------------------------------
# AFTER CONFRONTATION – RAGE, DESPAIR, RESOLUTION
# ------------------------------------------------------------

label orkney_after_confrontation:

    scene bg bedroom with fade
    show victor anxious_closed at left_side

    n "All is again silent, but the creature’s words ring in his ears."

    show victor anxious_open at left_side
    v "\"I will be with you on your wedding-night.\""

    show victor anxious_closed at left_side
    n "He burns to pursue the murderer of his peace and cast him into the sea, yet the opportunity is gone."

    show victor tired at left_side
    n "He paces his room, imagination conjuring a thousand images to torment him."

    # --- TRIVIA 6: about what Victor fears most (himself vs Elizabeth vs humanity) ---
    call trivia_6

    show victor panic_open at left_side
    v "When that hour comes, I shall die—and at once satisfy and extinguish his malice."

    show victor panic_closed at left_side
    n "The thought does not move him to fear; but when he thinks of Elizabeth, tears—his first in months—stream from his eyes."

    show victor neutral_open at left_side
    v "I will not fall before my enemy without a bitter struggle."

    show victor neutral_closed at left_side

    # At this point, Orkney section is complete; you can later jump to montage/minigame/etc.
    n "For now, the barren rock of Orkney still holds him between guilt and defiance, between the memory of one monster—and the promise of another."

    return


# ------------------------------------------------------------
# TRIVIA LABELS
# (All use pattern: wrong answer -> hearts-- and repeat question;
#  right answer -> correct_sfx and continue.)
# ------------------------------------------------------------

label trivia_1:
    # About his first experiment & remorse
    n "Victor reflects that his first creation left him with..."

    menu:
        "a) Pride in his scientific genius":
            call lose_heart
            jump trivia_1
        "b) Unparalleled barbarity that desolated his heart with remorse":
            play sound audio.correct_sfx
            n "He cannot forget that his first work brought only grief and guilt."
            return
        "c) A chance to impress the philosophers of Ingolstadt":
            call lose_heart
            jump trivia_1

label trivia_2:
    n "Whose promise is Victor now questioning as he works on the bride?"
    menu:
        "a) His own vow never to repeat the experiment":
            call lose_heart
            jump trivia_2
        "b) The creature’s promise to quit the neighbourhood of man, which the bride might refuse to share":
            play sound audio.correct_sfx
            n "The compact was made with one being only; the second has no such obligation."
            return
        "c) Elizabeth’s promise to wait for him in Geneva":
            call lose_heart
            jump trivia_2

label trivia_3:
    # About offspring / race of devils
    n "What future consequence most horrifies Victor as he imagines the pair together?"
    menu:
        "a) That they will live quietly in the new world, forgotten by all":
            call lose_heart
            jump trivia_3
        "b) That they will have children and propagate a race of devils upon the earth":
            play sound audio.correct_sfx
            n "He imagines future generations cursing him for unleashing such a race."
            return
        "c) That they will become celebrated curiosities in human society":
            call lose_heart
            jump trivia_3

label trivia_4:
    # About moral responsibility shift
    n "What changes in Victor’s understanding of his promise in this moment?"
    menu:
        "a) He realises the creature never truly meant his threats.":
            call lose_heart
            jump trivia_4
        "b) He sees for the first time that the wickedness lies in his own promise, not just in the creature’s demands.":
            play sound audio.correct_sfx
            n "He finally recognises that he himself may become the ‘pest’ of future ages."
            return
        "c) He believes that time will erase his guilt regardless of his actions.":
            call lose_heart
            jump trivia_4

label trivia_5:
    n "How does the creature now describe the power between creator and created?"
    menu:
        "a) Victor remains master, and the creature is his humble servant.":
            call lose_heart
            jump trivia_5
        "b) Victor is creator in name only; the creature now claims to be the true master through power to cause misery.":
            play sound audio.correct_sfx
            n "The creature insists he can make Victor so wretched that daylight will be hateful."
            return
        "c) They are equals who can reason calmly together.":
            call lose_heart
            jump trivia_5

label trivia_6:
    # About Victor's fear and Elizabeth
    n "When the creature promises to be with him on his wedding-night, what thought finally brings Victor to tears?"
    menu:
        "a) His own death, which he accepts almost calmly.":
            call lose_heart
            jump trivia_6
        "b) Elizabeth’s endless sorrow if she loses him so barbarously.":
            play sound audio.correct_sfx
            n "He weeps not for himself, but for the grief Elizabeth will endure."
            return
        "c) The possibility that the creature will forgive him.":
            call lose_heart
            jump trivia_6


# ------------------------------------------------------------
# GAME OVER (PANIC / GUILT DEATH ENDING)
# ------------------------------------------------------------

label game_over_panic:

    stop music
    stop ambient

    scene bg lab_night with fade
    show victor panic_open at left_side

    v "Why can I not remember? Why does my mind recoil from what I myself have done?"

    show victor panic_closed at left_side
    n "The strain of his reflections shatters what remains of his strength."

    scene black with fade
    n "On that barren rock, consumed by guilt and terror, Victor’s body finally yields where his conscience could not."

    # Simple game over screen
    call screen game_over_screen

    return


screen game_over_screen():
    modal True
    frame:
        align (0.5, 0.5)
        vbox:
            spacing 20
            text "GAME OVER" size 60 xalign 0.5
            text "Victor collapses under the weight of guilt and dread." xalign 0.5
            text "You have exhausted his strength." xalign 0.5

            textbutton "Return to Main Menu" action MainMenu() xalign 0.5
            textbutton "Restart Orkney Scene" action Start() xalign 0.5
