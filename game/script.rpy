#CHARACTERS

#PENDING change colors later
define b = Character("Basara", color="#c9443a")
define m = Character('Me', color="#67b870")
define c = Character('Waitress', color="#FFFFFF")
define i = Character('Shop Owner', color="#FFFFFF")


#PENDING EDIT THIS LATER
#PENDING birthday event later

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
 
 play sound audio/birds.mp3
 scene akusho with dissolve
 
 "It's a pretty nice day out today."
 
 scene door with dissolve

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

  b *groans* Alright just... *yawn* let's get some coffee or somethin...

  jump morningDateChoice


 label c2Morning:

 scene bedmorningplay
 with dissolve
 
 play sound "audio/strum.mp3"

 b "....."
 m "Helloooo, Basaraaaa?"
 b "....."
 m "Basara!"

 menu:
 
  "(Wait.)":
  jump waiting
  
  "...Let's play a trick":
  jump tricktime
  
  
 label tricktime:
 
 scene downstairs with dissolve
 
 m "I have just the right idea."
 
 menu:
 
	"Grab an icecube":
	$ ice = True
	jump trix
	
	"Grab a water bottle":
	$ ice = False
	jump trix
	

 label trix:
 
 m "Heh, perfect."
 
 scene basaraback with dissolve
 
 m "(And now...)"
 
 if ice:
  m "(I drop the ice cube in his shirt.)
  b "GYAH. THE HELL--??" with hpunch
  m "Hi Basara!"
  
  scene bedmorning 
  with dissolve
  
  show guitarannoyed
  with dissolve
    
  b "Crap! What the heck did you do, jeez that's cold!" with hpunch
  b "Man, ice?! What were you thinking?!" with hpunch
  m "I called you a few times and you didnt answer."
  m "Decided to play a prank."
  b "*huffs* Yeah, I noticed! What the heck do you want anyway?"
  m "We had a date remember?"
  
  show guitarconfused
  
  b "Huh........ "
  m "A few days ago I said I'd be here to pick you up, remember?"
  m "I wanted to hang out with you."
  
  show guitarsideeye
  
  b " Uhh...."
  
  show guitarnormal
  
  b "Oh.... "
  b "Well, fine. Give me a minute."
  
  jump morningDateChoice
  
 else:
  m "(maybe this is a bit much....)"
  m "(it's too late to turn back now.)"
  m "(I dump the water over his head.)"
  
  scene bedmorningguitar
  with dissolve
  
  show standannoyed
  with dissolve
  
  b "..."
  m "..."
  b "..."
  m "..."
  b "....Hey."
  m "I'm sorry."
  b "............."
  m "You weren't answering me so..."
  b "-SIGH-"
  b "At least you didnt get the sheet music wet..."
  
  show standsideeye
  
  b "Why are you here anyway?"
  b "... Oh, weren't we going to hang out?"
  m "I really dont know what came over me."
  
  show standnormal
  
  b "It's fine, let's go then."
  m "Not gonna change?"
  
  show standsmirk
  
  b "Nah, it's just a little water. C'mon, are you coming or not?"
  
  scene bedmorningguitar
  with dissolve
  
  m "Yeah... yeah, let's go!"
  
  jump morningDateChoice
  
  
  
 label waiting:

 b "I hear you. Give me a minute."
 m "(oops, i think i made him mad.)"

 scene bedmorning
 with dissolve

 show guitarannoyed
 with dissolve
 
 b "Why are you here anyway?"

 m "We were going to hang out, remember?"

 show guitarsideeye

 b "aahhhnn.... Did we? I dont remember..."
 
 m "..."
 
 b "Whatever, I'm stuck anyway. Let's go out."

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

  #PENDING outside cafe scene
  
  p "Okay, we're here."
  b "This place?"
  p "Yeah, it just opened."
  p "I've got a coupon, so let's give it a shot."
  b "..."
  
  scene cafe
  with dissolve
  
  p "Table for two please."
  c "Right this way please."

  scene cafewindow
  with dissolve
 
  play music "audio/bitchesblue.mp3"
  
  p "I wonder what the menu is..."
  b "Dunno."

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
   b "...."
   b "....What?"
   b "... You want some?"
   m "No thanks, you enjoy it."
   
  else:
   m "nice(CHANGE EDIT)"
   show orangefull
   with dissolve

  b "..."
  m "(He's poking at it...)"
  m "Mine is pretty good! How is yours?"
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
  
  
 label faiyaa:
 
  scene cafesitannoyed
  with dissolve
  
  if bigParfait:
   show frappefull
  else:
   show orangefull
  
  b "Gimme a break."
  jump cafeMorningNext

 label bombaa:
 
  scene cafesitannoyed
  with dissolve
  
  if bigParfait:
   show frappefull
  else:
   show orangefull
 
  b "You think you're being funny, huh?"
  jump cafeMorningNext
  
 label cafeMorningNext:
 
 scene cafesitnormal

 if bigParfait:
  show frappehalf
 else:
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
  
  stop music fadeout 1.0
 
  show standnormal
  with dissolve
  
  m "So where did you want to go?"
  b "Huh?"
  m "Huh?"
  b ".........."
  m "What is it??"
  
  show standsmirk
  
  b "Kicked something... Oh, it's a rock. Heh."
  "He kicks the rock"
  b ".... It's really going."
  m "Let me try..."
  pause 2.0
  m "Haha, how's that!"
  b "Wow."
  
  scene outsidemorning with dissolve
  m "(We kicked the rock for a while.)
  
  show standsideeye with dissolve
  b "I saw it while Ray was driving the other day and wanted to check it out. "
  
  "Kick."
  
  p "What?"
  
  "Kick."
  
  b "You asked--"
  
  "Kick."
  
  p "Yeah, I remember now, sorry."
  
  "Kick."
  
  
  scene blackscreen with dissolve
  scene outsidemorning with dissolve
  show standnormal with dissolve
  
  b "This is it."
  b "Here, hold onto this."
  m "(He hands me something.)"
  
  scene outsidemorning with dissolve
  
  m "Huh?"
  m "Oh, this is the rock we were kicking."
  m "Hey, Basara... Huh?"
  m "He went ahead."
  m "Good grief..."
  
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
  play music "audio/galaxymuffle.mp3"
 
  show standsideeye
  with dissolve
  
  pause 1.0
  
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
 
  scene instrumens
  
  show erhulook
  with dissolve
  
  jump instrument

 label instrument:
 
  m "What did you find?"
  b "This."
  
  b "Huh... two strings... and a bow. So I guess it's played like that huh... Hm."
  b "Is there somewhere I can.......... Oh, over there!"

  scene erhuplay
  stop music fadeout 1.0

  b "..."
  b "..."
  b "..."
  m "(Wow, he's so absorbed in it...)"
  b "I think... something like this?"
  
  play sound "audio/erhu.mp3"
 # source https://www.youtube.com/watch?v=thqUc1bf8IU
  pause 30.0
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
  
  play sound "audio/bell.mp3"
 
  m "Wow! He left, just like that!"
  m "Hey, wait for me Basara!"
  
  play sound "audio/bell.mp3"
 
  i "Ohh... not again...."
  
  scene sunset
  play sound "audio/crickets.mp3" fadeout 1.0
 
  m "Hey, Basara!"
  
  show wave with dissolve
 
  b "I want to get thing home and show Ray. Sorry, you should go do whatever you want."

  m "Oh, already?"
  b "Ahh... You wanted to do anything else?"
  m "No, I didnt have anything else planned but--"

  hide wave
  show standsmile

  b "Okay."
  b "See ya!"

  hide standsmile

  m "..... Aahh..."
  #PENDING make good ed image
  scene endingpending with dissolve
  
  "ENDING #1"

 label lunchMorning:
  
 #lunch script

 label nightChoice:

 #night script

# This ends the game.

return


