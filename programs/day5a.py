lines = open('input/input5.txt', 'r').readlines()
D = [line.strip() for line in lines]

seeds = [int(num) for num in D[0].split(':')[1].split()]

seed_to_soil = [[int(num) for num in line.split()] for line in D[3:35]]
soil_to_fert = [[int(num) for num in line.split()] for line in D[37:55]]
fert_to_water = [[int(num) for num in line.split()] for line in D[57:105]]
water_to_light = [[int(num) for num in line.split()] for line in D[107:140]]
light_to_temp = [[int(num) for num in line.split()] for line in D[142:178]]
temp_to_hum = [[int(num) for num in line.split()] for line in D[180:209]]
hum_to_loc = [[int(num) for num in line.split()] for line in D[211:]]

mappings = [seed_to_soil,
            soil_to_fert,
            fert_to_water,
            water_to_light,
            light_to_temp,
            temp_to_hum,
            hum_to_loc]

for mapping in mappings:
    mapping.sort(key=lambda x: x[1])

locations = []
for seed in seeds:
    destination = seed
    for mapping in mappings:
        for dest, src, length in mapping:
            if src + length > destination:
                if src <= destination:
                    destination = destination - src + dest
                break
    locations.append(destination)
print(min(locations))
