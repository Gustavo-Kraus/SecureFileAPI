# SecureFileAPI

**SecureFileAPI** é uma API desenvolvida para realizar downloads de arquivos diretamente do servidor, garantindo proteção por autenticação JWT (JSON Web Token).  
O objetivo é fornecer um meio seguro e controlado para que apenas usuários autorizados possam acessar documentos, relatórios ou dados sensíveis.

---

## Principais características

- **Segurança:** Autenticação e autorização via JWT para evitar acessos não autorizados.
- **Configuração flexível:** Usuário, senha e chave JWT configurados por variáveis de ambiente, facilitando implantação em diferentes ambientes (desenvolvimento, staging, produção).
- **Desempenho otimizado:** Compatível com servidores ASGI via `uvicorn` para melhor performance.
- **Simplicidade de uso:** Rotas enxutas e objetivas:  
  - `/login` para autenticação  
  - `/baixar_arquivo` para download protegido.

---

## Fluxo de funcionamento

1. O usuário envia suas credenciais para o endpoint `/login`.  
2. Recebe um token JWT válido por tempo limitado.  
3. Utiliza esse token no header da requisição para acessar o endpoint `/baixar_arquivo`.  
4. O servidor valida o token e, se autorizado, envia o arquivo solicitado.

---

## Exemplos de uso

### Exemplo 1 — Login e obtenção do token JWT (Python)

```python
import requests

BASE_URL = "http://localhost:5000"

login_data = {
    "username": "user",
    "password": "123"
}

response = requests.post(f"{BASE_URL}/login", json=login_data)

if response.status_code == 200:
    token = response.json()["access_token"]
    print("Token JWT:", token)
else:
    print("Erro ao autenticar:", response.json())
```
### Exemplo 2 — Download de arquivo usando token JWT (Python)
```python
import requests

BASE_URL = "http://localhost:5000"
TOKEN = "seu_token_aqui"

params = {
    "file_path": "C:/Users/Kraus/Downloads/arquivo.txt"  # Caminho completo do arquivo no servidor
}

response = requests.get(
    f"{BASE_URL}/baixar_arquivo",
    params=params,
    headers={"Authorization": f"Bearer {TOKEN}"}
)

if response.status_code == 200:
    with open("arquivo_baixado.txt", "wb") as f:
        f.write(response.content)
    print("Arquivo baixado com sucesso!")
else:
    print("Erro:", response.json())
```
