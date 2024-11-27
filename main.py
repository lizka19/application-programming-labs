from create_annotation import create_annotation
from download_images import download_images
from iterator import SimpleIterator
from parser import parse_args

def main():

    keyword, save_path, annotation_path = parse_args()
    try:
        download_images(keyword, save_path)
        create_annotation(save_path, annotation_path)
        iterator = SimpleIterator(annotation_path=annotation_path)
        for image in iterator:
            print(image)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()