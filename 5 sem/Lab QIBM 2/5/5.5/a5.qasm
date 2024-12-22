OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
ry(1.6709637) q[0];
cx q[0], q[1];
z q[1];
