class Human:
    def __init__(self, id_number, name, age, priority, blood_type):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        self.blood_type = blood_type
        self.family = []

    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def add_person(self, person):
        if person.age >= 60 or person.priority:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        if person in self.humans:
            return self.humans.index(person)
        else:
            return -1

    def swap(self, person1, person2):
        index1 = self.find_in_queue(person1)
        index2 = self.find_in_queue(person2)

        if index1 != -1 and index2 != -1:
            self.humans[index1], self.humans[index2] = self.humans[index2], self.humans[index1]

    def get_next(self):
        if self.humans:
            return self.humans.pop(0)
        else:
            return None

    def get_next_blood_type(self, blood_type):
        for i, person in enumerate(self.humans):
            if person.blood_type == blood_type:
                return self.humans.pop(i)

        return None

    def sort_by_age(self):
        def age_priority_key(person):
            if person.priority:
                return (0, person.age)
            else:
                return (1, -person.age)

        self.humans.sort(key=age_priority_key)

    def rearrange_queue(self):
        for i in range(len(self.humans) - 1):
            if self.humans[i].family and self.humans[i+1].family:
                if self.humans[i].family[0] == self.humans[i+1].family[0]:
                    self.swap(self.humans[i], self.humans[i+1])
