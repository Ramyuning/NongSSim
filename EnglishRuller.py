def drawOneTickWoL(ticklength):
    for i in range(ticklength):
        print("-", end='')
    print("")
    
def drawOneTickWL(ticklength,tickLabel):
    for i in range(ticklength):
        print("-", end='')
    print(tickLabel)
    
def drawTicks(tickLength):
    if tickLength >0:
        drawTicks(tickLength-1)
        drawOneTickWoL(tickLength)
        drawTicks(tickLength-1)
def drawRuler(nInches, majorLength):
    drawOneTickWL(majorLength, 0)
    for i in range(nInches):
        drawTicks(majorLength-1)
        drawOneTickWL(majorLength, i+1)
drawRuler(2,4)