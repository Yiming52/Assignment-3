class EuclideanAlgorithm:
    def __init__(self):
        pass

    def gcd(self, a, b):
        """
        This method calculates the greatest common divisor (GCD) of two numbers
        using the Euclidean Algorithm.

        Parameters:
        a (int): First positive integer
        b (int): Second positive integer

task.pytask.py        Returns:
        int: GCD of the two integers
        """
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a


# Example usage
if __name__ == "__main__":
    algo = EuclideanAlgorithm()
    result = algo.gcd(48, 18)
    print("GCD is:", result)

