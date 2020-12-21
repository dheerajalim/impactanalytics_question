import pytest
from ProductSum import ProductSum


def input_testcases():
    
    testcases = [
                ([2,4,[3,-4,[2,3],[5]],[6,[9]],8], 161),
                ([[6,[[[6,8]]]]],348),
                ([[[[[[1,2,3]]]]]],192),
                ([[1,2,[3],[4]]],42),
                ([1,2,3,4,[1,2],[[[1,2]]]],52),
                ([],0)
                ]
    return testcases

@pytest.mark.parametrize("test_input,expected", input_testcases())
def test_eval(test_input, expected):
    assert ProductSum(test_input) == expected
    

