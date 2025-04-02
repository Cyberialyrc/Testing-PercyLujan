import unittest
from queue import Queue  # Asegúrate de importar tu clase correctamente
from hypothesis import given, strategies as st

class TestQueue(unittest.TestCase):
    
    def test_empty_queue(self):
        q = Queue(3)
        self.assertTrue(q.empty())
    
    def test_enqueue_dequeue(self):
        q = Queue(3)
        self.assertTrue(q.enqueue(5))
        self.assertTrue(q.enqueue(10))
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), 10)
    
    def test_full_queue(self):
        q = Queue(2)
        self.assertTrue(q.enqueue(1))
        self.assertTrue(q.enqueue(2))
        self.assertFalse(q.enqueue(3))  # No debe permitir más elementos
    
    def test_dequeue_empty_queue(self):
        q = Queue(2)
        self.assertIsNone(q.dequeue())
    
    def test_circular_behavior(self):
        q = Queue(2)
        self.assertTrue(q.enqueue(1))
        self.assertTrue(q.enqueue(2))
        self.assertEqual(q.dequeue(), 1)
        self.assertTrue(q.enqueue(3))  # Reutiliza espacio de la cola
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        self.assertTrue(q.empty())

    @given(st.lists(st.integers(), min_size=1, max_size=10))
    def test_random_enqueue_dequeue(self, values):
        q = Queue(len(values))
        for v in values:
            self.assertTrue(q.enqueue(v))
        for v in values:
            self.assertEqual(q.dequeue(), v)
        self.assertTrue(q.empty())
        
if __name__ == "__main__":
    unittest.main()
