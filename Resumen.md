# Shotgun Frenzy Plus — Project Summary

## Overview
**Shotgun Frenzy Plus** is a large-scale **Doom 2** modification for **Zandronum** (a Skulltag-derived source port). It is a fork of the original Shotgun Frenzy by Wad'a'holic, maintained and extended by **Samu**. The mod blends **Tower Defense**, **RTS**, and **FPS** gameplay: buy weapons, kill demons, rank up, and protect cores.

## Tech Stack
- **Scripting:** ACS (Action Code Script) — compiled with `zt-bcc` (GCC-based ACS compiler), *not* plain ACC
- **Actors:** DECORATE (no ZScript in this project)
- **Build System:** Custom `pack-o-daemon.exe` configured via `project.json`
- **Port:** Zandronum 3.2 alpha (Skulltag-actor based multiplayer port)
- **Distribution:** Three `.pk3` files — Core, Resources, Music
- **Version:** v1.8.2 (latest release)

## Build Instructions
1. Edit `project.json` paths if needed
2. Run `pack-o-daemon.exe` from the project root
3. The tool compiles ACS via `zt-bcc.exe`, packs assets, and outputs `.pk3` files to `dist/`

## Project Structure
```
shotgun-frenzy-plus/
├── core/                 # Core mod (sfplus_core_*.pk3)
│   ├── Source/           # ACS source code (~86 files)
│   │   ├── sfplus.acs    # Main entry point
│   │   ├── sfcommon.acs  # Common includes
│   │   ├── Commander stuff/   # Commander building scripts (14 files)
│   │   ├── Cool stuff/        # Utilities (queue, acsutils, acsrect)
│   │   ├── Core/              # Init, sectors, techs, lump reading
│   │   ├── Demons/            # AI, spawning, champions, kill tracking
│   │   ├── Huds/              # HUD scripts (fullscreen, killstreak, item HUD)
│   │   ├── Maps/              # Per-map scripts + map libraries
│   │   ├── Players/           # Stats, rank, runes, save, music
│   │   ├── Samu-Terminal/     # Client-sided terminal UI framework (31 files)
│   │   │   ├── Components/    # Cursor, buttons, panels, prompt, toast, etc.
│   │   │   ├── Execute/       # Terminal execute handlers
│   │   │   └── Pages/         # Terminal page definitions (buy, upgrade, runes, etc.)
│   │   ├── Samu's Tools/      # Shared utilities & constants
│   │   └── Shop/              # Item/pricing directories
│   ├── ACS/              # Compiled .o files
│   ├── Actors/           # DECORATE (~80+ files): weapons, monsters, turrets, items, runes
│   ├── Bars/             # SBARINFO definitions
│   ├── Maps/             # Map WAD files
│   └── Config files:     # DECORATE.dec, MAPINFO, MENUDEF, CVARINFO, etc.
├── res/                  # Sprites, sounds, graphics, textures, fonts
├── mus/                  # 31 OGG soundtrack files
├── addons/               # Optional addon PK3s (custom weapons, monster sets)
├── dist/                 # Built release PK3s and zip archives
├── tools/                # Build tools (zt-bcc, Zandronum, PWADs)
├── project.json          # Build configuration
├── pack-o-daemon.exe     # Build tool
└── README.md             # Project docs
```

## Game Modes
- **Combat Frenzy (CF):** Arena-based survival (6 maps: cf01–cf06)
- **Survival Defender (SD):** Core-defense mode (2 maps: sd01–sd02)
- **Shotgun Frenzy (SF):** Classic mode (5 maps: sf01–sf05, sf00)

## Key Systems
- **Samu-Terminal:** Fully client-sided ACS GUI framework (cursor, buttons, labels, images, panels, numeric input, prompt dialogs, toast notifications, card/grid layouts)
- **Commander System:** Airstrikes, Mech Factory, turret deployables, building upgrades, tech research
- **Wave Spawning:** Configurable monster sets via `SFMWAVES` lump, adaptive spawn spots (TIDs 201–209)
- **Champions:** Elite monster variants with special effects (on-hit, on-death, constant FX)
- **Runes:** Perk system with configurable rune loadouts
- **Kill Streaks:** Reward system for consecutive kills
- **Player Upgrades:** Health, armor, speed, ammo capacity, backpack via the Genetics terminal
- **Weapon System:** ~20 weapons with upgrades, alt-fires, and weapon packs
- **Items/Powerups:** Configurable via `SFITMDEF` custom lump
- **Map Music:** Per-map music overrides via `SFMAPMUS` custom lump

## Important ACS Files
| File | Purpose |
|---|---|
| `sfplus.acs` | Global library entry point |
| `f_IntDB.acs` | Global state, game database, constants |
| `f_SecMan.acs` / `f_ScManS.acs` | Sector control (CF/SF and SD modes) |
| `fp_AISet.acs` / `f_AIDir.acs` | Enemy AI and wave sets |
| `f_FinalF.acs` | Guardian wave endgame flow |
| `samuterm.acs` | Terminal runtime entry |
| `samut_vars.acs` | Central config/state for terminal |
| `samut_input.acs` | Terminal input/keybind system |

## Custom Lumps
- **SFITMDEF** — Define items, runes, powerups, drops
- **SFWEPDEF** — Define weapons, ammo, starter equipment
- **SFMAPMUS** — Map music definitions
- **SFMWAVES** — Monster wave set definitions

## Known Bugs & Fixes
- **`LumpRead_NextArgDefault` int→str conversion bug** (`core/Source/Core/fp_lumpread.acs:265`): `StrCheckIfEmpty(value)` recibía un `int` convertido a `str`, pero zt-bcc no convierte int→str en parámetros de función — el entero se interpretaba como dirección de string inválida, causando que `StrIsEmpty` retornara `true` siempre. Arreglado verificando `res1` (string crudo) en lugar de `value` (int parseado). Esto afectaba a `LumpRead_NextArgDefault` con `LUMPR_VALUE_INT` (como `ibtn`/`powerupid` en powerups de `SFITMDEF.shop`).

## Recent Changes

### Rune page panel refactor (`core/Source/Samu-Terminal/Pages/samut_pages_runep.acs`)
- Replaced Grid + Card with absolute components inside a Panel (75, 60, 58, 29).
- 5 rune button slots per tier (20 total), repurposed dynamically per page.
- 4 NumInput paginators (loop, BtnDistance=240) with `NumInput_SetLabelOffsets(0,20)`.
- Tier names (DBIGFONT) and prices (SMALLFNT, CR_GOLD) as absolute labels at X=354.
- "Unlock Tier" button + price label using `upgr_x`/`upgr_y` vars.
- "Linked Rune" as absolute labels (X=40, LEFT TOP).
- Hover panel (75, 315, 58, 6) with rune name + word-wrapped description.
- Array: `[100]`, `RUNEPAGE_NPRIVARS=35`.
- **New:** `NumInput_SetLabelOffsets()` via `ST_CPROP15/16`.

### Cursor system overhaul (`core/Source/Samu-Terminal/`)
- **Cursor trail** with configurable count, max alpha, step dist, idle tics (cursor props via ST_CPROP15-18).
- Trail interpolates positions when cursor jumps; fades on idle; resets positions to cursor when idle expires; render skip after idle.
- `ST_HID_CURSOR = 10050` (higher priority), `ST_HID_CURSORTRAIL = 10100` (lower priority), trails use HID = CURSORTRAIL - ti.
- **Tooltip fade in/out** via `tooltip_alpha_timer`, `Cursor_SetTooltipAlphaTics()`, `Cursor_SetTooltipMaxAlpha()`. Last position preserved during fade-out.
- **Tooltip back** fixed: word-wrap aware, max_line = longest wrapped line, not wrap width.
- **`Cursor_SetPositionNoTrail(x, y)`** to teleport cursor without trail artifacts.
- **`StripControlChars()`** in `samut_comps_cursor.acs` for cleaning tooltip text.
- Tooltip & trail logic split: `UpdateTooltip()` + `UpdateTrail()` in `samut_update.acs`, rendering in `samut_disp.acs`. Variables shared via global scope.
- Trail init on `Cursor_Initialize()`: fills buffer with current position using `Cursor_getTrailCount()`.
- On idle complete (idle == TrailIdleTics+1): resets trail positions to cursor. On re-move before idle expires: sets idle = 0 (does not restore previous alpha).

## Development TODO (from Todo.txt)
- Achievements system
- Testing map with full CF simulator
- New monsters (Zombiemarine, Zsec)
- ACS source documentation
- Sprite replacements (Railgun, Flinger)
- Elite weapons implementation
- Grenade types (fire, shell, drone, plasma)
- Spectator freezing issue on commanding
- Ammo/health indicators

## Wiki Documentation
Located at `../shotgun-frenzy-plus.wiki/` with full reference for:
- Adding custom waves
- Map TIDs, scripts, and mapping conventions
- ACS compiler notes
- Samu-Terminal framework (all components, execution, input, layouts, variables, display)
- All custom lump formats (SFITMDEF, SFWEPDEF, SFMAPMUS, SFMWAVES)
