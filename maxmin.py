

def calculateMax(vec):
    max = vec[0][2]
    for v in vec:
        if (v[2] > max):
            max = v[2]
    return max


def calculateMin(vec):
    min = vec[0][2]
    for v in vec:
        if (v[2] < min):
            min = v[2]
    return min

def calculateMed(vec, size):
    return (vec[size-1][3])/size
