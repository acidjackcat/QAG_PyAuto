"""Let's create couple classes for our school"""

class Students(object):
    """Here is the class which should represent students in our school"""

    def __init__(self, f_name, l_name, year, gender):
        self.f_name = f_name
        self.l_name = l_name
        self.year = year
        self.gender = gender

    def run(self):
        print(f"Я {self.f_name} {self.l_name} бігаю по школі")

    def laugh(self):
        print(f"Я {self.f_name} {self.l_name} сміюсь")

    def learn(self):
        print(f"Я {self.f_name} {self.l_name} вчуся у школі")


class Teachers(object):
    """Simple class to simulatr teachers."""

    def __init__(self, f_name, l_name, gender, stream)
        self.f_name = f_name
        self.l_name = l_name
        self.gender = gender
        self.stream = stream

    def teach(self):
        print(f"I'm {self.f_name} {self.l_name} teaching children.")

    def punish(self):
        print(f"I'm {self.f_name} {self.l_name} punishing students")




class Director(object):


