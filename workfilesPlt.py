import matplotlib.pyplot as plt
import numpy as np


def show_graph(hist_list: list)->None:
    """
    Создаёт граф по гистограмме, полученной в другой функции
    """
    plt.plot(hist_list[0], color='blue', label='channel blue')
    plt.plot(hist_list[1],color='red', label='channel red')
    plt.plot(hist_list[2],color='green', label='channel green')

    plt.title('Image histogram')
    plt.xlabel('brightness')
    plt.ylabel('number of pixels')
    plt.legend()

    plt.show()


def show_images(img:np.ndarray, f_img:np.ndarray)->None:
    """
    Показывает два изображения: оригинальное и инвертнутое
    """
    plt.figure(figsize=(10,5))

    plt.subplot(1,2,1)
    plt.title("Original Image")
    plt.imshow(img)
    plt.axis('off')

    plt.subplot(1,2,2)
    plt.title("Inverted Image")
    plt.imshow(f_img)
    plt.axis('off')

    plt.show()