import time
from collections import deque

def measure_time_memory(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

if __name__ == "__main__":
    with open("lista_arquivos.txt", "r") as f:
        file_list = f.read().splitlines()

    # Hashtable
    hashtable = {}
    _, time_insert_hash = measure_time_memory(lambda: [hashtable.update({i: file}) for i, file in enumerate(file_list)])
    print(f"Hashtable: Inserção de {len(file_list)} itens levou {time_insert_hash:.6f} segundos")

    positions = [1, 100, 1000, 5000, len(file_list) - 1]
    _, time_search_hash = measure_time_memory(lambda: [hashtable.get(pos) for pos in positions])
    print(f"Hashtable: Recuperação levou {time_search_hash:.6f} segundos")

    _, time_remove_hash = measure_time_memory(lambda: [hashtable.pop(i, None) for i in positions])
    print(f"Hashtable: Remoção levou {time_remove_hash:.6f} segundos")

    # Pilha
    stack = []
    _, time_insert_stack = measure_time_memory(lambda: [stack.append(file) for file in file_list])
    print(f"Pilha: Inserção de {len(file_list)} itens levou {time_insert_stack:.6f} segundos")

    _, time_search_stack = measure_time_memory(lambda: [stack[pos] for pos in positions])
    print(f"Pilha: Recuperação levou {time_search_stack:.6f} segundos")

    _, time_remove_stack = measure_time_memory(lambda: [stack.pop() for _ in positions])
    print(f"Pilha: Remoção levou {time_remove_stack:.6f} segundos")

    # Fila
    queue = deque()
    _, time_insert_queue = measure_time_memory(lambda: [queue.append(file) for file in file_list])
    print(f"Fila: Inserção de {len(file_list)} itens levou {time_insert_queue:.6f} segundos")

    _, time_search_queue = measure_time_memory(lambda: [list(queue)[pos] for pos in positions])
    print(f"Fila: Recuperação levou {time_search_queue:.6f} segundos")

    _, time_remove_queue = measure_time_memory(lambda: [queue.popleft() for _ in positions])
    print(f"Fila: Remoção levou {time_remove_queue:.6f} segundos")
