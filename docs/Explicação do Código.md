# Explicação do Projeto de Conversão de AFe para AFN

Este projeto tem como objetivo a conversão de autômatos finitos com movimentos vazios (AFe) em autômatos finitos não determinísticos (AFN). Utilizando Python, o projeto implementa uma interface gráfica simples que permite ao usuário carregar uma definição de AFe a partir de um arquivo JSON, processá-lo e visualizar as transições resultantes tanto do AFe quanto do AFN.

## Código - main.py

### 1. Sobre as bibliotecas
 ![image](https://github.com/user-attachments/assets/b79e10bb-cadb-4b84-932b-dfc323bffa50)

O código começa com a importação das bibliotecas necessárias:

- **graphviz**: Usada para visualizar os autômatos em forma de grafo. 
- **json**: Para manipulação de arquivos JSON, que contêm as definições dos autômatos.
- **tkinter**: Biblioteca para criação de interfaces gráficas. É usada para criar a janela que abre para selecionar o arquivo JSON.
- 

### 2. Sobre as funções:

#### a. load_automaton_from_json: Função que carrega os dados de um autômato a partir de um arquivo JSON.
![image](https://github.com/user-attachments/assets/70b0329a-58fa-4290-bcb1-136cbb36bc19)
- **filepath**: Caminho para o arquivo JSON.
- **transitions**: Dicionário que representa as transições do autômato.
- **start_state**: Estado inicial do autômato.
- **final_state**: Um ou mais estados finais do autômato.

**> A função tenta abrir e ler o arquivo JSON especificado pelo caminho. Se o arquivo for encontrado e estiver corretamente formatado, ela retorna as transições, o estado inicial e os estados finais do autômato. Caso ocorra um erro (como o arquivo não ser encontrado ou estar mal formatado), a função imprime uma mensagem de erro e retorna None para cada um dos valores esperados.**

#### b. select_file: Função que permite ao usuário selecionar um arquivo JSON contendo os dados de um autômato e realiza várias operações com esses dados.
![image](https://github.com/user-attachments/assets/43f2ee49-22e5-414b-ae92-58b2c9429c61)
- **filepath**: Caminho para o arquivo JSON selecionado pelo usuário.
- **afe_transitions**: Dicionário que representa as transições do autômato finito estocástico (AFE).
- **start_state**: Estado inicial do AFE.
- **final_states**: Conjunto de estados finais do AFE.
- **image_folder**: Pasta onde as imagens geradas serão salvas.
- **afn_transitions**: Dicionário que representa as transições do autômato finito não-determinístico (AFN).
- **afn_final_states**: Conjunto de estados finais do AFN.

**> A função abre um diálogo para o usuário selecionar um arquivo JSON. Se um arquivo for selecionado, ela carrega os dados do autômato, exibe as informações no console, cria uma pasta para salvar as imagens geradas, visualiza o AFE, converte o AFE para AFN, exibe as informações do AFN no console e visualiza o AFN.**

#### c. create_gui: Função que cria a interface gráfica para o usuário selecionar o arquivo JSON com o AFe.
![image](https://github.com/user-attachments/assets/c9ec767f-0a1e-493c-a1ef-d64df6dae448)
- **root**: Janela principal da interface gráfica.
- **frame**: Contêiner dentro da janela principal para organizar os widgets.
- **label**: Rótulo que instrui o usuário a selecionar o arquivo JSON.
- **button**: Botão que, ao ser clicado, abre o diálogo para seleção do arquivo JSON.

**> A função cria uma janela principal com um título, adiciona um contêiner para organizar os widgets, insere um rótulo com instruções e um botão que chama a função `select_file` ao ser clicado. A interface gráfica é mantida em execução com `root.mainloop()`.**

#### d. main(): Função principal para rodar a aplicação.
![image](https://github.com/user-attachments/assets/c0ea892d-0992-4f52-9cef-16398123d860)

**> A função chama `create_gui()` para iniciar a interface gráfica do usuário, permitindo a seleção do arquivo JSON com o AFe.**

## Código AFe_to_AFN.py

### 1. Sobre as bibliotecas
![image](https://github.com/user-attachments/assets/d1241c39-2d5f-4532-ae30-ed426c818aa0)

O código começa com a importação das bibliotecas necessárias:

- **graphviz**: Usada para visualizar os autômatos em forma de grafo.
- **collections.defaultdict**: Uma subclasse do dicionário que retorna um valor padrão quando uma chave não existe. Isso é útil para simplificar a criação de dicionários onde os valores são listas ou conjuntos.

#### a. Função 'visualize_automaton': Essa função objetiva permitir a visualização de um autômato utilizando as transições, estado inicial e estado(s) final(is) fornecidos.
![image](https://github.com/user-attachments/assets/10297e29-1db9-4ed9-a142-4442caa3dc53)

- **transitions**: Dicionário que representa as transições do autômato.
- **start_state**: Estado inicial do autômato.
- **final_state**: Um ou mais estados finais do autômato. 
- **title**: Título do autômato.
- **Digraph**: Vem da biblioteca Graphviz e configura a imagem como png usando o "dot" para renderização.
- **rankdir**: Diz respeito à orientação do gráfico, como sendo LR, ou seja, da esquerda para a direita.

**> Há a Adição de Estados, conforme mostrada no trecho do código a seguir. Esse trecho mostra uma iteração sobre cada estado nas transições. Caso o estado seja um estado final, é incluído um duplo círculo para destacá-lo, caso contrário, o círculo ficará normal.**
![image](https://github.com/user-attachments/assets/f23b3f87-3543-4c53-b566-58755738b253)

**> O trecho sobre a adição do Estado Inicial, conforme imagem a seguir, mostra uma destaque que não é exibido graficamente, para poder diferenciá-lo dos demais. Após isso, é adicionado uma aresta que conecta o estado inicial ao autômato, demonstrando a transição de início.**
![image](https://github.com/user-attachments/assets/3c485d37-dc2d-44be-a2cc-451107dec392)

**> Sobre a Adição de Transições, o trecho a seguir demonstra que para cada estado e suas transições é criado um dicionário para poder agrupar as transições por origem e destino. As transições entre os estados são adicionadas ao grafo, onde ',' representa o síbolo que indica as transições.**
![image](https://github.com/user-attachments/assets/7c34fa76-22c9-4660-8b00-bbf48739c0d5)

**> Sobre a Renderização do Gráfico, no trecho de código a seguir, é definido além do tamanho do título do gráfico gerado, também a definição de como o título será apresentado, removendo os espaços por sublinhados e abrindo o arquivo PNG no final.**
![image](https://github.com/user-attachments/assets/66db7f91-5516-4157-8647-830688cd1366)

#### b. Função 'e_closure': Essa função calcula o fecho-ε para um estado específico, que corresponde ao conjunto de estados alcançáveis a partir de um estado, usando transições ε.
![image](https://github.com/user-attachments/assets/30d494ed-2c8d-40b9-9856-5c14e7ac54ce)

- **state**: O estado do qual se quer calcular o fecho-ε.
- **transitions**: Dicionário de transições do autômato.
- **stack**: Inicia uma pilha 'stack' com o estado atual e um conjunto 'closure' que armazena todos os estados que podem ser alcançados. Enquanto houver estados na pilha, remove o estado atual e verifica se há transições ε para outros estados. Se sim, adiciona esses estados ao fecho-ε e à pilha, repetindo o processo até que não haja mais estados a serem processados. Ao final, retorna o conjunto de estados que formam o fecho-ε do estado dado.

#### c. Função 'convert_afe_to_afn': Essa função converte um autômato finito com movimentos vazios em um autômato finito não determinístico.
![image](https://github.com/user-attachments/assets/ec8c2336-6343-48ad-b9f1-a5fe54860537)

- **afe_transitions**: Transições do AFe que está sendo convertido.
- **start_state**: Estado inicial do AFe.
- **final_states**: Conjunto de estados finais do AFe.
- **defaultdict**: Armazena as transições do AFN, na qual cada estado pode ter várias transições para outros estados dependendo dos símbolos de entrada.
- **e_closure**: Calcula o fecho-ε para cada estado do AFe utilizando a função 'e_closure', armazenando os resultados em um dicionário 'closures'.

**> Sobre a Coleta de Símbolos, o trecho a seguir mostra a criação de um conjunto de todos os simbolos, exceto ε, que aparecem nas transições do AFe para serem utilizados durante a conversão.**
![image](https://github.com/user-attachments/assets/2b92482c-2820-4035-b6d5-a51cdd10ec6a)

**> Sobre a Montagem do AFN, o trecho a seguir mostra que para cada estado e seu fecho-ε, itera sobre todos os símbolos e encontra os estados alcançáveis a partir do fecho-ε. Cada um dos estados do AFe e suas transições são usadas para construir as transições do AFN. além disso, o código atualiza os estados finais do AFN com os estados do fecho-ε, se necessário. Ao fim, em 'return', ele retorna um dicionário com as transições do AFN e o conjunto atualizado de seus estados finais.**
![image](https://github.com/user-attachments/assets/57ac2c17-a117-4bcd-8efc-fdeb00003bb9)


## Estrutura dos arquivos JSON utilizados

Os arquivos JSON utilizados para representar os autômatos possuem a seguinte estrutura:

- **transitions**: Um dicionário onde as chaves são os estados e os valores são dicionários que mapeiam símbolos de entrada para listas de estados de destino.
    - Exemplo:
        ```json
        "transitions": {
            "q0": {"ε": ["q1", "q2"]},
            "q1": {"a": ["q1", "q3"]},
            "q2": {"b": ["q2"]},
            "q3": {"ε": ["q4"]},
            "q4": {"c": ["q4"]}
        }
        ```
- **start_state**: O estado inicial do autômato.
    - Exemplo:
        ```json
        "start_state": "q0"
        ```
- **final_states**: Uma lista de estados finais do autômato.
    - Exemplo:
        ```json
        "final_states": ["q4"]
        ```

**> Este formato permite representar tanto autômatos finitos estocásticos (AFE) quanto autômatos finitos não-determinísticos (AFN), facilitando a conversão entre eles e a visualização das transições e estados.**




