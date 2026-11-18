# Lab 7 — Fuzzing for Input Validation Bugs

Student SRN: PES1UG25CS836

## Files
- `marathon_registration_parser.py`: corrected input-validation functions
- `test_marathon_registration_parser.py`: three Hypothesis fuzz tests plus two regression tests

## Run
```bash
python -m pip install pytest hypothesis
python marathon_registration_parser.py
python -m pytest -v test_marathon_registration_parser.py
```

## Results
The supplied terminal evidence shows **5 passed** with Python 3.14.9, pytest 9.2.0, and Hypothesis 6.170.12.

The initial attempted test run failed to find the test file (`collected 0 items`); it is **not** evidence of failing fuzz tests on the original parser. For that screenshot, run the completed tests against the original parser from the same directory.

The submission PDF with screenshots is available separately from the assistant's generated artifacts and is not yet included in this Git branch.
