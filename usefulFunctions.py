def format_duration(seconds):
    if seconds < 0:
        raise ValueError("Time cannot be negative")

    if seconds == 0:
        return "0 seconds"

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    duration = []
    if days:
        duration.append(f"{days} day{'s' if days > 1 else ''}")
    if hours:
        duration.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes:
        duration.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if seconds:
        duration.append(f"{seconds} second{'s' if seconds > 1 else ''}")

    if len(duration) == 1:
        return duration[0]
    elif len(duration) == 2:
        return f" and ".join(duration)
    else:
        return f", ".join(duration[:-1]) + f", and {duration[-1]}"