import unittest
from libsemigroups_cppyy import ToddCoxeter


class TestToddCoxeter(unittest.TestCase):
    def test_constructors(self):
        try:
            ToddCoxeter("left")
        except:
            self.fail("Unexpected exception thrown")
        try:
            ToddCoxeter("right")
        except:
            self.fail("Unexpected exception thrown")
        try:
            ToddCoxeter("twosided")
        except:
            self.fail("Unexpected exception thrown")

        with self.assertRaises(TypeError):
            ToddCoxeter(45)
        with self.assertRaises(ValueError):
            ToddCoxeter("lft")

        tc = ToddCoxeter("left")
        tc.set_nr_generators(1)
        tc.add_pair([0, 0, 0, 0, 0, 0], [0, 0, 0])
        self.assertEqual(tc.nr_classes(), 5)
        self.assertTrue(tc.contains([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]))
        self.assertFalse(tc.contains([0, 0, 0], [0, 0]))
        self.assertEqual(tc.kind(), "left")
        self.assertEqual(tc.class_index_to_word(1), [0, 0])
