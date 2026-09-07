# Quote Calculator

Python 3.10+; standard library only. No network or credentials required.
From this directory:

```sh
python quote.py 12.345
python -m unittest -v
```

The CLI prints `12.35`. In Python, import `round_half_up` or `format_money`
from `quote`. Strings and Decimal inputs are rounded half up to cents;
negative ties round away from zero. Formatting always includes two decimals.