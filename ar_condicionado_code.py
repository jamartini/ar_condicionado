print('Primeiro serão pedidas as medidas da sala, utilize os valores em metros e, para números com casas decimais, no lugar da vírgula utilize ponto.')
sala_largura = float(input('Digite a largura da sala:'))
sala_comprimento = float(input('Digite o comprimento da sala:'))
sala_altura = float(input('Digite o pé direito da sala:'))
sala_volume = sala_largura * sala_comprimento * sala_altura
print(sala_volume)

sala_localizacao = input('A sala é entre andares? [S/N]')
if sala_localizacao == 's' or sala_localizacao == 'S' :
    sala_entre_andares = True
elif sala_localizacao == 'n' or sala_localizacao == 'N' :
    sala_entre_andares = False  

if sala_entre_andares == True :
    carga_volume = sala_volume * 16
else :
    carga_volume = sala_volume * 22.333
print(carga_volume)    

print('Agora serão pedidas informações sobre as janelas da sala. Para número de janelas use apenas valores inteiros.')
janelas_num = int(input('Quantas janelas a sala possui?'))
janelas_largura = float(input('Digite a largura das janelas:'))
janelas_altura = float(input('Digite a altura das janelas:'))
janelas_area = janelas_largura * janelas_altura
print(janelas_area)

janelas_sol = input('As janelas recebem luz solar em algum momento do dia? [S/N]')
if janelas_sol == 's' or janelas_sol == 'S' :
    recebe_sol = True
elif janelas_sol == 'n' or janelas_sol == 'N' :
    recebe_sol = False
    
if recebe_sol == False :
    carga_janelas = janelas_num * janelas_area * 37
    print(carga_janelas)
else :
    sol_manha = input('A sala recebe sol de manhã? [S/N]')
    if sol_manha == 's' or sol_manha == 'S' :
      sol_de_manha = True
    elif sol_manha == 'n' or sol_manha == 'N' :
      sol_de_manha = False

    cortinas = input('As janelas possuem cortinas? [S/N]')
    if cortinas == 's' or cortinas == 'S' :
      tem_cortinas = True
    elif cortinas == 'n' or cortinas == 'N' :
      tem_cortinas = False    
  
    if sol_de_manha == True and tem_cortinas == True :
      carga_janelas = janelas_num * janelas_area * 160
    elif sol_de_manha == False and tem_cortinas == True :
      carga_janelas = janelas_num * janelas_area * 212  
    elif sol_de_manha == True and tem_cortinas == False :
      carga_janelas = janelas_num * janelas_area * 222
    else :
      carga_janelas = janelas_num * janelas_area * 410
    print(carga_janelas)

print('Agora serão pedidas informações sobre as portas, novamente para quantidade de portas utilize apenas números inteiros.')
portas_num = int(input('Quantas portas existem na sala?'))
portas_largura = float(input('Digite a largura da porta:'))
portas_altura = float(input('Digite a altura da porta:'))
portas_area = portas_largura * portas_altura
print(portas_area)
carga_portas = portas_area * 125
print(carga_portas)

pessoas_num = int(input('Quantas pessoas ficam na sala?'))
carga_pessoas = pessoas_num * 125
print(carga_pessoas)

print('Para a potência dos demais aparelhos na sala, utilize também apenas valores inteiros.')
aparelhos_potencia = int(input('Digite a potência nominal combinada dos demais aparelhos elétricos na sala:'))
carga_aparelhos = aparelhos_potencia * 0.9
print(carga_aparelhos)

carga_total = carga_volume + carga_janelas + carga_portas + carga_pessoas + carga_aparelhos
print(carga_total)

carga_btu = carga_total * 3.92
print(carga_btu)