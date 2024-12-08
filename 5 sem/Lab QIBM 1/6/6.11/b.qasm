OPENQASM 2.0;
include "qelib1.inc";

qreg q[1];
creg c[1];
reset q[0];
rx(1.04720) q[0];
rz(pi/2) q[0];
barrier q; // @phaseDisk
