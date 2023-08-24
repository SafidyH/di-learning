from django.shortcuts import render

name = 'Bob Smith'
age = 35
country = 'USA'
people = ['bob','martha', 'fabio', 'john']

all_people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
    'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
    'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
    'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]


def display_person(request):
    
    person_data = {
        'name': 'Bob Smith',
        'age': 35,
        'location': 'USA',
    }

    return render(request, 'person.html', {'person': person_data})

def display_people(request):
    sorted_people = sorted(people)
    capitalized_people = [person.capitalize() for person in sorted_people]

    return render(request, 'people.html', {'people': capitalized_people})

def display_all_people(request):
    sorted_people = sorted(all_people, key=lambda person: person['age'])

    return render(request, 'all_people.html', {'people': sorted_people})
