# Projeto: Servidor Web Apache com Docker Compose 🚀

Este repositório contém a entrega do primeiro projeto prático de **Fundamentos em Docker**. O objetivo é demonstrar a orquestração de um servidor web Apache (`httpd`) utilizando o Docker Compose para servir uma aplicação HTML customizada.

## 📋 Descrição do Projeto

O projeto consiste em configurar e executar um contêiner Docker que hospeda uma página web. Foi utilizado o conceito de **Volumes** para vincular os arquivos de código localizados na máquina hospedeira diretamente com o diretório de exibição do servidor Apache dentro do contêiner.

### Requisitos Atendidos:
* Criação de um arquivo `docker-compose.yml` com definições de servidor Apache
* Especificação do local dos arquivos da aplicação via volumes
* Implementação de uma aplicação web (HTML/CSS)
* Versionamento e subida do código para repositório GitHub

---

## 🛠️ Tecnologias Utilizadas

* **Docker**: Plataforma de conteinerização.
* **Docker Compose**: Ferramenta para definir e rodar aplicações multi-contêiner.
* **Apache (httpd)**: Servidor web de código aberto.
* **HTML5/CSS3**: Para a interface da aplicação.

---

## 📂 Estrutura de Pastas

```text
meu-projeto-web/
├── app/
│   └── index.html       # Arquivo da aplicação web
└── docker-compose.yml   # Configuração da orquestração Docker