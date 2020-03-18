import os
FILE_NAME = "hightemp.txt"
absolute_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def tail(file_name, N):
    with open(file_name) as f:
        lines = f.readlines()
        print("".join(lines[len(lines) - N:]))

if __name__ == "__main__":
    N = int(input("N: "))
    tail("hightemp.txt", N)
