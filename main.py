from patient import Patient
from bmi_calculator import BMICalculator
import google.generativeai as genai
from utils import register, login
import os
from dotenv import load_dotenv
import colorama
from colorama import Fore
import getpass

def main():
    load_dotenv()
    api_key = os.environ["API_KEY"]
    genai.configure(api_key=api_key)

    os.system("figlet Negpod 7")

    print(Fore.BLUE + f"{'Welcome to the BMI App':^0}")
    menu = (
            "╔════════════════════════════════════════════════════╗\n"
            "║                      1. Register                   ║\n"
            "║                      2. Login                      ║\n"
            "║                      3. Exit                       ║\n"
            "╚════════════════════════════════════════════════════╝"
    )
    print(menu)

    try:
        while True:
            choice = input(f"{'Enter your choice:':^0} ")

            if choice == '1':
                register()
            elif choice == '2':
                patient = login()
                if patient:
                    while True:
                        submenu = (
                           "╔════════════════════════════════════════════════════╗\n"
                f"║                          Hi {patient.username}!                ║\n"
                           "║                                                    ║\n"
                           "║                      1. Enter Parameters           ║\n"
                           "║                      2. Get BMI Result             ║\n"
                           "║                      3. View History               ║\n"
                           "║                      4. Health Tips                ║\n"
                           "║                      5. Chat with Dr Claude        ║\n"
                           "║                      6. Exit                       ║\n"
                           "╚════════════════════════════════════════════════════╝"

               )
                        print(submenu)

                        sub_choice = input(f"{'Enter your choice:':^0} ")

                        if sub_choice == '1':
                            height = float(input("Enter your height in cm: "))
                            weight = float(input("Enter your weight in kg: "))
                            date = input("Enter the date (YYYY-MM-DD): ")
                            patient.save_parameters(height, weight, date)
                            print("Parameters Entered Successfully! Check your BMI on 2")
                        elif sub_choice == '2':
                            if patient.height and patient.weight:
                                bmi = BMICalculator.calculate_bmi(patient.height, patient.weight)
                                print(f"Your BMI is: {bmi}")
                            else:
                                print("Please enter your parameters first.")
                        elif sub_choice == '3':
                            patient.view_history()
                        elif sub_choice == '4':
                            print("You need a documentation about your health status hold ctrl on your keyboard and click: https://www.betterhealth.vic.gov.au/health/healthyliving/body-mass-index-bmi")
                        elif sub_choice == '5':
                            query = input(f"Hi {patient.username} I would like to know how to help: ")
                            response = genai.generate_text(
                                model='models/text-bison-001',
                                prompt=query
                            )
                            print(response.result)
                        elif sub_choice == '6':
                            print(menu)
                            break
                        else:
                            print("Invalid choice. Please try again.")
            elif choice == '3':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting gracefully...")

if __name__ == "__main__":
    main()
