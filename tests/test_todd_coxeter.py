import unittest
from libsemigroups_cppyy import ToddCoxeter
from libsemigroups_cppyy import FroidurePin
from libsemigroups_cppyy import Transformation


class TestToddCoxeter(unittest.TestCase):
    def test_constructors(self):
        try:
            ToddCoxeter("left")
        except:
            self.fail("unexpected exception thrown")
        try:
            ToddCoxeter("right")
        except:
            self.fail("unexpected exception thrown")
        try:
            ToddCoxeter("twosided")
        except:
            self.fail("unexpected exception thrown")

        with self.assertRaises(TypeError):
            ToddCoxeter(45)
        with self.assertRaises(ValueError):
            ToddCoxeter("lft")
        with self.assertRaises(TypeError):
            ToddCoxeter("twosided", "left", "right")

        S = FroidurePin(Transformation([0, 0, 1, 2, 3]))
        with self.assertRaises(TypeError):
            ToddCoxeter(S)
        try:
            ToddCoxeter("twosided", S)
        except:
            self.fail("unexpected exception thrown")

        K = KnuthBendix()
        with self.assertRaises(TypeError):
            ToddCoxeter("left", K)
        K.set_alphabet("a")
        try:
            ToddCoxeter("left", K)
        except:
            self.fail("unexpected exception thrown")

        T = ToddCoxeter("left")
        try:
            ToddCoxeter("left", T)
        except:
            self.fail("unexpected exception thrown")

    def test_attributes(self):
        tc = ToddCoxeter("left")
        tc.set_nr_generators(1)
        tc.add_pair([0, 0, 0, 0, 0, 0], [0, 0, 0])
        self.assertEqual(tc.nr_classes(), 5)
        self.assertTrue(tc.contains([0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0]))
        self.assertFalse(tc.contains([0, 0, 0], [0, 0]))
        self.assertEqual(tc.kind(), "left")
        self.assertEqual(tc.class_index_to_word(1), [0, 0])
        self.assertFalse(tc.has_parent_froidure_pin())
        self.assertEqual(tc.nr_generators(), 1)
        self.assertEqual(tc.nr_generating_pairs(), 1)

        S = FroidurePin(Transformation([1, 2, 2]), Transformation([2, 0, 1]))
        tc = ToddCoxeter("twosided", S)
        self.assertEqual(tc.nr_classes(), 24)
        self.assertTrue(tc.has_parent_froidure_pin())

        K = KnuthBendix()
        K.set_alphabet("a")
        K.add_rule("aaaa", "aa")
        tc = ToddCoxeter("left", K)
        self.assertEqual(tc.nr_classes(), 3)


    def test_iterators(self):
        tc = ToddCoxeter("left")
        tc.set_nr_generators(2)
        tc.add_pair([0, 0, 0, 0], [0])
        tc.add_pair([1, 1, 1, 1], [1])
        tc.add_pair([0, 1], [1, 0])
        self.assertEqual(
            tc.generating_pairs(),
            [[[0, 0, 0, 0], [0]], [[1, 1, 1, 1], [1]], [[0, 1], [1, 0]]],
        )
        self.assertEqual(
            tc.normal_forms(),
            [
                [0],
                [1],
                [0, 0],
                [1, 0],
                [1, 1],
                [0, 0, 0],
                [1, 0, 0],
                [1, 1, 0],
                [1, 1, 1],
                [1, 0, 0, 0],
                [1, 1, 0, 0],
                [1, 1, 1, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [1, 1, 1, 0, 0, 0],
            ],
        )
        S = FroidurePin(
            Transformation([1, 3, 4, 2, 3]), Transformation([3, 2, 1, 3, 3])
        )
        tc = ToddCoxeter("left", S)
        tc.add_pair(
            S.factorisation(Transformation([3, 4, 4, 4, 4])),
            S.factorisation([3, 1, 3, 3, 3]),
        )
        self.assertEqual(
            tc.non_trivial_classes(),
            [
                [
                    [0, 0, 1],
                    [1, 0, 1],
                    [0, 0, 0, 1],
                    [0, 1, 0, 1],
                    [1, 0, 0, 1],
                    [0, 0, 0, 0, 1],
                    [0, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [0, 0, 0, 1, 0, 1],
                    [0, 1, 0, 0, 0, 1],
                    [0, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 0, 1],
                    [0, 0, 0, 0, 1, 0, 1],
                    [0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 0, 1],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 1],
                    [0, 1, 0, 0, 0, 1, 1, 0, 0],
                ]
            ],
        )
