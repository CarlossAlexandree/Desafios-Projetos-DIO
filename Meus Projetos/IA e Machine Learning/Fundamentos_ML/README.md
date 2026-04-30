# Fundamentos de Machine Learning

Repositório dedicado aos conceitos base que garantem a performance, escalabilidade e compreensão profunda de modelos de inteligência artificial.

## 🧪 Conteúdos Atuais

### 1. [Fundamentos de Tensores e Diferenciação](./Fundamentos_ML/)
Base teórica e prática utilizando a biblioteca **PyTorch** para manipulação de dados e cálculo computacional.
- **Tensores em 2D:** Criação, propriedades (shape, size), conversões para NumPy/Pandas, fatiamento e operações matriciais avançadas.
- **Diferenciação Automática:** Implementação prática de gradientes (Autograd) para funções simples e derivadas parciais, conceito essencial para o algoritmo de *Backpropagation*.

### 2. [Manipulação e Customização de Dados](./Fundamentos_ML/)
Estruturas necessárias para alimentar modelos de forma eficiente.
- **Dataset Personalizado:** Construção de classes `Dataset` customizadas para dados sintéticos e aplicação de transformações lineares.
- **DataLoaders:** Gerenciamento de lotes (*batches*) e embaralhamento (*shuffling*) para treinamento otimizado.
- **Dataset de Imagens Sintéticas:** Geração programática de formas geométricas para validação de visão computacional e aplicação de transformações (rotação, flip, normalização).

### 3. [Pipelines de Treinamento e Avaliação](./Fundamentos_ML/)
O fluxo completo de desenvolvimento de um modelo.
- **Datasets Pré-construídos:** Exploração de benchmarks como **MNIST** e **Fashion-MNIST**, incluindo técnicas de *Data Augmentation*.
- **Construção de Redes Neurais:** Implementação de arquiteturas `nn.Module`, funções de perda (*Cross Entropy*) e otimizadores (*Adam*).
- **Ciclo de Treinamento:** Monitoramento de métricas de *Loss* e *Accuracy* tanto em treino quanto em validação para controle de performance.

### 4. [Generalização e Regularização](./Generalizacao-Regularizacao/)
- **Overfitting & Underfitting:** Análise de como o modelo aprende padrões vs. memorização.
- **Regularização L1/L2:** Técnicas para penalizar pesos complexos e melhorar a generalização.
- **Validação Cruzada:** Estratégias robustas para avaliação de performance.

## 🎯 Objetivo
Garantir que os modelos desenvolvidos não apenas performem bem em dados de treino, mas sejam resilientes a dados novos (produção), fundamentados em uma manipulação de dados rigorosa e cálculos matemáticos precisos.

---

### 🛠 Ferramentas Utilizadas
- **Python 3.x**
- **PyTorch** (Tensors, Autograd, nn, optim)
- **Matplotlib** (Visualização de dados e funções)
- **NumPy & Pandas** (Processamento de dados)