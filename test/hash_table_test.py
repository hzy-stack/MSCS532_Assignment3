import unittest

from hash_table.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(initial_capacity=8)

    def test_insert_and_search(self):
        self.assertIsNone(self.ht.search("key1"))
        self.ht.insert("key1", 100)
        self.assertEqual(self.ht.search("key1"), 100)

    def test_update_value(self):
        self.ht.insert("k", 1)
        self.assertEqual(self.ht.search("k"), 1)

        self.ht.insert("k", 2)
        self.assertEqual(self.ht.search("k"), 2)

    def test_delete(self):
        self.ht.insert("x", 42)
        self.assertEqual(self.ht.search("x"), 42)
        self.ht.delete("x")
        self.assertIsNone(self.ht.search("x"))

    def test_delete_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.ht.delete("no_such_key")

    def test_load_factor(self):
        self.assertEqual(self.ht.load_factor(), 0)

        self.ht.insert("a", 1)
        self.assertAlmostEqual(self.ht.load_factor(), 1 / 8)

    def test_rehash_expand(self):

        for i in range(7):
            self.ht.insert(f"k{i}", i)
        self.assertEqual(self.ht._m, 16)

        for i in range(7):
            self.assertEqual(self.ht.search(f"k{i}"), i)

        # Check load factor after resize
        self.assertAlmostEqual(self.ht.load_factor(), 7 / 16)

    def test_rehash_shrink(self):
        for i in range(7):
            self.ht.insert(f"k{i}", i)
        self.assertEqual(self.ht._m, 16)

        for i in range(5):
            self.ht.delete(f"k{i}")
        self.assertEqual(self.ht._m, 8)

        self.assertEqual(self.ht.search("k5"), 5)
        self.assertEqual(self.ht.search("k6"), 6)

    def test_chaining_collisions(self):

        self.ht._hash = lambda key: 0
        keys = ["a", "b", "c"]
        for idx, key in enumerate(keys):
            self.ht.insert(key, idx)

        self.assertEqual(self.ht._buckets[0], [("a", 0), ("b", 1), ("c", 2)])

        for idx, key in enumerate(keys):
            self.assertEqual(self.ht.search(key), idx)

        self.ht.delete("b")
        self.assertIsNone(self.ht.search("b"))
        self.assertEqual(self.ht._buckets[0], [("a", 0), ("c", 2)])


if __name__ == '__main__':
    unittest.main()
