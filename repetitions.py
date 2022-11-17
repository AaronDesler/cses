a = input()
b = a[0]
a = a[1:]
count = 1
max = 1
for letter in a:
  if letter == b:
    count += 1
  else:
    count = 1
  if count > max : max = count
  b = letter
print(max)
