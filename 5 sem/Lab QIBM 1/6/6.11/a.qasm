OPENQASM 2.0;
include "qelib1.inc";

qreg q[1];
creg c[1];
rx(0.927) q[0];
h q[0];
measure q[0] -> c[0];
