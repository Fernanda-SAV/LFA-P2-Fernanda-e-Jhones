# LFA P2 - Fernanda Assunção e Jhones de Sousa
Trabalho submetido à disciplina de Linguagens Formais e Autômatos - Conversor AFe para AFN.


# Conversor de Autômato Finito com Movimentos Vazios (AFe) para Autômato Finito Não Determinístico (AFN)

<div align="center">
  <img src="https://img.shields.io/badge/Versão-1.0-blue.svg" alt="Versão 1.0">
  <img src="https://img.shields.io/badge/Licença-MIT-green.svg" alt="Licença MIT">
</div>

---

## Resumo do Trabalho

> **Este projeto apresenta o desenvolvimento de um conversor que transforma um **Autômato Finito com Movimentos Vazios (AFe)** em um **Autômato Finito Não-Determinístico (AFN)**. Utilizando o Python como recurso para criação do algoritmo, calcula-se o fecho-𝜀 e remove-se as transições vazias, gerando representações dos grafos desses autômatos. Este trabalho agrega conteúdo à disciplina de Linguagens Formais e Autômatos, pois permite entender melhor a relação que para cada AFe é possível construir um AFN equivalente. Este projeto visa proporcionar uma ferramenta prática para estudantes e pesquisadores que desejam explorar e entender as nuances da teoria dos autômatos, especialmente no que diz respeito aos AFe's e AFN's.**
 
## Descrição
> **A conversão de AFe para AFN marca um aspecto importânte que fala sobre a equivalência entre autômatos AFe e AFN. Este projeto se mostra relevante para para cursos de ciência da computação, matemática e áreas afins, onde o entendimento de autômatos se torna mais "palpável" ao ter um conversor para verificar se os autômatos estão corretos. Sobre as tecnologias utilizadas, foram aplicadas como linguagem de programação o Python, pela sua simplicidade e ampla biblioteca de manipulação de dados. O ambiente de desenvolvimento usado foi o Visual Studio Code pelo suporte a várias ferramentas. Dentre as bibliotecas aplicadas estão, principalmente: graphviz, defaltdict, json e tkinter.**
>**Os passos aplicados no desenvolvimento do projeto consistiu no:**
- **Levantamento da literatura: foi necessário entender as definições de AFe e AFN, além das regras de conversão;**
- **Conhecimento da estrutura de um autômato e adaptação ao código: explorou-se a estruturação dos autômatos, onde os estados são nós e transições são arestas;**
- **Desenvolvimento iterativo: incremento de funcionalidades que facilitava vários testes de diferentes autômatos, realizando melhorias contínuas;**
- **Testes: validação dos resultados utilizando exemplos conhecidos na literatura.**

> **Dentre os desafios enfrentados e soluções adotadas no decorrer do projeto, contou-se com a detecção de ciclos, para verificar o controle dos estados ja processados, além da revisão do algoritmo para que as transições sejam eficientes, houve também a vistoria para garantir que o comportamento do AFN resultante fosse idêntico ao AFe original, testando com alguns casos.**

## Estrutura do Repositório 

- **`/apresentacoes/`**: Apresentações relacionadas ao projeto (slide e artigo).
- **`/docs/`**: Documentações adicionais - contém a explicação do código.
- **`/src/`**: Contém o código de conversão AFe_to_AFN.py e os arquivos JSON dos autômatos Fe. Além disso, fora dessa pasta há o código "main.py", que chama o código de conversão AFe para AFN.
- **`/src/automatos_teste/`**: Arquivos JSON para usar no código "main.py" São referentes à construção do AFe para poder ser convertido pelo programa para o AFN. (Opcional)

---

## Autores

- [Fernanda Sousa de Assunção Vale](fernanda.sav@discente.ufma.br)  
- [Jhones de Sousa Soares](jhones.sousa@discente.ufma.br)  

---

## Agradecimentos

- **Universidade Federal do Maranhão (UFMA)**  
- **Professor Doutor Thales Levi Azevedo Valente**  
- **Colegas de curso**

Agradecemos a todas as pessoas e instituições que contribuíram para a realização deste trabalho.

---

## Materiais de Apoio para o Projeto

- [Link para referência bibliográfica](https://www.marcusramos.com.br/univasf/lfa-2008-1/Apostila.pdf)
- [Link para material usado como referência de exercícios e exemplos](https://github.com/thalesvalente/teaching/tree/main/formal-languages-and-automata)

---

## Copyright / License

Este material é resultado de um trabalho acadêmico para a disciplina **Linguagens Formais e Autômatos**, sob a orientação do professor **Dr. THALES LEVI AZEVEDO VALENTE**, no semestre letivo **2024.2**, do curso de **Engenharia da Computação** na Universidade Federal do Maranhão (**UFMA**).

Todo o material sob esta licença é **software livre**: pode ser usado para fins acadêmicos e comerciais **sem nenhum custo**. Não há papelada, nem royalties, nem restrições de “copyleft” do tipo GNU. Ele é licenciado sob os termos da **Licença MIT**, reproduzida abaixo, e, portanto, é compatível com a GPL e também se qualifica como software de código aberto. É de domínio público. O espírito desta licença é que você é livre para usar este material para qualquer finalidade, sem nenhum custo. O único requisito é que, se você usá-lo, nos dê crédito.



Copyright © 202X Material Educacional

Este material está licenciado sob a Licença MIT. É permitido o uso, cópia, modificação, e distribuição deste material para qualquer fim, desde que acompanhado deste aviso de direitos autorais.

O MATERIAL É FORNECIDO "COMO ESTÁ", SEM GARANTIA DE QUALQUER TIPO, EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO, ADEQUAÇÃO A UM DETERMINADO FIM E NÃO VIOLAÇÃO. EM HIPÓTESE ALGUMA OS AUTORES OU DETENTORES DE DIREITOS AUTORAIS SERÃO RESPONSÁVEIS POR QUALQUER RECLAMAÇÃO, DANOS OU OUTRA RESPONSABILIDADE, SEJA EM UMA AÇÃO DE CONTRATO, ATO ILÍCITO OU DE OUTRA FORMA, DECORRENTE DE, OU EM CONEXÃO COM O MATERIAL OU O USO OU OUTRAS NEGOCIAÇÕES NO MATERIAL.

Para mais informações sobre a Licença MIT: https://opensource.org/licenses/MIT.

Copyright © 202X Educational Material

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Para mais informações sobre a **Licença MIT**: [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

---

<div align="center">
Feito com ♥ por <strong>Alunos UFMA</strong>
</div>
