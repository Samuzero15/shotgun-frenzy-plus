# Shotgun Frenzy Plus
A fork from Shotgun Frenzy (a Doom 2 mod) which adds more stuff for Zandronum.

## Shotgun Frenzy? Er... wut?
That's a Doom mod with some Tower Defense game style, fusionated with some elements from the RTS (Real-Time Strategy), and of course, the First Person Shooter in a single place, mixed up with countless waves of demons Invading your base.

The game loop is simple, buy some weapons, kill demons to rise your ranks to open new upgrades, protect the cores, until you survive (or not) long enough to face the guardian wave. Other endings are avilable up to the date.

The original mod was made by Wad'a'holic, but for unknown reasons he stopped the project and decided to move on Total Chaos.

## What is this?
This is a fork for Shotgun Frenzy.

## How did you get in here Samu?
Yet the development was'nt stopped at all, Greg339 (I think...) and T3h Player decided to launch a set of unoffical patches which it introduced some more fixes to the mod. Like the reducction of lag, balances on demons, cheaper prices, etc...

One day, when we're playing the mod, Zanieon was pissed with some Cyber-Barons (a strong enemy on the mod) for the excess of damage output dealt against players, so he did some other balances more. And i've followed him, just to support the changes.

And now the latest update for the patch was the unofficial v8f, it was intended to develop another patch, but for the unstability of the code, I've decided to make an entire fork to fix the problems from the roots. 

## Play setup

To run this you need:
* Zandronum 3.1 Alpha OR Zandronum 3.0
* A copy of Doom 2 or Freedoom 2.
* The Skulltag Content wad.

Loading order should be:
* skulltag-content3.0-beta.pk3
* sfplus_res_xxx.pk3  // Contains the rest of it, like textures, sprites, sounds etc.
* sfplus_mus_xxx.pk3  // Contains the soundtrack for the mod. (Optional)
* sfplus_core_xxx.pk3 // Contains the source code.

## Build setup

For building, get Python 3, and run the Play.py or Build.py files.

##### Play.py parameters
	-s  -> Saves the generated temporary files.
	-xr -> Skips the resource folder zipping routine.
	-xm -> Skips the music folder zipping routine.
	-xrm -> Skips the resource and music folders zipping routine. Meant for quick tests.
For a faster run, do:
``` python play.py -s ```
For the first time and:
``` **python play.py -s -srm** ```
The rest of them, that should get you playing the mod in no time. Note that in the play.py compiles the ACS before running.

##### Build.py parameters
	-d  -> Makes a versioned copy (depending on project.ini).
	-xr -> Skips the resource folder zipping routine.
	-xm -> Skips the music folder zipping routine.
	-xrm -> Skips the resources and music folder zipping routine. Building only the core directory.
With this, you can make the pk3 files to be used in Slade, just in case you want to do something else. Also, this is useful for making new versions.

## For all of changes made, read the changelog.md file!
