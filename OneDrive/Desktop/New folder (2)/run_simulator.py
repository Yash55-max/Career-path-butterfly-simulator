"""
Quick demo of the Stupid Simulator output
"""
import subprocess
import sys

print("=" * 70)
print("RUNNING STUPID SIMULATOR")
print("=" * 70)
print()

# Run the simulator
result = subprocess.run([sys.executable, "stupid_simulator.py"], 
                       capture_output=True, text=True)

# Print all output
print(result.stdout)
if result.stderr:
    print("ERRORS:", result.stderr)

print()
print("=" * 70)
print("SIMULATION COMPLETE!")
print("Check 'stupid_simulator_results.png' for visualizations")
print("=" * 70)
