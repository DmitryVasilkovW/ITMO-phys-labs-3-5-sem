OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
reset q[0];
reset q[1];
ry(2.0943951) q[0];
cx q[0], q[1];
x q[1];
z q[1];
