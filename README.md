# 👥 Sistema de Cadastro de Funcionários (CRUD)

Este projeto consiste em um sistema de gerenciamento de funcionários desenvolvido em Python, convertido para interface web com **Streamlit**. O sistema utiliza os conceitos de funções, dicionários e persistência de dados em arquivos.

## 🔗 Links

- **GitHub:** https://github.com/erkxz/Trabalho
- **Streamlit:** https://funcionarioscrud.streamlit.app/

---

## 📋 Funcionalidades (CRUD)

O sistema conta com as 5 operações fundamentais de gerenciamento:

1. **Cadastrar (Create):** Adiciona um novo funcionário utilizando o CPF como identificador único.
2. **Listar (Read):** Exibe na tela todos os funcionários cadastrados.
3. **Buscar (Read):** Localiza e exibe os dados detalhados de um funcionário específico através do CPF.
4. **Atualizar (Update):** Permite alterar o nome, cargo ou salário de um funcionário existente (mantendo os dados antigos caso o usuário pressione Enter).
5. **Excluir (Delete):** Remove permanentemente um funcionário do sistema.

---

## 🧠 Explicação dos Processos Técnicos

- **Estrutura de Dados:** Utilizamos **Dicionários** (com o formato de dicionário de dicionários). A chave principal é o `CPF` do funcionário, e o valor associado é outro dicionário contendo as propriedades `nome`, `cargo` e `salario`. Isso garante uma busca extremamente rápida e eficiente.
- **Persistência de Dados (Arquivos):** Para garantir que os dados não sejam perdidos ao fechar o programa, utilizamos a biblioteca nativa `json`. O sistema foi projetado para carregar automaticamente o arquivo `funcionarios.json` ao iniciar e atualizar o arquivo em disco imediatamente após qualquer alteração (cadastro, edição ou exclusão).
- **Modularização:** Toda a lógica foi dividida em funções específicas (`carregar`, `salvar`, `cadastrar`, `listar`, `buscar`, `atualizar` e `excluir`), facilitando a manutenção do código.

---

## ⚠️ Dificuldades Enfrentadas

Durante o desenvolvimento, a nossa maior dificuldade foi estruturar o caminho do arquivo JSON de forma relativa utilizando a biblioteca `os`. Inicialmente, o programa apresentava erro ao procurar o arquivo caso fosse executado de pastas diferentes. Resolvemos o problema utilizando os métodos `os.path.dirname` e `os.path.abspath` para mapear a pasta do script dinamicamente.

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Streamlit
- JSON (armazenamento de dados)

---

## 🤖 Uso de Inteligência Artificial

Em conformidade com as regras estabelecidas, realizamos intervenções de IA durante o projeto:

**Projeto original (terminal):**
1. **Intervenção 1:** Consulta para entender a melhor forma de atualizar dados no dicionário permitindo que o usuário dê "Enter" para manter o valor atual (implementado na função `atualizar`).
2. **Intervenção 2:** Auxílio na formatação e estrutura do design técnico deste arquivo `README.md` para a apresentação do repositório.

**Conversão para Streamlit — IA utilizada: Claude (Anthropic)**

### Prompts utilizados:

1. *"https://github.com/erkxz/Trabalho meu github"* — envio do repositório para leitura e conversão para Streamlit
2. *"como eu faço pra criar e mandar isso pra alguém"* — dúvida sobre deploy no Streamlit Cloud
3. *"só retire os # do código"* — remoção dos comentários do app.py
4. *"o que é o requirements.txt"* — dúvida sobre o arquivo de dependências
5. *"preciso fazer isso?"* — confirmação sobre a necessidade do requirements.txt
6. *"agora crie um readme pra eu colocar com tudo que foi colocado e os links tanto do github quanto do streamlit que é esse https://funcionarioscrud.streamlit.app/"* — geração do README
7. *"pegue o slide que eu mandei e deixe o readme que já tem mas acrescente o que o slide pede"* — atualização do README conforme o enunciado do trabalho

---

## 🚀 Como Rodar Localmente

```bash
pip install streamlit
streamlit run app.py
```
