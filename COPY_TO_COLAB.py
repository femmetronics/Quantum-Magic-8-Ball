"""
═══════════════════════════════════════════════════════════════
🎮 COPY THIS ENTIRE CODE INTO GOOGLE COLAB AND RUN IT! 🎮
═══════════════════════════════════════════════════════════════

INSTRUCTIONS:
1. Go to: https://colab.research.google.com
2. Click: File → New Notebook
3. Copy this ENTIRE file (Ctrl+A, Ctrl+C)
4. Paste into the gray cell (Ctrl+V)
5. Click the ▶️ play button (or press Shift+Enter)
6. Wait 10 seconds, then press ENTER
7. See your quantum answer!

═══════════════════════════════════════════════════════════════
"""

# QUANTUM MAGIC 8-BALL - EASIEST QUANTUM PROJECT EVER!

# Install (takes 10 seconds first time)
# NOTE: The line below with ! only works in Google Colab/Jupyter
# If running locally, install separately: pip install qiskit qiskit-aer
print("📦 Setting up quantum tools...")
import sys
# Uncomment the next line when using in Google Colab:
# !pip install qiskit qiskit-aer -q
print("✅ Ready!\n")

# Import
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Introduction
print("╔" + "=" * 58 + "╗")
print("║" + " " * 16 + "🔮 QUANTUM MAGIC 8-BALL" + " " * 18 + "║")
print("║" + " " * 12 + "Let Quantum Mechanics Decide!" + " " * 16 + "║")
print("╚" + "=" * 58 + "╝")

print("\n💭 Think of a YES or NO question...")
print("   Examples:")
print("   • Will it be sunny tomorrow?")
print("   • Should I study now?")
print("   • Is today my lucky day?")
print("   • Will I ace my test?")

input("\n👉 Press ENTER when ready to get your quantum answer...")

# Create quantum circuit (1 qubit)
print("\n⚛️  Creating quantum superposition...")
qc = QuantumCircuit(1, 1)
qc.h(0)            # Hadamard gate - creates 50/50 superposition
qc.measure(0, 0)   # Measure - collapses to YES or NO

# Run quantum simulation
print("🎲 Consulting the quantum universe...")
simulator = AerSimulator()
job = simulator.run(qc, shots=1)
result = job.result()
counts = result.get_counts()

# Get answer
answer_bit = list(counts.keys())[0]

# Display result with style!
print("\n" + "═" * 60)
if answer_bit == '0':
    print("""
    ██╗   ██╗███████╗███████╗    ██╗
    ╚██╗ ██╔╝██╔════╝██╔════╝    ██║
     ╚████╔╝ █████╗  ███████╗    ██║
      ╚██╔╝  ██╔══╝  ╚════██║    ╚═╝
       ██║   ███████╗███████║    ██╗
       ╚═╝   ╚══════╝╚══════╝    ╚═╝
    """)
    print("    ✨ The quantum universe says: YES! ✨")
else:
    print("""
    ███╗   ██╗ ██████╗ 
    ████╗  ██║██╔═══██╗
    ██╔██╗ ██║██║   ██║
    ██║╚██╗██║██║   ██║
    ██║ ╚████║╚██████╔╝
    ╚═╝  ╚═══╝ ╚═════╝ 
    """)
    print("    🌙 The quantum universe says: NO")

print("═" * 60)

# Educational section
print("\n" + "╔" + "═" * 58 + "╗")
print("║" + " " * 18 + "🎓 WHAT JUST HAPPENED?" + " " * 17 + "║")
print("╚" + "═" * 58 + "╝")

print("""
🔹 Step 1: We created 1 quantum bit (qubit)
           Started in state |0⟩

🔹 Step 2: Applied 'H' gate (Hadamard)
           Put qubit in SUPERPOSITION: 50% |0⟩ + 50% |1⟩
           It was YES and NO at the SAME TIME!

🔹 Step 3: Measured the qubit
           Forced it to "choose" either 0 or 1
           This is TRUE quantum randomness!

🔹 Step 4: Converted to answer
           0 = YES, 1 = NO
           Decided by actual quantum mechanics!

⚛️  Fun Fact: Even with the world's most powerful supercomputer,
   NO ONE could have predicted your answer! That's quantum physics!
""")

# Show the quantum circuit
print("\n📐 The Quantum Circuit We Used:")
print("─" * 60)
print(qc.draw(output='text'))
print("─" * 60)
print("H = Hadamard gate (creates superposition)")
print("M = Measurement (collapses superposition)")

# Call to action
print("\n" + "╔" + "═" * 58 + "╗")
print("║" + " " * 20 + "🚀 WHAT'S NEXT?" + " " * 21 + "║")
print("╚" + "═" * 58 + "╝")

print("""
✅ You just ran a REAL quantum program!
✅ You used quantum superposition!
✅ You made a quantum measurement!
✅ You're officially a quantum programmer!

🎮 Want to try again?
   → Just click the ▶️ play button again!

🎯 Ready for more?
   → Change '0' to 'HEADS' and '1' to 'TAILS' for a coin flip!
   → Use 2 qubits to pick between 4 options!
   → Use 3 qubits to roll a dice (1-6)!

💡 Pro Tip: This is using a simulator, but IBM has REAL
   quantum computers you can use for free!
   Sign up at: https://quantum.ibm.com
""")

print("═" * 60)
print("✨ Thanks for quantum computing with us! ✨")
print("═" * 60)
