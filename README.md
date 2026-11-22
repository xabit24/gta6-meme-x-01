# Post a GTA 6 meme on X (gta6-meme-x-01)

A meme about GTA 6 (Rockstar's Grand Theft Auto VI, out 2026-11-19) for the
make.fun bounty "Post a GTA 6 meme on X". Boss R posts it on X from
@alytcihuy; the post's address goes in `POST.json`.

## The meme

`meme.png` (1200x675, 16:9) — a Vice City neon-sunset street (AI-generated,
no text) with make.fun's real press-pack ghost mark composited in large and
central, and the caption set in Inter Bold, make.fun's press-pack font.

**The joke:** "WAITED" is a pun on GTA's iconic "WASTED" death screen. The
ghost waited 13 years for GTA 6 (the thirteen-year wait since GTA V) — while
its AI agent earned real money on make.fun in the meantime.

- Top: "WAITED 13 YEARS FOR GTA 6"
- Bottom: "MY AI AGENT EARNS REAL MONEY / ON make.fun"

The picture shows make.fun's ghost mascot (the white ghost with sparkle
eyes and magenta star coin, from https://make.fun/press/mark-on-dark-1024.png)
and make.fun's name, both recognisable when the picture is shrunk to 480px.
Verified: the meme reads cleanly at 480x270 (top line, ghost, bottom lines
all legible).

Made by `compose_meme.py` (PIL): background `assets/vice-city-bg.webp`,
ghost `assets/mark-on-dark-1024.png`, font `assets/Inter-Bold.otf`.
`main.ts` reproduces `meme.png` (and `POST.json`) deterministically by
copying the vendored files to `/output/`.

## The X post (Boss R posts this himself)

Post `meme.png` as the post's first (and only) picture from @alytcihuy,
public, with this text:

> Waited 13 years for GTA 6. My AI agent earned real money on make.fun while I waited.
>
> https://make.fun/bounty/gta6-meme-x-01
> makefun-banister-shrimp-tusk

The text carries a make.fun link (the bounty's page) and the play code
`makefun-banister-shrimp-tusk`. Keep the post up and the account public
until the results are out. Then send the post's address
(`https://x.com/alytcihuy/status/<id>`) back so it goes into `POST.json`.

## Run it

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` and `out/meme.png` are then byte for byte this directory's.

## Status

- **Not posted, not submitted.** `POST.json` still holds the placeholder
  until Boss R posts and sends back the URL.
- Bounty: $500, 50 places (1st $100, 2nd $60, 3rd $30, 4th–10th $10,
  11th–50th $6). Entries close Mon 23 Nov 2026 14:00 UTC (21:00 WIB).
- Referral code: `d2r4akr8` (https://make.fun/r/d2r4akr8). Play code:
  `makefun-banister-shrimp-tusk`.
