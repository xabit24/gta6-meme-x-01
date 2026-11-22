// A gta6-meme-x-01 entry (Node 22, standard library only).
//
// The entry is the X post itself: the agent makes a GTA 6 meme, it is posted
// on X from a public account with make.fun (a link) and the entrant's play
// code in its text, POST.json names the post, and the house reads the post
// from X (its first picture and its text) and hands that to the judge.
//
// This program reproduces the entry's two files deterministically:
//   1. POST.json — copied from this repository to /output/POST.json, where
//      the gate reads it. That is the file the gate needs.
//   2. meme.png — the meme picture itself (1200x675), copied from this
//      repository to /output/meme.png. It is the picture Boss R posts as the
//      post's first image. The picture is vendored (see compose_meme.py for
//      how it was made: an AI-generated Vice City background, make.fun's real
//      press-pack ghost mark composited in, and the caption set in Inter Bold,
//      make.fun's press-pack font). Copying it writes the same bytes every
//      run, so two runs are byte-identical.
//
// The meme: "WAITED 13 YEARS FOR GTA 6 / MY AI AGENT EARNS REAL MONEY ON
// make.fun". "WAITED" is a pun on GTA's iconic "WASTED" death screen — the
// ghost waited 13 years for GTA 6 (out 2026-11-19, after the thirteen-year
// wait since GTA V) while its AI agent earned real money on make.fun.
//
// Outside the grader's container, MAKEFUN_BOT_DIR and MAKEFUN_OUTPUT_DIR
// stand in for /bot and /output:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(OUTPUT_DIR, { recursive: true });

for (const name of ['POST.json', 'meme.png']) {
  try {
    copyFileSync(join(BOT_DIR, name), join(OUTPUT_DIR, name));
  } catch (err) {
    console.error(`${name} could not be copied from ${BOT_DIR}: ${(err as Error).message}`);
    process.exit(1);
  }
}
