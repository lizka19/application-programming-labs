import matplotlib.pyplot as plt
import pandas as pd

def create_histogram(df: pd.DataFrame) -> None:
    """
    Строит гистограмму распределения области изображения
    :param df: DataFrame с путями, формами и областями изображений
    """
    plt.figure(figsize=(10, 5))
    df['area'].hist(bins=30)
    plt.title('Image area distribution')
    plt.xlabel('Area')
    plt.ylabel('Freq')
    plt.show()