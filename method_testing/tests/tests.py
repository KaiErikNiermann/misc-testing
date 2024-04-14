from src import main

import traceback
import unittest
import inspect
import pprint
from typing import Generator
class TestSolution(unittest.TestCase): 
    @staticmethod
    def method_gettr(func_filter) -> Generator[callable, None, None]: 
        for _, method in inspect.getmembers(
            main.Testing, predicate=func_filter
        ): yield method

    def data_func(self, inout, problem, func_filter): 
        for data, expected in inout:
            for method in TestSolution.method_gettr(func_filter): 
                print(inspect.signature(method))
                self.assertEqual(method(problem.Testing(), data), expected)
    
    def test_give_first_sig_filt(self):
        # create a signature of list[int]
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
        
        print(type(t_signature))
        
        self.data_func([
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ], main, lambda x: inspect.isfunction(x) and inspect.signature(x) == t_signature)
        
    def test_give_first_name_filt(self):
        self.data_func([
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ], main, lambda x: inspect.isfunction(x) and x.__name__.startswith("give_first"))
        
    def test_give_first_best(self):
        inout = [
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ]
        for i in inout: 
            for method in TestSolution.method_gettr(lambda x: inspect.isfunction(x) and x.__name__.startswith("give_first")): 
                self.assertEqual(method(main.Testing(), i[0]), i[1])
        
    def test_give_first_bad(self): 
        self.assertEqual(main.Testing().give_first([1, 2, 3]), 1)
        self.assertEqual(main.Testing().give_first_alt([1, 2, 3]), 1)
        self.assertEqual(main.Testing().give_first([4, 5, 6]), 4)
        self.assertEqual(main.Testing().give_first_alt([4, 5, 6]), 4)
        self.assertEqual(main.Testing().give_first([7, 8, 9]), 7)
        self.assertEqual(main.Testing().give_first_alt([7, 8, 9]), 7)
        
    def test_give_first_better(self): 
        for method in TestSolution.method_gettr(lambda x: inspect.isfunction(x) and x.__name__.startswith("give_first")): 
            self.assertEqual(method(main.Testing(), [1, 2, 3]), 1)
            self.assertEqual(method(main.Testing(), [4, 5, 6]), 4)
            self.assertEqual(method(main.Testing(), [7, 8, 9]), 7)


    def test_give_first_too_far(self):
        inout = [
            ([1, 2, 3], 1),
            ([4, 5, 6], 4),
            ([7, 8, 9], 7)
        ]
        methods = [method for method in TestSolution.method_gettr(lambda x: inspect.isfunction(x) and x.__name__.startswith("give_first"))]
        for data, expected in inout: 
            results = map(lambda method: method(main.Testing(), data), methods)
            self.assertEqual(list(results), [expected] * len(methods))
        
if __name__ == "__main__": 
    unittest.main()