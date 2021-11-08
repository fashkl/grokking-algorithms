import math

bipedal_dino = {}


def speed(stride, leg):
    return ((float(stride) / float(leg)) - 1) * math.sqrt(float(leg) * 9.8)


def read_csv(path):
    with open(path, 'r') as csv_file:
        next(csv_file)
        for line in csv_file:
            line = line.split(",")
            name = line[0]
            leg_or_stride = line[1]
            stance = line[2]
            if 'bipedal' in stance or name in bipedal_dino:
                if name not in bipedal_dino:
                    bipedal_dino[name] = {'stride': leg_or_stride}
                else:
                    bipedal_dino[name]['leg'] = leg_or_stride
        csv_file.close()


def read_csv_files(file1, file2):
    bi_dino = {}
    with open(file2, 'r') as csv_file2:
        next(csv_file2)
        for line in csv_file2:
            name, stride, stance = line.split(",")
            if 'bipedal' in stance:
                if name not in bi_dino:
                    bi_dino[name] = {'stride': stride}

        csv_file2.close()

    bi_dino_list = []
    with open(file1, 'r') as csv_file1:
        next(csv_file1)
        for line in csv_file1:
            line = line.split(",")
            name = line[0]

            if name in bi_dino.keys():
                leg_length = line[1]
                bi_dino_list.append({'name': name, 'speed': speed(bi_dino[name]['stride'], leg_length)})

        csv_file1.close()

    bi_dino_list.sort(key=lambda dino: dino['speed'], reverse=True)

    print(*[dino['name'] for dino in bi_dino_list], sep='\n')


if __name__ == '__main__':
    read_csv_files('dataset1.csv', 'dataset2.csv')
    print('**********************************')
    read_csv('dataset2.csv')
    read_csv('dataset1.csv')

    order = []
    for item in bipedal_dino:
        if 'leg' in bipedal_dino[item]:
            order.append({'name': item, 'speed': speed(bipedal_dino[item]['stride'], bipedal_dino[item]['leg'])})

    order.sort(key=lambda x: x['speed'], reverse=True)

    for dino in order:
        print(dino['name'])
