# The leaky integrate-and-fire (LIF) model

import matplotlib.pyplot as plt

N = 1000           # number of measurememnts (time points)
g_L = 0.7          # leak conductance [nS]
c_m = 20           # conductance [nF/mm^2]
tau_M = c_m /g_L   # membrane time constant [ms]
i = 50             # input current [nA]
v_reset = -65      # reset potential [mV] (mimics the neuron returning to its resting state)
v_thresh = -50     # threshold [mV]
dt = 0.1           # time step
E_L = -75          # leak reversal potential [mV]
v = [v_reset]      # list of potential values, start at v_reset

for _ in range(N):
    # increment of memebrane potential
    dv = (-(v[-1] - E_L) + i/g_L) * dt / tau_M
    v_new = v[-1] + dv # new membrane potential
    if v_new >= v_thresh:
        v.append(v_reset)
    else:
        v.append(v_new)

plt.figure(figsize=(10,5), facecolor = 'white')
plt.plot(v, color = 'black', lw=4)
plt.axhline(
    v_thresh, linestyle='dashed',
    lw=1, label='Threshold',
    color='red')
plt.axhline(
    v_reset, linestyle='dashed',
    lw=1, label='Reset',
    color='blue')
plt.legend()
plt.xlabel('Time point')
plt.ylabel('V, [mV]')
plt.title('Membrane potential', fontsize=14, fontweight='bold')
plt.show()