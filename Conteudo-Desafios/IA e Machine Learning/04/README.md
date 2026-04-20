# 🧠 Classificador de Dígitos com Keras (MNIST)

Este projeto foi desenvolvido como parte do exercicio prático nas aulas de meu mestrado internacional em Inteligência Artificial. Utilizando Keras e TensorFlow, treinamos uma rede neural para classificar dígitos manuscritos do famoso dataset **MNIST**.

---

## 📂 Estrutura do Projeto

- `Keras_Modelo_de_Classificação_com_MNIST.ipynb`: Notebook com código completo, explicado passo a passo.
- `imagens/`: Contém gráficos gerados (ex: acurácia, matriz de confusão).
- `README.md`: Este arquivo, com a descrição do projeto.

---

## 🧪 Técnicas utilizadas

- Pré-processamento de dados com `to_categorical`
- Modelagem com redes densas (Fully Connected)
- Treinamento com validação
- Avaliação da acurácia com gráficos comparativos

---

## 📊 Resultados

- **Acurácia no teste:** ~98%
- **Perda (loss):** < 0.07
- Gráficos: Curva de aprendizado, acurácia x épocas, perda x épocas

---

## 📈 Gráficos de desempenho

Exemplos (adicione na pasta `/imagens` depois):
- ![Acurácia](imagens/acuracia.png)
- ![Perda](imagens/loss.png)

---

## 🏁 Como executar

1. Clone este repositório
```bash
git clone https://github.com/seu-usuario/classificador-mnist-keras
