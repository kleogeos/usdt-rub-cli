#!/usr/bin/env python3
import subprocess
import sys
import json
import unittest

from usdt_rub import compute


class TestCompute(unittest.TestCase):
    def test_basic_amounts(self):
        r = compute(100, 95, "p2p", custom_fee=0.5)
        self.assertEqual(r["gross_rub"], 9500.0)
        self.assertEqual(r["results_rub"]["p2p"], 9438.25)
        self.assertEqual(r["results_rub"]["exchanger"], 9310.0)

    def test_zero_amount(self):
        r = compute(0, 95, "p2p", custom_fee=0.5)
        self.assertEqual(r["gross_rub"], 0.0)
        self.assertEqual(r["results_rub"]["p2p"], 0.0)

    def test_best_and_worst_differ_correctly(self):
        r = compute(1000, 93.5, "p2p", custom_fee=0.5)
        # p2p spread (0.65%) is smaller than exchanger spread (2%), so p2p must win
        self.assertEqual(r["best_method"], "p2p")
        self.assertGreater(r["difference_vs_worst_rub"], 0)

    def test_custom_method_adds_custom_result(self):
        r = compute(100, 95, "custom", custom_fee=0.1)
        self.assertIn("custom", r["results_rub"])
        self.assertEqual(r["results_rub"]["custom"], 9500 * (1 - 0.1 / 100))
        # non-custom methods never add the "custom" key
        r2 = compute(100, 95, "p2p", custom_fee=0.1)
        self.assertNotIn("custom", r2["results_rub"])

    def test_cli_output_matches_readme_example(self):
        out = subprocess.run(
            [sys.executable, "usdt_rub.py", "--amount", "100", "--rate", "95",
             "--method", "custom", "--custom-fee", "0.5", "--json"],
            capture_output=True, text=True, check=True,
        ).stdout
        data = json.loads(out)
        self.assertEqual(data["results_rub"]["p2p"], 9438.25)
        self.assertEqual(data["results_rub"]["exchanger"], 9310.0)


if __name__ == "__main__":
    unittest.main()
