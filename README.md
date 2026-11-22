# QuBlitz-2026----Alberts
Quantum Minesweeper: QuBlitz 2026 Error Correction Challenge
Team: The Alberts (Airas Farrell, Noah Bayih, Tabish Farrell)

The goal of this Challenge was to create a quantum error correction algorithm to amend single Pauli errors on one qubit in a system of 3 qubits. This was achieved by detecting where the error occurred with 2 ancillary qubits and flipping the erred qubit without measuring it and collapsing the qubit system.
Summary

Level 1:
Pauli X error in one unknown qubit (run on IQM Garnet Software. q0, q1, and q2 hold data, while q3 and q4 were utilized as ancilla qubits. 2 CNOTs spread information across 3 qubits. CNOTs were utilized to write 2 parity checks into the ancilla qubits q3 and q4, where q3 detects differences in q0 and q1 value, and q4 detects differences in q1 and q2 value. Both superposition branches are exact opposites, and therefore produce the same parities, which are then used to detect which qubit was flipped without revealing  and . To correct the flipped qubit, CCX gates were incorporated controlled by q3 and q4. Decoding the message is done by applying the 2 CNOTs in reverse order.

Level 2:
The Pauli Z errors in the default frame are not always recognized by the parity checks, as Z only changes sign while maintaining the probabilities. Utilizing n H gate to all three data qubits before and after the Pauli Z error take place produce the frame of reference equivalent to that of the X Pauli error, given by the property HZH = X. In this reference frame, the previous Level 1 parity checks are run and decoded in the same fashion. 

Level 3
The Pauli Y error, defined by Y = iXZ, produces a bit flip that can be detected immediately by the previous parity set up, however it does not account for the sign change of the Z factor. We apply an S to all 3 data qubits before the flip occurs and an S after, as the relation between Y and X can be defined as SYS = X. Using this relation, once again the Level 1 parity check algorithm can be run. 
Results of Methods to Scrutiny

To test our program results, we used Statevector and show_state to show the original state vector the qubits were in before encoding, what the state vector looked like with the error, and then what it looked like after the correction algorithm was run. Ignoring the ancilla qubit values, the first 3 qubits in the Original had to match those in the Fixed in both bit strings and complex amplitudes, in order to be deemed successful. We tested |+->, |+-i>, including |0> and |1>, to definitively check that quantum information survived along with the classical bit.
IQM Hardware Results of Level 1 Circuit

The utilized backend was Garnet IQM Resonance, 1000 shots per circuit. Because a real chip returns measured string bits and not state vectors, we redesigned the circuit such that the correct result is a definite string. Using Qiskit, the string is written as q4q3q0. The right most digit is the message qubit. 0 means it survived. The left two digits are the syndrome. 
Attached in this Repository are the raw counts from the shots on our circuit using Garnet. The correct string was the most frequent outcome in all 4 cases: no error, q0, q1,q2. The most common failure was right syndrome, damaged message; the second most common string has the correct syndrome but a 1 in message digit. We attempt to explain this using the chips own noise, producing dephasing/Z errors. Z errors flip |-> to |+>, which is read as 1 after the second H is applied. The parity checks used in Level 1 cannot detect Z flips, so this extra noise is a factor when the X errors are fixed correctly. 


Mine
Ideal string
Most frequent string
All 3 bits right
Syndrome right
Message survived
none
000
000
64.9%
81.8%
74.7%
q0
010
010
63.4%
77.9%
77.0%
q1
110
110
58.2%
73.2%
73.6%
q2
100
100
52.3%
78.2%
64.3%

