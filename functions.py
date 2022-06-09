#print(2+4)
#print(3+6)
#print(9+4)


def add(x, y):
  print(x+y)

#add(2,4)
#add(3,6)
#add(9,4)

add_em = [[4,6], [9,2], [11,8], [10,34]]

#for sets in add_em:
  #a = sets[0]
  #b = sets[1]
  #add(a,b)


#take the add_em and mulitpy the numbers, add the result to a string that says "4 * 6 = 24"

def multipy(x,y):
  math_string = f"{x} * {y} = {x*y}"
  return math_string

for newset in add_em:
  a = newset[0]
  b = newset[1]
  print(multipy(a,b))

def greeting():
  return "Hello World"

print(greeting())


