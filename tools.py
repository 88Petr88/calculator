class API:
    @classmethod
    def get_data(cls):
        with open("nums.txt", "r") as file:
            lines = file.read().splitlines()
        return lines


def load_nums_from_file():
    nums = []
    lines = API.get_data()
    for line in lines:
        pair = line.split(",")
        if len(pair) == 2:
            x = float(pair[0].strip())
            y = float(pair[1].strip())
            nums.append((x, y))
    return nums
