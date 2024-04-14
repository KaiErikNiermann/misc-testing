from src import main

import traceback
import unittest
import inspect
import pprint
from typing import Generator
class TestSolution(unittest.TestCase): 
    @staticmethod
    def method_gettr(problem, f_filter) -> Generator[callable, None, None]: 
        """
        Get all methods from the problem class that pass the filter function.
        """
        for _, method in inspect.getmembers(
            problem, 
            predicate=lambda func: inspect.isfunction(func) and f_filter(func)
        ): yield method

    def data_func(self, inout, problem, f_filter): 
        """
        Test the methods from the problem class with the given input/output pairs.
        """
        for data, expected in inout:
            for method in TestSolution.method_gettr(problem, f_filter): 
                self.assertEqual(method(problem(), data), expected)
    
    def test_give_first_sig_filt(self):
        """
        Test the functions of the class Testing in main.py if they have the specified signature
        """
        t_signature = inspect.Signature(
            parameters=[
                inspect.Parameter(
                    name="self", kind=inspect.Parameter.POSITIONAL_OR_KEYWORD
                ),
                inspect.Parameter(
                    name="nums", kind=inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation=list[int]
                )
            ], return_annotation=int
        )
        
        self.data_func([
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ], main.Testing, lambda func: inspect.signature(func) == t_signature)
        
    def test_give_first_name_filt(self):
        """
        Test the functions of the class Testing in main.py if they have the specified name
        """
        self.data_func([
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ], main.Testing, lambda func: func.__name__.startswith("give_first"))
        
    def test_give_first_best(self):
        inout = [
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ]
        for i in inout: 
            for method in TestSolution.method_gettr(main.Testing, lambda func: func.__name__.startswith("give_first")): 
                self.assertEqual(method(main.Testing(), i[0]), i[1])
        
    def test_give_first_bad(self): 
        self.assertEqual(main.Testing().give_first([1, 2, 3]), 1)
        self.assertEqual(main.Testing().give_first_alt([1, 2, 3]), 1)
        self.assertEqual(main.Testing().give_first([4, 5, 6]), 4)
        self.assertEqual(main.Testing().give_first_alt([4, 5, 6]), 4)
        self.assertEqual(main.Testing().give_first([7, 8, 9]), 7)
        self.assertEqual(main.Testing().give_first_alt([7, 8, 9]), 7)
        
    def test_give_first_better(self): 
        for method in TestSolution.method_gettr(main.Testing, lambda func: func.__name__.startswith("give_first")): 
            self.assertEqual(method(main.Testing(), [1, 2, 3]), 1)
            self.assertEqual(method(main.Testing(), [4, 5, 6]), 4)
            self.assertEqual(method(main.Testing(), [7, 8, 9]), 7)

    def test_give_first_too_far(self):
        inout = [
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ]
        methods = [method for method in TestSolution.method_gettr(main.Testing, lambda func: func.__name__.startswith("give_first"))]
        for data, expected in inout: 
            results = map(lambda method: method(main.Testing(), data), methods)
            self.assertEqual(list(results), [expected] * len(methods))
        
if __name__ == "__main__": 
    unittest.main()