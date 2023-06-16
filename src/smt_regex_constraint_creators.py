def create_concat_regex(r_lis):
    regex = ""
    isOnlyStrings = True
    consecutive_chars = ""
    for r in r_lis:
        if r.startswith("(str.to_re"):
            # r is of the form (str.to_re "<string>")
            split = r.split(" ")

            # split[1] is "<string>")
            # Here, we extract <string> from split[1]
            string = split[1][1:len(split[1])-2]

            consecutive_chars += string
        else:
            isOnlyStrings = False
            if consecutive_chars != "":
                regex = regex + f"(str.to_re \"{consecutive_chars}\")"
                consecutive_chars = ""
            regex = regex + (" " if regex != "" else "") + r

    if consecutive_chars != "":
        regex = regex + (" " if regex != "" else "") + f"(str.to_re \"{consecutive_chars}\")"

    if not isOnlyStrings:
        # We need the ++ syntax only if we have some regex which is not string
        # for all strings, we just concat them to str.to_re "<complete_string>"
        regex =  "(re.++ " + regex + ")"

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