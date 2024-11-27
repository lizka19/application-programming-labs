import argparse

def parse_args():
    """
    получаем аргументы из командной строки
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('keyword', type=str, help="Word for search")
    parser.add_argument("save_path", type=str, help="Path to save images")
    parser.add_argument("annotation_path", type=str, help="Path to save annotation file")
    args = parser.parse_args()
    return args.keyword, args.save_path, args.annotation_path