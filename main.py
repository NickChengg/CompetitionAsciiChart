boxWidth = 0
maxLayer = 6
def printBoxText(text):
    return ' ' + text + ' ' * (boxWidth - text.__len__() - 3)


def printBox(message, competitors, layer):
    start = 0
    separate = pow(2, layer + 2)
    if layer != 0:
        for i in range(layer):
            start += pow(2, i + 1)
    for line in range(competitors.__len__() * 4):
        boxIndex = (line - start) % separate
        if boxIndex < 4:
            if boxIndex in [0, 3]:
                message[line] += '=' * boxWidth
            elif layer == 0:
                if boxIndex == 1:  # name
                    message[line] += '|' + printBoxText(competitors[line // 4]['name']) + '|'
                elif boxIndex == 2:
                    message[line] += '|' + printBoxText(competitors[line // 4]['school']) + '|'
            elif layer == maxLayer and boxIndex == 1:
                message[line] += '|' + printBoxText('Champion') + '|'
            else:
                message[line] += '|' + ' ' * (boxWidth - 2) + '|' # blank box
        else: message[line] += ' ' * boxWidth # blank spaces

def printRepeat(message, item, first, separate, height = 1):
    for line in range(message.__len__()):
        if (line - first) % separate < height:
            message[line] += item
        else:
            message[line] += ' ' * item.__len__()

def printConnection(message, layer): # layer >= 1
    first_ = 0
    for i in range(layer):
        first_ += pow(2, i)
    separate = pow(2, layer + 1)
    printRepeat(message, '__', first_, separate)
    printRepeat(message, '|', first_ + 1, separate * 2, separate)
    printRepeat(message, '__', first_ + separate // 2, separate * 2)


def printCompetitors(competitors, maxLayer):
    message = []
    for line in range(competitors.__len__() * 4): # init
        message.append('')

    for layer in range(maxLayer + 1):
        if (layer != 0): # initial layer, no connectors
            printConnection(message, layer)
        printBox(message, competitors, layer)

    # print
    for line in message:
        print(line)


# main
competitors = []
for i in range(pow(2, maxLayer)): # init, 2^n
    competitors.append({'name': 'Chan Tai Man', 'school': 'AA School'})
boxWidth = competitors[0]['name'].__len__() + 4 # dummy

printCompetitors(competitors, maxLayer)

