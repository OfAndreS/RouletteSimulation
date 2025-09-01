import numpy as np
import matplotlib.pyplot as plt

# Função de input permanece a mesma
def inputDataToCG(outputSentence):
    while(True):
        try:
            userInput = int(input(outputSentence))
            return userInput
        except:
            print("| Tipo de dado incorreto!")

# Lógica de negócio permanece a mesma
def businessLogic(luckyOfTheUser):
    if luckyOfTheUser < 0.5:
        return False
    else:
        return True

# Simula as apostas para UM único apostador e retorna seu histórico
def generateDataOfBets(numberOfBets: int, initialMoney: int):
    listOfUserMoney = []
    userMoney = initialMoney # Começa com o dinheiro inicial para esta simulação
    for i in range(numberOfBets):
        luckyOfTheUser = np.random.random()
        if businessLogic(luckyOfTheUser):
            userMoney = userMoney + 130
        else:
            userMoney = userMoney - 100
        listOfUserMoney.append(userMoney)
    return listOfUserMoney

# Função de plotagem agora plota a MÉDIA e também alguns casos individuais para comparação
def plotData(bets, averageEvolution, allCases):
    # Eixo X agora representa cada aposta
    eixo_x = np.arange(0, bets)

    plt.figure(figsize=(12, 7))
    
    # Plota algumas trajetórias individuais com baixa opacidade
    # Pega no máximo 20 casos para não poluir o gráfico
    num_cases_to_plot = min(20, len(allCases)) 
    for i in range(num_cases_to_plot):
        plt.plot(eixo_x, allCases[i], color='gray', alpha=0.2)

    # Plota a média de todos os casos com destaque
    plt.plot(eixo_x, averageEvolution, 'r', linewidth=2.5, label="Média de Dinheiro de Todos os Apostadores")
    
    plt.title("Evolução Média do Dinheiro de Múltiplos Apostadores")
    plt.xlabel("Número da Aposta")
    plt.ylabel("Dinheiro Acumulado (R$)")
    plt.legend() # Mostra a legenda
    plt.grid(True)
    plt.axhline(0, color='black', linestyle='--') # Linha no zero para referência

    plt.savefig('grafico_simulacao_media.png')
    plt.show()

if __name__ == "__main__":
    initialMoney = 0
    
    numberOfBets = inputDataToCG("| Quantas apostas você deseja fazer por apostador? ")
    numberOfCases = inputDataToCG("| Quantos apostadores (simulações) você deseja ter? ")

    # 1. Armazena o histórico de cada apostador em uma lista de listas
    allCasesHistories = []
    for case in range(numberOfCases):
        # Roda uma simulação completa para cada "caso" ou "apostador"
        history = generateDataOfBets(numberOfBets, initialMoney)
        allCasesHistories.append(history)

    # 2. Converte a lista de listas em um array NumPy para facilitar o cálculo da média
    # O array terá o formato: (número de apostadores x número de apostas)
    allCasesArray = np.array(allCasesHistories)

    # 3. Calcula a média "verticalmente" (ao longo do eixo 0)
    # Isso nos dá uma lista onde cada item é a média de todos os apostadores naquela rodada de aposta
    averageEvolution = np.mean(allCasesArray, axis=0)

    # 4. Passa os dados corretos para a função de plotagem
    plotData(numberOfBets, averageEvolution, allCasesHistories)