class BMICalculator:
    @staticmethod
    def calculate_bmi(height, weight):
        try:
            height_m = height / 100  # Convert height to meters
            bmi = weight / (height_m ** 2)
            return round(bmi, 2)
        except ZeroDivisionError:
            print("Height must be greater than 0.")
            return None
