# news-image — 24 November 2026

![Competition](https://make.fun/badge/news-image-20261124.svg)
![Rank](https://make.fun/badge/news-image-20261124/Henra09/news-image-24nov/rank.svg)
![Reward](https://make.fun/badge/news-image-20261124/Henra09/news-image-24nov/reward.svg)

One picture that sums up the world's news of Tuesday, 24 November 2026.


`entry.png` is a 1024x1024 infographic with nine story cards spanning the
Middle East, Europe, the Americas, markets, trade, science and sport, each
with a short headline and one-line detail. The program in `main.ts` copies the
image to the output directory (`/output`, or `MAKEFUN_OUTPUT_DIR` locally).

## Run

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

The image was drawn with Python/Pillow (see `draw.py`); the program itself
uses only the Node.js standard library.

## License

MIT — see [LICENSE](LICENSE).

Built for [make.fun's news-image bounty](https://make.fun/bounty/news-image-20261124).
