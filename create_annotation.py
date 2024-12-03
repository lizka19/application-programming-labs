import csv
import os

def create_annotation(save_path: str, annotation_path: str) -> None:
    """
    Создает файл аннотаций с абсолютными и относительными путями к изображениям.
    :param save_path: Путь для сохранения изображений.
    :param annotation_path: Путь для сохранения файла аннотации.
    """
    try:
        with open(annotation_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Absolute', 'Relative'])
            for filename in os.listdir(save_path):
                absolute_path = os.path.abspath(os.path.join(save_path, filename))
                relative_path = os.path.join(save_path, filename)
                writer.writerow([absolute_path, relative_path])
    except Exception as e:
        raise Exception(f"Cannot create a file: {e}")