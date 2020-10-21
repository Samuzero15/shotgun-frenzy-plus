# Shotgun Frenzy Plus Changelog

## v0 - Before the beginning...

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
