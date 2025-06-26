import unittest
from src.infrastructure.input_parser import parse_input
from src.infrastructure.exceptions import InputParseError

class TestInputParser(unittest.TestCase):
    def test_parse_valid_input(self):
        input_data = (
            "55\n"
            "12 N\n"
            "LMLMLMLMM\n"
            "33 E\n"
            "MMRMMRMRRM"
        )
        coords_len, width, height, robots = parse_input(input_data)
        self.assertEqual(coords_len, 1)
        self.assertEqual(width, 5)
        self.assertEqual(height, 5)
        self.assertEqual(len(robots), 2)
        self.assertEqual(robots[0], (1, 2, "N", "LMLMLMLMM"))
        self.assertEqual(robots[1], (3, 3, "E", "MMRMMRMRRM"))

    def test_empty_input_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("")

    def test_invalid_first_line_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("5A\n12 N\nLMLMLMLMM")

    def test_odd_length_first_line_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("555\n12 N\nLMLMLMLMM")

    def test_negative_dimensions_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("00\n12 N\nLMLMLMLMM")

    def test_missing_robot_instructions_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("55\n12 N")

    def test_invalid_position_line_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("55\n12N\nLMLMLMLMM")

    def test_invalid_robot_coords_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("55\n1A N\nLMLMLMLMM")

    def test_invalid_direction_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("55\n12 X\nLMLMLMLMM")

    def test_invalid_instruction_char_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("55\n12 N\nLMLMLMLMX")

    def test_robot_coords_length_differs_from_board_raises(self):
        with self.assertRaises(InputParseError):
            parse_input("55\n123 N\nLMLMLMLMM")

if __name__ == "__main__":
    unittest.main()