import numpy as np
import sys
sys.path.append('C:\\Users\\Leonardo\\Documents\\gaussian_python\\Quantum-Gaussian-Information-Toolbox-main')
import matplotlib.pyplot as plt
import random
import quantum_gaussian_toolbox as gauss
import time
#C:\Users\Leonardo\Documents\gaussian_python\Quantum-Gaussian-Information-Toolbox-main
#
# R = np.random.uniform(1, 10, size=(4, 1))
# V=np.random.uniform(1, 10, size=(4, 4))

start_time = time.time()
#
# x = np.linspace(-5, 5, 100)
# y=x**2+x

results1 = []
count = 0
while count < 1000:
    state = gauss.generate_entangled(2.5)
    avqfi = gauss.avqfi(state)
    nbar = (gauss.only_modes(state,[0]).occupation_number().item())
    valor = (nbar,avqfi)
    results1.append(valor)
    count += 1
    print(count)

np.savetxt("avqfi_sep_teste.dat", results1)

# results2 = []
# count = 0
# while count < 100000:
#     state = gauss.generate_mixed_thermal(2.5)
#     interf_power = gauss.interf_power(state.V)
#     nbar = (gauss.only_modes(state,[0]).occupation_number().item())
#     valor = (nbar,interf_power)
#     results2.append(valor)
#     count += 1
#     print(count)
#
# np.savetxt("interf_power_mixed1.dat", results2)

# results3 = []
# count = 0
# while count < 100000:
#     state = gauss.generate_standard(2.5)
#     interf_power = gauss.interf_power(state.V)
#     nbar = (gauss.only_modes(state,[0]).occupation_number().item())
#     valor = (nbar,interf_power)
#     results3.append(valor)
#     count += 1
#
# np.savetxt("interf_power_all1.dat", results3)

# nbar_values = [result[0] for result in results]
# interf_power_values = [result[1] for result in results]

# plt.scatter( nbar_values, interf_power_values, marker='o',color = 'blue', s=2)
# plt.plot(x, y,color='r',linestyle='--')
# plt.xlabel('$n_A$')
# plt.ylabel('$\mathcal{P}_A$')
# plt.title('Gráfico de Interf Power vs $n_A$ - teste 1')
# plt.grid(True, color='0.7')
# plt.xlim(0, 2.1)
# plt.ylim(0, 7)
# plt.show()

end_time = time.time()
execution_time = end_time - start_time

print(f"Tempo total de execução: {execution_time:.4f} segundos")