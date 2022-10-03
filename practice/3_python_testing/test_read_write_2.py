"""
Write tests for python_part_2/task_read_write_2.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""
from practice.python_part_2.task_read_write_2 import read_write_2


def test_task_read_write_2(tmpdir, mocker):
    mocker.patch('practice.python_part_2.task_read_write_2.generate_words', return_value=['abc', 'def', 'xyz'])
    file1 = tmpdir.join('file1.txt')
    file2 = tmpdir.join('file2.txt')
    read_write_2(file1, file2, 3)

    assert file1.read() == "abc\ndef\nxyz"
    assert file2.read() == "xyz,def,abc"
