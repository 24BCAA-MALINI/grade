# Grade Calculator (Drop the Lowest Score)

A short Python program that calculates a final grade from **5 scores**. It **drops the lowest score**, averages the other 4, and then adds an optional **curve**.

## How it works

1. Add up all 5 grades.
2. Subtract the lowest grade.
3. Divide by 4 to get the average.
4. Print the average before the curve.
5. Add the curve and return the final result.

## How to run

1. Install Python 3.
2. Save the code in a file called `grades.py`.
3. Run:

```bash
python grades.py
```

Nothing prints until you call a function, so add this at the bottom of the file:

```python
print(get_grade(82, 93, 87, 64, 91))
```

Output:

```
Average grade pre-curve: 88.25
88.25
```

## The function

```python
get_grade(gr1, gr2, gr3, gr4, gr5, curve=0)
```

| Parameter | Meaning |
|---|---|
| `gr1` to `gr5` | The five grades |
| `curve` | Points added to the final average (optional, default is `0`) |

**Returns:** the average of the best 4 grades, plus the curve.

## Code walkthrough

| Line | What it does |
|---|---|
| `all_grades = gr1 + ... + gr5` | Adds all five grades |
| `all_grades - min(...)` | Removes the lowest grade from the total |
| `average = ... / 4` | Averages the remaining four grades |
| `print("Average grade pre-curve:", average)` | Shows the average before the curve |
| `return average + curve` | Adds the curve and returns the result |

## Examples

**Example 1: no curve**

```python
get_grade(82, 93, 87, 64, 91)
```

- Lowest grade dropped: 64
- Remaining total: 82 + 93 + 87 + 91 = 353
- Average: 353 / 4 = **88.25**

**Example 2: with a curve**

```python
get_grade(75, 80, 85, 90, 95, curve=2)
```

- Lowest grade dropped: 75
- Average: (80 + 85 + 90 + 95) / 4 = 87.5
- Final: 87.5 + 2 = **89.5**

**Example 3: all grades the same**

```python
get_grade(75, 75, 75, 75, 75, curve=10)
```

- One 75 is dropped, the other four average 75.0
- Final: 75.0 + 10 = **85**

## Testing

The program includes `test_get_grade()`, which checks the three examples above using `assert`.

| Call | Expected result |
|---|---|
| `get_grade(82, 93, 87, 64, 91)` | 88.25 |
| `get_grade(75, 80, 85, 90, 95, curve=2)` | 89.5 |
| `get_grade(75, 75, 75, 75, 75, curve=10)` | 85 |

The test function only runs if you call it. Add this line at the bottom of the file:

```python
test_get_grade()
```

If everything passes, you will see:

```
Testing get_grade...
Average grade pre-curve: 88.25
Average grade pre-curve: 87.5
Average grade pre-curve: 75.0
... done!
```

If any check fails, Python stops with an `AssertionError`.

## Notes

- You must pass exactly 5 grades.
- If two grades tie for the lowest, only one of them is dropped.
- The curve is added **after** averaging, and it is not capped at 100.

## Summary

| Item | Detail |
|---|---|
| Language | Python 3 |
| Input | 5 grades and an optional curve |
| Output | Average of the top 4 grades plus the curve |
| Dependencies | None |
