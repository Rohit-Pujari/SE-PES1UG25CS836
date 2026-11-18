"""Robust marathon registration input parsing.

Invalid input returns a neutral result instead of raising an exception:
empty string for bib names, None for finish times and split averages.
"""


def format_bib_name(name):
    """Return an uppercase, trimmed bib name of at most 12 characters."""
    if not isinstance(name, str):
        return ""
    return name.strip().upper()[:12]


def parse_finish_time(text):
    """Convert H:MM:SS to seconds, or return None for invalid input."""
    if not isinstance(text, str):
        return None
    parts = text.strip().split(":")
    if len(parts) != 3:
        return None
    hours, minutes, seconds = parts
    if not (hours.isascii() and hours.isdecimal()
            and len(minutes) == 2 and minutes.isascii() and minutes.isdecimal()
            and len(seconds) == 2 and seconds.isascii() and seconds.isdecimal()):
        return None
    if len(hours) > 100:
        return None
    h, m, s = int(hours), int(minutes), int(seconds)
    if not (0 <= m < 60 and 0 <= s < 60):
        return None
    return h * 3600 + m * 60 + s


def average_split(text):
    """Average nonnegative integer split minutes, or return None if invalid."""
    if not isinstance(text, str):
        return None
    parts = text.split()
    if not parts or any(
        len(p) > 100 or not (p.isascii() and p.isdecimal())
        for p in parts
    ):
        return None
    numbers = [int(p) for p in parts]
    try:
        return sum(numbers) / len(numbers)
    except OverflowError:
        return None


def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    print("Bib name:", format_bib_name(value))

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    print("Finish time in seconds:", parse_finish_time(value))

    print("\n==== Running average_split ====")
    value = input("Enter your 5 km split times in minutes separated by spaces (e.g. 25 26 24): ")
    print("Average split (minutes):", average_split(value))


if __name__ == "__main__":
    main()
