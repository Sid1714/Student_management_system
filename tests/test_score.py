from src.score_calculator import calculate_average

def test_calculate_average():
    assert calculate_average([90, 80, 70]) == 80
    assert calculate_average([]) == 0
    assert calculate_average([100, 50]) == 75
