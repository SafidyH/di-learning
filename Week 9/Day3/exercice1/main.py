import urllib.request

# Download the file
url = 'http://www.practicepython.org/assets/nameslist.txt'
filename = 'nameslist.txt'
urllib.request.urlretrieve(url, filename)
# Read the file line by line
with open('nameslist.txt', 'r') as file:
    lines = file.readlines()

# Read only the 5th line of the file
fifth_line = lines[4].strip()

# Read only the first 5 characters of the file
first_five_characters = lines[0][:5]

# Read all the file and return it as a list of strings, then split each word
all_words = []
for line in lines:
    all_words.extend(line.strip().split())

# Find the number of occurrences of the names "Darth", "Luke", and "Lea" in the file
name_counts = {
    'Darth': 0,
    'Luke': 0,
    'Lea': 0
}
for word in all_words:
    if word == 'Darth':
        name_counts['Darth'] += 1
    elif word == 'Luke':
        name_counts['Luke'] += 1
    elif word == 'Lea':
        name_counts['Lea'] += 1

# Append your first name at the end of the file
your_name = 'YourFirstName'
with open('nameslist.txt', 'a') as file:
    file.write(your_name + '\n')

# Append "SkyWalker" next to each first name "Luke"
with open('nameslist.txt', 'r+') as file:
    contents = file.read()
    contents = contents.replace('Luke', 'LukeSkyWalker')
    file.seek(0)
    file.write(contents)
    file.truncate()
