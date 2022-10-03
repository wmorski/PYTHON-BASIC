"""
Write tests for python_part_2/task_read_write.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
from practice.python_part_2.task_read_write import read_write


def test_read_write_task(tmpdir):
    path_to_files = '/Users/wmorski/PycharmProjects/PYTHON-BASIC/practice/python_part_2/files'
    result = tmpdir.join('test_result.txt')
    read_write(result, path_to_files)
    assert result.read() == '80, 37, 15, 14, 99, 99, 59, 90, 69, 39, 67, 91, 74, 40, 32, 82, 48, 1, 95, 66'
