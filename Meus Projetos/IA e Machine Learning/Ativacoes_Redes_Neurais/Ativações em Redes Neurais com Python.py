import numpy as np
import matplotlib.pyplot as plt

# --- FUNÇÕES DE APOIO ---

def sigmoid(x):
    """Função de ativação Sigmóide."""
    return 1.0 / (1.0 + np.exp(-x))

def sigmoid_derivative(x):
    """Derivada da função Sigmóide para o Backpropagation."""
    sig = sigmoid(x)
    return sig * (1 - sig)

def mean_squared_error(y_true, y_pred):
    """Cálculo do Erro Quadrático Médio."""
    return np.mean((y_true - y_pred) ** 2)

# --- ARQUITETURA E PROPAGAÇÃO ---

def initialize_network(num_inputs, num_hidden_layers, num_nodes_hidden, num_nodes_output):
    """Inicializa pesos e bias da rede neural."""
    np.random.seed(42)
    num_nodes_previous = num_inputs
    network = {}

    for layer in range(num_hidden_layers + 1):
        if layer == num_hidden_layers:
            layer_name = 'output'
            num_nodes = num_nodes_output
        else:
            layer_name = f'layer_{layer + 1}'
            num_nodes = num_nodes_hidden[layer]

        network[layer_name] = {}
        for node in range(num_nodes):
            node_name = f'node_{node + 1}'
            network[layer_name][node_name] = {
                'weights': np.around(np.random.uniform(size=num_nodes_previous), decimals=2),
                'bias': np.around(np.random.uniform(size=1), decimals=2)[0]
            }
        num_nodes_previous = num_nodes

    return network

def forward_propagate_with_tracking(network, inputs):
    """Realiza a propagação para frente e rastreia as saídas de cada camada."""
    layer_inputs = list(inputs)
    all_layer_outputs = []

    for layer in network:
        layer_data = network[layer]
        layer_outputs = []

        for node_name in layer_data:
            node_data = layer_data[node_name]
            # Soma ponderada: sum(inputs * weights) + bias
            weighted_sum = np.sum(layer_inputs * node_data['weights']) + node_data['bias']
            node_output = sigmoid(weighted_sum)
            layer_outputs.append(np.around(node_output, 4))

        all_layer_outputs.append(layer_outputs)
        layer_inputs = layer_outputs

    return all_layer_outputs, layer_outputs

# --- VISUALIZAÇÃO ---

def plot_layer_outputs(all_layer_outputs):
    """Gera gráficos de barras das saídas de cada camada."""
    plt.figure(figsize=(12, 5))
    num_layers = len(all_layer_outputs)

    for i, outputs in enumerate(all_layer_outputs, 1):
        plt.subplot(1, num_layers, i)
        plt.bar([f"Nó {j+1}" for j in range(len(outputs))], outputs, color='skyblue')
        plt.title(f'Camada {i}')
        plt.ylim(0, 1)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

# --- TREINAMENTO (BACKPROPAGATION) ---

def train_network(X, y, epochs=1000, lr=0.1, l2_lambda=0.01):
    """Treina uma rede simples de 2 camadas com Regularização L2."""
    np.random.seed(42)

    # Inicialização simplificada para exemplo XOR
    w1 = np.random.uniform(size=(2, 2))
    b1 = np.random.uniform(size=2)
    w2 = np.random.uniform(size=2)
    b2 = np.random.uniform()

    print("\n📈 Iniciando Treinamento...")
    for epoch in range(epochs):
        # Forward Pass
        z1 = np.dot(X, w1) + b1
        a1 = sigmoid(z1)
        z2 = np.dot(a1, w2) + b2
        a2 = sigmoid(z2)

        # Custo com L2
        cost = mean_squared_error(y, a2) + l2_lambda * (np.sum(w1**2) + np.sum(w2**2))

        # Backpropagation
        dz2 = (a2 - y) * sigmoid_derivative(z2)
        dw2 = np.dot(a1.T, dz2) + l2_lambda * w2
        db2 = np.sum(dz2)

        dz1 = np.dot(dz2.reshape(-1, 1), w2.reshape(1, -1)) * sigmoid_derivative(z1)
        dw1 = np.dot(X.T, dz1) + l2_lambda * w1
        db1 = np.sum(dz1, axis=0)

        # Gradiente Descendente
        w2 -= lr * dw2
        b2 -= lr * db2
        w1 -= lr * dw1
        b1 -= lr * db1

        if epoch % 200 == 0:
            print(f'Época {epoch}, Custo: {round(cost, 4)}')

    print("✅ Treinamento concluído.\n")
    return w1, b1, w2, b2

# --- BLOCO PRINCIPAL ---

if __name__ == "__main__":
    # 1. Simulação de Propagação
    print("🌟 --- PARTE 1: INICIALIZAÇÃO E FORWARD ---")
    n_inputs = 5
    input_data = np.around(np.random.uniform(size=n_inputs), decimals=2)
    print(f"Entradas: {input_data}")

    # Rede: 5 entradas, 3 camadas ocultas [3, 2, 3 nós], 1 saída
    my_net = initialize_network(n_inputs, 3, [3, 2, 3], 1)
    all_outputs, final_pred = forward_propagate_with_tracking(my_net, input_data)
    
    print(f"Previsão final: {final_pred}")
    plot_layer_outputs(all_outputs)

    # 2. Simulação de Treinamento (XOR)
    print("🌟 --- PARTE 2: TREINAMENTO (BACKPROP) ---")
    X_train = np.array([[0,0], [0,1], [1,0], [1,1]])
    y_train = np.array([0, 1, 1, 0])
    
    w1, b1, w2, b2 = train_network(X_train, y_train)