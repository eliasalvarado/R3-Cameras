from npPirata import multMV, multMM

def vertexShader(vertex, **kwargs):
    modelMatrix = kwargs["modelMatrix"]
    viewMatrix = kwargs["viewMatrix"]
    projectionMatrix = kwargs["projectionMatrix"]
    vpMatrix = kwargs["vpMatrix"]

    vt = [vertex[0], 
        vertex[1], 
        vertex[2], 
        1]

    temp1 = multMM([vpMatrix, projectionMatrix])
    temp2 = multMM([temp1, viewMatrix])
    matrix = multMM([temp2, modelMatrix])

    """ vt = multMV(modelMatrix, vt)
    vt = multMV(viewMatrix, vt)
    vt = multMV(projectionMatrix, vt)
    vt = multMV(vpMatrix, vt) """
    """ vt = multMV(vpMatrix, vt)
    vt = multMV(projectionMatrix, vt)
    vt = multMV(viewMatrix, vt)
    vt = multMV(modelMatrix, vt) """

    #matrix = multMM([vpMatrix, projectionMatrix, viewMatrix, modelMatrix])
    
    vt = multMV(matrix, vt)

    vt = [vt[0] / vt[3],
        vt[1] / vt[3],
        vt[2] / vt[3]]

    return vt

def fragmentShader(**kwargs):
    texCoords = kwargs["texCoords"]
    texture = kwargs["texture"]
    
    if (texture != None):
        color = texture.getColor(texCoords[0], texCoords[1])
    else:
        color = (1, 1, 1)

    return color

