from braket.circuits import Circuit
from braket.devices import LocalSimulator
# from braket.aws import AwsDevice

# Create a quantum circuit and adding a Hadamard-gate on the first qubit h(0)
qc = Circuit().h(0)

# The result of the Hadamard-gate gets finally processed using a cNOT-gate
qc.cnot(control=0, target=1)
print(qc)

# Set up the device to run the circuit on LocalSimulator
device = LocalSimulator()

# Set up the device to run the circuit on
# device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")

# Run the circuit on the device(Local/Managed Stimulator)
result = device.run(qc, shots=1000).result()

# Print the results
# print(result)

# Process the results of the circuit
counts = result.measurement_counts
print("Hello, quantum computing:", counts)