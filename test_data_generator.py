#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""module to generate test data for is_leap module"""

from calendar import isleap


# generate_test.data with calendar libm for period 2000 BE - 2000 C
def generate_data():
    value = "#!/usr/bin/env python3\n"
    value += "# -*- coding: utf-8 -*-\n"
    value += "test_data = "
    value += "["
    for i in range(-2000, 2001, 1):
        value += "(" + str(i) + "," + str(isleap(i)) + ")"
    value += "]"
    print(value)
    with open("test_data.py", "w") as fout:
        fout.write(value)


if __name__ == "__main__":
    generate_data()
