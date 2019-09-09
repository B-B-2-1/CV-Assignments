size = 2
sizey = None
size = int(size)
if not sizey:
    sizey = size
else:
    sizey = int(sizey)
x, y = scipy.mgrid[-size: size + 1, -sizey: sizey + 1]
g = scipy.exp(- (x ** 2/float(size) + y ** 2 / float(sizey)))
print (g / np.sqrt(2 * np.pi))