import math
time = [49, 78, 79, 80]
distance = [298, 1185, 1066, 1181]

p1 = 1
for total_time, record in zip(time, distance):
    ways_to_beat_record = 0
    for charge_time in range(total_time + 1):
        distance = charge_time * (total_time - charge_time)
        if distance > record:
            ways_to_beat_record += 1
    p1 *= ways_to_beat_record
print(p1)

time = 49787980
distance = 298118510661181

# solution to quadratic equation:
lower_bound = math.ceil(24893990 - math.sqrt(321592227458919))
upper_bound = math.floor(24893990 + math.sqrt(321592227458919))

print(upper_bound - lower_bound + 1)
