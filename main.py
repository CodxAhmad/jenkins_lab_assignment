
import numpy as np
import time

# Ask the user for matrix size
n = int(input("Enter the matrix size (N): "))

# Start total execution timer
total_start = time.perf_counter()

# Generate two random matrices
generation_start = time.perf_counter()

A = np.random.rand(n, n)
B = np.random.rand(n, n)

generation_end = time.perf_counter()

print("\nMatrix generation completed.")
print("Matrix A  Shape:", A.shape)
print("Matrix B shape:", B.shape)
print("Time before multiplication:", generation_end - total_start, "seconds")
