import unittest

from py import normalize_codes


class NormalizeCodesTests(unittest.TestCase):
    def test_removes_spaces_and_preserves_order_and_length(self):
        values = ["dsa", "abc", "qet", "abc dsad"]

        self.assertEqual(
            normalize_codes(values),
            ["dsa", "abc", "qet", "abcdsad"],
        )
        self.assertEqual(len(normalize_codes(values)), len(values))

    def test_leaves_values_without_spaces_unchanged(self):
        self.assertEqual(
            normalize_codes(["plain", "no-spaces"]),
            ["plain", "no-spaces"],
        )

    def test_removes_repeated_spaces_and_maps_spaces_only_to_empty(self):
        self.assertEqual(
            normalize_codes(["a  b", "   "]),
            ["ab", ""],
        )

    def test_empty_input_returns_empty_list(self):
        self.assertEqual(normalize_codes([]), [])

    def test_preserves_non_space_whitespace(self):
        self.assertEqual(normalize_codes(["a\tb"]), ["a\tb"])


if __name__ == "__main__":
    unittest.main()
