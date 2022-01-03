import string
import random

GardenSize = random.randint(25, 50)

def drawgarden(seed):

    random.seed(seed)
    
    plant_emojis = {'&#127805;':0.5, ':&#127794;':0.5, '&#127813;':0.5, '&#127804;':0.5, '&#127801;':0.5, '&#127816;':0.5, '&#127794;':0.5, '&#127807;':0.5, '&#127827;':0.5, '&#127793;':1, '&#127799;':1, '&#127812;':0.5, '&#129419;':0.5, '&#128056;':0.5, '&#129417;':0.5, '&#129364;':0.5, '&#127795;':1, '&#128012;':0.5, '&#128027;':1, '&#128030;':1, '&#128029;':1}

    #Fancy way to initialize a 2d array
    garden = [[''] * GardenSize for i in range(GardenSize)]

    #Add plants, bugs, etc
    for y in range(GardenSize):
        for x in range(GardenSize):

            for z, q in plant_emojis.items():
                if q >= random.randint(0,100):
                    garden[y][x] = z

    #Fill in empty space with grass
    for y in range(GardenSize):
        for x in range(GardenSize):
            if garden[y][x] == '':
                garden[y][x] = '&#127793;'

    #Lets drawn a creek/pond
    garden = drawstream(garden)

    return cleanup(garden)


def drawstream(garden):
    #Pick a random point on the edge of the garden 
    EntryPoint = []
    BoundryLimits = [0, GardenSize-1]
    Axis = random.randint(0, 1)
    Boundry = random.choice(BoundryLimits)
    BoundryCoordinate = random.randint(0,GardenSize-1)
    stream_emoji = ['&#128998;', ]

    #Assemble our entry point
    if Axis == 0:
        #start with x axis
        EntryPoint = [Boundry, BoundryCoordinate]
    else:
        #start with y axis
        EntryPoint = [BoundryCoordinate, Boundry]


    #Add path emoji to our entry point
    garden[EntryPoint[0]][EntryPoint[1]] = stream_emoji[0]
    print(EntryPoint)
    #Assign our positionand check for the next path block to draw
    position = [EntryPoint[0], EntryPoint[1]]

    while True:
        #Get our heading
        direction = random.randint(1,4)

        if direction == 1:
            #Check if out of bounds
            if position[0]-1 < 0:

                if position != EntryPoint:
                    print(position)
                    break

            #Check if existing path
            elif garden[position[0]-1][position[1]] == stream_emoji[0]:
                continue

            #Add path and update position
            else:
                garden[position[0]-1][position[1]] = stream_emoji[0]
                position[0] = position[0]-1
                continue
        
        elif direction == 2:
            #Check if out of bounds
            if position[1]+1 > GardenSize-1:
                
                if position != EntryPoint:
                    print(position)
                    break

            #Check if existing path
            elif garden[position[0]][position[1]+1] == stream_emoji[0]:
                continue

            #Add path and update position
            else:
                garden[position[0]][position[1]+1] = stream_emoji[0]
                position[1] = position[1]+1
                continue

        elif direction == 3:
            #Check if out of bounds
            if position[0]+1 > GardenSize-1:
                
                if position != EntryPoint:
                    print(position)
                    break

            #Check if existing path
            elif garden[position[0]+1][position[1]] == stream_emoji[0]:
                continue

            #Add path and update position
            else:
                garden[position[0]+1][position[1]] = stream_emoji[0]
                position[0] = position[0]+1
                continue

        elif direction == 4:
            #Check if out of bounds
            if position[1]-1 < 0:
                
                if position != EntryPoint:
                    print(position)
                    continue
    
    return garden


def cleanup(garden):
    #Cleanup array for web rendering
    for x in range(GardenSize):
       garden[x] = '<p>' + str(garden[x]) + '</p>'

    garden = ''.join(map(str, garden))

    garden = str(garden)

    chars = [",","\'", "[", "]", ":"]

    for x in chars:
        garden = garden.replace(x, "")

    return '<body style="background-color:#855b36;">' + garden
