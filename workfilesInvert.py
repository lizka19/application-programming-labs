import cv2
import numpy as np


def get_histogram(img:np.ndarray)->list:
    """
    Получает гистограмму по цветам
    """
    hist_list = []
    for i in range(0,3):
        hist = cv2.calcHist(img,[i],None,[256],[0,256])
        hist_list.append(hist)
    return hist_list


def get_inverted_img(img:np.ndarray)->np.ndarray:
    """
    Инвертирует цвета картинки
    """
    return cv2.bitwise_not(img)


def save_inverted_img(img:np.ndarray, f_img:str)->None:
    """
    Сохраняет итоговое изображение в необходимую директорию
    """
    cv2.imwrite(f_img,img)

