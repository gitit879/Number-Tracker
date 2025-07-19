# app.py
def track_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or 'q' to quit): ")
        if num == 'q':
            break
        numbers.append(float(num))
        print(f"Current numbers: {numbers}")

if __name__ == "__main__":
    track_numbers()
