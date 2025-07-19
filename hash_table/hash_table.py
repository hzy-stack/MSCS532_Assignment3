import random


class HashTable:
    """
    A simple hash table with chaining collision resolution.
    Uses a universal hash function of the form:
        h(k) = ((a * hash(k) + b) % p) % m
    where p is a prime > initial capacity m, and a, b are random in [1, p-1] and [0, p-1].
    """

    def __init__(self, initial_capacity=8):
        self._m = initial_capacity
        self._p = self._next_prime(2 * self._m)
        self._a = random.randint(1, self._p - 1)
        self._b = random.randint(0, self._p - 1)
        self._buckets = [[] for _ in range(self._m)]
        self._n = 0

    def _next_prime(self, n):
        """Return a prime number ≥ n (simple check)."""

        def is_prime(x):
            if x < 2:
                return False
            if x % 2 == 0:
                return x == 2
            r = int(x ** 0.5)
            for i in range(3, r + 1, 2):
                if x % i == 0:
                    return False
            return True

        while not is_prime(n):
            n += 1
        return n

    def _hash(self, key):
        """Compute bucket index for a given key."""
        h_raw = hash(key)
        # Ensure non-negative
        h_raw = h_raw if h_raw >= 0 else -h_raw
        return ((self._a * h_raw + self._b) % self._p) % self._m

    def insert(self, key, value):
        """Insert or update the key with the given value."""
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # Not found, append
        bucket.append((key, value))
        self._n += 1
        # Resize if load factor too high
        if self.load_factor() > 0.75:
            self._resize(2 * self._m)

    def search(self, key):
        """Return the value for the given key, or None if not present."""
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Remove the key-value pair if present. Raises KeyError if absent."""
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._n -= 1
                if self._m > 8 and self.load_factor() < 0.2:
                    self._resize(max(8, self._m // 2))
                return
        raise KeyError(f"Key not found: {key}")

    def load_factor(self):
        """Current load factor α = n/m."""
        return self._n / self._m

    def _resize(self, new_capacity):
        """Resize table to new_capacity and rehash all entries."""
        old_items = []
        for bucket in self._buckets:
            old_items.extend(bucket)

        self._m = new_capacity
        self._p = self._next_prime(2 * self._m)
        self._a = random.randint(1, self._p - 1)
        self._b = random.randint(0, self._p - 1)
        self._buckets = [[] for _ in range(self._m)]
        self._n = 0

        for k, v in old_items:
            self.insert(k, v)
