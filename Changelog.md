# Shotgun Frenzy Plus Changelog

	Legend:
	*) Changed / Fixed
	+) Added
	-) Removed
	// Comments
	!) Pretty important stuff.

## v1 - The path of the damned...

#### (24 / 9 / 2024) [Combat boomstick now works with grenades and fist]
	*) What says in the title, still WIP

#### (22 / 9 / 2024) [Fisting, Grenade Throwing and new keys]
	+) (For the base Beretta and base Boomstick) Now these weapons can be able to throw grenades and fist up foes!
	*) Now using idkfa or idfa will give the normal backpack ammo capacity and will not be overriden by the ammo pad.
	+) Added some hand sprites for throwing and punching.
	*) Fixed the Soul Rune pickup sprite.
	*) De-harcoded the stay time of the pickups spawned by the supplier.

#### (15 / 9 / 2024) [Weapon Quick-Switch on the works]
	*) Renamed all the weapon decorate files with the .dec extension, just for easier readability with visual studio code.
	+) Added a new Decorate file, "frenzy_weapon.dec". Which it holds all the weapons that exists in the game.
	*) Generalized the boomstick and beretta into the frenzy_weapon actor, now these guns can quick-switch between them!
	// Fire when raising a weapon to instantly fire, no need to wait for the raising animation to work.
	// To be implemented in the rest of weapons.

#### (14 / 9 / 2024) [Spitters shootable grenades, Patcher's Move and Recycle modes & Sprite Repleacements]
	// 'Sup! how is it going?
	// Yeah I got no excuse for not doing any progress since like 10 months with no activity on the repository.
	// I'm finally graduated as a Informatics Engineer. And i've been goofing arround with some of my closest friends. Not to mention also the tense situation of my country (yes, i'm venezuelan, the electoral fraud really pissed us all), and also my lack of motivation to continue doing some updates on SF+, but you know what? Screw it. I'll keep doing what I love to do. Doing some more shotgun frenzy stuff :D.
	// So, what did i done this time?
	!*) Some sprite replacements on the Spitter and the Beretta + Variants, specially adding those black cool gloves to the weapons.
	!*) Now the base spitter gun will have an attached grenade launcher, with 5 grenades as base ammuniton.
	*) The animation after launching a grenade with the spitter can be cancelled with the primary fire.
	*) The grenades thrown by spitters can be shot for a greater radius AoD.
	!+) The patcher now can do some extra functions, move, and recycle turrets and dispensers!
	// Switch between modes with the Reload key. Yeah, sounds ridiculous, the reload key used ONLY for the Patcher. However, I MIGHT give it some other uses with other weapons.
	// Move mode can move turrets and dispensers, aim to a building and fire with the alt-fire, hold the altfire to the place where you want to move your turret, the release the trigger and voalá!, your building is teleported from spot A to spot B. The price depends on how far you're planning to move your building.
	// Sell mode can dismount buildings for some extra coins. Aim to a building and fire with the alt-fire, release the trigger to sell the building. The price depends on how advanced and how expensive is the upgrade price.
	*) Cleanup and optimization on the lumpread.acs file.
	*) Now the terminals will not open until the game has started.
	// Also added a new branch, the dev branch. Just to play arround with branch developing.

#### (11 / 11 / 2023) [New custom Lumps, monster waves, and improvements]
	// 4 weeks with no commits?! Shiet. Let's fix that.
	*) Updated Pack-o-daemon
	*) Sprite re-organization on the resources part, specally adding folders on each monster sprite.
	*) Some new sprites for both SSGs. Courtesy of Sonik.k.o (ThatSonicFan).
	+) A new monster wave is being added! The Aerial wave!
	// Airbone monsters will come to attack from the sky! Let's hope you dont have Quiroptophobia, because Bats will be the first of your problems, not for their health, but actually for the sheer numbers.
	+) Speaking of bats, added Giant Bats, a bad (skulled bat), and re-added the bat familiar.
	!+) To celebrate the addition of the SCORINFO lump, the scoreboard is now modified for showing the credits, upgrade points, kills, kill-streaks, deaths and of course the players in the game!
	!+) Now the Item Hud is now customizable! Change the position, alpha (transpaency), and the orientation of the item bar! On SF+ Settings > User Options.
	*) Reworked the lump reading scripts, shorter and straight to the point.
	!+) Added the SFRUNDEF, SFMWAVES and SFITMDEF lumps, also refactored the SFWEPDEF lump for easier addition and readability!
	// SFRUNDEF defines the runes, SFITMDEF defines the items, SFMWAVES defines the monster waves! Cool additions for the modders to play around!
	!*) The Autosave feature has been reworked and now it's lagless, and smart! (although, again, needs some testing)
	+) Now monster's stamina (in decorate), will hardcode the class which a monster belongs to.
	+) Also the monster's accuracy (in decorate), will tell if the monster can be championized (-1=no, 0=yes, 1=always).
	*) Some small fixes on the Samu Terminal

#### (6 / 6 - 18 / 7 / 2023) [New SFWEPDEF Lump, Inputs on terminals]
	// Heyo! another month of developing with some other changes!
	*) Splitted the 3 terminal main functions (Draw, Input and Update) into 3 scripts for more processing. (and fool out the runaway errors!)
	*) Prompt dialoge has been rewritten with the new Panels on Samu Terminal.
	*) Done some refactoring in Samu-Terminal related to panels.
	*) Now you can use your own input to select clickable components!
	// Move with movement keys, use to click, alt-fire to close (controls still pending to mention)
	!*) Now buy weapon page is now revamped, including the new panels!
	!*) Now it is possible to add 50 packs per category, 3 weapons per pack, and 8 upgrades* per weapon through modding (and the new SFWEPDEF will help you with that!)
	// *The upgrade weapon page still needs some work to be actually useful with the new incoming 8 upgrades per weapon.
	!+) 3 wild SFWEPDEF lump file has appeared!
	// SFWEPDEF? da hell is that? you might ask. That lump is not supported by Zdoom, or Zandronum in general, uuuh what?
	// Well, since Zandronum 3.2 recent alpha (Look up Readme file for the link), I went full on experiment with some new TDRR functions for reading lumps.
	// Thanks to that, it is now possible to simplify and make it accesible for everyone in adding new mods on SF+.
	// You do not need to use ACS to recompile a script, now weapon addons are extremly easy to add! That's why SFWEPDEFs are there.
	// But more about that later~ I'll update the docs for it, I Promise.
	*) Fixed the cvar pricing for stimpacks, mechs and runes.

#### (4 - 5 / 6 / 2023) [SSG's reworks, Price Edit, Cvarified Prices]
	!*) Now the prices will be checked by console vars!
	+) A new Price Edit option menu.
	*) Some re-ordering on menudef and cvar info just to separate the prices in their own files.
	*) Testing an template addon for adding custom weapons, it's not in it's final stage so plz do not use it yet.

#### (2 / 6 / 2023) 
	*) Well, ssg has been reworked. Now you can deal more damage on close shots.
	// Base SSG can create ricoshot bullets and explosive damage.
	// Autoload SSG can spread more ricoshots, aside of firing more bullets.
	// Explosive SSG can create a long standing fire in flesh hits (on demon hit) that stands for like 3-5 seconds.

#### (18 / 5 -  1 / 6 / 2023) [Panels, constant effects delays, and Readme edit]
	*) Moved the custom monster set to a dedicated folder for addons, called addons. Duh.
	*) The readme.md has been updated, with some more clearer build instructions.
	*) Now the altered states, like burning or shocked, and the constant scripts for the turrets, like regeneration intervals will start off with a small delay, just to reduce the packet consumption online.
	!*) Now samuterm is no longger limited to execute scripts with arguments with the 256 byte limitations.
	!*) Panels in samu-terminal! Finally! (Expect an ammo/health terminal remake soon :>)

#### (13 / 5 / 2023) [Main menu, f1 screens and fonts]
	*) Smallfont is now replaced with the confont graphics.
	*) Bigfont now it is replaced by the Statbigs
	*) Changed the colors and fonts for the menu, for the sake of consistency and readability.
	*) Added a Conback, and a pair of f1 screens.

#### (5 / 5 / 2023) [Some sprite reorganization]
	*) Just moving the sprites in the resource part.
	*) Now Samu-Terminal will only init the db once! Thank u Buu42!

#### (23 / 4 / 2023) [Alright, alright, let's commit some stuff]
	*) Now the scripts for music and for showing sbarinfo data are now optimized and clientsided respectively, and that means less lag!
	*) Updated pack-o-daemon and adapted the project.json to the current project settings.
	*) Added a new map, the Map Hub!
	// Now here you can choose what map or difficulty you want, you will get yourself teleported to the following map! (a cvar is there to help you out with that)
	+) Now, it is possible to add custom waves and custom monster sets!
	+) New cvar for the use of the damage per experience algorithm, and also added some achievement cvars for the server :)
	*) Now the invulnerability granted by powerups or defense rune will be overriden to the last powerup used.
	*) Now the rune messages will only appear when not using a mech
	*) Added some invulnerability checks for tanks.
	+) Added the "Monster Pressure" stat (the AIDir Level).
	*) Some extra fixes in the AIDir scripts
	*) Now, poison champions will not do it's AOE damage when invulnerable.
	*) Mech upgrades, are now counted to the AIDir.
	*) Simplified weapon language data. For an easier addition on weapons (Custom weapons soon)
	*) Fixed some other stuff.

#### (6 - 9 / 2 / 2023) [Rune's buffs and Skill modifiers]
	*) Now the temperance rune will give 100 AP upon each armor pickup.
	*) Health rune will extend the user's health to 100 hp. Obeying the current techs.
	*) Ammunition runes will extend the user's base ammo capacity to x2. Obeying backpack tech and personal backpack item.
	*) CF02 map's certain linedef who caused a TID switch for the players has been changed now to change it for the monsters.
	*) Some extra fixes on the armors.
	!+) New skill levels are added! These skill levels change the game completly.
	// Classic, the pre 1.0 version additions (like extra items and champions) are removed.
	// Normal, SF+ with common settings.
	// Hard, x2 Damage taken by monsters and x2 HP extra health for monsters.
	// Turbo, Fast movement and aggresive monsters.
	// Miserable, Less drops (specially gems, some turrets and armors/medikits), less money (25% less) and 25% of prices are increased.
	// Masochist, Hard + Turbo + Miserable. And no Megasphere and Godsphere. 

#### (26 - 29 / 1 / 2023) (v1.7 Release!) [Buffs, fixes and little map changes]
	*) CF01 now in the first battery zone, a teleporter in front of the teleport destination has been placed in there, if you want to get to the other side of the room, where the battery is ubicated :)
	// Oh and, the back side area, there is a "spiky surprise".
	*) SF01's Sector 1 has been slightly changed, now there are 2 teleport destinations in each side of the outposts. With a pair of health and ammo dispensers. And now, the platforms should now lower properly.
	*) CF04's Sector 1 has been slightly changed, now the area it's a little less cramped, and now you have a red barrier that protects you from the spawn killing caused by the crowd. Also moved the home teleport to the spawn area of Sector 1.
	*) Dualshot nails will now bounce only once, and razor blade upgrade bounces up to 4 times. Buffed their damages too.
	*) Repeaters damage has been buffed up. Now they take less time to overheat. Remember, overheating means less accuracy, but more damage.
	*) Deployers will now instead of giving the item on failure. Will stop the deployer from consuming, which that removes the scrolling active items from the inventory bar.
	*) Drones are also buffed too, and reduced the prices of them.
	*) Flame turret price drops to 2750 credits.
	*) BFG Overcharged upgrade will now consume 200 cells.
	*) Rage rune will now not be overriden by the helltrigger powerup.
	*) Ok now, personal backpack and global backpack should do their respective values in either order of picks.
	*) Renamed a pair of visual inconvenient icons on the item shop from the armory.
	*) Rampage and Health runes are now spawnable and pickable up again.
	*) Rewritten and modified the Mech class.
	*) Rampage rune's additive effect is now limited up to 10 seconds.

#### (21 / 1 / 2023) (v1.6 Release!) [Particle clientsiding, and some balances]
	!*) Now causing burns is not guaranteed, and causing the fire chain is also reduced. There is a chance for triggering it.
	!*) Flamers will launch a fire projectile that will not rip (and does more damage for the first target) along side of the ripper version.
	!*) Helltrigger loses it's capability to give infinite ammo. Partially.
	// Helltrigger will give ammo regeneration, and ammo infinity but for only the first 2.5 seconds. (5 seconds with pow.up upgrade)
	// Fast fire is still intact.
	// Hey, let's face it, the powerup asked for a nerf lol.
	*) Lightbars will now be spawned by ACS when using powerups, and the champion effects (Like healing and emperor champions).
	*) Touched the Altstates's delay and some few rewrites.
	*) Changed the prices of the item shop turrets.

#### (9 - 20 / 1 / 2023) [Optimizating stuff, and some fixes.]
	*) Some more optimizations on the scripts.
	*) Now fading items will not be done by decorate but done now by an small ACS script.
	*) Turrets will now add credits to it's owner.
	*) Another attempt to call always the kill streak HUD.
	*) Spread will always spend x3 Ammo. For the sake of a nerf.
	*) Did some adjusts in the Enemy Marker actor. (Thanks Mr. Satan!)
	*) Clientsided some other HUD scripts.
	*) Patcher projectiles will now they activate as Hitscan projectiles!
	*) Optimized the display code for the patcher turret checker.
	*) Now, stealth champions will be actually traslucent up to 25% of alpha by the help of ACS. (they did'nt fade in server side)
	*) Spawn shield will now call a 3 second cooldown timer after triggering its effects.
	*) Some other code rewrites.
	*) Marker Enemy is now clientsided, yay! (and now follows the enemies through an ACS script)

#### (1 / 1 / 2023) (v1.5a Quickfix!) [New year fixes.]
	//2023 is here, shit, 3 years in this lol
	*) Modified the item hud, killstreak hud and powerup hud in order to stay shown no matter how much
	*) Some attempts to prevent the desync.
	*) Fix on magnet for Credits and armor and health bonus.
	*) Added some clientside flags for many particles.

#### (28 - 30 / 21 / 2022) (v1.5 Release!) [Optimizing code & Patcher's lower prices]
	*) Done some optimizations in the Killstreak and fullscreen huds by, heh, literally fully clientside both of modules.
	*) Now you can customize the killstreak hud with your own colors and with the transparency level.
	*) Modified the particle spawning in acs way for the Stun and Burn altered states.
	*) Lowered down the prices from the turrets in repairing and upgrading turrets.
	+) Restored the particle system back where it belongs.
	*) Toned down the prices of the patcher for the fixing and upgrading turrets.
	*) Buffed the fixing effect for the patcher, now heals 20 % of health
	*) Upgraded Turrets will now regenerate 10% of their HPs.
	*) Attempting to reduce the problem of "FireRockets state not found"
	*) Sparks from the buildings can be switched in the menu now.
	*) Now flame bullets will spread fire always! (And that affects the Combat Boomstick, Flame SSG and Flame Buckshot)

#### (26 / 12 / 2022) (v1.4c Quickfix!) [Rewritting patcher's upgrade powerups]
	*) Re-written the powerup upgrades from the patcher in turrets.
	*) Now the patcher will be drawn faster, and with a small sound as the beretta.

#### (25 / 12 / 2022) (v1.4b Quickfix!) [A gift of fixes in christmas]
	*) Music will not be resetted when the guardian wave ends.
	*) Some other fixes about the zombie champion
	+) Champion descriptions! (on the menu > champion banlist)
	*) Lowered the price of the bullet turret to 650 credits (in order to add 2 turrets more for the player who want's to go full support)
	*) Re-implemented the upgrade powerups from the patcher to the turrets.
	*) Soulsphere and Megaspheres healing factors are restored to their original 100 and 200 Ohp.
	*) Re-implemented the building aggresion scripts, lets give this another try before dropping this idea.
	*) Increased the spawn time from 3 seconds to 5 seconds in the waves.
	*) Re-implemented the stun effect, now it should retarget back to where it belongs.

#### (24 / 12 / 2022) (v1.4a Quickfix!) [Attempt to fix the cpu memory overload]
	-) Removed the aggro attraction from all buildings. For now.
	*) Now sector recapturing will be counted in the final score.
	*) Now sector recaps are enabled once again with no recap minimal (when this var is 0).
	// Oh merry christmas :D

#### (18 - 23 / 12 / 2022) (v1.4 Release!) [Some extra fixes and goodies]
	*) Fixed a thing_hate problem which hoarded the cpu usage on server side.
	*) Demons and mech demons will jump in a shorter range now, between 200 and 300 map units respectively.
	*) Now the chaingun turret should'nt flicker in multiplayer.
	*) Powerups will launch their upgraded effects without overriding the type of upgrade.
	*) Defense rune has been fixed, now it can trigger in any kind of damage event (with armor or not)
	*) Defense rune will activate after 1 tick of recieving damage, in case of hitscan attacks, they must hit the target before activating the effect of this rune.
	*) Defense rune's duration has been buffed to 52 tics (almost 1.5 seconds)
	*) Now all baron's green fire attack will pass through the horde.
	*) Cyberbarons will attack with the green fireball more often rather than going with the rockets.
	*) Cybruiser's projectile speed has been nerfed a bit.
	*) Zombiemans will face the target before shooting a bullet.
	*) Reduced the errors caused by the shell grenades.
	*) Buckshots, Spitters and the Advanced Plasmagun will fire faster with the help of the Rage Rune.
	*) Now the backpack will not be shown in the item hud.
	*) Dropped runes will mention their names on the game, when you're near of them.
	*) Changed the messages when players are building turrets. Just to reduce the spam in console, caused by print msgs.
	*) Some sound feedback when the building deploying fails.
	*) Double Slug Railgun can attack through the hordes, dealing half damage to everyone behind the first enemy hit.
	*) Prosperity rune's effect is now restored to it's 450 Hp/Ap max effect.

#### (16 / 12 / 2022) (v1.3b Quickfix!) [Removing the cvars related to particles]
	-) Removed the particle removal for clients as an attempt to reduce the CPU usage from the server.

#### (15 / 12 / 2022) (v1.3a Quickfix!) [Division issue]
	*) A division by 0 on the final fight script now is fixed, i hope.

#### (14 / 12 / 2022) (v1.3 Release!)  [Touching the item drops]
	*) Refactored some rune drop scripts.
	*) Fixed the limit of dropping the first 4 items.
	*) Now the credits, health bonuses and armor shard drops chances will be dependant of the monster type and if it's a champion.
	*) Now the stimpack upgrade "Hard Shell" will now grant extra 5% on the armor repair.
	-) Nerfed a bit the Titanium armor. 45% damage absorbtion (+ 15% with the temperance).

#### (10 - 11 / 12 / 2022) [Particle control, maunal picked runes, other fixes]
	*) Added new cvars to control the particles in game. Meant to reduce the lag in clientside.
	*) Now runes will not be picked up and linked when you bump on them, you will have to press use when bumping into a rune. Meant to reduce the inconvenience of suddenly change the rune in mid-battle.
	*) Now the patcher will not damage the cores.
	*) Steel plating armor effect has been fixed.
	*) Now the gems, titanium armor and upgrade card will disappear over time. Same thing for the medikits and steel plating armors.
	*) Modified the item pools for monsters, adding the shotgun and chaingun turrets, and the greedsphere for the champions.
	*) Fixed the price of the plasma pack back to 6000 credits.

#### (8 / 12 / 2022) [Item directory rewrite & rewrites & fixes] 
	*) Made a new file for data storage of items called Language Items.
	*) Rewrote the Item directory, and encapsulated a few things in there.
	*) Now the laser from the Spear-Taser Railgun is now visible in multiplayer (although the taser projectile was nerfed visually :( daang you limited zandronum!)
	*) Now the Stimpack is invisible in the Item Hud.
	*) Fixed the disbalance of monster spawning when 3 or more players join in.
	*) Modified the skill system. SHOULD be a little more exact.
	*) Refactorized the hud messages from the final fights. And now added 2 extra stats, Cores protected (CF and SF), and Waves cleared (SD)
	*) After a zombie champion is killed, it will re-target again to the risked core.
	*) After shocking an enemy, it will also re-target again to the risked core.
	*) Alright, now turrets will not interrupt the hate command, hopefuly.

#### (7 / 12 / 2022) (v1.2 Release!) [Zombie Champ. balance and crash fix]
	*) Fixed the crash caused by a raising Zombie Champion after deleting it's corpse. (Again, thanks Kaminsky for the hint!)
	*) Now some particle gore effects will spawn over the dead zombie champion after using all it's lives.
	*) Now a champion zombie will try to rise with only 2 extra lives (in that way, you can kill it up to 3 times) resurrect chances are: 70% at first death and 35% at second death.
	*) If a champion zombie is resurrected by any enemy resurrecter (like archviles), it will consume 1 life for the early raising.
	*) A zombie champion after the first death, will not drop any reward items after dying again. (but still you will get paid after the kill).

#### (5 / 12 / 2022)
	*) Now the autosave function will only trigger when activating the sfp_autosaveitems on ccmd.
	*) Reworked the autosave function to keep items for everyone, with a little less lag (i hope).

#### (3 / 12 / 2022)
	*) Reduced the prices of the stimpack upgrades, in order to get pursached in early game.
	*) Fixed the rune terminal not showing it's runes.
	*) Rune Sync. will now be granted in 1000 kills on CF/SD maps
	*) Save functions will be a little more patient now, in order to reduce the server lag.
	*) Modified the tech research message, to include also the icon of the research.
	*) Cleared out some left overs of logs messages.
	*) Buckshots when using it for the first time, now starts with some ammo loaded in the chamber!

#### (28 / 11 - 1 / 12 / 2022) (v1.1 Release!) [A quick Hotfix]
	*) Fixed the strange text in the Kill streak hud.
	*) Fixed the random dissapeareance of the Health bonuses and Armor shards, same for the credits and minerals.
	*) Swapped the order of the SSG upgrades, now you can buy the proper ones.
	*) Reduced the desyncing of coins and hb/as generation.
	*) Optimized the price syncher.
	*) Saves now can save stimpack upgrades and current rune.
	*) Recycle page now allows you to recycle the upgraded gun.
	*) Hidden some debug messages.
	*) Changed the font of the messages caused by HB and AS.
	*) Removed the message of powerups when re-entering the game.
	*) Reduced the price of the minerals, small worths 50 and big worths 150 now.
	*) Timer display has been changed to show on the last 10 seconds of the game the last miliseconds instead of tics left.
	*) Re-ordered the weapons, and narrowed them in 5 slots
	// Slot 1 is for pistol and shotgun, basic slot
	// Slot 2 for standard weapons, with their upgraded variants.
	// Slot 3 for advanced weapons, with their upgraded variants.
	// Slot 4 for overpowered weapons, with their upgraded variants.
	// Slot 5 for the other supportive weapons (like patcher or supplier)
	*) Ok, forgot the random probability of the champion apperance, lul.

## v0 - Before the beginning...

#### (15 - 27 / 11 / 2022) (v1.0 Release!) [Rune terminal, C.Pulses, techs & relase!]
	!+) Rune shop available in the Health terminal!
	+) Now champions can drop extra rewards exclusive to their pools. In their drops also include Runes, a new red armor, and gems (extra credits)
	*) Stimpack upgrade and Rune shop are locked behind their new techs.
	*) New / Revamped Core pulses 
	// Warcry: Damage up and fast fire for all marines
	// Repair: Fully repairs your risked core
	// Heal: Instant free megasphere, resistance up & a few invincibility seconds.
	// Smite: Damage the demons near of the risked sector with a high damage.
	+) New techs
	// In refinery upgrades
	// Compensation: Coins worths 5 times more.
	// Engine Boost: Faster coin production in the refinery.
	// Core Booster: Increases the intensity / duration of core effects
	// Core Optimizer: Decreases the standby time and start up time when calling a core pulse.
	// Rune sync: Unlocks the rune shop. (Rewarded in 2000 kills on CF/SD maps)
	*) Also implemented the poison champion.
	// While in it's range, damages you, and debuffs you with -25% damage, and -25% resistance.
	// About time to make a release! (although it's barely tested online, but should be stable enough, SHOULD)

#### (30 / 10 - 14 / 11 / 2022) [Stimpack upgrades!, fixes and champion drops (wip)]
	!+) Yes!, now the stimpacks are upgradeable! Get them on the Health terminal!
	-) Reduced the amount of stimpacks given by 5, but, you can go back to 10 with the stimpack upgrades.
	+) Added some extra items for the future item drops from champions (WIP)
	*) Some small rewrite on the teminal menus.
	*) Moved the patcher code to a separated file.
	*) Clientsided the scripts coming from the patcher display (needs testing tho)
	+) Added a new CVAR to toggle the mech message upon using your mech.
	*) Fixed dissapearing base turrets.
	+) Now the flame turret on level 5, will add a fire ring upon each fire state!
	*) Changed some sounds for armor/ammo pickups and added some feedback sounds for the patcher.
	+) Added some stimpack counter for the full screen.
	*) Modified the fullscreen player hud, now kill-streaks are visible! (inluding high, current and next milestone)
	// That, and now you can see your rank + the current experience in a neat way.
	+) Talking about the new champ-drops, added:
	// An upgrade card (Adds 1 U.P)
	// Minerals (Small = 100$, Big = 250$)
	// Titanium Armor (400 AP with a 50% (+20% with temperance rune) Damage absorb)

#### (16 - 24 / 10 / 2022) [Sprites for flame and rail turrets + BFG upgrade]
	*) Extra touchs on the turret code
	+) Extra sprites for the Rail Turret, Thanks MadCat!
	+) New sprite replacement for the flamer turret! (yes, i did frankedsprited this one, and im proud of it uwu)
	*) Some renames in the files.
	*) Updating the showcase list.
	*) Super BFG now becomes the Splash-Spread BFG, specially beacuse now this weapon spreads faster and does some extra damage.
	*) BFG and all the other bfgs gains an altfire, the beta's Doom BFG. (that flurry of plasmas 'member?)
	!+) A new upgrade for the BFG! The Overcharged BFG!
	// This big bastard fires a ball that hits 10 times. Exploding on each hit, and increasing it's damage and size. Also Seeks.
	// While it's by far the most expensive in ammo consumption (300 cells per shot), slow compared to the original bfg, and quite expensive in the terminal (6 UPs). This weapon works as a nice counterpart to it's splashy counsin. Making it effective for dealing a shietton of damage with a massive big ball. It's powerful enough to oneshot a Cyberdemon-Annihilator! And, you don't really waste ammo, since it's projectile seeking will get rid of any loose ends on the battlefield, so this is also a good choice to consider. 
	
#### (11 / 10 / 2022) [Map markers on the last enemies]
	+) Now, on the last enemies before starting a guardian wave or before ending the map, a red dot will be marked on your automap, so you will know what enemies are remaining in the map.
	
#### (10 / 10 / 2022) [Aggro on dispensers]
	*) Now health and ammo dispensers are more prone on attacks compared to the rest of buildings.
	*) Shortened the duration of the shell pellets to 5 seconds, and now they deal more damage.
	*) The timer will disappear on any gamemodes that are not specified.

#### (9 / 10 / 2022) [Spitter buffs, stimpacks and hand-grenades (wip)]
	*) Now the auto spitter can fire a perfectly aimed bullet on the first shot, reduced the ammo consumption and takes no breaks for each shot round.
	*) Now the spread spitter can fire a perfectly aimed bullet on the first shot and uses less ammo (2 clips per shot).
	*) Base Quadshot primary fire now quakes as intended upon fire.
	*) Revamped the weapon recycle page, now features a rough scrollbar and shows only 10 weapons, use the up and down buttons to navigate through the list.
	*) Now the stimpacks can be researched in the CMD terminal and auto given in CF-SD maps.
	*) Hand grenades can be researched in the CMD terminal. Hand grenades can be used as a throwable projectile, deals damage depending on the user's rank (WIP)

#### (2 / 10 / 2022) [Rewrites, and some weapon tweaks, and icons, yeah]
	*) Rewritten the commander terminal, a bit more optimized now.
	*) Now the strings related to the CMD terminal are separated in their language files (just to add a quick translation patch).
	*) Now Healing and Emperor champions spawns their particles better.
	+) Added some more icons! for the CMD Terminal!
	*) Big Chamber Buckshot is now renamed to Ricochet Buckshot, due to it's added capability to throw bouncing bullets, which they pass-through enemies.
	*) Little visual tweaks on the Quadshot. Quadshot fire ratio was reduced slightly, in order to make it teorically slower than the Explosive SSG.
	*) Plasma gun can do an alt-fire, which it charges bigger balls that does multiple hits in one target, exploding on each impact. Also, the normal plasmaballs can do some small and weak Area of Damage upon hit.

#### (26 / 6 / 2022) [Less warnings and a Patcher Bugfix]
	*) Removed the warning messages from the startup (most of them)
	*) Better display on the messages when upgrading with the patcher.
	*) Patcher will now deal no damage to the monsters.

#### (5 - 20 / 6 / 2022) [Armor revamps, (WIP) Hand-Grenades and you]
	// It's been a while huh?
	*) Health bonuses are buffed, +5 HP, up to 300 MaxHP 
	+) Armor shards are added, +5 AP up to 300 MaxAP, 33% protection like vanilla armor.
	+) Now enemies can drop a splash of Health Bonuses and Armor Shards! (And they can chase you, like coins!)
	*) Armors can now protect your health from any harm with 100%.
	*) Armors when getting damaged, can absorb a piece of damage, Steel-Plating Armor (a.k.a The green armor) can absorb the 17.5% of the damage while the Megasphere armor can absorb 25% of damage.
	// It looks like a nerf, but when you think about it, armors are like a second health bar, but they can absorb damage.
	*) Temperance behavior has been changed, now temperance adds extra absorb percent on armors, and spawns extra Armor Shards.
	*) When having a lot of shards, the armor you pickup will replace the shard's protection percent and take the same amount of shards you got if the duration is greater than base armor. (If you have 150 Armor Shards, and you pickup a Steel-Plating Armor, the armor will have the duraton of 150 AP)
	*) Steel-Plating Armor is now added into the drops of monsters with a chance of 17.5% of spawning.
	+) Grenades are now added as an item. Launches a Shell grenade (WIP) (Needs an item sprite for it)
	*) Added the HellTrigger and Hand Grenade hotkey control in item hotkeys
	// But wait!, there's more -Jarl 'Balling' Balgruff-

#### (24 / 5 / 2022) [BFG Turret Button, login/logout msg in terminals]
	*) Now the SamuTerminal's login and logout can be customized anytime.
	+) Added some messages when login or logout in any terminal
	+) Added the sprite for the BFG Turret button.
	+) The BFG Turret button is now ready on the commander terminal (20000 credits per deploy)

#### (15 / 5 / 2022) [Adding Ranks and a new Tech]
	*) Refactorized and prettified the standard hud code.
	+) New extra ranks, the elite ranks! (10 lvls more to grind!)
	+) A new tech, Veteran Mercenaries! Get it on the Marine Command! (Needs the button graphic tho)
	// Extra experience for the new players, x3 if under Sergant rank and x2 under Major rank!
	// Also rewarded upon 6900 kills on CF and SD maps.

#### (9 / 5 / 2022) [Playing around with the scores]
	*) Weaker waves are more durable depending on the player count.
	*) The counter for killed monsters and the player deaths now show simultaneously.
	*) Now the monster counter can count faster on higher numbers if the kills are higher than 1000 or 10000
	*) Splitted the champion code in separate files for readability sake.

#### (11 - 14 / 3 / 2022) [Champion ban-list, MenuDef refactoring & Fixes]
	*) The menu for the SF+ settings has been revamped, and now shows 4 submenus for each option.
	// Game Options, User Options, Item Hotkeys and the Champion Ban-List.
	+) The Champion Ban-List is now added to your menu for your server.
	// This menu is cappable to prevent the spawning the champions you don't want to see anymore.
	// And instead of spawning it, might do 1 of the 2 things, spawn a normal monster OR a not-banned champion.
	*) Some variable renaming in the mSpawn.acs
	*) Allied monsters can't be spawned as champion variants now.
	*) The healing effect from the healing champ, will not insta-kill monsters.
	+) Added the credit stealing effect from the golden champion. (needs some sfx tho)
	*) Demon buildings can't be spawned as champion variants now.
	*) Now the rainbow translations will be lost after the death of the champion.
	*) Switched the puller to pusher and viceversa in the MenuDef.
	-) Player's heavy mass has been disabled for now. BUT
	*) Archviles will no longer push upon making the fire attack
	*) For this reason, now puller and pusher champions can now move the player!
	*) Some more fixes.

#### (9 / 3 / 2022) [Champions still in Progress + Some docing]
	*) Some balance changes on the champions.
	// Alright, here they are, Champions!
	// Champions are stronger enemies which they will appear depending on the fast monster factor (which should be renamed to champion factor).
	// (WIP) Champions will drop unique stuff. Including Runes!
	// Here you go the list of them.
	// Meaty (Red): HP x5 
	// Quick (Yellow): Speed x2
	// Strong (Dark-Red): Damage x4
	// Stealth: Nearly invisible
	// Poison (Dark-Green): (WIP) Poisoning aura, leaves a poison smoke on death.
	// Explosive (Bronze): Explodes on death.
	// Golden (well, gold): (WIP) Credit thieft, Drops credits on death.
	// Split (Blue): 2 copies of the same monster will appear after death. 50% hp each one.
	// Teleport (Green): Wanders arround by teleporting, dodges frecuently.
	// Healing (Pinky): Heals 3% of HP each second for all monsters in it's AoE. (256 M.U.)
	// Emperor (Black): x3 Dmg + 50% Def, Buffs (x2 Dmg + 30% Def) all monsters in it's AoE. (256 M.U.)
	// Pusher (Cyan): Pushes all enemies arround it.
	// Puller (Silver): Pulls all enemies arround it.
	// Hybrid (2 Colors): 2 Champions in 1. (Banned Combos for now:
	2 Skills from the same champion, Pusher + Puller, Emperor + Strong or Meaty, Prideful)
	// Zombie (Brown): Revives after death. 3 Lives. Each revival is less likely to succeed depending on how many lives it used. (30 % on the third life, 60 % on the second, 100 % first life)
	// Prideful (Rainbow): Strong, Fast, Meaty (x3 Hp), Zombie (1 Life), Healing, Puller, Explosive & Golden in a single champion. Lucky this arsehole is rare to find. (WIP) Drops lotta stuff on death.
	*) Adding the yellow and purple streaks to visualize the monster who get's affected by the champion aura buffs.
	*) Prideful will do now the emperor's effect.
	*) Pridefuls are not target for the healing and emperor champions effects.
	*) Fixed up the temporal speed for the emperor improving.
	*) Set a better black for the emeperor, instead of being, literally a black siluoette.

#### (25 / 2 - 8 / 3 / 2022) [Champions in Progress (WIP)]
	!+) Implementing new champions borrowing some translations from mikk's gzdoom champions and tddr's rainbow monsters!
	// More detailed info about them later.
	+) Playing with the in built particles in order to make new graphical effects.

#### (22 / 2 / 2022) [Champions in Progress]
	+) Now the monsters can be spawned in their champion forms!
	// No rewards on death for now.
	// 3 champion types implemented, Strong, Meaty and Fast champions.
	*) Moved the monster modification code to fp_Mspwn.acs
	*) Wrote some ideas of a new weapon pack, the Cryomancer pack. (You're free to take a look in the language.weapons file :3)

#### (17 / 2 / 2022) [Burning Flamers & Demon Build's raise.]
	!*) Demon buildings (like the flesh wall and demon turret) can now regenerate back to action.
	// In consecuence, in order to advance to the demon core, you will be in constant attack by these structures, even if you destroyed one of them!
	*) Buffed the flesh wall to 6000 hp.
	!*) Flamer guns are now modified!, now they can actually burn the enemies arround them!
	// A burning enemy spawns a flame under it's feet to take damage for a short time.
	// If the enemy is killed and it's still burning, it will ignite the surrounding enemies to take the burning effect again. A flaming-satisfying chain reaction!
	*) Flamer can now rip though the horde, but with fixed damage.
	*) Super Flamer can fire more flames, resulting in a spreadier attack. Still, with fixed damage.
	*) Player's corpse can now properly disappear without affecting the Acs code.

#### (14 / 2 / 2022) [Spear-Taser Railgun's little lover touch]
	*) Buffed the damage of the spear-taser railgun.
	*) This weapon costs 2 cells to fire, and consumes faster when it's fully winded up.
	*) Stun effect will not take effect on dormant actors.
	*) Taser's attack will pierce thorugh, meaning this weapon can now stun whole hordes.
	*) Taser's attack will now cost 8 cells.
	
#### (11 - 13 / 2 / 2022) [Spear-Taser Railgun and Buckshot's touch]
	*) Spear-Taser Railgun's attacks are modified with proper sounds and with ammo checks.
	*) If the buckshot's chamber is empty, and you have some ammo for it, reloads once.
	// For 2xclick mouse problemtic users, potentially a time-saver.
	// You can hold fire (or alt-fire) to fully reload.
	*) Spear-Taser Railgun's alt-fire can now properly stun enemies for 3 seconds!
	*) Now laser's from railgun will no longer spew blood on impacting enemies.
	*) Modified a bit the spear-taser railgun's pri-fire attack. :)

#### (7 - 10 / 2 / 2022) [Supplier's extra goodies~~ + Railgun tests]
	*) Now the supplier can spawn all types of ammo, including the gasoline, nails, heavy bullets, grenades, 2 pistol clips, and 3 medikits on the health mode.
	*) The Mega Supplier can now spawn the adobe mentioned ammo but twice as much!
	*) Mega Supplier can spawn 2 armors when spawning the 5 medikits.
	*) The supplies spawned by the Mega Supplier or the Supplier shall stand in the floor for 1 minute. If they take too long they will disappear from the map.
	*) Using both suppliers will grant a 30% chance to earn 1 exp point.
	*) The Spear-Taser Railgun can now, do a proper tasing and laser attack!
	// (WIP) Taser stuns enemies with low damage.
	// The laser attack Pierces through the enemies.
	*) Now the Double Slug Railgun can fire a second laser for the primary fire.
	*) The Laser Railgun's laser (redundant i know) can now pierce through 20 weak enemies. And overall deals more damage. Slug's Laser pierces though 40 enemies.
	// Although this is still WIP.

#### (3 - 6 / 2 / 2022) [Upgradeable Toorets!]
	!+) Now Turrets can now be upgraded with the patcher's altfire!
	// Max turret level is 5
	// Turrets gain an upgradeable regeneration of 3 points, x0.2 Damage up and x0.1 Resistance up per level.
	// In level 5, that's x1.5 resistance, and 2.0 damage multiplers and 15 points on regeneration!
	// Also they gain extra effects that enhances their overall performance!
	// There is a lot'sa them, that I'm too lazy to document that up :p
	// For now, works on bullet, shotgun, chaingun, rocket, plasma and bfg turrets.
	!*) Turrets can now attract the aggresion of the monsters! Now the turrets are exposed from monster attacks!
	*) Patcher's price for reparing or upgrading are not health dependent.
	*) Repairing turrets can now grant 1 point of experience, no dices.
	*) Upgrading turrets can now grant 5 points of experience.
	*) Generalizing the code for the turrets.

#### (28 - 31 / 1 - 1 / 2 / 2022) [Refundable Turrets + Sprites + BFG Turret!]
	!*) All the spawned turrets by players can now be refundable.
	// If you place a turret in a blocked area (obstructed by something), or placed in liquids. The turret will simply not spawn, and instead you get the deployer back to your inventory, to try it again.
	*) Boomer cannon will no longer lock you up if cheating with idfa or idkfa cheats. (And if it does, altfire should take it from you)
	+) New sprites replacers for the Chaingun, Tesla and for the BFG Turret!
	*) Players can now die with their good ol' gibs.
	*) War-mech sprites renamed in order to avoid confusions.
	*) Fixed the patcher and prettyfied the patcher's ACS code.
	!+) Yes, The BFG turret is here :3 (In code, not accesible yet.)
	// This Resistant bastard fires 2 BFG Balls at the hordes.
	// The slowest turret in the game in building and firing speed. But, the most brutally harmful one! 
	// This turret should be built by the commander only, for 20000 credits.
	
#### (27 / 1 / 2022) [Repeater's fix]
	*) Refactorized the heat calculation code for all repeaters.
	*) Repeaters will insta-lower if the player dies.
	*) Now the heat factor of the repeater can grant a greater damage bonus.

#### (26 / 1 / 2022) [Flinger's Alt fires]
	+) Now the flinger can do a new alt-fire, throws a grenade that explodes on contact.
	+) Now the Expanding G. Flinger can do a new alt-fire, throws a cluster grenade that explodes quickly, and drops the mini grenades, this can give you the capacity of throwing multiple mini grenades in a wide range.
	*) Balanced the spread plasma's primary fire more, buffing it in the process.
	*) Nullified the knockback caused by the last set of projectiles on split for the spread plasma's primary fire.
	!*) Mini-grenades, spawned by the cluster grenades from the Expanding G. Flinger now they explode on contact, no more lame waiting! It's way more satisfactory.
	*) Expanding G. Flinger will use 2 grenades per shot, in both fire modes.

#### (24 - 25 / 1 / 2022) [Tweaking projectiles and some guns]
	*) Modified the shell blast code, giving it ripper to each pellet. And factorizing it in the process.
	*) Now the spread plasma gun primary attack will now make splitable plasmaballs on impact!
	*) Now the advanced plasma gun secondary attack will now make a big plasma ball that causes a lotta damage on impact, spreading 8 advanced plasmaballs that chases enemies arround. Launching this attack will cost 10 cells from now on.

#### (17 / 1 / 2022) [Little Touch]
	*) Modified the code for the bullet, shotgun, rocket and plasma turrets.
	-) Deleted the old sprites for the turrets. 
	*) Deleted the setslot part from the keyconf, already defined on the player class.

#### (4 - 16 / 1 / 2022) [New turret sprites, Patcher gun! and stuff]
	*) Now the tracing of the Plasma Rifle advanced, will now stop chasing, after 5 seconds of flight.
	*) Now the Hell-trigger powerup is added on the shop.
	*) Re-factorized the weapon names and descriptions, creating the Language.weapons file.
	!+) Finally a new we-TOOL, yes tool! The Patcher Gun!
	// Fix turrets/dispensers/drones paying 10 credits per valid shot!
	// Shows the buildings health at the aim of this tool!
	// Also is cappable of stunning enemies!
	// 5% chance for Experience Point for each turret fix!
	+) New sprites for the bullet, plasma, rocket and shotgun turrets!
	// Im fixing the dissaperance of the turret bases and other bugs with these sprites, Im tired.
	+) New sprites for the Temperance rune!
	

#### (1 - 3 / 1 / 2022) [Runes on the works (4), Sorting stuff]
	*) Created new language separated files, for runes, techs and command descriptions.
	-) Reduced the speed of players to 1.0
	*) Changing inheritance from PlayerPawn to DoomPlayer, for testing the skins.
	+) New sprites for Health, Ammunition, Blast, Defense, Rampage and Resurrection runes!
	// I'm not the best graphic designer, but these sprites will do the job. Until I get better ones.
	+) More voices. With echo and demonic sounds on the runes.
	+) Health rune will now drop blood drips, overheals 10 hp (15 for the rune wielder).
	*) Now, health rune blood drips will appear more often, and between 2 and 5 drips.
	+) Ammunition rune will now drop satchels, they re-stock a little your ammo.
	*) Now, ammunition rune's satchels will appear more often, between 1 and 3 packs.

#### (31 / 12 / 2021) [Sounds, announcer sounds on runes]
	+) Added some template sounds for the rune pickup
	*) Factorizing powerups, and items.

#### (30 / 12 / 2021) [Sprites, and gfx for Temp. Rune]
	+) The map markers are re-added again.
	+) Added some sounds for the temperance rune.
	*) Modified the original script, in order to play the proper sounds.
	+) Added some effects for the armor breaking in the temperance rune.

#### (27 / 12 / 2021) [Autoload SSG' bouncy pellets]
	-) The Autoload SSG, loses it's ability to cause knockback on monsters.
	+) Instead, now their pellets can bounce arround the room, "ripping" the monster who gets hit by the bounce.
	// Use the walls to spew those peelets across the room!

#### (25 - 26 / 12 / 2021) [Runes on the works (3), Item Drop Overhaul]
	*) Changes made for the runes.
	// Health: Implemented the extra-health mechanic.
	// Ammunition: Added the chance to get infinite ammo. Works properly.
	+) 2 Runes runes added. (On code)
	// Soul: 100 Kills = 1 Free Soulsphere.
	// Resurrection: Activates a free Megasphere when you're almost done for. One-time use.
	*) Some more organization in the runes decorate files.
	*) Now, rune effects are activated by custom inventories, for the sake of order and simplicity.
	*) Moved the Teleport effect script from fp_decsc.acs to the fp_event.acs
	*) Re-added some missing sprites for the demonic wall, and other sprites.
	+) Added some sprites for the blast effect.
	*) Re-written the Prometeo Protocol script. Uses the power of the Event Scripts!
	*) Modified the drop chances, converting the chance from integer to float
	-) Removed the senseless random actors for dropping items.
	*) For all monster classes, a Medikit has a chance to spawn with 25%
	*) Now the Upgrade list will show each half second each time you step in a health or ammo pad.

#### (22 - 24 / 12 / 2021) [Runes on the works (2)]
	+) Some few new runes are being added.
	// Health: Stimpacks, Medikits, and Armors are more common, (wip) Any source of healing gives 50% more of health.
	// Ammunition: Ammo satchels (Right now, small ammoes) are more common; (wip) Sometimes, firing will not consume ammunition.
	// Fortune: Credits are more common, Monsters drop items more often.
	// Temperance: The damage is deducted on the armor, causing it to deteriorate faster, however, as long as you have armor, your health is left unharmed.
	// Blast: (wip) Any damage recived, will create a blast, pushing surrounding monsters.
	*) The item drops are separated in a new module, fp_itemdr.acs.
	*) Now, when an item is dropped by monsters, the item fog and sound will show in battlefield.
	*) Now, the credit shower will be summoned more often depending of the type of kill and monster.
	-) A little bit of a nerf in the armor damage absorbsion just to test the Temperance rune.
	-) Removed the decorate spawning of credits, now this credit shower will be summoned on ACS.

#### (zan3.1)-) (8 / 12 / 2021) [Timer on SF and Cf maps]
	*) Small fixes on the changelog.
	+) Added the sf_guardianlength cvar, this will let you control the guardian wave warning time.
	+) Added the duration timer, for the SF and CF maps! Now you will know when the game will finish.
	*) Fixed the Prometeo Protocol bug, if it's active, it persists the budda state when traveling to the next map.

#### (zan3.1)-) (5 / 12 / 2021) [Some extra stuff + fixes]
	*) Recovered the missing sounds.
	*) More Ranks implementing.
	*) Extra techs are being implemented too.
	*) Now when the states are reloading the killstreak will not jump the message.

#### (zan3.1)-) (23 / 11 / 2021) [Fixin Bug]
	*) sfp_Changelog fixed (needs testing tho), should do justice in showing the big changes.
	*) Modified the Showcase text to show the big changes.

#### (zan3.1)-) (10 / 11 / 2021) [Smoll rune tweak]
	*) Smoll fix on the Rampage Rune.
	*) Forgot to add the last commit on the changelog.

#### (zan3.1)-) (3 / 11 / 2021) [Runes on the works]
	+) Added new runes, rampage and defense.
	// Defense grants you 15 ticks (1/2 second) of invulnerability for each damage taken. Great against fast attacking demons.
	// Rampage grants you a x1.5 Damage multipler and Invulnerability per each enemy killed, for 8 ticks (almost a 1/4 of second). The time is stackable, the more you kill, the longer it lasts.
	*) Powerup Hud will take care of the Runes display even for the infinite duration powerups.
	+) New events for player damage and monster kill added, so much wacky stuff will happen there!

#### (zan3.1)-) (1 / 10 / 2021) [A... Damage tracker?]
	// Just forked the whole sf+ repo to test it with the new build.
	+) Now the monsters can call an event script to tell the damage done by the player... huh?
	// This... this, will change the xp system.

#### -) (2 - 3 / 03 ,28 / 09 / 2021) [Added Powerup HellTrigger, Re-organized res part]
	// 
	!+) Added an new powerup, Hell-trigger!
	// Allows you to fire fast, and with infinite ammo for a short time!
	// For now it costs 5500 credits.
	// In the powered-up version, this effect holds a bit longer.
	*) The powerup upgrade for the players has been split in 2 upgrades, one upgrading the offensive powerups, and the other the deffensive powerups. It's all your choice if you want to go defensive or offensive.
	*) Re-Organized the resource part, deleting all the wad containers, in order to keep it in a single pk3 mod. 

#### -) (23 - 24 / 03 / 2021) [Autosave Player Stats & few touches]
	+) Now the game autosaves your progress each 10 seconds in the game!
	// Saves weapons, items, stats, and current upgrades (player and mech)
	*) Mech upgrades now will be shown in the stocking pad.
	*) Small touches in the kill streak hud, just to make it a bit cleaner.
	*) Inventory, Player & Kill-Streak huds will clean itself once the player disconnects (or spectates).

#### -) (11, 16, 20 / 03 / 2021) [SBarinfo revamping, Ammosphere arises]
	*) Now the full screen display has been updated with a better font and display.
	-) Removed the old item list on the fullscreen hud.
	+) Now you can see what are you holding up! The items you got will be shown in the lower HUD!
	*) Some touches on the powerup and armory items on the terminals.
	*) Created a new folder (Bars) to hold up the sbarinfo files in their separate places just if I need to edit something.
	*) Armor-Repair dispenser's effect ha been patched up.
	+) Now the ammosphere is now buyable on the health terminal!
	+) Ammosphere with the powerup upgrade, there is a 50% chance of not being consumed upon use!
	-) Ammosphere's max capacity drops down to 1.
	+) Different messages will be displayed upon enter, death and disconnect events.
	
#### -) (4 - 7 / 03 / 2021) [Giving the touches]
	*) De-hardcoded the extra item shop in the ammo terminal.
	*) A bit of testing fixes for the turret.

#### -) (23 - 26 / 02 / 2021)  [Tinkering and selling turrets, and some fixes]
	+) Shotgun and Chaingun turrets can now be displayed in the standard HUD, added with some new custom item inventory :)
	+) Ohoho! Shotgun and Chaingun turrets can now be pursacheable on the ammo terminal!
	*) Now the turrets will drop the smoke if they're low of its 50% of their health
	*) The turret base now will be destroyed once the head is down.
	*) Now the turret displays an explosion, with fires and stuff.
	*) Prometeo protocol's invul effect has been nerfed to 5 seconds.
	*) The extra effects for prometeo can be displayed on the game.
	*) Ammo giving script is back to normal.
	*) Fixed the Rank titles for the old an new hud.
	*) Fixed a bug on pursaching weapons, after upgrading a weapon, the base weapons can be brought back but with no chances to upgrade it.
	*) Mech Sync upgrade now costs 10 U.P.s, that thing is waaay too powerful to let it go cheap.
	*) Mech Sync upgrade will only appear in the shotgun frenzy maps.

#### -) (6 to 11 / 01 / 2021) [Relase! v0-t13] [Mech nerfs and fixes]
	+) A new Mech Upgrade! Efficiency: Reduces the time on the repairings, rocket reloading and autorepair intervals.
	*) Mech Rocket Upgrade price rises to 5500.
	*) Slowed a bit the rocket reloading time for the Mech. You can restore it with the efficiency upgrade.
	*) Returning the mech back to the base will have a delay penalty depending on the health. Just to discourage the insta-healing of the mechs.
	*) The mech moves a bit more faster in the base level, but it's upgrades does less effect, maxing it up will make the tank run like a normal marine.
	*) The mech exit at the entrance no longer will be instant. If you need to hop off the mech, pass to the entrance and press use. (It's still insta-exit)
	*) Fixed up the cmd list, now it should show to the players.
	*) Pistol now it should'nt use the same clip that uses the spitter. That and with other tweaks to it. (thanks BathySalts!)
	*) Stimpacks now heals 20 hp.
	*) Upgrade reminders show behavior has been changed too. Now they appear and shine.

#### -) (1 to 3 / 01 / 2021) [Starting with a good feet]
	*) Rewritten the CMD event handling system, and optimized the cmd terminal.
	*) Turret Rail in the ammo terminal should be given after pursache once again.
	*) Prosesing phase 1 and 2 can boost up the enemy bounty for the players and commander together!
	*) Enemies killed with cripple pulse will not grant credits to the player. (However, the commander can gain credits for that)
	*) Auto-Researching's Script has been revamped too, now notifying the players the new researchs on CF and SD maps! (Also, stimpacks and adrenaline can be given with this revamp.)
	*) Other smoll fixes.
	// 2020 was filled with updates, with more new mechanics, less bugs, and more. (with coronavirus and all ._.)
	// So for a 2021 goal, I'll bring this mod up to the v1, the version where the maps can be added.
	// I've still got some ideas left to add it in, so expect it to be updated =)

#### -) (23 to 26 / 12 / 2020) [Winterish Hotfixes]
	*) Fixed a glitch which let's you create turrets, but without checking the credits.
	*) Now the commander should check the terrain, if the spawning of a turret or dispenser is being blocked, or placed in liquids (wip) the spawning will fail, but the team credits will be refunded.
	*) Hidden some spamming on the server log console.
	*) The turrets shall now delete themselves with the base included.
	*) Now the kill-streak flow will not be interrupted by the building of a deployable item.
	*) Spawnshield should work again (needs some testing though)
	*) Pressing F12 (Coop Spy) will force you to look at the commander screen.
	*) Small fix on the sf_doorholdtime cvar.
	*) Removed the useless rune sync from the player upgrades. But this is'nt the last time you see it.
	*) Other smoll fixes.

#### -) (23 / 11 to 18 / 12 / 2020) [Relase! v0-t12] [Bye buy.py and play.py, Hello pack-o-daemon!]
	// Miss me?
	-) Like the commit said, the buy.py and play.py scripts are deleted.
	+) But now they're replaced with a parallel project that I've been working since a month, pack-o-daemon!
	// It's the build and play scripts, but in a GUI interface. Really it's the same thing.
	*) Now the Samu-Terminal old folder structure is now back to action!
	*) Renamed back the file extensions from .ach to .acs to make the pack-o-daemon acs compilation work.
	*) Cyberdemons will no longer be harmed by their own rockets. However, they're vulnerable to the area-damage of explosives!
	*) Updated the README.MD regarding about the pack-o-daemon addition.

#### -) (13 - 14 - 15 / 11 / 2020) [SBARINFO and Mech related stuff perks]
	*) Re-arranged the kill counters, for a better comprehension.
	+) Now, a timer should be displayed when the mech is on cool-down phase on the normal status bar.
	*) Now the timer should display correctly, forgot to add that extra second to make it work.
	+) Small new icons for the normal status bar, only to reference the mech status.
	*) Small fixes on the Mech buy page, on samu-terminal, also, you can check out the current upgrades you got so far.
	*) Small touches on the Mech in cf04.
	*) Since the plasma turret upgraded is overwhelming on cf04, the cacodemon waves from the rear attack will spawn more (and appear like a jumping ambush :D)

#### -) (11 - 12 / 11 / 2020) [Map Doors, Sector Cap, Mech and HUD fixes.]
	*) Now the doors should open-close properly in the SF maps!
	+) Now, the old hud will display the mech status, which it shows the current time for re-using a mech!
	*) Now, when you hop off the mech, you should wait a small cooldown of 15 seconds.
	*) Small touches on the SF04 map. Cursed AF.
	*) Mech users shall now gain experience and credits!
	*) Some more fixes on the sector management scripts.
	*) Moved the icons for the normal status bar a bit. It's a lil' bigger.
	*) Now the kill streaks should be seen in the normal status bar.

#### -) (10 / 11 / 2020) [Mechs touches and addons. SF04 map turrets fixed.]
	*) Alright, map SF04's map turrets should be cleared and occupied correctly.
	+) Now, you can look up the current mech upgrades when using a mech.
	*) This time the Mech factory door can be used again to open the entrance, just like always.
	*) The use key will no longer exit the vehicle inmediatly, but instead, you exit as long as you hold use for 1 second.
	// Meant to let the mech players use the door entrance in case they got stuck once again.
	+) A small Mech Upgrade is here, Auto-Repair!
	// A stereotypical regeneration upgrade that it does'nt take too long to work!
	+) Soulspheres and Megaspheres, (With the Mech-Sync upgrade) are now cappable to heal the Mech units!
	// Although, they don't over heal it, sadly.
	*) Other small fixes...

#### -) (2 - 6 / 11 / 2020) [Scalable Monster HP and Player Damage]
	*) Game is getting high on players? Well now you can change the incremental scale for the monster health and the player damage!
	// Since the game get's harder when the server gets more popularized, it's completly fair to add this.
	// Both things works when the player count rises to 3 and adobe.
	+) Added a bunch of cvars. All of them for the server.
		-) sfp_monsterhpmult, to set an incremental percentage depending on players, in monster health.
		-) sfp_monsterhpmult, to set an incremental percentage depending on players, in player damage.
		-) sfp_dropcredits_delay, to change the delay time between droppings.
		-) sfp_dropcredits_nostartcredits, to only drop the current credits without using the starting credits. Leave this activated to reduce exploits.
	*) Some more fixes upon the game variables.

#### -) (1 / 11 / 2020) [Hotfix 5]
	*) Re-factorized the variable setting for each sf map.
	*) Now, when a cvar is set to 0, the map will load the default variables.
	*) SD maps have an editable time between waves, use sf_doorholdtime to change it!
	*) SD maps will now sound the starting horn (and the timer beeps) once the game starts.
	*) Some other fixes

#### -) (30 - 31 / 10 / 2020) [Hotfix 4 + A Greedsphere]
	+) Hidden on the game, only spawnable with summon command, but... Meet the greedsphere!
	// x2 Credits for 15 seconds! (30 with the Player Up. Powerup Upgrade)
	*) Fixed up the spawning tids for the SF maps, that should set the monsters correctly.
	*) Just to add a little bit of softness for the SF02 map. Archons of hell and Dark Dogs(New!) will come to cause some grief!
	// Not a big fan of the difficulty spike when the cyberdemons come.
	*) Now the damage hud, can be streched depending on the aspect ratio!
	*) Now, the batteries should'nt be revived by the archviles.
	+) Added the cvars: sfp_minrecap (Minimum monsters before recapturing) and sfp_monstercap (Max monsters)

#### -) (28 - 29 / 10 / 2020)
	*) Re-factorized the inventoy item's decorate. Less code, more read.
	+) Added the fp_puhud.acs, showing you the current powerups you got in your blood!
	*) Now, when going no-hud, the old hud will not be shown.

#### -) (24 / 10 / 2020) [Hotfix #3]
	*) Clearing some of the few log messages I left out.
	*) Deploy TID Assigner is set to the dispensers too.
	*) Build.py should compile the acs before packing.

#### -) (22 - 23 / 10 / 2020) [Hotfix #2]
	*) Removed the welcome messages from the server log.
	*) Gave some fixes on the soundtrack mixer script, now it should work properly.
	*) Guardian wave can now terminate the sector management main loop script.
	*) Turrets and drones TID assignment has been separated from the player tid. For the monster kill script fixes.
	*) Small fixes on the credit display thing.
	*) Auto-Use scripts should act faster now.
	*) Resetted the monster limit to 250.
	*) Now the Turrets and Drones will properly grant credits. 
		// For the drones, they have a 25% to grant a kill (experience).
	*) Boss-waves should grant more credits and experience now.
	+) Added the fp_cons.acs, just to hold all the variables. (Not being used for now.)

#### -) (21 / 10 / 2020) [Some late fixes]
	*) Modified the Kill-Streak Clientside scripts, now the number should scale pretty well on clientside.
	*) Some small touches on the sector management scripts.
	*) Forgot to show the player upgrades for the health terminal, now it should be shown

#### -) (20 / 10 / 2020) [Quick Fixes & More Fixes]
	*) Rewritten the sector management script for the sf/cf maps.
	*) The non-risked cores, will be de-activated. (unless i find a way to animate them in this state) For the archvile protection, and for not breaking the sector flow so quickly.
	*) Put back the Battery script again.
	*) Some more fixes on the music player, minding on initialization.
	*) Fixing up the dropping script on the enter script...
	*) Alright, Health and Ammo dispensers are placed in their respective cmd buttons, as it should be.
	*) Merging up some quick fixes from zanieon.

#### -) (17 - 18 / 10 / 2020) [Good-old music is here + some fixes]
	*) Removed the +nointeraction flag for the spready grenade. (Why?)
	*) Made the tank nails a fast projectile, improving their current speed for all levels.
	*) Gauss J Repeater is kind of beefed up. Damages the first enemy more than the rest of them.
	-) Repeaters will spin-down before switching to another weapon.
	+) Alright, now sfp_oldsoundtrack works!, when you feel nostalgic, put this to true, and have fun!
	*) All the acs for the maps we're been library-compacted! (1 step close for mapping!)
	*) Some cleanup later...
	-) Turret health bar will no longer be coloured depending on the health (stoopid zandronum)
	*) Smol fixes not worth mentioning.

#### -) (14 - 15 / 10 / 2020) [Being freindly to the players.]
	*) Fixing up the messages coming from the drop credits module.
	*) Now sfp_dropcredits contains a delay time between uses, to prevent over-charging the server.
	+) Now, I can print the most important changes about the game with the showcase.txt!
	+) New commands! sfp_ccmdlist (shows all mod commands) and sfp_changelog (shows the most relevant changes). 
	*) Some more touches in play.py and build.py files
	+) Now all players will be greet with a simple welcome message :) (Quick tutorial soon!)
	// If you find this annoying, disable it with sfp_welcome 0.
	*) Updated the readme.txt a bit more...
	*) Updated the buildinfo.txt files for the core and resource part.
	*) Not implemented yet, but, sfp_oldsoundtrack will make it sound the good old music, just for nostalgia peeps.

#### -) (13 / 10 / 2020) [Any spare change?]
	+) Now marines can drop credits! 
	//	Use sfp_dropcredits (amount) to drop credits!
	+) New CVAR added! sfp_allowcreditdrop, this will allow the already shown command.
	*) Small fix on the commander camera.
	*) Now airstrikes waves goes faster than the usual.

#### -) (12 / 10 / 2020) [Turret deployer hot-fix]
	*) Now the base clase for the turret has been patched up (let's hope they don't break in mp again.)
	-) Removed the turret destruction in mid-deploying. That was a low punch tbh.
	*) Now heath dispensers, can shield you up!
	// Armor repair and expansive restock will grant more protection.
	// Yet again, must merge the zanieon changes to fix up somethings.

#### -) (9 - 10 / 10 / 2020) [Turret touchups, and a Shotgun Turret]
	*) Generalized the guardian wave end script for all the maps.
	// At least if this fails it will be repeated on the other maps.
	+) New icons for the turrets in the commander terminal.
	// Going to commit on this point, I should merge the Zanieon fixes.

#### -) (1 - 8 / 10 / 2020) 
	*) Some clean up on the turret's code. (Needs mp testing if they still works as usual)
	+) The turret deployer decorate code has been generalized and improved a lot.
	// In fact, the columns will always vary themselves on their building state.
	*) The turret progress bar now can warp itself to the deployer, so no more flying bars!
	+) The turret construction time can be modified though decorate! and in a simple way to do it.
	// That opens me another possible tech in the game.
	*) The blue particles will not be rendered in large distances, so just 512 map units will be good.
	// Spamming the turrets will always cause lag, for the shieton of sparks puked by the columns.
	// I'm just saving you the lag spikes caused by the sparks, maybe I should do this with the other casings, and blood gibs.

#### -) (21, 29 / 09 / 2020)
	+) Shotgun turret is finally here!
	//	Thank you madcat for the sprites!
		The shotgun turret, (only on SF maps for now) can now shoot shells against the horde!
		Slightly resistant than the bullet turret, and fires twice before recharging.
		With this, and with the incoming BFG turret, the turret research access might vary a bit on the commander chair.
		But for now, adding this, and the bfg turret, should do the trick.
		
	+) Just as a small addednum, now turrets can display health!
	*) Fixed up the changelog dates xd

#### -) (14 - 15 / 09 / 2020) [Better Air Strikes, and incoming Pulses.]
	+) 2 New pulses WILL be fully implemented, SMITE and HEAL. (WIP)
	// Wait, HEAL?, we did'nt had that already?
		Yes and no, we had REVIVE, which actually fully heals all the Cores (Or at least the risked one.)
		Heal will repair ALL Turrets in game (Thought it actually heals gradually all the cores right now, but I'll get that idea working soon.)
		Smite is a cripple pulse, except its limited to the risked sector, and deals a whoopin 3000 dmg to the demons on the sector!
	*) Small touches with the CMDer Terminal.
	*) Replacing the old message functions with the new notifiers...
	+) The spot light of this 2 days, an Air Strike menu overhaul!
		Now, with the Air-strike menu, you can make Point Targeted attacks!
		The amount of attacks made in the targets can be changed! (Between 1, 3 or 5 projectiles per target)
		The airstrike will no longer be executed after making a line of targets. INSTEAD, you can plan the air strike strategy and THEN Activate it with the button!
		Also you can cancel your Air-Strikes as well.
		Depending on how complex is your plan, and how many attacks you require, The price of an air strike will vary.
	*) Now, if a sector is re-captured too quickly, the timer will be reset (and re-shut all safe sectors doors).
	*) Yet, some small other fixes in the Tip notifications...
	*) Oh yeah, made some small touches on the blood particles, let's hope it reduces the incoming lag after doing an explosive attack... I think.

#### -) (11 - 12 / 09 / 2020)
	-) Removed the old progresive scripts for the construction and re-charging.
	*) Revamped the progress counter and timer scripts, for a more general and extended use!
	+) Added the fp_ptdir.acs file, which it contains a wrapper for the timed notifications.
	*) Re-factoring the scripts a bit in the f_tip.acs file
	+) Not an official feature. But, a small new core pulse is coming up to the game.
	*) Now, if you spawn a turret in the command chair, the space will be checked before charging credits to the team.

#### -) (9 / 09 / 2020) [Flak dualshot(? is here, and some more fixes]
	*) Now, if a turret is miss-placed (for occupied sector or things like that), credits will not be charged.
	*) Yet another small fix on the play.py
	*) Sticky grenades for the sticky flinger has been tweaked, fixing a couple of bugs.
	*) Re-Arranging the carpets for the samu-terminal

#### -) (5 / 09 / 2020)
	+) Added a mirrored saw for the dualshot's upgrade: Razor Saw.
	+) Added an alt attack for the razor saw's dualshot upgrade, letting you to fire saws 1 per time!
	*) Small fix on play.py

#### -) (29 / 08 / 2020) 
	+) Temporally added a new weapon uprgade for the dualshot. The Flak Dualshot
	+) Added the fp_blur.dec file just to add the blur on the flak shards.
	*) Small experiment with the flak projectiles.
	*) Some more edits on the rusher monster set. (needs some mp testing)
	+) New CVAR created: sfp_monsterset, useful to define which monster set you want to use. by default, this is 0 (the classic monster set)
	*) In the TEST map, now the monster randomizer buttons can be shoted!, I suggest you to use your common pistol.

#### -) (28 / 08 / 2020)
	*) Edited the rusher demon set. It consists mainly on the fast demons, starting with zombies with some suicide bombers.
	// In later levels, you will face a big demon stampede! Along side of the barons.
	*) Small fix on the TEST map on the monster randomizer.
	*) Reduced the archvile's target range from 896 to 512. I know, we hate those sniping archviles.
	*) Modified the Demon, Mech Demon, Blood Fiend and Stone Demon. Specially on their attacks and HP on the Stone and Blood fiends.

#### -) (26 / 08 / 2020) [Experimenting with Monster sets]
	+) Now in the TEST map, you can see the monster waves separatedly. Check out the Monster Randomizer section!
	+) New file fp_aidspawn_rusher.dec, to create a new monster set. Rusher set.
	// Fast and weak monsters, pretty dangerous in masse.
	*) New parameter on play.py: -xa, this will skip the ACS compilation. 
	   Cool if you need to edit your maps, without compiling all the acs source code again.
	*) Now acs compilation will clear all old compiled files for cleaning up!
	*) Small fixes on the play.py file.
	// Yeah, not so much progress over here due to some health issues, but im pretty good for now, thanks for asking. 

#### -) (19 / 08 / 2020) [Dmg. Hud, Status bar tweaks and fixes]
	+) Here it is an experimental Damage hud. Resided on fp_dmhud.acs
	*) Moved the sbarinfo only scripts to a new file fp_sbinf.acs
	*) Simplified the health code on the SBarinfo, let that decision-taking to ACS.
	*) Now the health numbers on the normal Staus Bar will light itself depending on the health state.
	+) Small reminder added on the fp_monster.dec just in case I forgot how to add another monster.

#### -) (15 / 08 / 2020)
	+) The zombie scientists joins to the bestiary!
	*) Simplified the decorate code for the demon wave sets. made the fp_aidspawn_default.dec and fp_aidspawn_survival.dec

#### -) (14 / 08 / 2020)
	*) Now Player Upgrades will crank up the difficulty.
	+) New CVAR added, sfp_killstreakhud, this will help you to show and hide this hud.
	*) Now defending the batteries can grant you Credits and U.Ps
	*) Edited slightly the battery or core attack warning.
	-) Deleting some of the old code from the pmen.acs, we're not needing that anymore at all.
	*) Made a teleportfog replacement to apply the spawn shield effect globally.
	*) Some more fixes...

#### -) (13 / 08 / 2020) [Kill-Streak system implemented]
	+) New file fp_kshud.acs for the Kill Streak HUD.
	+) Now the Kill-Streaks will be displayed each time you... kill.
	*) Modified the prices of the Player Upgrades a bit.
	*) Modified the Kill-Streak formula for the milestones.
	+) Now you can see the high score kill-streak in each run.
	*) For now, the max milestone level for the kill-streaks are capped to level 10.

#### -) (12 / 08 / 2020) [Player Upgrades are ready to go!]
	+) The Player Upgrades are now ready to be used in the health terminal!
	// For now all the upgrades cost 1 U.P. better balance those prices.
	+) Added the scale functions for the images in Samu-Terminal.
	+) Now when you break a kill-streak milestone, you will hear the old promotion sound.
	// All it lefts is to get a better display for a kill-streak counter.

#### -) (11 / 08 / 2020)
	*) The H.Terminal Player Upgrade pages is now in WIP.
	+) New icons for the Health Terminal Player Upgrade page!
	*) Silly fix on play.py

#### -) (10 / 08 / 2020)
	+) New file fl_PupDir.acs has been added, introducing the Player Upgrade directory!
	*) All of the Player upgrades inside are finished. It just needs their respective page.
	*) Small debug fixes.

#### -) (9 / 08 / 2020)
	*) Changing the .txt, to .dec extensions for notepad++ access.
	*) Moved and renamed upgrades.dec to fp_p_upgrades.dec, it is inside of the gameobjects folder.
	*) Some more experiments on those health terminal upgrades.
	*) Some more re-factoring on f_StockP.acs
	+) New streak system!, now here you can gain additional upgrade points!
	// Now you have a reason to keep yourself alive!
	*) Implementing some more H.Terminal upgrades...

#### -) (8 / 08 / 2020) [Fix n Tweaks, H.Terminal Ups on progress...]
	*) Now health dispensers can give 10HP to the player per 6 tics.
	*) Some small implementation of some new health terminal upgrades...
	*) Refactorized f_StockP.acs for a wider and better display of the unit upgrades.
	*) Small tweak done on the SBARINFO for some of the up-coming Health Terminal Upgrades..

#### -) (5 / 08 / 2020)
	*) Now the commander kick script will teleport the player outside of the chair, to let the others command.
	*) Found a bug on spectating while commanding, I should fix that soon.
	*) The commander terminal will restrict only 1 player (preventing another player to command)
	*) Giving the inventory "SamuTInv_ForcedExit" will force the exit for the player when it is on the terminal. (needs some testing on MP though)

#### -) (4 / 08 / 2020) [Build.py and play.py tweaks]
	*) Some more edits on the play and build py files.
	*) Relative paths are now supported on the play.py and build.py files.
	+) A new file has been added for the building scripts, funs_n_cons.py!
	*) Now the project.ini file will now read relative paths.
	*) Updated the Readme.md file, addresing the build instructions.
	// It was about time to update that readme file.
	*) The changelog will be written on the core part!

#### -) (3 / 08 / 2020) [Changelog moved. Play.py tweaked.]
	*) Markdownified the changelog. Just because fuck it.
	*) Moved the changelog outside of the soruce directory, so it could be shown outside of the repository.
	*) Splitted the to-do list from the changelog.
	*) Moved the achivement guide outside of the source directory.
	*) Some touches to the play.py file, just to get a good setup in the temporary pc.

#### -) (5 / 07 / 2020) [I'm taking a small break...]
	// Took a small break for modding, I'll be back in 12 - 7 - 2020 or sooner.
	*) Now the ammo is going to be resetted, for each player entering in game, this is just to take the personal backpack effect.
    
####  -) (29 / 06 / 2020)
	*) Team Credit rewarding has been fixed, on SF maps, when you kill "hard enemies", your team recives 3 (or 5) times the reward. Too much reward for let it go wander arround!
	*) When you kill a "hard enemy", the display should show on sfp_earningdisp = 1

####  -) (28 / 06 / 2020) (Test 11 Relase!) [Life save upgrade for Mechas, yet more fixes.]
	-) Sandbags will no longer cause infighting on monsters :/
	*) Turrets will now fire through sandbags!
	*) Bullet and Chaingun turret fire mode has been switched to the projectile mode.
	// Because Zandro is outdated, the projectiles will not have pitch.
	*) Arachnotron, Spider Mastermind and some more other monsters will fire though themselves.
	*) Nerfing a bit the Tankguns on their nails and rockets.
	-) Now mechas loses the ability to teleport back to the base. But instead, lets make that a feature.
	+) A new Mecha Upgrade has been added! Lifesave Upgrade!
	// When you press use (in a war-mech). You will be teleported back to the base.
	   This upgrade costs 30000 whoopin' credits to be installed!
	// Why so expensive? Well, you can attack and rethreat repeatidly without even minding of the wait time.

#### -) (27 / 06 / 2020) [Chaingun Turret now works on SF maps. And More fixes.]
	+) The chaingun turret is ready to be deployed on SF Maps!
	// Requires Advanced Systems, and it costs 2300 credits.
	*) Now refinery will give 2 (6 with pump 1 and 10 with pump 2 techs) passive credits.
	-) Again I had to re-order my folder structure in the Samu Terminal -.- play.py's being a bitch.
	*) Flame and tesla turrets will attack now on a range of 512 map units.
	*) Chaingun turret casings will now fade faster for performace.
	*) Created the fp_Junk.dec to store all junk throwed by turrets and sand bags.
	// For the sake of refactorization.
	*) Touched a bit the tank guns, and gave it a new file specially for it. fp_tankguns.dec 

#### -) (26 / 06 / 2020)
	+) The chaingun turret is coming in the game!
	*) Some file renaming, just for notepad++ acessibility.
	*) Re-ordered the folder structure on the Samu Terminal acs scripts.
	// What makes this turret special from the bullet turret?
	   Well, it fires everything at sight and it won't 
	   rest untill everybody in it sight is dead!
	// This will be implemented in the sf maps for now 
	   (untill I get a pickup sprite for it.)
	// The tentative sprite for this turret could be 2000 credits, but that's just me 
	   measuring how valuable is this badboy. 
	// Oh yeah, Thank you Captain J! That chaingun turret fits perfectly inside here!
	
#### -) (25 / 06 / 2020)
	*) Now the base turret will not duplicate its stand on spawning.
	*) Modified the particle effects for the turret/dispenser construction. 
	   To make it fade upon floor's touch. This will reduce the lag a bit upon spamming up the turrets.
	*) Replaced the plasma attacks for the plasma turret. 
	   Now it fires faster but it loses the ability to cause explosive damage.
	// Did you know the turrets can actually fire plasmas and cause damage 
	   like a rocket in the past patches?
	*) When the turret base is gone, now the turret head will die at the same time.
	*) Shell grenade's pellets buffed up to 7. Suceptible to Doom Random damage.
	*) No bfg splash for the spider demolisher, because its pretty OP on numbers.
	*) Modified the play script again, now on project ini you can specify the map where you want to test :D
	*) Also, now the acs compilation can be applied with folders and subfolders! (Thank you sirJuddington!)
	*) Now my old organization forthe Samu Terminal is finally back :D

#### -) (23 / 06 / 2020)
	*)Some more re-ordering, and python script fixes.
	*)Now the python scripts contains a loading bar :3
	// After all these changes, now I can work by directories,
	   and therefore, complie quicker builds!
	// However it broke me the file order made in the Samu-Terminal,
	   but it still works at least...
	// Now, next update should be on some more fixes, and then,
	   another testing release for the public.

#### -) (22 / 06 / 2020)
	*) Now the bats are replaced by some cute pair of python scripts! (Thank you Xaser!)
	*) Merged the sndinfo files into a single one. I should re-order that.

#### -) (16 / 06 / 2020)
	*) Fixed the fire ratio from the mecha guns in the nails.
	*) Fixed a small bug on samu etrminal where it overlaps the hud with the commander view.
	*) Some more reordering in the resource pack...

#### -) (13 / 06 / 2020) (Test 10 Relase!)
	*) Small fixes on some monsters on their xdeath states.
	*) Modified the Spider demolisher to let it enter on the monster fray.
	+) Spider Demolisher is now ready to destroy!
	*) Ammo counters for the standard hud can tell the amount of ammo, 
	   and what ammo are you using!
	*) Improved the exploding rocket launcher, and fixed up a bit.
	
#### -) (12 / 06 / 2020)
	*) Let's hope this time fixes the disappearing single upgrade weapons.
	*) Improved the railgun projectiles, now this, is what I call a Railgun!
	// I'd just edit the slug attack for the slug laser railgun later...
	+) Meet the Gasoline, the Flamer's new Ammo type!
	// Yeah, Sometimes I'd prefer to fire plasma with cells and flamer with gasoline.
	*) Small improvements on the weapons, and also renamed their tags.

#### -) (10 / 06 / 2020)
	+) Shell grenade is finally here!
	// This grenade will spit pellets across the map. 
	// Weak in it's explosion, but im sure you will enjoy it with your
	// Spitter's Shell Grenade upgrade. (This weapon can fire a pair of 'em!)
	*) Now Nerve Gas grenades can relase gas on the way! Just to cause some small 
	   grief on the enemy lines.  
	*) Tweaked the Ammo counter a bit, just to give it more contrast on the HUD.

#### -) (7 / 06 / 2020) (Test 09 Relase!)
	*) Now the texture warnings are (almost) gone! meaning more speed on loading!
	*) Some small fixes on the texture definitions...
	*) Small fix on building turrets, flames are flames, and teslas are teslas :p
	*) Separated the ammo in fp_ammo.dec, just to keep on track those ammos.
	*) Moved the texture definitions to the resource pack, for easier maintanbility.

#### -) (6 / 06 / 2020)
	+) Some more graphics, now focused on the ammo counter!
	*) Also, adjusted the graphics in the sbarinfo to let it work.
	*) A new game file has been created, the music pack!
	// If the music changes, only this pack will be affected, separated from the resource pack.
	
#### -) (4 / 06 / 2020)
	*) Fixed the miss-buying from the ammo terminal where you buy a mine,
	   and it mistakes with the p_backpack.
	+) Talking about that... the personal backpack is now ready to go! 
	// Grants you some ammo space, completly separated from your backpack given by the commander.
	*) Trying to clear some logs I've left up scattered arround.
	*) Hopefully, drones will not activate wrong lines on the map.

#### -) (1 / 06 / 2020) (Test 08 Relase!)
	*) Fixed up the disappearing bodies after being killed.
	
#### -) (30 - 31 / 05 / 2020) (Test 06 & Test 07 Relases!)
	*) Created some placeholding sprites for the explosive quadshot.
	*) Quadshot full replaced with the Quadshot explosive, just for the sake of the tests.
	*) A monster counter in the final fight can appear now in the screen to track the monsters remaining before the guardian wave rounds.
	*) Now the terminal has been fixed enough for being compatible with the Zandro's 3.0.1 stable!
	*) Some more small touchups...

#### -) (29 / 05 / 2020)
	*) Now the coins will chase you when you're pretty close of them!
	// Being brave is not exactly a reason to go for that penny in the middle of the disaster.
	*) Small fix on the death, asking me for the dang mecha.

#### -) (28 / 05 / 2020)
	*) Now the spawn algorithm has been refactorized for good!
	*) Now the spawn algorithm is now converted in the Decorate way.
	// This will allow the modders add the monsters inside the spawning algorigthm without even touching the acs behind it.

#### -) (26 / 05 / 2020)
	*) Some fixups on the monsters decorate, now appyling an almost universal kill script for all monsters.
	*) Now boss-like monsters (and hard-to-kill ones) can grant more than just 1 kill point!
	// There is a lot of stuff to fix. And i mean a lot.

#### -) (24 / 05 / 2020)
	*) Some adjusts	on the Quadshot, also doing another alternative version of it.

#### -) (23 / 05 / 2020)
	+) New Quadshot Sprites! Now as the Cntered SW''s Riot Gun! (thanks Mike12!)
	*) Now you can alt-fire the quadshot like a slower, but powerful and acurrate buckshot!

#### -) (21 / 05 / 2020)
	*) Fixups on the commander terminal so it will work in multiplayer.
	// This time, fixes should be done in the whole project.

#### -) (12 - 20 / 5 / 2020)
	*) Commander's terminal is now ready for action! (Fi-friggin-nally!)
	+) Sandbags are now back! (on the commander's terminal.)
	// Phew, now its time to test it on mp, and there you go!, the first version is ready to go.

#### -) (10 - 11 / 5 / 2020)
	*) Re-coding terminals to apply new functions and make them more maintainable.
	+) Added fl_techs.acs for more easier manuvering with the researches.
	*) Configured terminals to let it work with fl_techs.acs and the buildings.
	*) Defined all data from the command buttons for the next terminal, the Commander Terminal!
	// After this terminal and some more touch ups, A new relase will be created, wait for it!
	*) Modified the comander terminal to let the syncing work.
	
#### -) (7 - 8 - 9 / 5 / 2020)
	*) Heat indicator, and shell indicator (for repeater and buckshot guns) are properly displayed in the status bar.
	*) Some more fixups on the Samu terminal.
	*) Now, meet the copper, silver and copper coins!
	*) Buckshot refactorized, for easier maintability. Also a small touch up on the animation.
	// from +1, +2, +5 credits. //Soon rare gems to award!
	+) It's not implemented yet, but there is an alternative version for the quadshot
		//What if e let it behave like a ssg huh? Double Barrel Quadshot,(Octashot??)
	+) New fl_IDir.acs and fl_MUpDir.acs to keep track on mech upgrades and items!

#### -) (3 - 4 - 5 - 6 / 5 / 2020)
	+) Gave some new ammo graphic for the repeater.
	*) Some more fixes on the repeater
	+) Added the global kill script, which now can run in zandronum!
	*) Toying arround with the flinger's mine placer upgrade... i think i've buffed it a lot.
	// Sticky grenades are a thing in this weapon now!
	*) Re-coding the ammo terminal to apply the new functions i gained so far.
	*) Some more fixups on the f_wdir.acs file on the upgrade thingy.

#### -) (1 - 2 / 5 / 2020)
	+) New graphic on the heat indicator available on full screen mode.
	*) Some more refactoring on the WDir file.
	*) Changed the rail colors from gray-blue, to cyan-blue On the Gauss J. repeater.

#### -) (30 / 04 / 2020)
	*) Repeaters are now enchanced! To give it a bit more of punch.
	// The more you fire it, the inacurrate but stronger becomes!
	+) Some sprites added for thoe Advanced Plasma Rifle.
	*) Small fixes on the fl_wdir about the strings and such.

#### -) (29 / 04 / 2020)
	*) Replaced the rippering porjectile from the plasma gun advanced with a
		seeking projectile that explodes. Also the Plasma Gun Advanced can shoot 4
		plasma balls per shot, with powerful plasma balls.
	+) Fl_Wdir added and programmed. Here it will save all data from the weapons.
	// Later will be the turn for the items.
	*) Revamping the Ammo terminal, starting with the upgrade section.
	// It will work slightly differently than the last time, but its the same way to use it.

#### -) (28 / 04 / 2020)
	*) Function renaming applied for the most used components on samu terminal.
	*) The test map now supports up to 128 monsters to be spawned! (Also extended 
	   the arena for easier combat and debuging.)
	*) Terminals are avilable now near on the entrance of the monster arena.
		(Mostly, the health and ammo terminals.)
	*) Small fix on the Samu terminal about the Alpha tags not showing as first
	   priority.
	*) Now the first string button on Samu terminal can be properly hovered.
	// Yes, soon enough, new monsters from the Realm667 will make an apperance
	   here. But before that, i need to fix some behaviors on the monsters. 
	// I'll leave that casting up to the first version.

#### -) (27 / 04 / 2020)
	+) On the testing map, now you can fight with (almost) all of the enemies in a 1v1 mortal kombat!
		//Meant to see the behavior between each monster in the mod.
	*) Now the prices are more acessible to be edited.
		//In fl_prices not only you can change it, you can also create your own prices!
		//A documentation about that soon.

#### -) (26 / 04 / 2020)
	*) Some adjustments on the price script for acessibility pruposes.

#### -) (22 / 04 / 2020) 
	+) Some documentation about the acs source code. For the modders out there.
		(still WIP)
	+) Disclamers added on the readme file. 

#### -) (15 - 16 - 17 / 04 / 2020) 
	*) Doing some works on the Commander terminal (Oh shiet.)
	+) For Samu Terminal, now the image buttons can use the Hover execute!
		//In case you want to execute a script just on the hovering of the button.
	+) Some new icons! Just to give a different feeling in the Commander Terminal.
	*) Tank Guns are now akimbo'd!
		// Shoot nails and rockets together!

#### -) (13 - 14 / 04 / 2020) 
	+) Mech terminal is now avilable to use!
	+) New upgrades can be applied to the War Mech!
		//Tank gun Advanced is still there just for backward compatibility to the mech in cf04.
		//Now everyone will love the mechs! (Even if they're more expensier than ever.)
	*) Now items will not be used inside of the tank!

#### -) (12 / 04 / 2020) 
	*) The acs hud is now fully clientsided! 
	// If you miss this hud, go to fullscreen mode!
	*) Gave it some little touches, just because I can do it. :p

#### -) (10 / 04 / 2020)	Testing relases! (Test 04 & Test 05 relases)
	*) Fixed the terminal access to the heath and ammo terminals!.
	*) Net Comunication for the samu terminal has been fixed too!, no more packet loss!
	*) Team credits are given as it should be!
	
	//With this testing relase, now its up to enable the mecha terminal,
	  and then fix some bugs more to launch the public alpha!

#### -) (08 / 04 / 2020)	Testing relases! (Test 01 & Test 02 & Test 03 relases)
	//Just to put on test the Samu terminal capabilities in multiplayer. 
	  Im hosting this and sfplus_res.pk3 with it to TSPG.
	
	//I've been testing this in single player with local machines, 
	  but i must test this on multiplayer, on real multiplayer.
	
	//Thanks for Zanieon, Cap. Jace, and TDDR. I've catched some more multiplayer bugs to fix.
	//But after all of this unstability, the samu terminal is working real good!
	//The only thing was the net package saving thingy code. I need to fix that crap.

#### -) (30 / 03 / 2020)
	+) Now in sbarinfo shows the ammount of ammo in the stock!
	+) A small popup to show what has been researched by the player! 
		(use the strife's weapon/item/stats key binding)
	
#### -) (29 / 03 / 2020)
	*) In cf01, a line was changed to change tid to be only monster activable. (That was kind of a problem in that map)
	*) Some fixes on the Banner script.
	   Now with some conditions, the banners will show! (oh and display duration set to 30 secs)
	*) Now weapons are selected by priority order!
	   (The more powerful is, the most likely to be selected.)
	   You can thank me later when you deplete your favorite weapon. 
	   This will switch to the second most powerful weapon on your inventory.

#### -) (28 / 03 / 2020)
	+) Now the banner on the SF maps can dynamically change! (at least in sf01, sf02 and sf03)
	   also, its kinda funny to seee these banners show in the game.
	*) After some re-arrangements on the building requisites, 
	   Now Mecha-Factory and Marine command are written and setted how it should be. Instead of Demonic lab.
	+) More voices from cepstral, announcing the mecha factory!

#### -) (26 / 03 / 2020)
	+) Powerups avilable now on the genetics lab! (After a lot of refactoring in samu terminal!)
	*) Refactoring and re ordering of the terminal, just to make more cleaner code.

#### -) (22 / 03 / 2020)
	+) Card layout helper same as grid to help building the powerup pages.
	*)Still working on the powerup page.
	*)Some voices changed on the core. Just for a change of peace.

#### -) (20 / 03 / 2020)
	+) Grid helper to make grids in no time for the smau terminal!.
	*) Some updates on the testing map. Not included in the mod for now.

#### -) (16 / 03 / 2020)
	*)In samu terminal, made a parser to set the properties without
	bothering on the other component functions.
		//It's implemented in the image button though.
	+)Some documentation about the samu-terminal.

#### -) (15 / 03 / 2020)
	*)Small Fixes on the SBARHUD.

#### -) (14 / 03 / 2020)
	+)Added some icons to spice up the hud in sbarinfo.
	+)Multi Launcher now contains a second altfire!
		This altfire will shoot the same 3 projectiles but in a triangular spread.
		Nifty if you want precision over spread.
	*)Doing some small adjustments to the sbarinfo about the info of the game.
	*)Setting the right display to the respective gamemode in the sbarinfo.
	*)Buckshot will be given with ammo in the chamber.
		(Just for comfyness. You'd hate to buy an assault pack, 
		discharge all of your spitter gun and then switch back 
		to a unloaded buckshot.)
	*)Somehow... In multiplayer the game did'nt gave the cash after finishing a map, fixed that.

#### -) (12 / 03 / 2020)
	+)Got some sound, to make some achivements on this crack.
	+)Just wrote some ideas in the achievements.
	*)Some more reordering on the sound files, just for the sake of order.

#### -) (18 / 02 / 2020)
	Now a confont tip is now added to the display. To make a difference between what you got and what they gave you by other means.
	
#### -) (15 / 02 / 2020) 
	Lot'sa stuff that i missed xd.
