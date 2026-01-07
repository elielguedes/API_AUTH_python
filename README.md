#API autenticação de usuarios e clientes com perfis personalizados 

## 📊 Diagrama ER - Modelagem de Dados
### 🔗 Relacionamentos
- **1:N** — Um **Usuário** pode cadastrar vários **Clientes**
- **1:N** — Um **Cliente** pode solicitar vários **Serviços**

```mermaid
erDiagram
    %% === ENTIDADES PRINCIPAIS ===
    USUARIO ||--O{ CLIENTES : "cadastrar"
    CLIENTES ||--O{ SERVICOS : "solicita"
    SERVICOS {
        int id pk "cheve primária"
        string nome
        string descricao
        float preco
        datetime duracao_min
        bool ativo
        datetime novo_horario
        int cliente_id FK "Referencia ao cliente"
    }
    CLIENTES {
        int id PK 
        string nome
        string email
        string senha
        int telefone
        bool ativo
    }
    USUARIO {
        int id FK
        string nome 
        string email
        string senha
        string ativo
        string admin
    }

