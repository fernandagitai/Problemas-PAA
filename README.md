# Problemas PAA
Solução em python para questões da disciplina de Projeto de Análise de Algoritmos (UFAL).

## ORDENAÇÃO DAS PANQUECAS
Existem n panquecas, todas de tamanhos diferentes, empilhadas umas sobre as outras. Você pode colocar uma espátula sob uma das panquecas e virar a pilha inteira acima da espátula. O objetivo é arranjar as panquecas de acordo com o tamanho, com a maior na parte inferior. A Figura mostra uma instância do quebra-cabeça para n = 7. Projete um algoritmo para resolver este problema e determine o número de operações feitas pelo algoritmo no pior caso.

![alt text](/img/demonstracao.png)

## TORRE DE HANOI
Resolver o problema da Torre de Hanói quando se dispõe de 4 torres, em vez de 3. Determinar o número de movimentos de disco.

## AGENDAMENTO
Considere o problema de agendamento de intervalos. Nós temos um conjunto de atividades {1,2, ... n}; cada atividade i possui um intervalo de tempo a partir de si e termina em fi. Um agendamento — conjunto de atividades — é dito compatível, se nenhuma atividade se sobrepõem no tempo. O objetivo é determinar um agendamento compatível com o maior número possível de atividades. Projete um algoritmo para este problema.

## CONVIDADOS DE FESTA
Alice quer dar uma festa e está decidindo quem chamar. Ela tem n pessoas as quais escolher, e ela fez uma lista de quais pares dessas pessoas conhecem uma a outra. Ela quer selecionar o maior número de pessoas possível, sujeito a duas restrições: na festa, cada pessoa deve ter pelo menos outras cinco pessoas que ela conhece e outras cinco pessoas que ela não conhece. Forneça um algoritmo eficiente que tome como entrada a lista das n pessoas e a lista de pares de quem conhece quem e calcule a melhor escolha de convidados para a festa. Dê o tempo de execução em termos de n.