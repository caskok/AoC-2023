lines = open('input/input15.txt', 'r').readlines()
# lines = open('examples/ex15.txt', 'r').readlines()
D = lines[0].strip().split(',')


def special_hash(string: str):
    hash_value = 0
    for char in string:
        hash_value += ord(char)
        hash_value = hash_value * 17 % 256

    return hash_value


class Lens:
    def __init__(self, label, focal_length) -> None:
        self.label = label
        self.focal_length = focal_length

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Lens):
            return False
        return __value.label == self.label

    def __hash__(self) -> int:
        return hash(self.label)

    def __repr__(self) -> str:
        return f"label '{self.label}' with fl {self.focal_length}"


class Box:
    def __init__(self, box_num) -> None:
        self.box_num = box_num
        self.order = []
        self.lenses = set()

    def add_lens(self, lens: Lens) -> None:
        if lens in self.lenses:
            old_lens_idx = self.order.index(lens)
            self.order[old_lens_idx] = lens
        else:
            self.order.append(lens)
        self.lenses.add(lens)

    def delete_lens(self, lens: Lens) -> None:
        if lens not in self.lenses:
            return
        self.order.remove(lens)
        self.lenses.remove(lens)

    def get_score(self) -> int:
        score = 0
        for slot_number, lens in enumerate(self.order, start=1):
            score += self.box_num * slot_number * lens.focal_length
        return score


boxes = [Box(i+1) for i in range(256)]

for step in D:
    if step.find('-') > 0:
        label = step[:-1]
        lens = Lens(label, 0)
        box_num = special_hash(label)
        boxes[box_num].delete_lens(lens)
    else:
        label, focal_length = step.split('=')
        lens = Lens(label, int(focal_length))
        box_num = special_hash(label)
        boxes[box_num].add_lens(lens)

print(sum([special_hash(step) for step in D]))
print(sum([box.get_score() for box in boxes]))
