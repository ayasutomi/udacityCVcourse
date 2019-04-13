import cv2
import numpy as np

def sp_noise(image, amount = 0.004):
    s_vs_p = 0.5
    out = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt))
            for i in image.shape]
    out[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper))
            for i in image.shape]
    out[coords] = 0
    return out

img = cv2.imread('imgs/watch.jpg', )
cv2.imshow('watch',img)


noisy_img = sp_noise(img, 0.02)
cv2.imshow('sp_noise', noisy_img)

f_size = 5
median = cv2.medianBlur( noisy_img, f_size )
cv2.imshow('median', median)

cv2.waitKey(0)
cv2.destroyAllWindows()
