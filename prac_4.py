def printInfo(name, age='N/A', cgpa=0.00):
  print(f'Name: {name}', f'Age: {age}', f'CGPA: {cgpa}')

# Default Arguments
printInfo('Mr.Z', 20, 3.8)
printInfo('Mr.Z', 20)
printInfo('Mr.Z')

# Keyword Arguments
printInfo(cgpa=3.9, age=30, name='Ms.D')
printInfo(cgpa=3.9, name='Ms.D')