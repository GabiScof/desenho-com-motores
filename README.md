# Desenho com Motores de Passo
Atividade de ENG4731 - Fundamentos de Mecatrônica

Projeto de um plotter polar com dois motores de passo, uma caneta e cordas. A ideia é converter uma imagem em coordenadas e transformar essas coordenadas em movimentos dos motores.

## Como funciona

O projeto segue este fluxo:

```text
Imagem
↓
Extração de contornos com OpenCV
↓
Conversão de pixels para centímetros
↓
Cálculo dos comprimentos das cordas
↓
Conversão para passos dos motores
↓
Envio dos comandos para o Arduino
↓
Movimento da caneta
```

## Hardware

* Arduino
* 2 motores de passo
* Driver A4988
* Cordas
* Caneta

## Configuração

Antes de executar o projeto, instale as dependências:

```bash
pip install -r requirements.txt
```

Depois, configure o arquivo `env.py` com os parâmetros físicos do sistema:

```python
class Env:

    COM = "COM5"

    POSICAO_INICIAL = (20, 20)

    RAIO_CARRETEL = 20

    DISTANCIA_MOTORES = 40
```

### Explicação das variáveis

`COM`  
Porta serial utilizada pelo Arduino.

`POSICAO_INICIAL`  
Posição inicial conhecida da caneta.

`RAIO_CARRETEL`  
Raio do carretel acoplado ao motor.

`DISTANCIA_MOTORES`  
Distância horizontal entre os dois motores.


## Execução

Para executar o projeto:

```bash
python main.py
```
