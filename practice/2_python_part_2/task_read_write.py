"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os


def read_write(path_to_files: str, path_to_result: str) -> None:
    result = []

    for file in os.listdir(path_to_files):
        with open(path_to_files + "/" + file) as opened_file:
            result.append(opened_file.read())

    with open(path_to_result, 'w') as result_file:
        result_file.write(', '.join(result))


read_write('files', 'result.txt')
