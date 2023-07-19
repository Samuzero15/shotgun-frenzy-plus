# Shotgun Frenzy Plus
A fork from Shotgun Frenzy (a Doom 2 mod) which adds more stuff for Zandronum.

## Shotgun Frenzy? Er... wut?
That's a Doom mod with some Tower Defense game style, fusionated with some elements from the RTS (Real-Time Strategy), and of course, the First Person Shooter in a single place, mixed up with countless waves of demons Invading your base.

The game loop is simple, buy some weapons, kill demons to rise your ranks in order to open new upgrades, protect the cores, until you survive (or not) long enough to face the guardian wave. Other endings are avilable up to the date.

The original mod was made by Wad'a'holic, but for unknown reasons he stopped the project and decided to move on Total Chaos.

## What is this?
This is a fork for Shotgun Frenzy.

## How did you get in here Samu?
Yet the development was'nt stopped at all, Greg339 (I think...) and T3h Player decided to launch a set of unoffical patches which it introduced some more fixes to the mod. Like the reducction of lag, balances on demons, cheaper prices, etc...

One day, when we're playing the mod, Zanieon was pissed with some Cyber-Barons (a strong enemy on the mod) for the excess of damage output dealt against players, so he did some other balances more. And I've followed him, just to support the changes.

And now the latest update for the patch was the unofficial v8f, it was intended to develop another patch, but for the unstability of the code, I've decided to make an entire fork to fix the problems from the roots.

## So, What's new?
* Commander's Airstrikes are more controlled, plan first, then bomb the field!
* Mech Factory now brings a lot of upgrades for your mech! Making it the best offensive tool in the game!
* Extra stuff, like Chaingun and Shotgun turrets.
* New normal HUD and extra touches on the full-screen hud!
* A brand new terminal fully clientsided!, Move the cursor with your mouse, and press the button!
* Weapons are balanced and changed! Some of them have new alt-fires that actually makes them useful.
* Kill streaks! Break milestones and earn extra U.Ps! 
* Player Upgrades! Use your U.P. Points to gain private perks for the marines!
* Runes to buy and use on the battlefield!
* Champions! (Thanks TDRR and Mikk!) They are strong and unique, but they also drop good loot!
* Stimpack upgrades for your recoveries anyplace, anytime!
* A lot of Console Vars to customize your battles!

## Play setup

To run this you need:
* Zandronum 3.2's latest alpha. (Get it here https://zandronum.com/forum/viewtopic.php?t=10973)
* A copy of Doom 2 or Freedoom 2.
* The Skulltag Content wad.

Loading order should be:
* skulltag-content3.0-beta.pk3
* sfplus_res_xxx.pk3  // Contains the rest of it, like textures, sprites, sounds etc.
* sfplus_mus_xxx.pk3  // Contains the soundtrack for the mod. (Optional)
* sfplus_core_xxx.pk3 // Contains the source code.

## Build setup

To build from git, clone the repo or download the zip it to wherever you want. 
Open project.json file and edit these lines here. Change these paths acordingly.

    "sourceport_path": "..\\tools\\zandronum\\zandronum.exe", 
    "pwads_before": [
        "..\\tools\\pwads\\skulltag_content-3-0-beta01.pk3"
    ],
    "pwads_after": [],
    "iwad_path": "..\\tools\\zandronum\\doom2.WAD",

If you need to compile acs in your own architecture, use 32 or 64 bits in here.

    "acs_compilation": {
        "type": "acc",
        "executeable": "..\\tools\\acc\\acc64.exe",
        "extra_params": ""
    }

And make sure the `Skip Acs Flag` is disabled in your first build. Check for that flag in the settings button.

Now, Press the build and play buttons when you need them, and there you go!

## For all of changes made, read the changelog.md file!
