lines = open('input/input12.txt', 'r').readlines()
D = [line.strip().split() for line in lines]

D = [[4 * (springs + '?') + springs, 5 * list(map(int, nums.split(',')))]
     for springs, nums in D]

lookup = {}


def string_still_valid(string: str, nums: list):
    is_valid = True
    is_complete = True

    qms = string.count('?')
    springs = string.count('#')
    dots = len(string) - springs - qms
    qms_left = qms
    # First make sure there are enough dots for each group.
    if dots < len(nums) - 1:
        qms_left = qms - (len(nums) - 1 - dots)
    # If not enough dots can be acquired by questionmarks,
    # the string is invalid.
    if qms_left < 0:
        return not is_valid, not is_complete, '', []
    # Now make sure that with the remaining questionmarks, we still can
    # make all the remaining groups.
    if sum(nums) > springs + qms_left:
        return not is_valid, not is_complete, '', []

    remaining_str = string
    must_satisfy = nums.copy()
    group = 0

    for i, char in enumerate(string):
        if char == '?':
            return is_valid, not is_complete, remaining_str, must_satisfy
        elif char == '#':
            if not must_satisfy:
                return not is_valid, not is_complete, '', []
            else:
                group = must_satisfy.pop(0)
                string_list = list(string)
                for group_offset in range(group):
                    if string_list[i + group_offset] not in ['#', '?']:
                        return not is_valid, not is_complete, '', []

                # Check the if the group does not continue and overshoot.
                # This can not happen if it is the end of the string.
                try:
                    if string_list[i + group_offset + 1] == '#':
                        return not is_valid, not is_complete, '', []
                    else:
                        string_list[i + group_offset + 1] = '.'
                except IndexError:
                    pass
                remaining_str = ''.join(string_list[i + group_offset + 1:])
                return string_still_valid(remaining_str, must_satisfy)

    # Pop the last group from the list and check.
    if group and len(must_satisfy) == 1 and must_satisfy.pop(0) != group:
        return not is_valid, is_complete, '', []
    # If there are requirements left it is not valid.
    if must_satisfy:
        return not is_valid, is_complete, '', []
    return is_valid, is_complete, remaining_str, must_satisfy


def try_string(string: str, nums: list[int]):
    if (string, tuple(nums)) in lookup:
        return lookup[(string, tuple(nums))]
    is_valid, is_complete, rs, new_nums = string_still_valid(string, nums)
    if not is_valid:
        return 0
    if is_complete:
        return 1
    qm_index = rs.find('?')
    string_list = list(rs)

    string_list[qm_index] = '.'
    empty = ''.join(string_list)
    string_list[qm_index] = '?'

    empty_count = try_string(empty, new_nums)

    if new_nums:
        replaced = True
        copy_nums = new_nums.copy()
        for i in range(copy_nums.pop(0)):
            if string_list[qm_index + i] in ['#', '?']:
                string_list[qm_index + i] = '#'
            else:
                replaced = False
                break

        # Check the if the group does not continue and overshoot.
        # This can not happen if it is the end of the string.
        try:
            if string_list[qm_index + i + 1] == '#':
                replaced = False
            else:
                string_list[qm_index + i + 1] = '.'
        except IndexError:
            pass

        if replaced:
            # Now that we added the group, check the rest of the string.
            spring = ''.join(string_list[qm_index + i + 1:])
            spring_count = try_string(spring, copy_nums)
            ans = empty_count + spring_count
            lookup[(spring, tuple(copy_nums))] = spring_count
            return ans
    lookup[(empty, tuple(new_nums))] = empty_count
    return empty_count


p2 = 0
for string, nums in D:
    p = try_string(string, nums)
    print(string, nums, p)
    p2 += p

print(p2)
