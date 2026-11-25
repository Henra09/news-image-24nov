// Entry program for the one-day world-news image contest.
//
// The finished picture is built beforehand and stored as entry.png next to this
// file; the job of this script is simply to place a copy of those exact bytes
// into the output folder the grader provides (/output, or MAKEFUN_OUTPUT_DIR
// when running locally). Both grader runs must produce identical bytes, which
// a plain copy guarantees.
//
// Local check:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR || '/output';
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
console.log('entry.png copied to', outDir);
