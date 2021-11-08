import math

dino = {}
sol = []


def read_data(path):
    with open(path, "r") as csv_file:
        next(csv_file)
        for line in csv_file:
            info = line.split(",")
            # print(info)
            name = info[0]
            sub = info[1]
            sub2 = info[2]
            if name not in dino:
                dino[name] = [sub]
            else:
                dino[name] = dino[name] + [sub] + [sub2]
    # print(dino)
    return dino


def speed(STRIDE_LENGTH, LEG_LENGTH):
    return ((float(STRIDE_LENGTH) / float(LEG_LENGTH)) - 1) * math.sqrt(float(LEG_LENGTH) * 9.8)


def run():
    read_data("dataset1.csv")
    # print('--------------------------------------------------------------------------------')
    read_data("dataset2.csv")
    # print("\n", 'Final ---->   ', dino)

    for i in dino:
        if len(dino[i]) == 3 and "bipedal" in dino[i][2]:
            rate = speed(dino[i][1], dino[i][0])
            sol.append([rate, i])
    print(sol)
    order = sorted(sol, reverse=True)

    print(order)
    for name in order:
        print(name[1])


run()
