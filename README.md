# LAB_api_dev

Bem-vindo ao repositório **LAB_api_dev**! Este projeto foi criado como parte de um laboratório de desenvolvimento de APIs, explorando conceitos fundamentais de bancos de dados e APIs RESTful.

## Sobre o Projeto

Neste projeto, construímos uma API para gerenciar entidades relacionadas ao ambiente acadêmico. A aplicação gerencia **Professores**, **Turmas** e **Alunos**, abordando operações essenciais (CRUD) para cada entidade e implementando relacionamentos entre elas.

### Estrutura das Entidades

1. **Professor**
   - Cada professor pode estar associado a várias turmas.
   - Atributos: `id`, `nome`, `especialidade`, entre outros.

2. **Turma**
   - Cada turma está associada a um único professor e pode incluir vários alunos.
   - Atributos: `id`, `nome`, `professor_id` (chave estrangeira), etc.

3. **Aluno**
   - Cada aluno pertence a uma única turma.
   - Atributos: `id`, `nome`, `idade`, `turma_id` (chave estrangeira), etc.

### Relacionamentos

- **One-to-Many**: Um professor pode lecionar em várias turmas, mas cada turma tem um único professor.
- **One-to-Many**: Uma turma pode ter vários alunos, mas cada aluno está em uma única turma.

### Ferramentas Utilizadas

- **Postman**: Para testar e documentar endpoints.
- **GitHub**: Para controle de versão e colaboração em equipe.
- **Linguagens e Frameworks**: (Detalhe aqui as tecnologias, como Python com Flask, Node.js, ou outra tecnologia que tenha utilizado.)


