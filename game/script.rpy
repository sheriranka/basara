#CHARACTERS

#PENDING change colors later
define b = Character("Basara", color="#c9443a")
define m = Character('Me', color="#67b870")
define c = Character('Waitress', color="#FFFFFF")
define i = Character('Shop Owner', color="#FFFFFF")


#PENDING EDIT THIS LATER

# The game starts here.

label start:

#game script starts here

 #first option

 scene blackscreen
 play sound "audio/knock.mp3"


 menu:

  "Good morning, Basara!":
   jump morningChoice

  "Good evening, Basara":
   jump nightChoice


 label morningChoice:


 #morning start script
 
 #PENDING nature sounds play here
 #PENDING akusho background
 #PENDING display door to basara's room

  menu:
   "Basara, are you here?":
    jump c1Morning
   
   "Basara, I'm here!":
    jump c2Morning


 label c1Morning:

  scene bedmorningsleep
  with dissolve

  b "....hrgnnn.......zzzzz....."
  m "(aw, he's asleep)"

  scene bedmorningguitar
  with dissolve

  show standconfused
  with dissolve

  b "zzzhk...? Huh? uh.... Hey, You? What are you doing here?"
  m "We had plans to hang out today, remember?"
  b "Uh.... Did we? What time is it? I finally fell asleep..."
  m "It's past 11am!"

  show standannoyed

  b "*groans* Alright just... *yawn* let's get some coffee..."

  jump morningDateChoice


 label c2Morning:

 scene bedmorningplay
 with dissolve
 
 play sound "audio/strum.mp3"

 b "....."
 m "Helloooo, Basaraaaa?"
 b "....."
 m "Basara!"
 b "I hear you. Give me a minute."
 m "(oops, i think i made him mad.)"

 scene bedmorning
 with dissolve

 show guitarannoyed
 with dissolve

 m "We were going to hang out, remember?"

 show guitarsideeye

 b "aahhhnn.... Did we? I dont remember... Whatever, I'm stuck anyway. Let's go out."

 jump morningDateChoice



 label morningDateChoice:

 scene outsidemorning
 pause 3.0


  menu:
   "Let's go out to a cafe":
    jump cafeMorning
   "Let's go out to to lunch":
    jump lunchMorning

 label cafeMorning:

  scene cafewindow
  with dissolve
 
 #PENDING bgm is "bitches blue" from galaxy network chart 1-

  c "What can I get for you?"
  menu: 
   "Order for yourself":
    jump orderMorning
   
   "Order for Basara":
    jump orderBasaraMorning

 label orderMorning:

  $ bigParfait = True

  m "I'll have the vanilla soda float."
  c "Understood."
  b "I'll have the chocolate unicorn frappe with the rainbow sprinkles."
  c ".... Understood."

  jump orderArrived

 label orderBasaraMorning:

  $ bigParfait = False
  m "He'll have the orange soda float, and I'll have the vanilla."
  c "Understood."
  
  scene cafewindowannoyed
  with dissolve

  b "Hey."
  m "Hehe, should have paid more attention to your surroundings."
  
  jump orderArrived



 label orderArrived:

  scene cafesitsmile
  with dissolve
  
  if bigParfait: 
  
   show frappefull
   with dissolve
   
   m "Woah! Huge!"
   b "....What? ... You want some?"
  else:
   m "nice(CHANGE EDIT)"
   show orangefull
   with dissolve

  b "..."
  m "(He's poking at it...)"
  m "Mine is so good! How's yours?"
  b "..."
  b "..."
  b ".... Not bad."
  m "You dont seem so impressed, though."
  b "What do you want me to say?"
  m "Maybe something like...."
 
  menu:

   "This is totally FIRE!":
    jump faiyaa
   "This is totally BOMBER!":
    jump bombaa

  scene cafesitannoyed
  with dissolve
  
  if bigParfait:
   show frappefull
  else:
   show orangefull
  
  
 label faiyaa:
 
  b "Gimme a break."
  jump cafeMorningNext

 label bombaa:
 
  b "You think you're being funny, huh?"
  jump cafeMorningNext
  
 label cafeMorningNext:

 if bigParfait:
  hide frappefull
  show frappehalf
 else:
  hide orangefull
  show orangehalf
 
  b "Lemme pick out the next place after this."
  m "You have any ideas?"
  b "Yeah."
  m "..."
  m "..."
  b "..."
  b "..."
  b "..."
  b "...What are you looking at?"
  
  menu:
   "You!":
    b "Heh, you're so weird."
  
  if bigParfait:
   hide frappehalf
   with dissolve
   show frappeempty
   with dissolve
  else:
   hide orangehalf
   with dissolve
   show orangeempty
   with dissolve

  b "I'm leaving."
  m "Hey, wait I have to pay!"
  b "Meet me outside."

  scene cafe
  with dissolve
  
  if bigParfait:
   show frappeempty
  else:
   show orangeempty
  
  m "I hope he doesn't get distracted and run off...."
  
  scene outsidemorning
  with dissolve
  
 #NO MUSIC
 #BIRD SFX
 
  show standnormal
  with dissolve
  
  m "So where did you want to go?"
  b "Over here. I saw it while Ray was driving the other day and wanted to check it out. Come on."

  hide standnormal
  with dissolve
  
  m "Wait for me!"
  
  show standsmile
  with dissolve
 
  b "Here it is."
  b "I knew I read the sign right.  Come on, let's go in."
  
  hide standsmile
  with dissolve
 
  m "(Basara is so excited....!)"
  
  scene instrumens
 #PENDING bgm: "galaxy" from galaxy network chart 1. muffle it, like it's coming from overhead off the stores radio)
 
  show standsideeye
  with dissolve
  
  hide standsideeye
  with dissolve
 
  m "Hm... "
  m "There are some instruments on display."
  m "What is Basara looking at? Is it the..."
  
  menu:

   "The didgeridoo?":
    jump didgeridoo
  
   "The castanets?":
    jump castanets
  
   "Something else?":
    jump erhu


 label didgeridoo:

  m "Basara, this didgeridoo is pretty cool. "
  b "Mn. Not really my style though...."
  m "(What is he looking at...)"
  jump instrument
  
 label castanets:
  m "Hehe, Basara, are you looking at those vintage castanets?"
  b "Heh. Maybe Gubaba could play them."
  b "Nah, something else."
  jump instrument

 label erhu:
 
  #PENDING cg of basara looking at erhu
  scene pending
  
  jump instrument

 label instrument:
 
  m "What did you find?"
  b "This."
  
 #PENDING sprite of basara holding erhu very interested happy flourishing in his lane relaxed 
 
  b "Huh... two strings... and a bow. So I guess it's played like that huh... Hm."
  b "Is there somewhere I can.......... Oh, over there!"

  scene pending
 #PENDING CG of basara sitting down with the instrument. bgm fades out and becomes silent-

  b "..."
  b "..."
  b "..."
  m "(Wow, he's so absorbed in it...)"
  b "I think... something like this?"
  
 #PENDING sound byte of instrument from here (https://www.youtube.com/watch?v=EoMxBTUMT-k Grab a sound bite from here?)
 
  m "Wow... that's--"
  b "Fire."
  
  scene instrumens
  show standnormal
 
  b ".... *sigh*"
  m "It's really nice."
  m "Are you going to buy it?"
  b "..."
  b "..."
  b "..."
  m "Basara? You hearing me?"
  
  #show standsmirk
  
  b "Mn. Hey, you behind the counter! I'll be taking this!"
  i "Hey, dont forget to pay!"
  b "Send the bill to Ray Lovelock in Akusho! See ya!"
  
  hide standnormal
  hide standsmirk
  with dissolve
  
 #PENDING door rattle ding-a-ling sfx?
 
  m "Wow! He left, just like that!"
  m "Hey, wait for me Basara!"
  
 #PENDING door rattle ding-a-ling sfx?
 
  i "Ohh... not again...."
  
  scene sunset
 # actuallly add bugs sfx ^^^^
 
  m "Hey, Basara!"
  
 #PENDING cut to cg. Basara giving a light little wave-
  scene pending

  show standsideeye
 
  b "I want to get thing home and show Ray. Sorry, you should go do whatever you want."

  m "Oh, already?"
  b "Ahh... You wanted to do anything else?"
  m "No, I didnt have anything else planned but--"

  show standsmile

  b "Okay."
  b "See ya!"

  hide standsmile

  m "..... Aahh..."

 label lunchMorning:
  
 #lunch script

 label nightChoice:

 #night script

# This ends the game.

return


