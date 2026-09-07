import subprocess
import sys
import unittest
from decimal import Decimal
from quote import round_half_up, format_money


class Acceptance(unittest.TestCase):
    def test_exact_cents(self):
        self.assertEqual(round_half_up("12.34"), Decimal("12.34"))

    def test_half_cent(self):
        self.assertEqual(round_half_up("0.005"), Decimal("0.01"))

    def test_below_half(self):
        self.assertEqual(round_half_up("0.0049"), Decimal("0.00"))

    def test_negative_half(self):
        self.assertEqual(round_half_up("-0.005"), Decimal("-0.01"))

    def test_negative_exact(self):
        self.assertEqual(round_half_up("-12.34"), Decimal("-12.34"))

    def test_decimal(self):
        self.assertEqual(round_half_up(Decimal("1.235")), Decimal("1.24"))

    def test_result_type(self):
        self.assertIsInstance(round_half_up("1"), Decimal)

    def test_large(self):
        self.assertEqual(
            round_half_up("123456789012345678901234567890.125"),
            Decimal("123456789012345678901234567890.13"),
        )

    def test_format_whole(self):
        self.assertEqual(format_money("12"), "12.00")

    def test_format_negative(self):
        self.assertEqual(format_money("-1.235"), "-1.24")

    def test_format_zero(self):
        self.assertEqual(format_money("0"), "0.00")

    def test_cli(self):
        result = subprocess.run(
            [sys.executable, "quote.py", "12.345"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout, "12.35\n")


if __name__ == "__main__":
    unittest.main()