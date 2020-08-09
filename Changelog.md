# Shotgun Frenzy Plus Changelog

## v0 - Before the beginning...

#### -) (8 / 08 / 2020) [Fix n Tweaks, H.Terminal Ups on progress...]
	*) Now health dispensers can give 10HP to the player per 6 tics.
	*) Some small implementation of some new health terminal upgrades...
	*) Refactorized f_StockP.acs for a wider and better display of the unit upgrades.
	*) Small tweak done on the SBARINFO for some of the up-coming Health Terminal Upgrades..

#### -) (5 / 08 / 2020)
	*) Now the commander kick script will teleport the player outside of the chair, to let the others command.
	*) Found a bug on spectating while commanding, I should fix that soon.
	*) The commander terminal will restrict only 1 player (preventing another player to command)
	*) Giving the inventory "SamuTInv_ForcedExit" will force the exit for the pllayer when it is on the terminal. (needs some testing on MP though)

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