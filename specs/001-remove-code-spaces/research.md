# Research: Remove Spaces from Code Values

## Unit-testing approach

- **Decision**: Use the Python standard library `unittest` with a focused `test_py.py` module beside `py.py`.
- **Rationale**: The feature is a single pure transformation and needs only a small number of direct input/output assertions. The standard library avoids adding a dependency or project configuration. Running the named module with `python -m unittest -v test_py` is explicit and avoids relying on recursive test discovery rules.
- **Alternatives considered**:
  - A `tests/` directory with recursive `unittest` discovery; this adds a directory and may require package setup for discovery, which is unnecessary for one test module.
  - `pytest`; its test discovery and function-style tests are convenient if the suite grows, but add a dependency that the current scope does not justify.

## Transformation behavior

- **Decision**: Remove occurrences of the ordinary space character from each string; leave all other characters unchanged.
- **Rationale**: This matches the existing script's `.replace(" ", "")` behavior and the specification's explicit ordinary-space boundary.
- **Alternatives considered**:
  - Remove every whitespace character; rejected because tabs and other whitespace were not requested and are explicitly outside the current behavior.

## External contracts

- **Decision**: Do not create a `contracts/` artifact.
- **Rationale**: The feature is a local script transformation with no external service, protocol, or public interface.
- **Alternatives considered**: Documenting a public API contract was considered unnecessary for this one-file internal script.
