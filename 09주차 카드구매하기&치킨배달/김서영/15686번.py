import sys
input_reader = sys.stdin.readline

N, M = map(int, input_reader().split())
grid = []
coordinates_of_2 = []
coordinates_of_1 = []

for y in range(N):
    line = list(map(int, input_reader().split()))
    if 2 in line:
        for x in range(len(line)):
            if line[x] == 2:
                coordinates_of_2.append((y, x))
    if 1 in line:
        for x in range(len(line)):
            if line[x] == 1:
                coordinates_of_1.append((y, x))
    grid.append(line)

min_distance = sys.maxsize
selected_coordinates = []
count_of_2 = len(coordinates_of_2)


def remove_2(start: int):
    condition = count_of_2 - len(selected_coordinates)
    if M == condition:
        calculate_distance(selected_coordinates)


    for i in range(start, len(coordinates_of_2)):
        (y, x) = coordinates_of_2[i]
        if (y, x) not in selected_coordinates:
            selected_coordinates.append((y, x))
            remove_2(i + 1)
            selected_coordinates.pop()


def calculate_distance(selected_coordinates: list):
    global min_distance
    distance = {}

    for fr in coordinates_of_2:
        if fr in selected_coordinates:
            continue
        for to in coordinates_of_1:
            if to not in distance.keys():
                distance[to] = sys.maxsize
            distance[to] = min(distance[to], abs(fr[0] - to[0]) + abs(fr[1] - to[1]))

    sum_of_distances = 0
    for i in distance.keys():
        sum_of_distances += distance[i]

    min_distance = min(min_distance, sum_of_distances)


remove_2(0)
print(min_distance)
