from functions import _min, _max, _sum, _mult
import pytest


f = open('tests_for_project.txt')
f1 = open('answers_for_tests.txt')


tests = [[int(number) for number in line.split()] for line in f.readlines()]
answers = [[int(number) for number in line.split()] for line in f1.readlines()]


@pytest.mark.parametrize("tests_for_project, answers_for_tests", [(nums, ans) for nums, ans in zip(tests, answers)])
def test_for_functions(tests_for_project, answers_for_tests):
    assert _min(tests_for_project) == answers_for_tests[0]
    assert _max(tests_for_project) == answers_for_tests[1]
    assert _sum(tests_for_project) == answers_for_tests[2]
    assert _mult(tests_for_project) == answers_for_tests[3]
