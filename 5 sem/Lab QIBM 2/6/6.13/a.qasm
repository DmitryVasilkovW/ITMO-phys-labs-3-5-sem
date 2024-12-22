OPENQASM 2.0;
include "qelib1.inc";

qreg q[6];
creg c[5];
x q[0];
x q[1];
x q[2];
cx q[1], q[3];
reset q[1];
cx q[2], q[4];
reset q[2];
measure q[3] -> c[3];
cx q[0], q[2];
measure q[4] -> c[4];
measure q[1] -> c[1];
reset q[0];
measure q[2] -> c[1];
measure q[0] -> c[0];
