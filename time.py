"""
      The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

      It is much easier to understand with an example:

      * For seconds = 62, your function should return 
          "1 minute and 2 seconds"
      * For seconds = 3662, your function should return
          "1 hour, 1 minute and 2 seconds"
      For the purpose of this Kata, a year is 365 days and a day is 24 hours.

      Note that spaces are important.
"""


def format_duration(seconds):
    if seconds <= 0:
        return "send help"

    time_formats = [(60 * 60 * 24 * 365), (60 * 60 * 24), (60 * 60), 60, 1]
    time_format = ["years", "days", "hours", "minutes", "seconds"]
    foo = []

    for time, format in zip(time_formats, time_format):
        bar = seconds // time
        if bar == 1:
            foo.append(f"{bar} {format[:-1]},")
        else:
            foo.append(f"{bar} {format},")

        seconds = seconds - (bar * time)

    foo = [n for n in foo if not n.startswith("0")]

    if len(foo) > 1:
        foo.insert(-1, "and")
        return " ".join(foo)[:-1]

    else:
        return (foo[0])[:-1]


result = format_duration(3662)
print(result)
