from decimal import Decimal, ROUND_HALF_UP, localcontext
import argparse


def round_half_up(amount: str | Decimal) -> Decimal:
    value = Decimal(amount)
    if not value.is_finite():
        raise ValueError("amount must be finite")
    with localcontext() as context:
        context.prec = max(28, len(value.as_tuple().digits), value.adjusted() + 3)
        return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def format_money(amount) -> str:
    return format(round_half_up(amount), ".2f")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Round currency half up to cents")
    parser.add_argument("amount", help="decimal amount, for example 12.345")
    args = parser.parse_args()
    print(format_money(args.amount))