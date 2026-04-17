# Script README.py atualizado
titulo = "# 💻 Desafios e Projetos - DIO\n"
descricao = "Repositório centralizador de desafios técnicos e projetos práticos desenvolvidos na plataforma DIO.\n"

tabela = "### 📚 Lista dos Desafios DIO\n\n"
tabela += "| Desafio | Titulo |\n"
tabela += "|:--- |:--- |\n"

# Dicionário de projetos atualizado com o Desafio 04
projetos_fixos = {
    0: "[Modelos de Entidade Relacional - EER](./00)",
    1: "[Modelagem Dimensional - Professor](./01)",
    2: "[E-commerce Database](./02)",
    3: "[Oficina Mecânica Database](./03)",
    4: "[Modelagem Star Schema - E-commerce](./04)",
    5: "[Dashboard Gerencial para Tomada de Decisões](./05)"
}

# Gerando as linhas da tabela
for i in range(16):
    nome_projeto = projetos_fixos.get(i, f"Desafio {i:02d} em desenvolvimento...")
    tabela += f"| Desafio {i:02d} | {nome_projeto} |\n"

tabela += "| Referência | [Documentação Git & GitHub](https://git-scm.com/docs) |\n"

# Rodapé estruturado para portfólio
footer = "\n---\n*Versionamento de código estruturado para portfólio acadêmico e profissional.*"

with open("README.md", "w", encoding="utf-8") as f:
    f.write(titulo + descricao + tabela + footer)

print("✅ README.md atualizado: Desafio 04 incluído e rodapé ajustado!")