import argparse

def parser()->tuple:
    """
    Получает путь к исходному изображению и путь, куда будет сохранено конечное изображение
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('original_image',type=str,help="the name of the original image")
    parser.add_argument('final_image',type=str,help="The name of the image-result")
    args = parser.parse_args()
    return args.original_image, args.final_image