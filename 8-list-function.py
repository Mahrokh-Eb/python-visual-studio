#adding one course to list
myCourses = ['python', 'kotlin', 'Ionic']

myCourses.append('JQuery')

print(myCourses)

# adding many different items to list
myCourses.extend(['x', 'y'])
print(myCourses)

# adding item in the middle
myCourses.insert(1, 'goli')
print(myCourses)

# index
print(myCourses.index('python'))

# reverse
print(myCourses.reverse())
