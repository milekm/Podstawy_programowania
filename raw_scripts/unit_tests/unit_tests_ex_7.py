import unittest
import threading


def perform_task():
    result = 0
    for i in range(1, 100000):
        result += i
    return result


class TestMultiThreading(unittest.TestCase):
    def test_multi_threading(self):
        num_threads = 10
        threads = []

        for _ in range(num_threads):
            t = threading.Thread(target=perform_task)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        for t in threads:
            self.assertFalse(t.is_alive())


if __name__ == '__main__':
    unittest.main()
