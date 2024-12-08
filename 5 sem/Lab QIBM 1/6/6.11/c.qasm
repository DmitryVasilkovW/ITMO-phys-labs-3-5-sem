OPENQASM 2.0;
include "qelib1.inc";

qreg q[1];
creg c[1];
reset q[0];
rx(0.927) q[0];
h q[0];
barrier q; // @phaseDisk
