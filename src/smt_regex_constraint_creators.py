def create_regex_from_str(s):
    return f"(str.to_re {s})"

def create_concat_regex(r1, r2):
    return f"(re.++ {r1} {r2})"

def create_union_regex(r1, r2):
    return f"(re.union {r1} {r2})"

def create_kstar_regex(r1):
    return f"(re.* {r1})"

def create_kplus_regex(r1):
    return f"(re.+ {r1})"