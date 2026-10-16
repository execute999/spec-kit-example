# Data Model: Remove Spaces from Code Values

## Code Value

- **Represents**: One string item in the input sequence.
- **Fields**: String content.
- **Validation**: Values are strings; each ordinary space character (`U+0020`) is removed. Other characters, including tabs, are preserved.
- **State transition**: Input value → normalized output value; a value containing only ordinary spaces becomes an empty string.

## Code List

- **Represents**: The ordered sequence of code values processed by the feature.
- **Fields**: An ordered list of code values.
- **Validation**: Each input item is a string.
- **Relationships**: Contains zero or more Code Values.
- **State transition**: Input list → output list with the same length and item order, with each value normalized independently.

No persistence or cross-entity relationships are involved.
