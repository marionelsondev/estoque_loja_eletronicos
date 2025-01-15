# Sistema de Controle de Estoque para Loja de Eletrônicos em Python

### Ferramentas Utilizadas:
- **Python**: Linguagem principal do projeto.
- **SQLAlchemy**: ORM (Object Relational Mapper) para interagir com o banco de dados.
- **SQLite**: Banco de dados leve e embutido utilizado no sistema.

---

### Como rodar o projeto?

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/marionelsondev/estoque_loja_eletronicos.git
    ```

2. **Crie um ambiente virtual para isolar as dependências:**
    ```bash
    python -m venv venv
    ```

3. **Ative o ambiente virtual:**
    - **Windows**:
      ```bash
      venv\Scripts\activate
      ```
    - **Linux/Mac**:
      ```bash
      source venv/bin/activate
      ```

4. **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Execute o sistema:**
    - Acesse o arquivo `main.py` e execute-o para interagir com o sistema:
      ```bash
      python main.py
      ```

---

### Estrutura do Projeto:

```plaintext
estoque_loja_eletronicos/
├── main.py          # Arquivo principal onde a aplicação é executada.
├── models.py        # Define os modelos/tabelas do banco de dados (SQLite).
├── crud.py          # Contém funções CRUD para manipular dados.
├── requirements.txt # Lista de dependências necessárias para o projeto.
└── README.md        # Documentação do projeto.
```

---

### Funcionalidades:
- **Cadastro de Produtos:** Adicione novos produtos ao sistema.
- **Atualização de Produtos:** Atualize informações como nome, preço ou quantidade.
- **Exclusão de Produtos:** Remova produtos do estoque.
- **Visualização de Estoque:** Consulte os produtos disponíveis e suas quantidades.
- **Realização de Vendas:** Registre vendas com detalhes de cliente, data e quantidade.
- **Relatório de Vendas:** Visualize todas as vendas realizadas no sistema.
