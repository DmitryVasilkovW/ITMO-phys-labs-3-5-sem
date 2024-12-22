OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
reset q[0];
reset q[1];
ry(pi / 2) q[0];
cry(pi/2) q[0], q[1];
