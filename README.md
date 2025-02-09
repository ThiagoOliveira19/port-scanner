# Python Port Scanner with GUI

## 📌 Introdução
Este projeto é um **Port Scanner em Python**, que utiliza a biblioteca **socket** para escanear portas abertas em um endereço IP ou hostname especificado pelo usuário. Além do scanner de portas, o projeto possui uma **interface gráfica (GUI)** criada com **Tkinter**, tornando a ferramenta mais acessível e amigável.  

Durante o desenvolvimento, contei com a ajuda do **ChatGPT**, que me ajudou na resolução de dúvidas e na implementação da interface gráfica com Tkinter, além de otimizar o uso de threads para garantir que a aplicação continuasse responsiva durante a execução do scanner.

---

## 📂 Estrutura do Projeto
```
📁 Port Scanner
│
├── port_scanner.py   # Código principal
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação do projeto
```

---

## 🚀 Funcionalidades
- Escaneia portas abertas em um intervalo especificado pelo usuário.
- Identifica o serviço associado às portas abertas (quando disponível).
- Interface gráfica com Tkinter, incluindo barra de progresso e exibição de resultados em tempo real.
- Permite salvar os resultados em um arquivo CSV.

---

## 🛠 Tecnologias Utilizadas
- **Python 3**  
- **Tkinter** (para a interface gráfica)  
- **Pandas** (para salvar resultados em CSV)  
- **Socket** (para realizar o scan de portas)  
- **Threading** (para manter a GUI responsiva)  

---

## ⚙️ Como Instalar e Executar

### 1️⃣ Clone o Repositório
```bash
git clone https://github.com/seu-usuario/port-scanner.git
cd port-scanner
```

### 2️⃣ Crie e Ative o Ambiente Virtual
```bash
python3 -m venv portscanner-env
source portscanner-env/bin/activate  # Linux/Mac
portscanner-env\Scripts\activate     # Windows
```

### 3️⃣ Instale as Dependências
```bash
pip install -r requirements.txt
```

> **Nota:** Certifique-se de que o Tkinter está instalado. No Kali Linux, por exemplo, você pode instalá-lo com:
```bash
sudo apt-get install python3-tk
```

### 4️⃣ Execute o Projeto
```bash
python port_scanner.py
```

---
## 📜  Exemplo de Saída
Ao realizar o escaneamento, os resultados são exibidos na interface gráfica e também podem ser salvos em um arquivo CSV. O arquivo gerado será um arquivo CSV contendo as portas abertas e seus serviços correspondentes.

### Exemplo de arquivo gerado: ***google.com_open_ports.csv***
```bash
| port | service     |
|------|-------------|
| 80   | http        |
| 443  | https       |
| 22   | ssh         |
```
O arquivo google.com_open_ports.csv é um exemplo de saída após a execução do script para o domínio google.com. O formato do arquivo é simples e contém duas colunas: a porta e o serviço associado.

## 📜 Explicação do Código

### Interface Gráfica com Tkinter
O Tkinter foi usado para criar uma interface simples e intuitiva. A interface contém:
- **Campos de entrada** para IP/Hostname, porta inicial e porta final.
- **Botão "Start Scan"**, que inicia a varredura em uma thread separada.
- **Barra de progresso** para acompanhar o progresso do scan.
- **Área de texto** para exibir os resultados em tempo real.

### Função `scan_ports()`
Essa função é responsável por escanear as portas no intervalo especificado. Para cada porta:
- Tenta estabelecer uma conexão usando a biblioteca `socket`.
- Se a porta estiver aberta, identifica o serviço associado (`socket.getservbyport`).
- Atualiza a interface gráfica em tempo real, exibindo os resultados.

---

## 📋 Dependências
As bibliotecas necessárias estão listadas no arquivo `requirements.txt`. Caso precise recriar o arquivo, utilize o comando:
```bash
pip freeze > requirements.txt
```

---

## ⚠️ Aviso Legal
Este projeto foi desenvolvido para fins educacionais. **Não use este scanner para escanear redes ou hosts sem permissão explícita**, pois isso pode ser considerado uma atividade ilegal. Use-o apenas para aprendizado e testes em ambientes autorizados.

---

## 📄 Licença
Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).  

---

## 🌟 Contribuição
Sinta-se à vontade para contribuir com melhorias, abrir issues ou enviar pull requests!

---

## 📧 Contato
Se tiver dúvidas ou sugestões, entre em contato pelo GitHub.
