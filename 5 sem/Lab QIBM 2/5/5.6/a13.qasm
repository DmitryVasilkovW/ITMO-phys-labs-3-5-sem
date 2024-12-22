OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];
creg c[1];
reset q[0];
reset q[1];
reset q[2];
ry(2.094) q[0];
x q[1];
cx q[0], q[2];
