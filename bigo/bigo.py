import math

class BigO:
    @staticmethod
    def constant_time():
        """
        Time Complexity: O(1)
        """
        return lambda n: 1
    
    @staticmethod
    def logarithmic_time():
        """
        Time Complexity: O(log n)
        """
        return lambda n: 0 if n <= 1 else 1 + BigO.logarithmic_time()(n // 2)
    
    @staticmethod
    def linear_time():
        """
        Time Complexity: O(n)
        """
        return lambda n: n
    
    @staticmethod
    def linearithmic_time():
        """
        Time Complexity: O(n log n)
        """
        return lambda n: 0 if n <= 1 else BigO.logarithmic_time()(n) + n * BigO.logarithmic_time()(n // 2)
    
    @staticmethod
    def quadratic_time():
        """
        Time Complexity: O(n^2)
        """
        return lambda n: n ** 2
    
    @staticmethod
    def cubic_time():
        """
        Time Complexity: O(n^3)
        """
        return lambda n: n ** 3
    
    @staticmethod
    def exponential_time():
        """
        Time Complexity: O(a^n) (where a > 1)
        """
        return lambda n: 2 ** n  # Change this to adjust the base of the exponent
    
    @staticmethod
    def factorial_time():
        """
        Time Complexity: O(n!)
        """
        return lambda n: 1 if n == 0 else n * BigO.factorial_time()(n-1)
