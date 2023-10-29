import matplotlib.pyplot as plt
import json

def load_data_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def visualize_data(data):
    warehouses = list(data.keys())
    algorithms = set()
    for warehouse in data:
        for result in data[warehouse]:
            algorithms.add(result["algorithm"])
    algorithms = list(algorithms)

    fig, axs = plt.subplots(len(warehouses), 1, figsize=(10, 6 * len(warehouses)))

    for idx, warehouse in enumerate(warehouses):
        algo_steps = []
        for algorithm in algorithms:
            steps_for_algo = next((x['steps'] for x in data[warehouse] if x['algorithm'] == algorithm), "N/A")
            if steps_for_algo == "Impossible":
                steps_for_algo = 0
            algo_steps.append(steps_for_algo)
        
        axs[idx].bar(algorithms, algo_steps, color=['blue', 'green', 'red', 'cyan'])
        axs[idx].set_title(warehouse)
        axs[idx].set_ylabel('Number of Steps')
        axs[idx].set_xlabel('Algorithm')
        for i, v in enumerate(algo_steps):
            if v == 0:
                axs[idx].text(i, 1, "Impossible", ha='center', va='bottom', rotation=0, color='black')
            else:
                axs[idx].text(i, v + 1, str(v), ha='center', va='bottom', rotation=0, color='black')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # file_path = input("Please enter the path to your JSON file: ")
    data = load_data_from_file('result.json')
    visualize_data(data)
