from src import main

import unittest
import inspect
from typing import Generator

class TestSolution(unittest.TestCase): 
    def method_gettr() -> Generator[callable, None, None]: 
        for _, method in inspect.getmembers(
            main.Testing, predicate=inspect.isfunction
        ): yield method
        
    def test_give_first_best(self):
        inout = [
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ]
        for i in inout: 
            for method in TestSolution.method_gettr(): 
                self.assertEqual(method(main.Testing(), i[0]), i[1])
        
    def test_give_first_bad(self): 
        self.assertEqual(main.Testing().give_first([1, 2, 3]), 1)
        self.assertEqual(main.Testing().give_first_alt([1, 2, 3]), 1)
        self.assertEqual(main.Testing().give_first([4, 5, 6]), 4)
        self.assertEqual(main.Testing().give_first_alt([4, 5, 6]), 4)
        self.assertEqual(main.Testing().give_first([7, 8, 9]), 7)
        self.assertEqual(main.Testing().give_first_alt([7, 8, 9]), 7)
        
    def test_give_first_better(self): 
        for method in TestSolution.method_gettr(): 
            self.assertEqual(method(main.Testing(), [1, 2, 3]), 1)
            self.assertEqual(method(main.Testing(), [4, 5, 6]), 4)
            self.assertEqual(method(main.Testing(), [7, 8, 9]), 7)

    def test_give_first_too_far(self):
        inout = [
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ]
        methods = [method for method in TestSolution.method_gettr()]
        for data, expected in inout: 
            results = map(lambda method: method(main.Testing(), data), methods)
            self.assertEqual(list(results), [expected] * len(methods))
        
if __name__ == "__main__": 
    unittest.main()