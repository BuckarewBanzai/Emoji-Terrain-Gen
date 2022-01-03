import string
import random

def drawpath(seed):

    random.seed(seed)

    GardenSize = random.randint(10, 250)

    dbug = ['b', 's']
    path_emoji = [':green_square:', ':brown_square:']
    plant_emojis = {'&#127805;':1, ':&#127794;':1, '&#127813;':1, '&#127804;':1, '&#127801;':1, '&#127816;':1, '&#127794;':1, '&#127807;':1, '&#127827;':1, '&#127793;':2, '&#127799;':2, '&#127812;':1, '&#129419;':1, '&#128056;':1, '&#129417;':0.5, '&#129364;':1, '&#127795;':2, '&#128012;':1, '&#128027;':2, '&#128030;':2, '&#128029;':2}

    #Fancy way to initialize a 2d array
    garden = [[''] * GardenSize for i in range(GardenSize)]

    #Add plants, bugs, etc
    for y in range(GardenSize):
        for x in range(GardenSize):

            for z, q in plant_emojis.items():
                if q >= random.randint(0,100):

                    if garden[y][x] != path_emoji[1]:
                        garden[y][x] = z

    #Fill in empty space with grass
    for y in range(GardenSize):
        for x in range(GardenSize):
            if garden[y][x] == '':
                garden[y][x] = '&#127793;'

    #Cleanup array for web rendering
    #for x in range(GardenSize):
    #   garden[x] = '<p>' + str(garden[x]) + '</p>'

    garden = ''.join(map(str, garden))

    garden = str(garden)

    chars = [",","\'", "[", "]", ":"]

    for x in chars:
        garden = garden.replace(x, "")


    return '<body style="background-color:#855b36;">' + garden
