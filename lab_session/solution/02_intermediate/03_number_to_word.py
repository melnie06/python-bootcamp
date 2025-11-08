def convert_below_thousand(num: int) -> str:
    # Word lists for single digits, teens, and tens
    ONES = ["zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]

    TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen",
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    TENS = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    """Helper to convert numbers from 1 to 999 into words."""
    parts = []

    # Extract hundreds and remainder
    hundreds = num // 100
    remainder = num % 100

    # Handle hundreds
    if hundreds > 0:
        parts.append(ONES[hundreds] + " hundred")

    # Handle remainder (below 100)
    if remainder > 0:
        if remainder < 10:
            parts.append(ONES[remainder])
        elif remainder < 20:
            parts.append(TEENS[remainder - 10])
        else:
            ten = remainder // 10
            unit = remainder % 10

            if unit > 0:
                parts.append(TENS[ten] + "-" + ONES[unit])
            else:
                parts.append(TENS[ten])

    return " ".join(parts)


def number_to_words(n: int) -> str:
    """
    Converts an integer into its English word representation.
    Supports numbers from 0 to 999,999.

    Examples:
    - 0         → "zero"
    - 42        → "forty-two"
    - 105       → "one hundred five"
    - 12045     → "twelve thousand forty-five"
    - 999999    → "nine hundred ninety-nine thousand nine hundred ninety-nine"
    """

    # Ensure number is within the allowed range
    if not 0 <= n <= 999_999:
        raise ValueError("Only numbers from 0 to 999,999 are supported.")

    # Split into thousands and remainder
    thousands = n // 1000
    below_thousand = n % 1000

    words = []

    # Handle thousands part
    if thousands > 0:
        words.append(convert_below_thousand(thousands))
        words.append("thousand")

    # Handle remainder part
    if below_thousand > 0:
        words.append(convert_below_thousand(below_thousand))

    # Special case: n == 0
    if not words:
        return "zero"

    return " ".join(words)


print(number_to_words(0))  # "zero"
print(number_to_words(13))  # "thirteen"
print(number_to_words(42))  # "forty-two"
print(number_to_words(100))  # "one hundred"
print(number_to_words(123))  # "one hundred twenty-three"
print(number_to_words(1000))  # "one thousand"
print(number_to_words(12045))  # "twelve thousand forty-five"
print(number_to_words(999999))  # "nine hundred ninety-nine thousand nine hundred ninety-nine"
