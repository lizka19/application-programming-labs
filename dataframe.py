import cv2
import os
import pandas as pd

def create_dataframe(annotation_path : str) -> pd.DataFrame:
    """
    Создает DataFrame с 2 столбцами
    :param annotation_path: Путь к файлу аннотаций.
    :return: DataFrame с двумя столбцами
    """
    if os.path.isfile(annotation_path):
        df = pd.read_csv(annotation_path)
        return df
    else:
        raise FileNotFoundError


def add_image_shape(df : pd.DataFrame) -> pd.DataFrame:
    """
    Добавляет информацию о размерах изображений в DataFrame.
    :param df: DataFrame с двумя столбцами
    :return: DataFrame с путями и формами изображений
    """
    height, width, depth = [],[],[]
    for Absolute in df["Absolute"]:
        img = cv2.imread(Absolute)
        if os.path.isfile(Absolute) and img is not None:
            hwd = img.shape
            height.append(hwd[0])
            width.append(hwd[1])
            depth.append(hwd[2])
        else:
            raise FileNotFoundError
    df["height"] = height
    df["width"] = width
    df["depth"] = depth
    return df


def compute_area(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычисляет площадь изображения и добавляет в столбец
    :param df: DataFrame с путями и формами изображений
    :return: DataFrame с путями, формами и областями изображений
    """
    df['area'] = df['height'] * df['width']
    return df


def get_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Вычисляет статистику для столбцов, содержащих информацию о размерах изображения.
    :param df: DataFrame с путями и формами изображений
    :return: Статистика DataFrame с информацией о размерах изображения.
    """
    return df[['height', 'width', 'depth']].describe()


def filter_images(df: pd.DataFrame, max_width: int, max_height: int) -> pd.DataFrame:
    """
    Фильтрует DataFrame по указанным параметрам
    :param df: DataFrame с путями и формами изображений
    :param max_width: Максимальная ширина фильтрации
    :param max_height: Максимальная высота фильтрации.
    :return: Фильтрация DataFrame по указанным параметрам.
    """
    return df[(df['height'] <= max_height) & (df['width'] <= max_width)]