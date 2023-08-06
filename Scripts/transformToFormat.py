import codecs
import os


# Description: This script tries to read a file with different encodings
def findFileType(input_file_path):
    """
    Determine the encoding of a file
    :param input_file_path:
    :return:
    """
    # Specify the input file path

    # List of possible encodings to try
    encodings = ['utf-8', 'latin-1', 'utf-16', 'utf-32']

    # Open the file and try different encodings
    for encoding in encodings:
        try:
            with codecs.open(input_file_path, 'r', encoding=encoding) as file:
                content = file.read()
            print("Successfully read the file with encoding:", encoding)
            break
        except UnicodeDecodeError:
            print("Failed to read the file with encoding:", encoding)

    # Process the content as needed
    print(content)




# Transform the files in given path to a given encoding
def transform_in_utf(input_encoding="latin-1", output_encoding="utf-8",
                     path="C:/Users/Laurentiu/PycharmProjects/FurnitureStoresExtraction/Data/"):
    """
    Transform the files in given path to a given encoding
    :param input_encoding:
    :param output_encoding:
    :param path:
    :return:
    """

    for f in os.listdir(path):
        if f.endswith(".txt"):
            print(f)
            input_file = path + f
            with codecs.open(input_file, 'r', encoding=input_encoding) as file:
                content = file.read()
            with codecs.open(input_file, 'w', encoding=output_encoding) as file:
                file.write(content)
