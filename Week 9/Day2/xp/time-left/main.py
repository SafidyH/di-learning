import datetime

def time_left_until_january_1():
    # Get the current date and time
    now = datetime.datetime.now()

    # Get the current year and the next year
    current_year = now.year
    next_year = current_year + 1

    # Calculate the target date (January 1st of the next year)
    target_date = datetime.datetime(next_year, 1, 1)

    # Calculate the time difference
    time_difference = target_date - now

    # Extract days, hours, and minutes from the time difference
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Display the time left
    print("The 1st of January is in {} days and {} hours, {} minutes, and {} seconds.".format(days, hours, minutes, seconds))

# Example usage:
time_left_until_january_1()
