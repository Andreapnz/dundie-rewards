# 🏆 Dundie Rewards

![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Versão](https://img.shields.io/badge/version-0.1.0-blue)
![Plataforma](https://img.shields.io/badge/terminal-app-informational)
![Licença](https://img.shields.io/badge/license-MIT-green)

Projeto de Sistema de recompensas desenvolvido para a Dunder Mifflin, fabricante de papel, com foco em motivar colaboradores através de pontos de desempenho e bonificações. 🧻✨

---

## 🚀 Visão Geral

O **Dundie Rewards** é um sistema de recompensas que permite ao gerente e aos colaboradores da empresa:

- Atribuir e visualizar pontos de performance.
- Transferir pontos entre funcionários.
- Armazenar e consultar movimentações.
- Exportar relatórios.
- Garantir segurança com autenticação por senha.

O MVP é totalmente funcional via **terminal**, com base de dados em **SQL** e leitura de arquivos `.csv` ou `.json`.

---

## 🎯 Funcionalidades do MVP `v0.1.0`

### 📁 Administração (`ADMIN`)

| Comando | Ação |
|--------|------|
| `dundie load people.txt` | Importa lista de funcionários do arquivo |
| `dundie show --filter --sort --limit --output` | Exibe relatório filtrado e exportável |
| `dundie add --dept=<nome> --value=<valor>` | Adiciona pontos para departamento |
| `dundie add --to=<email> --value=<valor>` | Adiciona pontos para usuário específico |

#### ✅ Regras
- Gerentes iniciam com **100 pontos**, associados com **500 pontos**.
- Atualizações são somadas à pontuação.
- Validação de e-mails e duplicatas.
- Geração de senha automática enviada por email.
- Acesso às funções administrativas **protegido por senha**.

---

### 👤 Movimentações (`FUNCIONÁRIO`)

| Ação | Descrição |
|------|-----------|
| Visualizar saldo de pontos | Histórico e total acumulado |
| Transferir pontos | Envio de pontos entre colegas |
| Segurança | Acesso protegido por senha individual |

---

### 🔐 Segurança
Todas as operações sensíveis são protegidas por login e senha. As senhas iniciais são geradas automaticamente e enviadas para os usuários por e-mail.

---
###  📈 Futuras Evoluções
 - Interface Web (Django ou Flask)
 - API RESTful
 - Interface Gráfica para Desktop
 - Resgate de pontos via integração com cartão de crédito

--- 
### 📁 Dados de Entrada
O sistema aceita arquivos .csv ou .json com os seguintes campos:
nome,departamento,cargo,email

---
### 🤝 Contribuições
Sinta-se à vontade para abrir issues ou enviar pull requests.

---
 
### 📬 Onde me encontrar
📧 [andrea_pnz@hotmail.com](mailto:andrea_pnz@hotmail.com)

🔗 [LinkedIn – Andrea Correia Costa](https://www.linkedin.com/in/andrea-correia-costa/)


