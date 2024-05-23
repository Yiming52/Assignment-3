class EuclideanAlgorithm:
    def __init__(self):
        pass

    def gcd(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    def lcm(self, a, b):
        gcd_value = self.gcd(a, b)
        return (a * b) // gcd_value


# Example usage
if __name__ == "__main__":
    algo = EuclideanAlgorithm()

    while True:
        try:
            a = int(input("Enter the first positive integer: "))
            b = int(input("Enter the second positive integer: "))
            if a <= 0 or b <= 0:
                raise ValueError("Both numbers must be positive integers.")
            break
        except ValueError as ve:
            print(ve)

    gcd_result = algo.gcd(a, b)
    lcm_result = algo.lcm(a, b)
    print("GCD is:", gcd_result)
    print("LCM is:", lcm_result)
