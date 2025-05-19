# Simulação de Movimento com Interface Gráfica

Este projeto implementa uma simulação do movimento de objetos e calcula possíveis pontos de encontro entre eles. Utiliza `matplotlib` para a visualização da movimentação e `tkinter` para a criação de uma interface gráfica interativa.

## Descrição do Código

### Código 1: Simulação e Gráfico (`grafico.py`)

O primeiro código contém:

- **Classe `Corpo`**: Representa um objeto em movimento e calcula possíveis colisões.
- **Função `diagrama_SxT`**: Gera um gráfico `SxT` (Posição x Tempo) que representa o movimento dos corpos e marca possíveis pontos de encontro.
- **Execução da simulação**: Instancia dois aviões e executa a função para visualizar a movimentação.

### Código 2: Interface Gráfica (`interface.py`)

O segundo código adiciona uma interface gráfica com `tkinter`, permitindo:

- Inserir objetos e definir velocidade e posição inicial via campos de entrada.
- Adicionar ou remover corpos do sistema dinamicamente.
- Determinar um tempo para a simulação e gerar um gráfico com os dados inseridos.

## Dependências

Antes de executar o código, instale as bibliotecas necessárias:

```bash
pip install matplotlib
```
