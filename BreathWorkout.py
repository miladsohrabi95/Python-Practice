import time

def breath_workout():
    print("Welcome to the Breath Workout App!")
    print("Follow the instructions below to do a quick breath exercise.")

    # Inhale
    print("\nStep 1: Inhale deeply for 4 seconds.")
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)
    print("Inhale")

    # Hold breath
    print("\nStep 2: Hold your breath for 4 seconds.")
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)
    print("Hold")

    # Exhale
    print("\nStep 3: Exhale slowly for 4 seconds.")
    for i in range(4, 0, -1):
        print(i)
        time.sleep(1)
    print("Exhale")

    print("\nGreat job! You have completed the breath exercise.")

if __name__ == "__main__":
    breath_workout()
