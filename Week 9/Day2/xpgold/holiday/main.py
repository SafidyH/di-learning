from datetime import datetime, timedelta

def display_today_and_next_holiday():
    # Get the current date and time
    current_datetime = datetime.now()

    # Get today's date
    today_date = current_datetime.date()

    # Assuming Halloween is the next holiday on October 31st
    next_holiday = datetime(current_datetime.year, 10, 31).date()

    # If Halloween has already passed this year, set it for next year
    if next_holiday < today_date:
        next_holiday = datetime(current_datetime.year + 1, 10, 31).date()

    # Calculate the time difference between today and the next holiday
    time_difference = next_holiday - today_date

    # Calculate the time left until the next holiday
    days_left = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Display today's date
    print("Today's date:", today_date)

    # Display the time left until the next holiday
    print("The next holiday (Halloween) is in {} days and {} hours, {} minutes, and {} seconds.".format(days_left, hours, minutes, seconds))

# Example usage:
display_today_and_next_holiday()
