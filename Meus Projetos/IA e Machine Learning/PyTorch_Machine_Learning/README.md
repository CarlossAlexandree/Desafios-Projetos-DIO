# 🤖 Engenharia de Deep Learning com PyTorch: Laboratórios Práticos

Este repositório reúne um ecossistema de projetos práticos focados no desenvolvimento, otimização e interpretabilidade de redes neurais profundas utilizando PyTorch. O conteúdo é estruturado para demonstrar, de forma progressiva, a construção de modelos de aprendizado profundo, desde fundamentos matemáticos até arquiteturas avançadas aplicadas.

Os laboratórios conectam teoria e prática por meio de uma abordagem orientada à Engenharia de Machine Learning, incorporando boas práticas de processamento de dados, treinamento acelerado em GPU e técnicas modernas de interpretabilidade (XAI). Além disso, os modelos são integrados a interfaces interativas, permitindo validação e análise em tempo real.
---

## 📂 Estrutura de Aprendizado e Laboratórios

Abaixo, os módulos organizados por evolução de complexidade e aplicação.

| Lab | Título do Laboratório | Descrição Técnica | Link |
|:--- |:--- |:--- |:--- |
| **01** | **Regressão Linear 1D** | Implementação "do zero" para entender a mecânica dos gradientes. | [🔗 Abrir](./Regressão_Linear_1D_com_Treinamento_do_Zero.ipynb) |
| **02** | **Custo e Gradiente (Batch)** | Estudo profundo sobre o comportamento do erro e convergência. | [🔗 Abrir](./Função_de_Custo_+_Gradiente_Descendente_(Batch).ipynb) |
| **03** | **Gradiente com Momentum** | Técnicas para acelerar a convergência e evitar mínimos locais. | [🔗 Abrir](./Gradiente_Descendente_com_Momentum.ipynb) |
| **04** | **Funções de Ativação** | Estudo comparativo entre Sigmoid, Tanh e ReLU (Derivadas). | [🔗 Abrir](./Funções_de_Ativação_Sigmoid,_Tanh_e_ReLU.ipynb) |
| **05** | **Inicialização de Pesos** | Técnicas Uniforme, Xavier e He para estabilidade do treino. | [🔗 Abrir](./Inicialização_de_Pesos_Uniforme,_Xavier_e_He.ipynb) |
| **06** | **Regressão Logística** | Classificação binária e visualização de fronteira de decisão. | [🔗 Abrir](./Regressão_Logística_com_Múltiplas_Entradas.ipynb) |
| **07** | **MSE vs BCELoss** | Comparação de funções de perda em problemas binários. | [🔗 Abrir](./Regressão_logística_binária_em_PyTorch,_comparando_(MSE)_com_(BCELoss).ipynb) |
| **08** | **Batch Norm vs. Dropout** | Estudo de técnicas de regularização contra overfitting. | [🔗 Abrir](./Batch_Normalization_vs_Dropout.ipynb) |
| **09** | **Fashion MNIST Class.** | **Classificação de vestuário utilizando `nn.Module` e `DataLoader`.** | [🔗 Abrir](./PyTorch_Classificação_com_Fashion_MNIST.ipynb) |
| **10** | **Operações Convolucionais** | Visualização de filtros e mapas de ativação (Feature Maps). | [🔗 Abrir](./Operações_Convolucionais.ipynb) |
| **11** | **Construção de CNNs** | Arquiteturas completas de Redes Convolucionais para visão. | [🔗 Abrir](./Construção_de_CNNs.ipynb) |
| **12** | **Uso de GPU com CUDA** | Scripts otimizados para aceleração via hardware NVIDIA. | [🔗 Abrir](./Uso_de_GPU_com_CUDA.ipynb) |
| **13** | **Visualização Grad-CAM** | Implementação de Mapeamento de Ativação de Classe (XAI). | [🔗 Abrir](./Visualização_com_Grad_CAM_(Gradient_weighted_Class_Activation_Mapping).ipynb) |
| **14** | **Visual Final Grad-CAM** | Auditoria de modelos com sobreposição de mapas de calor. | [🔗 Abrir](./Visual_final_Grad_CAM_sobre_imagem_de_entrada.ipynb) |

### 📊 Módulo 2: Engenharia de Analytics e Deploy Interativo (Streamlit)

Este módulo foca na transformação de modelos de Machine Learning em aplicações utilizáveis, cobrindo desde a fundação estatística até a exposição do modelo via interface web.

| Notebook | Título / Objetivo | Aplicação Prática | Link |
|:--- |:--- |:--- |:--- |
| **01** | **Classificação Logística** | Predição de resultados com métricas de acurácia. | [🔗 Abrir](./Notebook_1_—_Classificação_com_Regressão_Logística.ipynb) |
| **02** | **Limpeza de Dados** | Tratamento de inconsistências, nulos e conversão de tipos. | [🔗 Abrir](./Notebook_2_—_Exploração_e_Limpeza_de_Dados.ipynb) |
| **03** | **Estatística Descritiva** | Análise de variância, tendências centrais e correlação. | [🔗 Abrir](./Notebook_3_—_Estatística_Descritiva_e_Correlação.ipynb) |
| **04** | **Comparação de Modelos** | Benchmarking entre Regressão Logística, Árvores e SVM. | [🔗 Abrir](./Notebook_4_—_Comparação_de_Classificadores.ipynb) |
| **05** | **Interface com Streamlit** | Criação de UI para entrada de dados de modelos. | [🔗 Abrir](./Notebook_5_—_Interface_com_Streamlit.ipynb) |
| **06** | **Gráficos Dinâmicos** | Visualizações interativas com Plotly para dashboards. | [🔗 Abrir](./Notebook_6_—_Gráficos_Dinâmicos_com_Plotly.ipynb) |
| **07** | **Regressão Linear** | Predição de valores contínuos e visualização de tendências. | [🔗 Abrir](./Notebook_7_—_Regressão_com_Predição_Visual_de_Valores.ipynb) |
| **08** | **Consumo de API Pública** | Integração de dados externos (Câmbio) em tempo real. | [🔗 Abrir](./Notebook_8_—_Consumo_de_API_Pública.ipynb) |
| **09** | **Feature Importance** | Análise de relevância das variáveis na predição do modelo. | [🔗 Abrir](./Notebook_9_—_Visualização_de_Importância_das_Features.ipynb) |
| **10** | **Showcase Final** | Full-Stack: Modelo + Dashboard + Deploy via ngrok. | [🔗 Abrir](./Notebook_10_Showcase_com_Streamlit.ipynb) |

> **Nota de Deploy:** Os projetos que utilizam Streamlit (Notebooks 05, 10) requerem a instalação do `streamlit` e `pyngrok` para visualização externa a partir de ambientes como o Google Colab.
---

## 🏗️ Framework de Evolução em Deep Learning

O repositório está organizado para refletir o crescimento da complexidade dos modelos:

1.  **Fundamentos e Tensores**: Manipulação de dados e implementação de gradientes "do zero".
2.  **Otimização de Arquitetura**: Uso de `nn.Module`, `DataLoader` e técnicas de regularização.
3.  **Visão Computacional**: Redes Convolucionais (CNN) aplicadas a datasets como Fashion-MNIST.
4.  **Interpretabilidade (XAI)**: Uso de Grad-CAM para visualização de decisões da rede.
5.  **Deploy e Valor de Negócio**: Integração com Streamlit para interfaces produtivas.

---

## 🎯 Aplicação em Engenharia de Analytics

Este repositório endereça pilares críticos do mercado de dados:
* **Garantia de Eficiência**: Uso de CUDA para processamento de alto desempenho.
* **Interpretabilidade**: O uso do Grad-CAM permite que stakeholders confiem nas decisões do modelo (Explainable AI).
* **Reprodutibilidade**: Notebooks estruturados para execução direta via Google Colab e deploy via Streamlit/ngrok.

---

## 🧪 Pilha Tecnológica

* **Framework Principal**: PyTorch
* **Engenharia de Dados**: NumPy, Pandas, Scikit-learn
* **Infraestrutura**: Google Colab, pyngrok, CUDA (GPU NVIDIA)
* **Visualização e XAI**: Matplotlib, Plotly, OpenCV (cv2)

---

## 🚀 Como Executar

Cada arquivo `.ipynb` é um laboratório independente. Para rodar os projetos localmente:

1. **Clone o repositório**:
   ```bash
   git clone [https://github.com/CarlossAlexandree/PyTorch-com-Aprendizado-de-Maquina.git](https://github.com/CarlossAlexandree/PyTorch-com-Aprendizado-de-Maquina.git)
    ```
2.  **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Execução de Apps Interativos**:
    Para os modelos integrados ao Streamlit, execute:
    ```bash
    streamlit run nome_do_arquivo.py
    ```

---