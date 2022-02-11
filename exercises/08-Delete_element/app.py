people = ['juan','ana','michelle','daniella','stefany','lucy','barak']
#Your code go here:
def deletePerson(person_name):
    return list(filter(lambda name: name != person_name, people))

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))