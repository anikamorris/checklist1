checklist = list()

# CREATE
def create(item):
    checklist.append(item)

# READ
def read(index):
    return checklist[index]

checklist = ['blue', 'orange']
checklist[1] = 'cats'
print(checklist)