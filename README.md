# ar_condicionado
A seguir está um resumo de como o código funciona:
1) Entramos com os dados geométricos da sala (largura, comprimento e pé direito), o código calcula o volume e então usa esse dado para dar um valor de carga necessária do ar condicionado.
2) São pedidas as informações de janelas na sala (quantidade, largura e altura), o código calcula a área total ocupada por janelas.
3) Junto da área total das janelas são requeridas informações sobre a iluminação natural nessas janelas, se pegam sol, em caso afirmativo, se é de manhã ou de tarde e em ambos os casos se as janelas possuem ou não cortinas. Tendo todas essas informações, novamente o código calcula a carga necessária do ar condicionado.
4) A mesma coisa é pedida em relação às portas da sala (quantidade, largura e altura), o código calcula assim a área total ocupada por portas e dá o valor de carga necessária do ar condicionado.
5) Então, pede-se a quantidade de pessoas que geralmente estão presentes na sala e o programa dá o valor da carga necessária do ar condicionado.
6) Por fim, pede-se o valor da potência nominal combinada de todos os outros aparelhos elétricos da sala e o programa dá o valor da carga necessária do ar condicionado.
7) São somados todos os valores de carga (em kcal/h), dando o valor total que é convertido para BTUs.
