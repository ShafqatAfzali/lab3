import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# Tidsvektor (0 til 5 sekunder med steg på 0.01 sekund)
t = np.arange(0, 5, 0.01)
N_MAX = 5  # Antall harmoniske frekvenser
T = 1  # Periode i sekunder

# Funksjon for å lage Fourierserie


def fourierSeries(n_max, t):
    partialSums = 0
    for n in range(1, n_max):  # summerer over antall frekvenskomponenter
        try:
            # Beregner ampltitude basert på formel (7) i oppgaven
            bn = 4/(np.pi*(2*n-1))
            # Beregner frekvens basert på formel (7) i oppgaven
            wn = 2*np.pi*(2*n-1)/T
            partialSums = partialSums + bn*np.sin(wn*t+np.pi)
        except:
            print("pass")
            pass
    return partialSums


# lager fourierSerien for trekant signalet (denne koden blir lik for firkant)
f = fourierSeries(N_MAX, t)

# Plotter
plt.style.use("ggplot")
# Bruker signal biblioteket fra scipt for å plotte et trekant-signal
# For å plotte firkant brukes funksjonen signal.square
plt.plot(t, signal.square(2*np.pi*(1/T)*t-np.pi), color="blue", label="Signal")
plt.plot(t, f, 'r--', label="Fourierserie-approksimasjon")
plt.xlabel('t[s]')
plt.title("Fourierserie-approksimasjon med antall ledd = "+str(N_MAX))
plt.legend(loc=1)
plt.tight_layout()
plt.show()
