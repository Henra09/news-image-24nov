// Entry program: places the finished news picture into the grader's output
// folder. Node 22, standard library only.
//
// How it works:
// - entry.png sits at the repository root, next to this file. It was rendered
//   ahead of time (1024x1024 PNG, well under 1 MiB) so the exact judged bytes
//   are known and stable.
// - The judge's container exposes a writable /output directory; outside it we
//   honour MAKEFUN_OUTPUT_DIR so the same script can be smoke-tested locally.
// - A plain byte-for-byte copy means both required grader runs emit identical
//   files with no network access and no dependencies.
//
// Local smoke test:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const source = new URL('./entry.png', import.meta.url);
const destination = join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png');
copyFileSync(source, destination);
console.log('Copied entry.png to', destination);
