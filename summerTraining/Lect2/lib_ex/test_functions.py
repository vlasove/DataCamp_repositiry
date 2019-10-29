import functions as f
import unittest


class TestFunctions(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(f.add(2, 3), 5)
        self.assertEqual(f.add(-1, 1), 0)
        self.assertEqual(f.add(0, 0), 0)

    def testSub(self):
        self.assertEqual(f.sub(4, 2), 2)
        self.assertEqual(f.sub(5, 3), 2)


if __name__ == "__main__":
    unittest.main()
