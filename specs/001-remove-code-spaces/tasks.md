# Tasks: Remove Spaces from Code Values

**Input**: Design documents from `specs/001-remove-code-spaces/`

**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`

**Tests**: Included because the specification explicitly requests unit tests. Follow test-first ordering.

**Organization**: Tasks are grouped by user story and use the structure selected in `plan.md`.

## Phase 1: Setup

**Purpose**: Ensure generated Python files and common local environments are excluded from version control.

- [X] T001 Add Python runtime and bytecode ignore patterns in `.gitignore`

## Phase 2: Foundational

No shared infrastructure is needed for this single-script feature.

## Phase 3: User Story 1 - Normalize Code Values (Priority: P1) - MVP

**Goal**: Remove each ordinary space from every code value instead of rejecting values that contain spaces, while preserving list order and length.

**Independent Test**: Run `python -m unittest -v test_py` from the repository root and confirm tests for ordinary values, mixed values, repeated spaces, and empty input pass.

### Tests for User Story 1

- [X] T002 [US1] Add `unittest` cases in `test_py.py` for mixed values, strings with no spaces, repeated and only-space values, empty input, and preservation of order and length

### Implementation for User Story 1

- [X] T003 [US1] Implement one callable normalization method and apply it to the sample `codes` list in `py.py`, removing rejection-only behavior
- [X] T004 [US1] Run `python -m unittest -v test_py` and `python py.py` from the repository root to verify the feature and sample execution

**Checkpoint**: Story 1 is complete when the unit tests pass and running `py.py` does not reject the sample values.

## Phase 4: Polish & Cross-Cutting Concerns

**Purpose**: Ensure implementation documentation and working tree are consistent with the completed feature.

- [X] T005 [P] Confirm the validation commands and expected outcomes in `specs/001-remove-code-spaces/quickstart.md` match the final implementation

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies; establishes Python ignore patterns.
- **Foundational (Phase 2)**: No tasks; no shared infrastructure is required.
- **User Story 1 (Phase 3)**: Can start after setup. Write tests first; T003 follows T002; T004 follows T003.
- **Polish (Phase 4)**: Follows implementation and validation.

### User Story Dependencies

- **User Story 1 (P1)**: Independent; no other user stories exist.

### Parallel Opportunities

- There are no parallel implementation tasks: the unit test, its production method, and the validation depend on the same behavior and must be performed in order.
- T005 is separately reviewable after the implementation is complete.

## Parallel Example: User Story 1

No parallel coding is planned. First add and run the tests, then implement the method, then run the full focused validation.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Apply the Python ignore patterns.
2. Add unit tests and confirm they fail before the behavior is implemented.
3. Implement the single normalization method in `py.py`.
4. Run focused tests and execute the script.

The only user story is the MVP; no later story phase is required.
