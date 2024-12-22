OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
reset q[0];
reset q[1];
h q[0];
x q[1];
cx q[0], q[1];
