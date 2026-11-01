# Basic Comm Sys
import numpy as np
import matplotlib.pyplot as plt

# Convert Message into Binary
message = "Hello World"

binary_string = ''.join(format(ord(char), '08b') for char in message)

bits = np.array([int(bit) for bit in binary_string])

print("Message:", message)
print("Binary Data:")
print(binary_string)

# Plot Original Binary Data
plt.figure(figsize=(15,2))
plt.step(range(len(bits)), bits, where='mid')
plt.title("Original Binary Data (Hello World)")
plt.xlabel("Bit Index")
plt.ylabel("Bit Value")
plt.grid(True)
plt.show()

# BPSK Modulation
bpsk = 2 * bits - 1

print("BPSK Symbols:")
print(bpsk)

# Plot Transmitted BPSK Signal
plt.figure(figsize=(15,2))
plt.step(range(len(bpsk)), bpsk, where='mid')
plt.title("Transmitted BPSK Signal")
plt.xlabel("Bit Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Generate Noise
noise = np.random.normal(0, 0.5, len(bpsk))

print("Noise:")
print(noise)

# Received Signal
received = bpsk + noise

print("Received Signal:")
print(received)

# Plot Received Signal
plt.figure(figsize=(15,2))
plt.plot(received)
plt.title("Received BPSK Signal with AWGN")
plt.xlabel("Bit Index")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()

# Compare Transmitted and Received Signals
plt.figure(figsize=(15,4))

plt.plot(bpsk, label="Transmitted", linewidth=2)
plt.plot(received, label="Received with Noise", linestyle='--')

plt.title("Comparison of Transmitted and Received Signal")
plt.xlabel("Bit Index")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()



#theory
A basic communication system consists of three main parts: Transmitter (Tx), Channel, and Receiver (Rx). 
The transmitter converts the input binary message into a signal using BPSK modulation, where 0 is represented by -1 and 1 by +1. 
The signal passes through the communication channel, where AWGN (Additive White Gaussian Noise) may affect it. 
The receiver detects the received signal and converts it back into binary data.
The received signal is then plotted and compared with the transmitted signal to observe the effect of noise and differences between both signals.
