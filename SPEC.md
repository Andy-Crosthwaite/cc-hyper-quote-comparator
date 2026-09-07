Build exactly:
1. quote.py — round_half_up(amount: str | Decimal) -> Decimal and format_money(amount) -> str (half-up to nearest cent).
2. test_quote.py — >=10 unittest cases: exact cents, half-cent up (0.005 -> 0.01), negatives, string inputs, large values, formatting.
3. README.md — one-screen usage, <=3 commands.
4. python3 -m unittest -v must pass.
No web UI, DB, auth, or PyPI packaging.
