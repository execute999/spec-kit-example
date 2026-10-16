# Quickstart: Remove Spaces from Code Values

## Prerequisites

- Python 3.11 or a compatible Python 3 runtime.
- No third-party packages are required.

## Run the unit tests

From the repository root:

```powershell
python -m unittest -v test_py
```

Expected result: all focused normalization tests pass, including empty input, already-normalized values, repeated spaces, and a mixed list; the run exits with status 0.

## Validate the script behavior

Run the existing script from the repository root:

```powershell
python py.py
```

Expected result: each value in the sample `codes` list is normalized without raising an assertion, preserving its order and list length.
