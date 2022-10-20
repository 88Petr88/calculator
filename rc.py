class API:
    @classmethod
    def get_rc(cls):
        with open("rc.txt", "r") as file:
            lines = file.read().splitlines()
        return lines


def validate_rc():
    results = []
    rcs = API.get_rc()
    for rc in rcs:
        is_rc_valid = False
        if len(rc) == 10 and rc.isnumeric():
            rc_int = int(rc)
            if (rc_int % 11) == 0:
                is_rc_valid = True
        results.append((rc, is_rc_valid))
    return results



