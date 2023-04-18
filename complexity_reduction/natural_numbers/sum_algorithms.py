from fractions import Fraction

class NaturalNumbersSum:

    """Collection of functions to use for natural numbers.

    In this module natural numbers are positive integers and 0, even though
    the 0 is not a natural number by formal definitions.
    """

    @staticmethod
    def _verify_natural_number(n) -> None:
        assert type(n) == int
        assert n >= 0

    @staticmethod
    def _is_a_large_number(n) -> bool:
        return not (n == (n * n / 2) ** (0.5))
    
    @staticmethod
    def _is_multiplication_of_large_numbers(n, m):
        max_num = max(n, m)
        return NaturalNumbersSum._is_a_large_number(max_num)

    @staticmethod
    def sum_from_1_to_n(n: int):
        """Sum of natural numbers from 1 to n.

        To increase the performance of the function we use the following
        mathematical formula:

        1 + 2 + ... + n = n * (n + 1) / 2
    

        There is a technical issue with how Python calculates the float operations:
        >>> x = 10000000000000001
        >>> x == (x * (x) ) ** (1/2)
        False

        We need to consider this issue in solving this problem.

        Algorithm Complexity
        ------------
        Time Complexity: O(1)
        Memory Complexity: O(1)
        """
        NaturalNumbersSum._verify_natural_number(n)
        if NaturalNumbersSum._is_multiplication_of_large_numbers(n, n+1):
            return int(Fraction(n) * (Fraction(n) + Fraction(1)) / Fraction(2))
        else:
            return n * (n + 1) / 2

    @staticmethod
    def sum_from_m_to_n(m, n):
        """Sum of natural numbers from m to n.

        The m should be smaller than n, but even if it is not, the function
        will automatically handle it. So finally the function will return
        sum of natural number between min(m,n) to max(m, n).

        To increase the performance of the function we use the following
        mathematical formula:

        m + ... + n = (n - m + 1)(n + m) / 2   

        There is a technical issue with how Python calculates the float operations:
        >>> x = 10000000000000001
        >>> x == (x * (x) ) ** (1/2)
        False

        We need to consider this issue in solving this problem.

        Algorithm Complexity
        ------------
        Time Complexity: O(1)
        Memory Complexity: O(1)
        """
        NaturalNumbersSum._verify_natural_number(m)
        NaturalNumbersSum._verify_natural_number(n)
        if NaturalNumbersSum._is_multiplication_of_large_numbers(n + m , n - m + 1):
            return int((Fraction(n)-Fraction(m) + 1) * (Fraction(n) + Fraction(m)) / Fraction(2))
        else:
            return (n - m + 1) * (n + m) / 2