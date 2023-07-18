start = 1.5
end = 5
step = 0.5

float_sequence = []
current = start

while current <= end:
    float_sequence.append(current)
    current += step

print(float_sequence)
