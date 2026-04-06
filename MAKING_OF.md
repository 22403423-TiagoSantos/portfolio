# Making Of - Portfólio

## 1. Processo de Modelação: Unidade Curricular

### Evolução e Decisões de Modelação
* **Código da UC:** Inicialmente, seria intuitivo usar um campo numérico (`IntegerField`) para o código da disciplina. No entanto, após analisar os dados fornecidos pela API da Lusófona, verifiquei que o identificador único (`curricularIUnitReadableCode`) contém caracteres alfanuméricos e hífens (ex: `ULHT260-898`). Para garantir a compatibilidade e evitar perdas de dados, optei por usar um `CharField(max_length=20)`.
* **Separação de Ano e Semestre:** Na versão base, cheguei a ponderar um campo de texto único (`ano_semestre`). Contudo, decidi evoluir o modelo separando esta informação em dois campos numéricos distintos (`ano` e `semestre`, ambos `IntegerField`). Isto torna a base de dados muito mais robusta, permitindo fazer pesquisas e filtros exatos (ex: "Listar todas as UCs do 2º Semestre do 3º Ano").
* **Enriquecimento de Dados:** Para aproveitar a riqueza da informação devolvida pela API, adicionei campos `TextField` adicionais (`objetivos`, `conteúdos`, `bibliografia`, `metodologia`). Isto exigiu que definisse `blank=True, null=True` nestes campos para não quebrar a base de dados nas disciplinas criadas manualmente antes da execução do script de carregamento.

### Relações
* **ManyToMany com Docentes e Licenciaturas:** Foi estabelecida uma relação de "Muitos-para-Muitos". Uma Unidade Curricular pode ser lecionada por vários Docentes e partilhada entre várias Licenciaturas (ex: cadeiras comuns a Engenharia Informática e Informática de Gestão).

### Erros e Resoluções
* **Erro de Migração (Campos Non-Nullable):** Ao adicionar os campos extra no modelo já existente, o Django exigiu um valor por defeito (`default`). Resolvi o problema abortando a migração inicial, ajustando o `models.py` para permitir campos nulos e vazios, e voltando a correr `makemigrations` com sucesso.

### Evidências de Planeamento (Caderno)
![Diagrama de Entidade-Relacionamento](/media/makingof/der.jpeg)
![Atributos](/media/makingof/atributos.jpeg)
![Observações](/media/makingof/observações.jpeg)

---

## 2. Processo de Modelação: Projeto

### Evolução e Decisões de Modelação
* **Evolução Dinâmica (Tarefa 6):** Durante a fase de inserção de dados reais, percebi que apenas o título e a descrição não eram suficientes para um portfólio de engenharia. Decidi adicionar o campo `ano_realizacao` (`IntegerField`) para permitir uma ordenação cronológica e o campo `link_video` (`URLField`) para demonstrações práticas, algo que não estava previsto no planeamento inicial.
* **Detalhamento Técnico:** Adicionei o campo `conceitos_aplicados` (`TextField`) para destacar as aprendizagens teóricas aplicadas na prática, indo além da simples descrição do que o projeto faz.

### Relações
* **ForeignKey com Unidade Curricular:** Implementei uma relação de "Um-para-Muitos". Um projeto está obrigatoriamente ligado a uma disciplina, permitindo que o visitante do site navegue do trabalho prático para o contexto académico da cadeira.
* **ManyToMany com Tecnologias:** Como um projeto utiliza várias ferramentas (ex: Python e SQLite) e uma tecnologia pode estar em vários projetos, esta relação foi a escolha lógica para flexibilidade da base de dados.

### Evidências de Planeamento
![Atributos do Projeto](/media/makingof/atributos.jpeg)
![Relações de Projetos](/media/makingof/relações.jpeg)

---

## 3. Processo de Modelação: Perfil

### Evolução e Decisões de Modelação
* **Centralização de Dados:** O modelo `Perfil` foi criado para evitar a repetição de dados pessoais em múltiplas tabelas. Optei por usar `ImageField` para a foto e `URLField` para os links externos (LinkedIn/GitHub), garantindo a validação automática de endereços web pelo Django.
* **Título Profissional:** Incluí este campo para permitir uma apresentação mais formal (ex: "Estudante de Engenharia Informática") em vez de um simples nome.

### Relações
* **Ponto de Ligação Central:** O Perfil serve como a entidade "mestre", à qual a maioria das outras entidades (Competência, Formação, MakingOf) se liga por `ForeignKey`, garantindo que toda a informação do site pertence ao mesmo utilizador.

### Evidências de Planeamento
![Esquema do Perfil](/media/makingof/atributos.jpeg)

---

## 4. Processo de Modelação: TFC (Trabalho Final de Curso)

### Evolução e Decisões de Modelação
* **Adaptação para Dados Externos:** Após analisar o JSON de TFCs da DEISI, verifiquei que os campos `autor`, `orientador` e `resumo` eram essenciais. Adicionei campos para o `link_pdf` e `link_imagem` para que o portfólio pudesse exibir a capa e permitir o download do trabalho.
* **Classificação:** Mantive o campo `classificacao` como `IntegerField` para permitir, futuramente, filtrar os trabalhos com melhor nota.

### Relações
* **ForeignKey com Licenciatura:** Cada TFC está estritamente ligado a um curso específico, garantindo a integridade dos dados académicos.

### Evidências de Planeamento
![Observações TFC](/media/makingof/observações.jpeg)

---

## 5. Processo de Modelação: Tecnologia e Competência

### Evolução e Decisões de Modelação
* **Tecnologia (Visual):** Adicionei um campo de `logo` (`ImageField`) para permitir uma interface mais rica com ícones de cada linguagem ou framework.
* **Competência (Nível de Domínio):** Para tornar o portfólio mais informativo, criei o campo `nivel_dominio` (`IntegerField`). Isto permite ao utilizador perceber visualmente o meu grau de proficiência em cada área (ex: de 1 a 5).

### Relações
* **Relação com Projetos:** Ambas as entidades ligam-se a `Projeto` por Many-to-Many, permitindo filtrar quais projetos comprovam cada competência ou uso de tecnologia.

### Evidências de Planeamento
![Atributos Tecnologias](/media/makingof/atributos.jpeg)

---

## 6. Processo de Modelação: MakingOf (Entidade)

### Evolução e Decisões de Modelação
* **Documentação Nativa:** Criei esta entidade especificamente para cumprir o requisito de integrar o "diário de bordo" na própria aplicação. Usei `TextField` para permitir descrições detalhadas dos erros encontrados (como os problemas de migração).
* **Gestão de Imagens:** Incluí um campo `imagem` para possibilitar o upload e exibição das fotografias dos meus esquemas e apontamentos feitos no caderno diretamente no site.

### Justificação de Relação
* **Ligação ao Perfil:** Relacionado com `Perfil` para identificar o autor da documentação, mantendo a estrutura lógica de todo o sistema.

### Evidências de Planeamento
![Planeamento do Making Of](/media/makingof/atributos%20(continuação).jpeg)

---

## 7. Utilização de Inteligência Artificial e Metodologia

* **IA como Co-piloto:** O uso de IA foi estratégico para a criação dos scripts `loader.py` e `loader_ucs.py`, ajudando a processar a lógica de iteração dos ficheiros JSON. Foi também fundamental na resolução de erros de sintaxe e bugs de migração do Django.
* **Metodologia "Paper-First":** Como comprovado pelas fotografias anexadas, toda a lógica de relações e atributos foi primeiro desenhada em papel. A implementação no Django e o refinamento via IA serviram apenas para concretizar o que foi planeado manualmente.