# Implementação da Camada de Enlace com Codificação Hamming

Este projeto implementa os processos de **remetente** e **destinatário** para simular a camada de enlace, garantindo sincronização de frames e correção de erros usando o código de Hamming (7,4).

---

## 🎥 Vídeo Explicativo
[🔗 **Link para o Vídeo no YouTube**](https://youtu.be/DX-D8PdgBKc)

---

## 📌 Funcionalidades
- **Remetente**:
  - Recebe uma sequência de bits via entrada padrão (`stdin`).
  - Aplica **bit stuffing** para evitar conflitos com cabeçalho/terminador.
  - Codifica o payload com **Hamming (7,4)** para detecção e correção de erros.
  - Constrói o frame com cabeçalho, payload codificado e terminador.
  
- **Destinatário**:
  - Extrai o payload do frame.
  - Remove o bit stuffing.
  - Decodifica o Hamming e corrige erros de até 1 bit.
  - Exibe o payload original.

---

## 🚀 Uso
### Execução Básica
```bash
# Envia um payload e recebe a saída decodificada
./remetente "01101001" | ./destinatario
```
**Saída Esperada:**  
`01101001`

### Teste de Correção de Erros
1. Simule um erro no frame:
   ```bash
   echo "01111110010011001111111" | ./destinatario
   ```
2. O destinatário corrigirá o bit alterado e exibirá o payload original.

---

## 📡 Protocolo Desenvolvido
### Estrutura do Frame
| Componente   | Valor           | Descrição                              |
|--------------|-----------------|----------------------------------------|
| Cabeçalho    | `01111110`      | Marca o início do frame.               |
| Payload      | Bits codificados | Dados com bit stuffing e Hamming (7,4).|
| Terminador   | `01111111`      | Marca o fim do frame.                  |

### Bit Stuffing
- **Objetivo**: Evitar que o payload contenha sequências iguais ao cabeçalho/terminador.
- **Regra**: Insere um `0` após cinco `1`s consecutivos.  
  Exemplo: `11111` → `111110`.

### Codificação Hamming (7,4)
- **Funcionamento**:
  - Divide o payload em blocos de 4 bits.
  - Adiciona 3 bits de paridade calculados como:
    ```
    p1 = d1 ⊕ d2 ⊕ d4  
    p2 = d1 ⊕ d3 ⊕ d4  
    p3 = d2 ⊕ d3 ⊕ d4
    ```
  - Formato final do bloco: `[p1][p2][d1][p3][d2][d3][d4]`.