#!/usr/bin/env python3
import argparse

SPREADS = {
    "p2p": 0.65,       # midpoint of typical 0.3-1% P2P spread
    "exchanger": 2.0,  # midpoint of typical 1-3% exchanger spread
}


def compute(amount, rate, method, custom_fee):
    gross = amount * rate
    results = {}
    for name, spread in SPREADS.items():
        results[name] = round(gross * (1 - spread / 100), 2)
    if method == "custom":
        results["custom"] = round(gross * (1 - custom_fee / 100), 2)
    best = max(results, key=results.get)
    worst = min(results, key=results.get)
    return {
        "gross_rub": round(gross, 2),
        "results_rub": results,
        "best_method": best,
        "difference_vs_worst_rub": round(results[best] - results[worst], 2),
    }


def main():
    p = argparse.ArgumentParser(
        prog="usdt-rub",
        description="Estimate RUB received for USDT via P2P, exchanger, or a custom spread.",
    )
    p.add_argument("--amount", type=float, required=True, help="Amount of USDT")
    p.add_argument("--rate", type=float, required=True, help="Current USDT/RUB rate you see")
    p.add_argument("--method", choices=["p2p", "exchanger", "custom"], default="p2p",
                    help="Which method to highlight (default p2p); all three are always shown")
    p.add_argument("--custom-fee", type=float, default=0.5,
                    help="Spread/fee percent for --method custom (default 0.5)")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    args = p.parse_args()

    r = compute(args.amount, args.rate, args.method, args.custom_fee)

    if args.json:
        import json
        print(json.dumps(r, indent=2))
        return

    print(f"Gross value: {r['gross_rub']:,.2f} RUB")
    for name, value in r["results_rub"].items():
        marker = " <-- best" if name == r["best_method"] else ""
        print(f"  {name:10s} {value:>14,.2f} RUB{marker}")
    print(f"Difference between best and worst: {r['difference_vs_worst_rub']:,.2f} RUB")


if __name__ == "__main__":
    main()
