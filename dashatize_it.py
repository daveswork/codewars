#Innocent comment

def dashatize(num):
    working_list = str(num).strip("-")
    out_list = [""]
    interesting_char = ""
    if num is None:
        return "None"
    for i in range(0, len(working_list)):
        interesting_char = working_list[i]
        if int(interesting_char)%2 != 0:
            if len(working_list)>1 and i == 0 or out_list[-1] == "-" and i != len(working_list) - 1:
                out_list.append(interesting_char)
                out_list.append("-")
            elif i == 0:
                out_list.append(interesting_char)
            elif out_list[-1] == "-" and i == len(working_list) - 1:
                out_list.append(interesting_char)
            elif i == len(working_list) -1:
                out_list.append("-")
                out_list.append(interesting_char)
            else:
                out_list.append("-")
                out_list.append(interesting_char)
                out_list.append("-")
        else:
            out_list.append(interesting_char)
    return "".join(out_list)
