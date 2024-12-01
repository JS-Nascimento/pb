import matplotlib.pyplot as plt

algorithms = ['Bubble Sort', 'Selection Sort', 'Insertion Sort']
times = [4.463016, 1.951252, 2.012025]

plt.bar(algorithms, times, color=['red', 'blue', 'green'])
plt.title('Tempo de Execução dos Algoritmos de Ordenação')
plt.xlabel('Algoritmos')
plt.ylabel('Tempo (segundos)')
plt.show()
