# usdt-rub-cli

Estimate how many rubles you actually get for USDT via P2P, an exchanger, or your own spread — before you pick a method. No dependencies, no sign-up, just Python 3.

```bash
python3 usdt_rub.py --amount 100 --rate 95 --method custom --custom-fee 0.5
```

```
Gross value: 9,500.00 RUB
  p2p              9,438.25 RUB
  exchanger        9,310.00 RUB
  custom           9,452.50 RUB <-- best
Difference between best and worst: 142.50 RUB
```

### Install (optional)

```bash
pip install git+https://github.com/kleogeos/usdt-rub-cli
usdt-rub --amount 100 --rate 95
```

### Options

| Flag | Default | Meaning |
|---|---|---|
| `--amount` | required | Amount of USDT to convert |
| `--rate` | required | Current USDT/RUB rate you see on an aggregator |
| `--method` | p2p | Which method to highlight (`p2p`, `exchanger`, `custom`) — all three are always shown |
| `--custom-fee` | 0.5 | Spread/fee percent to use for `--method custom` |
| `--json` | off | Output as JSON |

P2P and exchanger spreads are typical-case midpoints (0.3–1% and 1–3%), not live rates — see the [write-up](https://kleogeos.github.io/freelancer-tools/kak-vyvesti-usdt-v-rubli.html) on where those ranges come from and the bigger risk (card freezes from frequent P2P transfers, not the spread itself).

## Why a CLI instead of a web app?

Same math as the [web calculator](https://kleogeos.github.io/freelancer-tools/usdt-v-rubli-kalkulyator.html), but scriptable for anyone who'd rather pipe `--json` into a script than fill a form.

Prefer a browser form? Use the free web version: [USDT→RUB calculator](https://kleogeos.github.io/freelancer-tools/usdt-v-rubli-kalkulyator.html) · [live network fee comparison](https://kleogeos.github.io/freelancer-tools/crypto-fee-comparison.html)

Check whether a USDT payment landed yet: [crypto-pay-cli](https://github.com/kleogeos/crypto-pay-cli)

Need the paperwork for crypto invoicing in Russian — invoice template, self-employment/115-FZ checklist, payment tracking? [RU Crypto Freelancer Kit (7 USDT)](https://kleogeos.github.io/freelancer-tools/ru-kit.html)

Free and will stay free. If it saved you time: [tip with crypto](https://kleogeos.github.io/freelancer-tools/donate.html).

## License

MIT — do whatever you want with it.
