T = int(input())
triangle = []
temp = [0,1,1,1,2,2]
Max = 0
for i in range(T):
  triangle.append(int(input()))
  if triangle[i] > Max:
    Max = triangle[i]

if Max <= 5:
  for i in range(T):
    print(temp[triangle[i]])
else:
  for i in range(1,Max - 4):
    temp.append(temp[i] + temp[i+4])

for i in range(T):
  print(temp[triangle[i]])