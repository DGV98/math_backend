import pytest 
from math_response import Problems, generate_prompt

def test_prompt():
    assert generate_prompt("algebra", "easy") == "Act like you are a math professor tutoring one of your students. Can you generate a list of 5 algebra problems that are of easy difficulty."
    assert generate_prompt("Calculus", "HARD") ==  "Act like you are a math professor tutoring one of your students. Can you generate a list of 5 calculus problems that are of hard difficulty."

    with pytest.raises(ValueError):
        generate_prompt("", "")

def test_problems():
    problems = Problems(generate_prompt("algebra", "easy"))
    assert len(problems.q) == 5
    assert problems.prompt == "Act like you are a math professor tutoring one of your students. Can you generate a list of 5 algebra problems that are of easy difficulty."
    next(problems)
    next(problems)
    assert len(problems.q) == 3
    next(problems)
    next(problems)
    next(problems)
    assert len(problems.q) == 5
    assert "" not in problems.q
     

    