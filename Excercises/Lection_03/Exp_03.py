"""names = ['Christopher', ' Good']
scores = []
scores.append(5)"""

"""for i in [1, 2, 4, 5, 5, 6]:
    print(i)"""

"""
i = 0
while i < 10"""
"""
#print(['love', 'python'][bool('plp')])

def make_shirt(size, text):
    print(f'\nThis t-shirt has size {size} \nand text: \"{text}\"')


make_shirt('L', "I Love Python")"""


def build_person(first_name, last_name, age = None):
    """Return a dictionary of information about a person:"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('Jonson', 'Klarkson', 44)
print(musician)