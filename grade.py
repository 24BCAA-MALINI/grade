def get_grade(gr1, gr2, gr3, gr4, gr5, curve=0):
    all_grades = gr1 + gr2 + gr3 + gr4 + gr5
    all_grades_minus_min = all_grades - min(gr1, gr2, gr3, gr4, gr5)
    average = all_grades_minus_min / 4
    print("Average grade pre-curve:", average)
    return average + curve

""" Test 7 """
def test_get_grade():
    print("Testing get_grade...")
    assert(get_grade(82, 93, 87, 64, 91) == 88.25) # prints "Average grade pre-curve: 88.25"
    assert(get_grade(75, 80, 85, 90, 95, curve=2) == 89.5) # prints "Average grade pre-curve: 87.5"
    assert(get_grade(75, 75, 75, 75, 75, curve=10) == 85) # prints "Average grade pre-curve: 75.0"
    print("... done!")