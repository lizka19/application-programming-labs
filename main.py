import cv2
import numpy as np
import workfilesInvert
import workfilesPlt
from parser import parser

def print_size(img:np.ndarray)->None:
    """
    Вывод размеров картинки (высота и ширина), а также кол-во потоков
    """
    height, width, channels = img.shape
    print(f"Высота: {height}, ширина: {width}")


def main():

    img1, img2 = parser()

    try:
        image = cv2.imread(img1)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        f_image = cv2.cvtColor(workfilesInvert.get_inverted_img(image),cv2.COLOR_RGB2BGR)
        workfilesInvert.save_inverted_img(f_image,img2)

        print_size(image)
        workfilesPlt.show_graph(workfilesInvert.get_histogram(image))
        workfilesPlt.show_images(image, f_image)
    except Exception as e:
        print(f"Ошибка с доступом к расположению: {e} ")


if __name__=="__main__":
    main()