dict = {}


def boolexp(string, i, j, bool):
    if i > j:
        return False
    if i == j:
        if bool == True:
            if string[i] == "T":
                return True
            else:
                return False
        else:
            if string[i] == "F":
                return True
            else:
                return False

    ke = str(i)+" "+str(j)+" "+str(bool)
    if ke in dict:
        return dict[ke]

    temp_ans = 0
    for k in range(i+1, j, 2):
        lt = boolexp(string, i, k-1, True)
        lf = boolexp(string, i, k-1, False)
        rt = boolexp(string, k+1, j, True)
        rf = boolexp(string, k+1, j, False)
        if (string[k] == '&'):
            if (bool == True):
                temp_ans = temp_ans + lt * rt
            else:
                temp_ans = temp_ans + lt * rf + lf * rt + lf * rf
        elif (string[k] == '|'):
            if (bool == True):
                temp_ans = temp_ans + lt * rt + lt * rf + lf * rt
            else:
                temp_ans = temp_ans + lf * rf
        elif (string[k] == '^'):
            if (bool == True):
                temp_ans = temp_ans + lt * rf + lf * rt
            else:
                temp_ans = temp_ans + lt * rt + lf * rf

    dict[ke] = temp_ans
    return temp_ans


string = "T^F|F"
i = 0
j = len(string)
print(boolexp(string, i, j-1, True))
