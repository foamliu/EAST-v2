import zipfile


def extract(filename):
    print('Extracting {}...'.format(filename))
    zip_ref = zipfile.ZipFile(filename, 'r')
    zip_ref.extractall('data')
    zip_ref.close()


if __name__ == "__main__":
    extract('data/train2014.zip')
    extract('data/COCO_Text.zip')

    # ensure_folder(test_data_path)
    # extract('data/ch4_test_images.zip', test_data_path)
    # extract('data/Challenge4_Test_Task1_GT.zip', test_data_path)
