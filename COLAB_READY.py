# ═══════════════════════════════════════════════════════════════
# 🎮 QUANTUM MAGIC 8-BALL - FOR GOOGLE COLAB
# ═══════════════════════════════════════════════════════════════
# 
# INSTRUCTIONS:
# 1. Go to: https://colab.research.google.com
# 2. Click: File → New Notebook
# 3. Copy this ENTIRE code
# 4. Paste into a Colab cell
# 5. Click ▶️ (or press Shift+Enter)
# 6. Wait 10 seconds, press ENTER, get your answer!
#
# ═══════════════════════════════════════════════════════════════

# Install quantum tools (only for Colab - takes 10 seconds)
!pip install qiskit qiskit-aer -q

# Import what we need
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Welcome message
print("╔" + "=" * 58 + "╗")
print("║" + " " * 16 + "🔮 QUANTUM MAGIC 8-BALL" + " " * 18 + "║")
print("║" + " " * 12 + "Let Quantum Mechanics Decide!" + " " * 16 + "║")
print("╚" + "=" * 58 + "╝")

print("\n💭 Think of a YES or NO question...")
print("   Examples:")
print("   • Will it be sunny tomorrow?")
print("   • Should I study now?")
print("   • Is today my lucky day?")

input("\n👉 Press ENTER to get your quantum answer...")

# Create quantum circuit
print("\n⚛️  Creating quantum superposition...")
qc = QuantumCircuit(1, 1)
qc.h(0)            # Hadamard gate
qc.measure(0, 0)   # Measurement

# Run simulation
print("🎲 Consulting the quantum universe...")
simulator = AerSimulator()
job = simulator.run(qc, shots=1)
result = job.result()
counts = result.get_counts()

# Get answer
answer_bit = list(counts.keys())[0]

# Show result
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

# Explain what happened
print("\n🎓 WHAT JUST HAPPENED?\n")
print("1️⃣ Created 1 quantum bit (qubit)")
print("2️⃣ Applied H gate → Put it in SUPERPOSITION")
print("   (It was YES and NO at the SAME TIME!)")
print("3️⃣ Measured it → Forced it to choose")
print("4️⃣ Got your answer from quantum mechanics!\n")

# Show circuit
print("📐 The Quantum Circuit:")
print(qc.draw(output='text'))
print("\n✨ You just ran a REAL quantum program! ✨")
print("🎮 Click ▶️ again to ask another question!")
