chamados = [
    {"nome": "Ana Gouveia de Oliveira", "urgencia": 2, "horario": 3}, #posição 0
    {"nome": "Bruno César Cavalcante", "urgencia": 5, "horario": 2}, #posição 1
    {"nome": "Carla Montenegro Dias", "urgencia": 2, "horario": 2}, # posição 2
    {"nome": "Diego da Silva Cunha", "urgencia": 3, "horario": 0}, # posição 3
    {"nome": "Carlos Alberto Bezerra de Almeida", "urgencia": 5, "horario": 6}, # posição 4
    {"nome": "José Carlos Pereira", "urgencia": 4, "horario": 0}, # posição 5
    {"nome": "Eduardo Alves do Nascimento", "urgencia": 4, "horario": 1}, # posição 6
    {"nome": "Maria Aparecida dos Santos", "urgencia": 3, "horario": 5}, # posição 7
    {"nome": "Anderson Nogueira Bastos", "urgencia": 3, "horario": 2}, # posição 8
    {"nome": "Felipe Prado da Rocha", "urgencia": 3, "horario": 7}, # posição 9
    {"nome": "Danilo Mendes de Assis", "urgencia": 5, "horario": 1}, # posição 10
]

def comparar(chamado_a, chamado_b):
    if chamado_a["urgencia"] > chamado_b["urgencia"]:
        return chamado_a
    elif chamado_a["urgencia"] < chamado_b["urgencia"]:
        return chamado_b
    else:
        if chamado_a["horario"] < chamado_b["horario"]:
            return chamado_a
        else:
            return chamado_b

print('• LISTA DE ATENDIMENTOS •')

pendentes = chamados.copy()
fila_organizada = []

while len(pendentes) > 0:
    melhor_ate_agora = pendentes[0]
    for chamado in pendentes:
        melhor_ate_agora = comparar(melhor_ate_agora, chamado)

    fila_organizada.append(melhor_ate_agora)
    pendentes.remove(melhor_ate_agora)

for chamado in fila_organizada:
    print(chamado['nome'].upper())    






    













 
melhor_ate_agora = chamados[0]
for chamado in chamados:
    melhor_ate_agora = comparar(melhor_ate_agora, chamados[1])

