from braket.circuits import Circuit
from braket.aws import AwsDevice
from braket.devices import LocalSimulator

# Define a simple quantum circuit
qc = Circuit().h(0).cnot(0, 1)

# Run the circuit on the local simulator
local_device = LocalSimulator()
local_result = local_device.run(qc, shots=1000).result()
local_counts = local_result.measurement_counts

# Run the circuit on the managed simulator
managed_device = AwsDevice('arn:aws:braket:::device/quantum-simulator/amazon/sv1')
managed_result = managed_device.run(qc, shots=1000).result()
managed_counts = managed_result.measurement_counts

# Compare the measurement outcomes
difference = {}
for key in local_counts.keys():
    difference[key] = local_counts[key] - managed_counts.get(key, 0)

print("Local counts:", local_counts)
print("Managed counts:", managed_counts)
print("Difference:", difference)

total_shots = sum(local_counts.values())  # or use managed_counts instead
local_probs = {k: v / total_shots for k, v in local_counts.items()}
managed_probs = {k: v / total_shots for k, v in managed_counts.items()}

from scipy.stats import pearsonr

corr_coef, p_value = pearsonr(list(local_probs.values()), list(managed_probs.values()))
print("Correlation coefficient:", corr_coef)
