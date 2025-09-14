# RouletteSimulation

Este projeto é uma simulação de Monte Carlo que modela e visualiza os resultados financeiros de múltiplos apostadores em um jogo de azar simples. O objetivo é demonstrar como, apesar dos resultados aleatórios para cada indivíduo, a média de um grande número de simulações converge para um valor esperado, revelando a tendência real do jogo.

## Como Funciona

A simulação é baseada em um jogo onde cada aposta tem as seguintes regras:

  - **50% de chance** de ganhar **R$130**.
  - **50% de chance** de perder **R$100**.

O programa executa esta lógica para um número configurável de "apostadores" (simulações) ao longo de um número também configurável de "apostas". Ao final, ele calcula a trajetória financeira média de todos os apostadores e a plota em um gráfico para análise.

## Saída do Gráfico

O script gera um gráfico que visualiza a evolução do dinheiro dos apostadores.

  - As **linhas cinzas** representam a trajetória financeira de apostadores individuais. Note como algumas são extremamente voláteis, com grandes ganhos ou perdas.
  - A **linha vermelha** representa a **média** do dinheiro de todos os apostadores a cada rodada de aposta. Ela mostra a tendência esperada do jogo, que neste caso é um ganho médio positivo ao longo do tempo.

<img width="1186" height="690" alt="image" src="https://github.com/user-attachments/assets/8863649b-c59c-4252-85bc-10c62155c101" />


## Como Executar o Projeto

Siga os passos abaixo para configurar e rodar a simulação.

### Pré-requisitos

  - Python 3.x

### 1\. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd Simula-oComputacional---CoinGain
```

### 2\. Criar um Ambiente Virtual (Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

### 3\. Instalar as Dependências

As dependências necessárias estão listadas no arquivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4\. Rodar a Simulação

Execute o script principal. O programa solicitará que você insira o número de apostas e o número de apostadores.

```bash
python app.py
```

O programa fará duas perguntas:

```
| Quantas apostas você deseja fazer por apostador? 
| Quantos apostadores (simulações) você deseja ter? 
```

Após inserir os valores, a simulação será executada e o gráfico será exibido e salvo como `grafico_simulacao_media.png` no diretório do projeto.

