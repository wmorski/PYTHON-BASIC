"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import pytest

from practice.python_part_2.task_classes import Homework, Teacher, Student


@pytest.fixture()
def active_homework():
    return Homework('Testing', 5)


@pytest.fixture()
def inactive_homework():
    return Homework('OOP', -3)


@pytest.fixture()
def teacher():
    return Teacher('Abigale', 'Fischer')


@pytest.fixture()
def student():
    return Student('Rome', 'Nolan')


def test_teacher_init(teacher):
    assert teacher.first_name == 'Abigale' and teacher.last_name == 'Fischer'


def test_teacher_create_homework(teacher):
    new_homework = teacher.create_homework('Errors and Exceptions', 2)
    assert new_homework.text == 'Errors and Exceptions' and str(new_homework.deadline) == '2 days, 0:00:00'


def test_student_init(student):
    assert student.first_name == 'Rome' and student.last_name == 'Nolan'


def test_student_do_active_homework(student, active_homework):
    assert student.do_homework(active_homework).text == 'Testing' \
           and str(student.do_homework(active_homework).deadline) == '5 days, 0:00:00'


def test_student_do_inactive_homework(student, inactive_homework, capfd):
    assert student.do_homework(inactive_homework) is None
    out, err = capfd.readouterr()
    assert out == 'You are late\n'


def test_homework_init(inactive_homework):
    assert inactive_homework.text == 'OOP' and str(inactive_homework.deadline) == '-3 days, 0:00:00'


def test_homework_is_active(active_homework, inactive_homework):
    assert active_homework.is_active() is True
    assert inactive_homework.is_active() is False
