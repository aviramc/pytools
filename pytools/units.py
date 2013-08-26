from collections import defaultdict

class PatternNotFound(Exception):
    pass

DEFAULT_PATTERN = "([0-9]*\\.?[0-9]*)([A-Za-z]*)"

def parse_units_string(units_string, units_mapping, pattern=DEFAULT_PATTERN, numeric_type=float, return_type=int):
    match_object = re.match(pattern, units_string)
    if match_object is None:
        raise PatternNotFound(units_string, pattern)

    number, units = match_object.groups()
    return return_type(numeric_type(number) * units_mapping[units])

def parse_file_size_string(file_size_string):
    return parse_units_string(file_size_string, defaultdict(lambda : 1,
                                                            {"b" : 1,
                                                             "k" : 1024,
                                                             "m" : 1024 * 1024,
                                                             }))

def parse_time_units_string(time_units_string):
    return parse_units_string(time_units_string, defaultdict(lambda : 1,
                                                             {"s" : 1,
                                                              "m" : 60,
                                                              "h" : 60 * 60,
                                                              "d" : 60 * 60 * 24,
                                                              }))
