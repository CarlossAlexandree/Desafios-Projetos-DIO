# 🤖 PyTorch & Deep Learning: Laboratórios de IA Avançada

Este repositório reúne um ecossistema de projetos práticos desenvolvidos durante a disciplina de **Artificial Intelligence Development** do Mestrado em IA. O foco central é a implementação, otimização e explicabilidade de redes neurais profundas utilizando **PyTorch**.

Os laboratórios aqui presentes conectam a teoria rigorosa com a **Engenharia de Analytics**, aplicando boas práticas de processamento de dados, treinamento em GPU e técnicas de interpretabilidade de modelos (XAI) para suportar decisões baseadas em dados.

---

## 📂 Estrutura dos Laboratórios

O repositório está organizado conforme a evolução da complexidade dos modelos:

### 1. Fundamentos e Otimização
* **Regressão Linear 1D:** Implementação do treinamento "do zero" para entender a mecânica dos gradientes.
* **Função de Custo & Gradiente Descendente:** Estudo profundo sobre o comportamento do erro e convergência.
* **Gradiente Descendente com Momentum:** Técnicas para acelerar a convergência e evitar mínimos locais.

### 2. Arquitetura de Redes Neurais
* **Funções de Ativação:** Estudo comparativo entre Sigmoid, Tanh e ReLU, incluindo a análise de suas derivadas.
* **Inicialização de Pesos:** Implementação de técnicas de inicialização Uniforme, Xavier e He para estabilidade do treinamento.
* **Regularização (Batch Norm vs Dropout):** Técnicas fundamentais para evitar overfitting e melhorar a generalização do modelo.

### 3. Visão Computacional Avançada
* **Operações Convolucionais:** Visualização de filtros e mapas de ativação em imagens.
* **Construção de CNNs:** Arquiteturas completas para classificação e processamento visual.
* **Uso de GPU com CUDA:** Scripts otimizados para transferência de tensores e aceleração de hardware.

### 4. Interpretabilidade e Explicabilidade (XAI)
* **Visualização com Grad-CAM:** Implementação de *Gradient-weighted Class Activation Mapping* para entender quais áreas da imagem o modelo prioriza para tomar uma decisão.
* **Visual Final sobre Imagem:** Sobreposição de mapas de calor para auditoria de modelos de visão computacional.

---

## 🛠️ Stack Tecnológica

* **Framework Principal:** PyTorch
* **Engenharia de Dados:** NumPy, Pandas
* **Visualização & XAI:** Matplotlib, OpenCV (cv2)
* **Infraestrutura:** Google Colab / CUDA (NVIDIA GPU)

---

## 🎯 Aplicação em Engenharia de Analytics

Este repositório endereça pilares críticos da Engenharia de Analytics ao:
1.  **Garantir a Eficiência:** Uso de CUDA para processamento de grandes volumes de dados.
2.  **Interpretabilidade:** O uso de Grad-CAM transforma "caixas-pretas" em modelos explicáveis, permitindo que stakeholders de negócio confiem nas previsões.
3.  **Reprodutibilidade:** Notebooks estruturados para execução direta via Google Colab.

---

## 🚀 Como Executar

Cada arquivo `.ipynb` é um laboratório independente. Para rodar:

1. Clone o repositório:
   ```bash
   git clone [https://github.com/CarlossAlexandree/PyTorch-com-Aprendizado-de-Maquina.git](https://github.com/CarlossAlexandree/PyTorch-com-Aprendizado-de-Maquina.git)
