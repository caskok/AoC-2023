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

seeds = sorted([(seeds[i], seeds[i+1]) for i
                in range(0, len(seeds) // 2 + 1, 2)], reverse=True)

for mapping in mappings:
    mapping.sort(key=lambda x: x[1])

sources = seeds.copy()
destinations = []
for mapping in mappings:
    mapping_start = 0
    while sources:
        src_start, src_length = sources.pop()
        for map_dest, map_start, map_length in mapping[mapping_start:]:
            map_end = map_start + map_length
            # We possibly hit a mapping range, check if and how to handle it.
            if map_end > src_start:
                src_end = src_start + src_length
                if src_end < map_start:
                    destinations.append((src_start, src_length))
                elif src_end > map_end:
                    if src_start > map_start:
                        destinations.append((src_start - map_start + map_dest,
                                            map_end - src_start))
                    else:
                        destinations.append((map_dest, map_length))
                        destinations.append((src_start,
                                             map_start - src_start - 1))
                    # We split the range and have to check the remaining in the
                    # future again.
                    sources.append((map_end, src_end - map_end))
                else:
                    if src_start > map_start:
                        destinations.append((src_start - map_start + map_dest,
                                            src_length))
                    else:
                        destinations.append(
                            (map_dest, src_end - map_start)
                        )
                        destinations.append((src_start, map_start - src_start))
                break
            # We did not hit this mapping and can skip it in the future.
            mapping_start += 1

    # The destinations now become the sources for the next mapping round and
    # we sort the sources again on ascending index.
    sources = sorted([(_, length) for (_, length)
                      in destinations if length > 0],
                     reverse=True)
    destinations = []

print(sources[-1][0])
