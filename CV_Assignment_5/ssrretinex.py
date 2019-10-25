import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread("lena.jpg", 1)
plt.imshow(image)


class BasicRetinexAlgo:

    def __init__(self, spread):
        self.spread = spread

    def basic_retinex(self, image):
        (n, m) = image.shape
        modified_image = np.zeros([n, m])
        for i in range(n):
            for j in range(m):
                gamma_square = i ** 2 + j ** 2
                power = float(gamma_square) / self.spread ** 2
                modified_image[i][j] = float(np.log((1 + image[i][j])) - np.log(1 + (image[i][j] * np.exp(-(power)))))

        factor = (255 / (np.amax(modified_image) - np.amin(modified_image)))
        processed_image = np.multiply(modified_image, factor).astype(int)
        return processed_image

r, g, b = cv2.split(image)

basrex = BasicRetinexAlgo(int(input("Enter varience value : ")))
r_modifiedimage = basrex.basic_retinex(r)
g_modifiedimage = basrex.basic_retinex(g)
b_modifiedimage = basrex.basic_retinex(b)


final_image = cv2.merge((r_modifiedimage, g_modifiedimage, b_modifiedimage))

plt.imshow(final_image)
cv2.imwrite('output.jpeg', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
