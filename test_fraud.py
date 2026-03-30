import requests
import json

# This is the address where your main.py is listening
URL = "http://127.0.0.1:8000/predict"

def run_test():
    print("\n================================")
    print("   AI FRAUD DETECTION CLIENT   ")
    print("================================\n")

    try:
        # Get inputs from you in the terminal
        v1 = float(input("Enter V1 (e.g., -1.1): "))
        v2 = float(input("Enter V2 (e.g., 2.5): "))
        v3 = float(input("Enter V3 (e.g., -0.2): "))
        v4 = float(input("Enter V4 (e.g., 0.5): "))
        amount = float(input("Enter Amount: "))

        # Create the data packet
        payload = {
            "V1": v1,
            "V2": v2,
            "V3": v3,
            "V4": v4,
            "Amount": amount
        }

        # Send the data to your AI server
        response = requests.post(URL, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            status = result['status']
            prob = result['probability']

            print("\n--- AI ANALYSIS RESULT ---")
            print(f"RESULT: {status}")
            print(f"FRAUD PROBABILITY: {float(prob)*100:.2f}%")
            print("--------------------------")
        else:
            print(f"Error: Server returned status code {response.status_code}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
    except Exception as e:
        print(f"Could not connect to AI. Make sure 'python main.py' is running! \nError: {e}")

if __name__ == "__main__":
    while True:
        run_test()
        again = input("\nTest another transaction? (y/n): ")
        if again.lower() != 'y':
            print("Exiting client...")
            break