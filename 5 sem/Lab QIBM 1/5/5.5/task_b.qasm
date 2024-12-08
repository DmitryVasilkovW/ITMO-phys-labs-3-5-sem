OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
x q[0];
h q[1];
h q[0];
cx q[1], q[0];
measure q[0] -> c[0];
