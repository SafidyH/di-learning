from datetime import datetime

def calculate_minutes_lived(birthdate):
    # Convert the birthdate string to a datetime object
    birthdate_obj = datetime.strptime(birthdate, '%Y-%m-%d')

    # Get the current date and time
    current_datetime = datetime.now()

    # Calculate the time difference between the birthdate and the current date
    time_difference = current_datetime - birthdate_obj

    # Calculate the total number of minutes lived
    minutes_lived = time_difference.total_seconds() / 60

    return int(minutes_lived)

# Example usage:
birthdate = '1990-08-15'
minutes_lived = calculate_minutes_lived(birthdate)
print(f"You have lived for {minutes_lived} minutes in your life.")
