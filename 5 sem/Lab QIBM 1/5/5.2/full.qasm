OPENQASM 2.0;
include "qelib1.inc";

qreg q[2];
creg c[1];
reset q[0];
reset q[1];
measure q[0] -> c[0];
x q[1];
measure q[1] -> c[0];
