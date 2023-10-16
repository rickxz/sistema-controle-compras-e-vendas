## 🏁 Comece

#

### ⚙️ Clone o projeto em sua máquina

- Para executar a aplicação, você deve possuir o **Python** instalado em sua máquina.


Você pode clonar o repositório executando os seguintes comandos em seu terminal:
```bash
git clone https://github.com/rickxz/sistema-controle-compras-e-vendas.git
cd sistema-controle-compras-e-vendas
python main.py
```

# 

###

## 📝 Informações do projeto

Uma aplicação para uma loja de cosméticos precisa armazenar informações sobre os
seus clientes, bem como sobre a compra/venda de produtos. Os dados a serem armazenados
sobre cada cliente, produto e sobre a compra/venda de produtos por cliente são apresentados
a seguir:

- Cliente = (<u>CPF</u>, Nome, Data de Nascimento, Sexo, Salário, E-mails, Telefones)
- Produto = (<u>Código</u>, Descrição, Peso, Preço, Desconto, Data de Validade)
- Compra/Venda = (<u>CPF Cliente, Código Produto, Data, Hora</u>, Valor)

**Atenção**: os atributos grifados são **chaves** e você NÃO deve permitir a inclusão de mais
de um cadastro com os mesmos valores para os atributos chaves.

Utilizando os conhecimentos aprendidos sobre Dicionários, Listas e Funções, desenvolva
um programa em Python que apresente o seguinte <u>menu de opções</u> para o usuário e implemente cada operação usando **função**. Escolha a estrutura de dados mais apropriada para armazenar os dados de cada entidade descrita anteriormente.

Menu Principal:
1. Submenu de Clientes
2. Submenu de Produtos
3. Submenu de Compra/Venda
4. Submenu Relatórios
5. Sair

Cada Submenu deverá oferecer as opções: Listar todos, Listar um, Incluir (sem
repetição), Alterar e Excluir (após confirmação dos dados) um elemento do conjunto.
Observe que as informações que estão no **plural** significam que deve ser possível incluir
vários itens do mesmo atributo, por exemplo, os atributos E-mails e Telefones, devem
permitir a inclusão de todos os e-mails e telefones daquele cliente. O Submenu Relatórios
deverá ter uma opção para cada um dos relatórios solicitados abaixo.

Relatórios:
1.  Mostrar todos os dados de todos os clientes que possuem mais do que
X telefones, onde X deve ser fornecido pelo usuário;
2.  Mostrar todos os dados de todos os produtos que já tiveram sua data
de validade vencida, considerando a data do sistema no momento da
execução;
3. Mostrar o CPF e nome do cliente, código do produto, descrição e os
demais dados das vendas que foram realizadas entre as datas X e Y,
onde ambas as datas devem ser fornecidas pelo usuário.

**OBS**: Utilize **Arquivos** para a persistência dos dados manipulados pela aplicação. Em outras
palavras, cada registro de cliente, produto e compra/venda deverá ser armazenado em um
**arquivo texto** específico, que conterá apenas registros daquele mesmo tipo de entidade. Os
relatórios também devem ser guardados em arquivos.