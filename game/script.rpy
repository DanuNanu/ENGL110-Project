# ------------------------------------------------------------
# CONFIG & VARIABLES
# ------------------------------------------------------------

# Optional: make text type out instead of instant (tweak or remove if you don't like it)
define config.default_text_cps = 30  # characters per second

# Characters
define v = Character("Victor", color="#e0d0ff")
define m = Character("Creature", color="#ffb0b0")
define n = Character("Narrator", color = "#ffffff")  # unnamed narrator (just text)



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
image bg lab_empty     = "images/backgrounds/bg_lab_empty.png"
image bg beach_escape = "images/backgrounds/bg_coastline_escape.png"
image bg rolling_hills = "images/backgrounds/bg_rolling_hills.png"
image bg swiss_cottages = "images/backgrounds/bg_sprawling_cottages.png"
image bg swiss_lakes = "images/backgrounds/bg_swiss_lake.png"
image bg stony_beach = "images/backgrounds/bg_stony_beach.png"
image white = Solid("#FFFFFF")


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

image creature grin            = "images/characters/monster/monster_grin.png"

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

define audio.wind         = "audio/wind_heavy.wav"
define audio.rain         = "audio/rain_heavy_outside.wav"
define audio.rain_inside  = "audio/rain_heavy_outside.wav"
define audio.thunder      = "audio/thunder.wav"
define audio.waves        = "audio/waves.mp3"
define audio.door_creak   = "audio/door_creek.mp3"
define audio.footsteps    = "audio/steps_heavy.mp3"
define audio.flesh_tear   = "audio/flesh_tear.mp3"
define audio.correct_sfx  = "audio/correct.mp3"
define audio.wrong_sfx    = "audio/wrong.mp3"
define audio.light_wind = "audio/wind_light.wav"

# NOTE: if you only want part of an sfx, you can:
# - trim it in an external audio editor, OR
# - lower the volume and stop it quickly using `queue` / `stop sound`.


# ------------------------------------------------------------
# TRANSFORMS (POSITION / SIZE)
# ------------------------------------------------------------

transform left_side:
    xalign 0.15
    yalign 1.0
    zoom 0.82          # scale to 90% size (adjust as you like)
    yoffset 100         # move downward (positive = down, negative = up)
    xoffset -150

transform right_side:
    xalign 0.85
    yalign 1.0
    zoom 0.70      # ← reduce size (adjust if needed)
    yoffset 30
    xzoom -1.0  
    xoffset 150

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
#-------audio control-------$
screen stop_waves_sfx():
    timer 1.8 action Stop("sound")

screen stop_heavy_wind_sfx():
    timer 1.8 action Stop("sound")

screen stop_light_wind_sfx():
    timer 1.9 action Stop("sound")

screen delay_sfx(delay_time1, delay_time2, sound_file):
    tag delay_sfx
    modal False
    timer delay_time1 action Play("sound",sound_file)
    timer delay_time2 action [Stop("sound"), Hide("delay_sfx")]

screen do_sfx(delay_time1, sound_file):
    tag do_sfx
    modal False
    $ renpy.music.set_volume(5, 0 ,"sound")
    timer 0.1 action Play("sound",sound_file)
    $ renpy.music.set_volume(5, 0 ,"sound")
    timer delay_time1 action [Stop("sound"), Hide("do_sfx")]


screen delay_music(delay_time1, delay_time2, sound_file):
    tag delay_music
    modal False
    timer delay_time1 action Play("music",sound_file, fadein = 1.0)
    timer delay_time2 action [Stop("music", fadeout = 1.8), Hide("delay_music")]


screen delay_music_no_fadein(delay_time1, delay_time2, sound_file):
    tag delay_music_fadein
    modal False
    timer delay_time1 action Play("music",sound_file, 1.0)
    timer delay_time2 action [Stop("music", fadeout = 1.0), Hide("delay_music_fadein")]
#-------------------------

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
    $ renpy.pause(2.0)
    stop music fadeout 1.0

    stop sound

    # Scene 1: Orkney establishing
    scene bg orkney_coast with fade
    #=======narattor expisiton=======================
    n "After being threatened by the Monster, Victor Frankenstein has sworn to fashion his creation a mate"
    n "To complete his work, he has come to the Orkney Islands, desolate and remote,far from Geneva, where the waves batter the coast and the wind never rests."
    n "Here upon this lonely shore, Victor means to resume the dreadful work he once began"
    #=========== victor speaking ====================
    show victor neutral_open at left_side
    v "I have finally traversed the northern highlands and fixed myself on one of the remortest parts of these Islands"
    show victor neutral_closed at left_side

    show victor neutral_open at left_side
    v "This place is well fitted my work being hardly more than a rock, whose sides are continually beaten upon by ....."
    show victor neutral_closed at left_side

    show victor neutral_open at left_side
    play sound audio.waves
    v ".....Waves"
    show screen stop_waves_sfx
    show victor neutral_closed at left_side 

    show victor anxious_open at left_side
    v "My abode was a miserable hut with only two rooms. The thatch had fallen in, the walls were unplastered, the door off its hinges."
    show victor tired at left_side

    show victor neutral_open at left_side
    v "I repaired what I could, bought a few pieces of wretched furniture, and took possesion of it."
    show victor neutral_closed at left_side

    show victor neutral_open at left_side
    v "The inhabitants here scarcely notice me. Their limbs are gaunt and scraggly from suffering"
    show victor neutral_closed at left_side

    show victor anxious_open at left_side
    v "Their misery has made them blunt to even the coarsest of sensations"
    show victor tired at left_side

    #---victor dailu routine-----#
    show victor neutral_open at left_side
    v "Initially, when I first arrived on this rock, I devoted my mornings to labour; but in the evenings, when the weather permitted, I--"

    scene bg stony_beach with fade
    show victor neutral_open at left_side
    show screen delay_music_no_fadein(0.3, 1.8, audio.waves)
    v "--walked on the stony beach of the sea to listen to the waves as they roared, and dashed at my feet"
    show victor tired at left_side

    show victor anxious_open at left_side
    v "Yet, even while I watched the monotonous ever-changing scene around me, my thoughts returned home back to Switzerland:"
    show victor tired at left_side
    #-----switzerland contrast: quick slide show monatage ----
    #Hills covered with vines scene
    scene bg rolling_hills with dissolve
    show victor anxious_open at left_side
    v "Hills covered with vines, rich and green, instead of naked rock"
    show victor tired at left_side
    # cottages scene
    scene bg swiss_cottages with dissolve
    show victor anxious_open at left_side
    v "Cottages scattered thickly over the plains, instead of this melancholic solitude."
    show victor tired at left_side
    #lakes and gentle sky
    scene bg swiss_lakes with dissolve
    play sound audio.light_wind 
    show victor anxious_open at left_side
    v "Fair lakes beneath a gentle sky, whose tumultous winds play like a lively infant--"
    show screen stop_light_wind_sfx
    $ renpy.pause(1.8)
    $renpy.pause(0.4)
    scene bg stony_beach with dissolve
    show screen delay_music(0.3,2.0, audio.wind)
    show victor angry_open at left_side
    v "---compared to roarings of the giant ocean of this appaling landscape"
    show victor angry_closed at left_side
    $renpy.pause(0.4)
    scene bg orkney_coast with fade
    show victor anxious_open at  left_side
    v "But as I proceeded, my work became each day more horrible and irksome to me"
    show victor anxious_closed at left_side
    $renpy.pause(0.4)
    show victor anxious_open at left_side
    v "Sometimes I could not prevail myself to enter my lab for several days"
    show victor tired at left_side
    $renpy.pause(0.4)
    scene bg lab_night with fade
    show victor anxious_open at left_side
    v "At other times I toiled day and night, eager to complete the task"
    show victor tired at left_side
    $renpy.pause(0.4)
    scene bg orkney_coast with dissolve
    show victor anxious_open at left_side
    v "During my first experiment, an enthusiatic frenzy had blinded me to the horror of my employment"
    show victor tired at left_side
    $renpy.pause(0.4)
    show victor anxious_open at left_side
    v "But now, my heart often sickened at the work of my hands."
    show victor tired at left_side
    $renpy.pause(0.4)
    show victor anxious_open at left_side
    v "Yet, in the midst of all this, my labour is considerably advanced"
    show victor tired at left_side
    $renpy.pause(0.4)
    show victor anxious_open at left_side
    v "I look towards its completion with a tremulous and eager hope I scarcely dare examine"
    show victor tired at left_side


    # Move into lab scene (evening)
    jump orkney_lab_evening


# ------------------------------------------------------------
# ORKNEY LAB – EVENING REFLECTION + TRIVIA
# ------------------------------------------------------------

label orkney_lab_evening:

    stop music fadeout 1.0
    play ambient audio.rain_inside
    scene black with fade
    n "Some time later..."
    n "Victor's labour continues into the evening as the sun starts to set"

    scene bg lab_night with fade

    show victor tired at left_side
    v "The sun has set and he moon is rising from the sea."
    v "I have not sufficient light for my employment"
    $renpy.pause(0.4)

    show victor neutral_open at left_side
    v "Should I abandon my labour for the night... or hasten its completion through unremetting attention?"
    show victor neutral_closed at left_side

    $renpy.pause(0.4)

    show victor neutral_open at left_side
    v "Three years ago I was engaged in the same manner"
    show victor neutral_closed at left_side

    $renpy.pause(0.4)

    n "A question arises"

    call trivia_1 from _call_trivia_1

    $renpy.pause(0.4)

    show victor anxious_open at left_side
    v "I created a fiend whose barbarity has desolated my heart, and filled it with the bitterest remorse."
    show victor tired at left_side

    $renpy.pause(0.4)

    show victor anxious_open at left_side
    v "And now I am about to form another being, of whose dispositions I was alike ignorant"
    show victor tired at left_side

    $renpy.pause(0.4)

    show victor anxious_closed at left_side
    v "!!!"
    n "Victor makes a horrible realisation that causes him to reconsider his promise"
    call trivia_2 from _call_trivia_2

    $renpy.pause(0.4)

    show victor anxious_open at left_side
    v "They might even hate each other"
    show victor anxious_closed at left_side
    $renpy.pause(0.4)

    show victor anxious_open at left_side
    v "The creature already loathes his own deformity, so might he not recoil more when he sees this abhorence in the female form?"
    $renpy.pause(0.4)

    show victor anxious_open at left_side
    v "She might turn from him in favour of the superior beauty of mankind"
    show victor tired at left_side
    $renpy.pause(0.4)

    show victor angry_closed at left_side
    v "...."
    n "Victor makes another realization"

    $renpy.pause(0.4)

    show victor anxious_open at left_side
    v "He would be alone again, exasperated by being deserted by one of his own species"
    show victor anxious_closed at left_side

    $renpy.pause(0.4)

    show victor angry_open at left_side
    v "Even if they were to leave Europe and inhabit the deserts of the new world---"
    v "--one of the first results of those sympathies for which the daemon thisted would be..."
    n "Incoming question:"
    call trivia_3 from _call_trivia_3 #change trivia to ask what would be thirsted and why he fear it
    $renpy.pause(0.4)
    v "Such thirst would lead to the propogation of a race of devils, who might make the very existence of the species of man--"
    v "--a condition precarious and full of terror"

    show victor angry_open at left_side
    v "Have I the right, for my own benefit, to inflict this curse upon everlasting generations?"
    show victor angry_closed at left_side

    $renpy.pause(0.4)

    show victor anxious_open at left_side
    v "I have been struck senseless by his fiendish threats--"
    v "--but now, for the first time the wickedness of my promise bursts upon me"
    show victor angry_closed at left_side
    $renpy.pause(0.4)
    show victor anxious_closed at left_side
    n "Victor shudders to imagine future ages cursing him as their pest"
    call trivia_4 from _call_trivia_4
    scene black 
    play music "audio/rain_heavy_outside.wav"
    $ renpy.music.set_volume(0.4, 0 ,"music")

    $renpy.pause(0.5)
    show screen do_sfx(0.8, audio.thunder)
    scene black
    show white
    $renpy.pause(0.1)
    hide white 
    $renpy.pause(0.3)
    scene black
    show white 
    $renpy.pause(0.1)
    hide white
    $renpy.pause(0.8)
    show screen do_sfx(0.8, audio.thunder)
    n "SUDDENLY!"
    #---- thunder next part then jump to windo-----$
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
    scene bg lab_empty with fade
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
    call trivia_5 from _call_trivia_5

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
    call trivia_6 from _call_trivia_6

    show victor panic_open at left_side
    v "When that hour comes, I shall die—and at once satisfy and extinguish his malice."

    show victor panic_closed at left_side
    n "The thought does not move him to fear; but when he thinks of Elizabeth, tears—his first in months—stream from his eyes."

    show victor neutral_open at left_side
    v "I will not fall before my enemy without a bitter struggle."

    show victor neutral_closed at left_side

    # At this point, Orkney section is complete; you can later jump to montage/minigame/etc.
    n "For now, the barren rock of Orkney still holds him between guilt and defiance, between the memory of one monster—and the promise of another."

    #need better transition to minigame fro now dummy transition is fine
    if hearts > 0:
        jump arctic_chase_entry
    else:
        # If somehow he reached this with 0 hearts, just go to game over or skip
        jump some_game_over
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
            call lose_heart from _call_lose_heart
            jump trivia_1
        "b) Unparalleled barbarity that desolated his heart with remorse":
            play sound audio.correct_sfx
            n "Correct! He cannot forget that his first work brought only grief and guilt."
            return
        "c) A chance to impress the philosophers of Ingolstadt":
            call lose_heart from _call_lose_heart_1
            jump trivia_1

label trivia_2:
    n "What could be the horrible realisation that causes Victor to reconsider his promose?"
    menu:
        "a) He does not have the finances or resources to make the monster a bride":
            call lose_heart from _call_lose_heart_2
            jump trivia_2
        "b) The creature had promised to quit the neighbourhood of man, but the bride had not":
            play sound audio.correct_sfx
            n "Thats right!, Victor is terrified of the unknown dispositons of the bride he is creating:"
            n "The bride, who in all probability, was to become a thinking and reasoning animal might refuse to comply with a compact--"
            n "--made before her creation. She could, infact, become ten thousand times more malignant than her mate and revel in murder and wretchedness"
            return
        "c) He did not swear on a bible when promising the monster a bride. As a result, the promise is null and void":
            call lose_heart from _call_lose_heart_3
            jump trivia_2

label trivia_3:
    # About offspring / race of devils
    n "Which sympathy that Creature yearn for horrifies Victor?"
    menu:
        "a) The Monster thirsts for sympathy from Victor, this horrifies Victor as he does not want to pay child support for his creation":
            call lose_heart from _call_lose_heart_4
            jump trivia_3
        "b) The monster yearns for children.":
            play sound audio.correct_sfx
            n "Thats correct! This horrifies Victor he believes thirst for such sympathies will result in a propogating a race of devils upon the Earth"
            return
        "c) The monster yearns for sympathy and empathy from humankind because he wants to feel a sense of belonging to battle his depressing solitude":
            call lose_heart from _call_lose_heart_5
            jump trivia_3

label trivia_4:
    # About moral responsibility shift
    n "Why does Victor imagine future ages cursing at him?"
    menu:
        "a) Because Victor did not share the knowledge of reanimation and potentially immortality with the world":
            call lose_heart from _call_lose_heart_6
            jump trivia_4
        "b) Victor realises the opportunity cost of creating the bride for the sake of his innerpeace could mean the potential downfall of humanity as a result.":
            play sound audio.correct_sfx
            n "Thats correct! The afformentioed reasons, by Victor, make it clear that risk posed by creating another Monster are too great to ignore"
            return
        "c) Because the act of reanimation is a cardinal sin for which he will never be forgiven throughout eternity":
            call lose_heart from _call_lose_heart_7
            jump trivia_4

label trivia_5:
    n "How does the creature now describe the power between creator and created?"
    menu:
        "a) Victor remains master, and the creature is his humble servant.":
            call lose_heart from _call_lose_heart_8
            jump trivia_5
        "b) Victor is creator in name only; the creature now claims to be the true master through power to cause misery.":
            play sound audio.correct_sfx
            n "The creature insists he can make Victor so wretched that daylight will be hateful."
            return
        "c) They are equals who can reason calmly together.":
            call lose_heart from _call_lose_heart_9
            jump trivia_5

label trivia_6:
    # About Victor's fear and Elizabeth
    n "When the creature promises to be with him on his wedding-night, what thought finally brings Victor to tears?"
    menu:
        "a) His own death, which he accepts almost calmly.":
            call lose_heart from _call_lose_heart_10
            jump trivia_6
        "b) Elizabeth’s endless sorrow if she loses him so barbarously.":
            play sound audio.correct_sfx
            n "He weeps not for himself, but for the grief Elizabeth will endure."
            return
        "c) The possibility that the creature will forgive him.":
            call lose_heart from _call_lose_heart_11
            jump trivia_6

# ------------------------------------------------------------
# ARCTIC CHASE MINIGAME – IMAGES
# ------------------------------------------------------------

# Backgrounds (1920x1080)
image bg_chase_day   = "minigame/ice_background_day.png"
image bg_chase_night = "minigame/ice_background_night.png"

# Obstacles
image obs_stalagmite = "minigame/stalagmite.png"    # jump over
image obs_bird       = "minigame/bird.png"          # duck under

# Runner sprites
image runner_victor  = "minigame/victor_idle.png"
image victor_duck    = "minigame/victor_duck.png"

image runner_monster = "minigame/monster_idle.png"
image monster_duck   = "minigame/monster_duck.png"

# ------------------------------------------------------------
# ARCTIC CHASE – VARIABLES
# ------------------------------------------------------------

# State
default chase_state        = "idle"      # idle, ready, running, pause, dead, success
default chase_elapsed      = 0.0         # time survived (seconds)
default chase_duration     = 40.0        # how long Victor must survive
default chase_internal_timer = 0.0

# Speed & difficulty
default chase_base_speed   = 600.0       # px/sec
default chase_speed        = 600.0
default chase_speed_scale  = 1.0         # grows over time

# Background scroll
default chase_bg_x1        = 0.0
default chase_bg_x2        = 1920.0
default chase_day          = True
default chase_day_timer    = 0.0         # day/night switches every 30s

# Ground position (feet)
default chase_ground_y     = config.screen_height-40

# Victor (player)
default victor_x           = 260
default victor_y           = 860
default victor_vy          = 0.0
default victor_on_ground   = True
default victor_duck        = False

# Monster (AI "perfect" follower)
default monster_x          = 760
default monster_y          = 860
default monster_vy         = 0.0
default monster_on_ground  = True
default monster_duck       = False

# Obstacles: list of dicts {x, y, kind, w, h}
default chase_obstacles    = []

# Obstacle spawn control
default chase_time_since_spawn = 0.0
default chase_spawn_min        = 0.9
default chase_spawn_max        = 1.6
default chase_bool_change_check = False
default chase_monster_gap = 400

# Add this code block to your image definitions section
#image arctic_chase_bg_day:
    # Use the images you defined
    #"bg_chase_day" xpos chase_bg_x1 ypos 0
    #"bg_chase_day" xpos chase_bg_x2 ypos 0

#image arctic_chase_bg_night:
    #"bg_chase_night" xpos chase_bg_x1 ypos 0
    #"bg_chase_night" xpos chase_bg_x2 ypos 0

# Safe “no obstacles” start time
define chase_safe_start_time = 0.5   # first 5s with no obstacles


# ------------------------------------------------------------
# PYTHON HELPERS
# ------------------------------------------------------------

init python:
    import random

    def _rects_overlap(ax, ay, aw, ah, bx, by, bw, bh):
        return (ax < bx + bw and ax + aw > bx and
                ay < by + bh and ay + ah > by)

    def reset_chase_variables():
        """
        Reset all runtime state for a fresh run.
        """
        global chase_state, chase_elapsed, chase_internal_timer
        global chase_speed, chase_speed_scale
        global chase_bg_x1, chase_bg_x2, chase_day, chase_day_timer
        global victor_y, victor_vy, victor_on_ground, victor_duck
        global monster_y, monster_vy, monster_on_ground, monster_duck
        global chase_obstacles, chase_time_since_spawn, chase_bool_change_check

        chase_state          = "ready"
        chase_elapsed        = 0.0
        chase_internal_timer = 0.0

        chase_speed          = chase_base_speed
        chase_speed_scale    = 1.0

        chase_bg_x1          = 0.0
        chase_bg_x2          = 1920.0
        chase_day            = True
        chase_day_timer      = 0.0

        victor_y             = store.chase_ground_y
        victor_vy            = 0.0
        victor_on_ground     = True
        victor_duck          = False

        monster_y            = store.chase_ground_y
        monster_vy           = 0.0
        monster_on_ground    = True
        monster_duck         = False

        chase_obstacles      = []
        chase_time_since_spawn = 0.0
        chase_bool_change_check = False

    def chase_start_running():
        """
        Start or resume the chase when SPACE is pressed in 'ready' or 'pause'.
        """
        global chase_state
        if chase_state in ("ready", "pause"):
            chase_state = "running"
        return 

    def chase_jump():
        """
        Victor's jump – smooth arc, only if on ground & running.
        """
        global victor_on_ground, victor_vy, victor_duck
        if store.chase_state != "running":
            return
        if victor_on_ground:
            victor_on_ground = False
            victor_duck = False
            victor_vy = -1280.0  # upward velocity

    def chase_duck_toggle():
        """
        Toggle duck on/off when DOWN or S is pressed.
        (Simpler than key-up handling.)
        """
        global victor_duck
        if store.chase_state != "running":
            return
        if store.victor_on_ground:
            victor_duck = not victor_duck

    def _spawn_obstacle():
        """
        Spawn either a stalagmite (jump) or bird (duck), ensuring
        no impossible overlapping combo.
        """
        kind = random.choice(["stalagmite", "bird"])
        if len(store.chase_obstacles) >= 2:
            last1 = store.chase_obstacles[-1]["kind"]
            last2 = store.chase_obstacles[-2]["kind"]
            if last1 == last2 == kind:
                kind = "bird" if kind == "stalagmite" else "stalagmite"

        x = config.screen_width + 200

        # Basic sizing/position
        if kind == "stalagmite":
            y = store.chase_ground_y - 128
            w, h = 128, 128
        else:
            y = store.chase_ground_y - 260   # overhead bird
            w, h = 160, 80

        # Fairness: don't stack a new obstacle too close to the last one
        if store.chase_obstacles:
            last = store.chase_obstacles[-1]
            # If too close horizontally, skip this spawn
            if x - last["x"] < 450:
                return

            # Prevent impossible "bird + stalagmite" at nearly same x
            if last["kind"] != kind and x - last["x"] < 600:
                return

        store.chase_obstacles.append({"x": x, "y": y, "kind": kind, "w": w, "h": h})

    def _update_victor(dt):
        """
        Smooth jump physics for Victor.
        Feet remain anchored using yanchor 1.0 in rendering.
        """
        g = 2850.0  # gravity

        # If airborne, apply gravity and update height
        if not store.victor_on_ground:
            store.victor_vy += g * dt
            store.victor_y  += int(store.victor_vy * dt)
            store.victor_x = int(store.victor_x+ 0.55)

            # Jump ceiling (feet upper limit)
            max_jump_feet = store.chase_ground_y - 170
            if store.victor_y < max_jump_feet:
                store.victor_y = max_jump_feet
                # do NOT zero vy here, keep arc smooth

            # Landing
            if store.victor_y >= store.chase_ground_y:
                store.victor_y = store.chase_ground_y
                store.victor_vy = 0.0
                store.victor_on_ground = True

    def _update_monster(dt, speed):
        """
        Very simple AI so the monster always dodges perfectly.
        """
        g = 2850

        # Look ahead for the nearest obstacle in front of the monster
        lookahead = None
        for obs in store.chase_obstacles:
            if obs["x"] > store.monster_x:
                if lookahead is None or obs["x"] < lookahead["x"]:
                    lookahead = obs

        # Decide actions
        if lookahead:
            dist = lookahead["x"] - store.monster_x
            if lookahead["kind"] == "stalagmite":
                # Jump a bit before hitting the stalagmite
                if dist < 260 and store.monster_on_ground:
                    store.monster_on_ground = False
                    store.monster_duck = False
                    store.monster_vy = -1280
                else:
                    store.monster_duck = False
            else:
                # Bird: duck when close
                if dist < 260:
                    store.monster_duck = True
                else:
                    store.monster_duck = False
        else:
            store.monster_duck = False

        # Apply jump physics
        if not store.monster_on_ground:
            store.monster_vy += g * dt
            store.monster_y  += int(store.monster_vy * dt)
            store.monster_x = int(store.monster_x + 0.35)

            max_jump_feet = store.chase_ground_y - 170
            if store.monster_y < max_jump_feet:
                store.monster_y = max_jump_feet

            if store.monster_y >= store.chase_ground_y:
                store.monster_y = store.chase_ground_y
                store.monster_vy = 0.0
                store.monster_on_ground = True

    def chase_update():
        renpy.notify("UPDATE FIRING")

        """
        Main game loop – called ~60fps by the screen timer.
        """
        dt = 0.016

        if store.chase_state != "running":
            return

        # ----- Timers -----
        store.chase_elapsed        += dt
        store.chase_internal_timer += dt
        store.chase_day_timer      += dt

        # ----- Day/night cycle (every 30 seconds) -----
        if store.chase_day_timer >= 20.0:
            store.chase_day = not store.chase_day
            store.chase_day_timer = 0.0
            store.chase_bool_change_check = True

        # ----- Speed scaling -----
        store.chase_speed_scale = 1.0 + 0.016 * store.chase_elapsed
        store.chase_speed  = store.chase_base_speed * store.chase_speed_scale
        speed = store.chase_speed

        # ----- Background scrolling -----
        store.chase_bg_x1 -= speed * dt
        store.chase_bg_x2 -= speed * dt

        if store.chase_bg_x1 <= -1920:
            store.chase_bg_x1 += 3840
        if store.chase_bg_x2 <= -1920:
            store.chase_bg_x2 += 3840

        # ----- Victory condition -----
        if store.chase_elapsed >= store.chase_duration:
            store.chase_state = "success"
            return

        # ----- Obstacle spawning (after safe start period) -----
        store.chase_time_since_spawn += dt
        if store.chase_elapsed > chase_safe_start_time:
            min_gap= max(0.46, 0.92/ store.chase_speed_scale)
            max_gap = max(0.68, 1.32 / store.chase_speed_scale)
            gap = random.uniform(min_gap, max_gap)
            if store.chase_time_since_spawn >= gap:
                _spawn_obstacle()
                store.chase_time_since_spawn = 0.0

        # ----- Move obstacles -----
        for obs in store.chase_obstacles:
            obs["x"] -= speed * dt
        store.chase_obstacles = [o for o in store.chase_obstacles if o["x"] > -300]

        # ----- Update Victor physics -----
        _update_victor(dt)

        # ----- Update Monster AI -----
        _update_monster(dt, speed)

        # ----- Collision for Victor only -----
        victor_w = 94
        victor_h = 186
        vx = store.victor_x

        # Bounding box depends on jump / duck
        if not store.victor_on_ground:
            vy = store.victor_y - victor_h * 0.6
            vh = victor_h * 0.6
        elif store.victor_duck:
            vy = store.victor_y - victor_h * 0.45
            vh = victor_h * 0.45
        else:
            vy = store.victor_y - victor_h
            vh = victor_h

        for obs in store.chase_obstacles:
            ox, oy, ow, oh = obs["x"], obs["y"], obs["w"], obs["h"]
            if _rects_overlap(vx, vy, victor_w, vh, ox, oy, ow, oh):

                # Lose a heart and pause
                store.hearts -= 1
                store.chase_state = "pause"

                # Reset Victor & monster safely
                store.victor_y = store.chase_ground_y
                store.victor_vy = 0.0
                store.victor_on_ground = True
                store.victor_duck = False

                store.monster_y = store.chase_ground_y
                store.monster_vy = 0.0
                store.monster_on_ground = True
                store.monster_duck = False

                # Clear obstacles so no instant-death
                store.chase_obstacles = []
                store.chase_time_since_spawn = 0.0

                # If no hearts left → dead
                if store.hearts <= 0:
                    store.chase_state = "dead"

                return
# ------------------------------------------------------------
# ARCTIC CHASE – START MENU SCREEN
# (Shown after Orkney, before actual gameplay)
# ------------------------------------------------------------

screen chase_start_menu():
    tag chase_menu
    modal True
    add "bg_chase_day"

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40, 40, 40)

        vbox:
            spacing 20
            text "Arctic Chase" size 60 xalign 0.5
            text "Victor pursues the Creature across the ice." size 30 xalign 0.5
            text "Survive until the timer runs out." size 24 xalign 0.5

            textbutton "Start Minigame" action Return("start") xalign 0.5
            textbutton "Quit to Main Menu" action MainMenu() xalign 0.5


# ------------------------------------------------------------
# ARCTIC CHASE – GAME SCREEN
# ------------------------------------------------------------

# ------------------------------------------------------------
# ARCTIC CHASE – GAME SCREEN (CORRECTED)
# ------------------------------------------------------------

# ------------------------------------------------------------
# ARCTIC CHASE – GAME SCREEN (FINAL CORRECTED)
# ------------------------------------------------------------

screen chase_game():
    tag chase_game
    modal True
    add Solid("#0000")
    # --- DAY/NIGHT TRANSITION (Controls the Master Layer) ---
    # This must be run on every frame update (the timer handles the update check)
    # --- 1. DAY/NIGHT TRANSITION (Controls the Master Layer) ---
    # FIX: Use Function(renpy.show) to execute the show command on the master layer
    # The 'as chase_bg' tag is important for Ren'Py to manage the transition smoothly.
    on "show":
        if chase_day:
            action Function(renpy.show, "bg_chase_day", tag="chase_bg", layer="master")
        else:
            action Function(renpy.show, "bg_chase_night", tag="chase_bg", layer="master")
    
    on "replace":
        if chase_day:
            action Function(renpy.show, "bg_chase_day", tag="chase_bg", layer="master")
        else:
            action Function(renpy.show, "bg_chase_night", tag="chase_bg", layer="master")
    # --- The screen's job is now only to draw the movable elements (sprites, HUD, obstacles) ---
    if chase_bool_change_check:
        on "replace" action With(dissolve)
        $ chase_bool_change_check = False

    if chase_day:
        add "bg_chase_day"
    else:
        add "bg_chase_night"
    


    # ===== GAME LOOP & UPDATE (Timer logic unchanged from last fix) =====
    timer 0.016 repeat True action If(
        chase_state == "running",
        [
            Function(chase_update),
            SetVariable("chase_internal_timer", chase_internal_timer),
            Function(renpy.restart_interaction)
        ]
    )

    # === BACKGROUND RENDERING (updates every frame) ===
    

    # ===== INPUT HANDLER (Consolidated) =====
    if chase_state == "running":
        key "K_SPACE" action Function(chase_jump)
        key "K_UP"    action Function(chase_jump)
        key "K_DOWN" action Function(chase_duck_toggle)
        key "K_s"    action Function(chase_duck_toggle)

    if chase_state in ("ready", "pause"):
        key "K_SPACE" action Function(chase_start_running)

    key "K_ESCAPE" action MainMenu()


    # ===== OBSTACLES (Corrected Positioning) =====
    for obs in chase_obstacles:
        #text "OBS!" xpos monster_x ypos obs["y"] color "#FF0000"
        #text "TYPE=[type(obs['y'])]" xpos 0.5 ypos 0.25 color "#FF0000"
        #ext "VAL=[obs['y']]" xpos 0.5 ypos 0.30 color "#FF0000"
        if obs["kind"] == "stalagmite":
            #nchor the bottom (1.0) to the ground line (chase_ground_y)
            add "obs_stalagmite" xpos int(obs["x"]) yanchor 1.0 ypos chase_ground_y 
        else:
            #Birds use their calculated top position (obs["y"])
            add "obs_bird" xpos int(obs["x"]) ypos obs["y"] 
    

    # ===== MONSTER (AI) =====
    if not victor_on_ground:
        add "runner_monster" xpos monster_x yanchor 1.0 ypos int(monster_y)
    elif victor_duck:
        add "monster_duck" xpos monster_x yanchor 1.0 ypos int(monster_y)
    else:
        add "runner_monster" xpos monster_x yanchor 1.0 ypos int(monster_y)

    # ----- Victor -----
    if not victor_on_ground:
        add "runner_victor" xpos victor_x yanchor 1.0 ypos int(victor_y)
    elif victor_duck:
        add "victor_duck" xpos victor_x yanchor 1.0 ypos int(victor_y)
    else:
        add "runner_victor" xpos victor_x yanchor 1.0 ypos int(victor_y)

    # ===== HUD ELEMENTS & MESSAGES (Rest of the screen is fine) =====
    # ... (Your HUD and Message frames go here) ...
    frame:
        xalign 0.02
        yalign 0.03
        background None
        hbox:
            spacing 6
            text "Hearts: [hearts]" size 28
    
    frame:
        xalign 0.98
        yalign 0.03
        background None
        $ remaining = max(0.0, chase_duration - chase_elapsed)
        text ("Time: [remaining:.2f]") size 28 xalign 1.0

    if chase_state == "ready":
        frame:
            xalign 0.5
            yalign 0.2
            background "#0008"
            padding (20,20,20,20)
            text "Press SPACE to begin the chase." size 36

    elif chase_state == "pause" and hearts > 0:
        frame:
            xalign 0.5
            yalign 0.2
            background "#0008"
            padding (20,20,20,20)
            text "You stumble on the ice. Press SPACE to continue." size 32

    elif chase_state == "dead":
        frame:
            xalign 0.5
            yalign 0.2
            background "#0008"
            padding (20,20,20,20)
            text "Victor collapses from exhaustion on the ice..." size 32

    # ===== RETURN ENDING (Exit the screen) =====
    if chase_state in ("success", "dead"):
        timer 0.1 action Return(chase_state)
# ------------------------------------------------------------
# ENTRY POINT FROM ORKNEY STORY
# (Call this once Orkney dialogue is done & hearts > 0)
# ------------------------------------------------------------

label arctic_chase_entry:
    # Simple start menu (Start / Quit)
    window hide
    $ choice = renpy.call_screen("chase_start_menu")
    if choice != "start":
        return
    # Reset state for new run
    $ reset_chase_variables()
    # FIX: Show the dynamic background on the master layer. This replaces 'scene black'.
    # Show minigame and wait until it returns "success" or "dead"
    $ result = renpy.call_screen("chase_game")

    # FIX: Clean up the dynamic background layer after the game is over.

    if result == "dead":
        # Hearts have hit zero → exhaustion ending
        jump arctic_chase_exhaustion
    else:
        # Survived full timer → continue to montage (you can replace this)
        jump arctic_chase_montage

# ------------------------------------------------------------
# EXHAUSTION / GAME OVER ENDING FROM CHASE
# ------------------------------------------------------------

label arctic_chase_exhaustion:
    window show
    scene black with fade
    n "On the desolate Arctic ice, Victor’s strength finally fails."
    n "The endless pursuit, the cold, and his own relentless guilt drain the last of his will."
    n "He collapses, the form of his enemy vanishing into the white distance."

    call screen game_over_screen
    return


# ------------------------------------------------------------
# SUCCESS ENDING (PLACEHOLDER – YOUR MONTAGE GOES HERE)
# ------------------------------------------------------------

label arctic_chase_montage:
    window show
    scene black with fade
    n "Victor staggers onward, refusing to yield. The fiend remains always a little ahead, a shadow taunting him across the endless ice."
    n "Days blur into nights; the chase becomes his whole world."

    # TODO: Replace this with your actual montage / final scenes.
    # For now, just go to your generic game-over / ending screen:
    call screen game_over_screen
    return





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