def create_concat_regex(r_lis):
    regex = "(re.++"
    for r in r_lis:
        regex = regex + " " + r
    regex = regex + ")"
    return regex

def create_union_regex(r_lis):
    regex = "(re.union"
    for r in r_lis:
        regex = regex + " " + r
    regex = regex + ")"
    return regex

def create_kstar_regex(r1):
    return f"(re.* {r1})"

def create_kplus_regex(r1):
    return f"(re.+ {r1})"

def create_regex_from_char(c):
    return f"(str.to_re \"{c}\")"

def create_all_char_regex():
    return "re.allchar"

def create_range_char_regex(c1, c2):
    return f"(re.range \"{c1}\" \"{c2}\")"