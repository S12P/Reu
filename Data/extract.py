import input_conv
import math
result = {
    "autotvm": {
        1:  {},
        2:  {},
        4:  {},
        8:  {},
        16: {},
        32: {},
    },
    "tvmttile": {
        1:  {},
        2:  {},
        4:  {},
        8:  {},
        16: {},
        32: {},
    },
}


def dico():
    for name_archi in ["XeonGold6130"]:
        for avx in ["avx512"]:
            for nbthread in [1, 2, 4, 8, 16, 32]:
                file_ = open(f"autotvm/result_1_{nbthread}_{avx}_{name_archi}.csv", "r")
                for line in file_:
                    l = line.split(";")
                    if l[0] != "Yolo9000_23":
                        result["autotvm"][nbthread][l[0]] = float(l[1])
                file_.close()
            for nbthread in [1, 16, 32]:
                for conv in input_conv.input_conv:
                    first = True
                    file_ = open(f"tvm+ttile/result_{nbthread}_{avx}_{name_archi}_{conv}.csv", "r")
                    mini = 400.0
                    for line in file_:
                        if not first:
                            l = line.split(";")
                            if float(l[3]) < mini:
                                mini = float(l[3])
                        else:
                            first = False
                    result["tvmttile"][nbthread][conv] = mini
                    file_.close()
    return result
