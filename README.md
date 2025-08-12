# SecureFileAPI
Essa é uma API desenvolvida para realizar downloads de arquivos diretamente do servidor, garantindo proteção por autenticação JWT (JSON Web Token).
O objetivo é fornecer um meio seguro e controlado para que apenas usuários autorizados possam acessar documentos, relatórios ou dados sensíveis.

Principais características:

Segurança: Implementação de autenticação e autorização com JWT, evitando acessos não autorizados.

Configuração flexível: Usuário, senha e chave JWT definidos por variáveis de ambiente, facilitando a implantação em diferentes ambientes (dev, staging, produção).

Desempenho otimizado: Compatível com servidores ASGI via uvicorn para melhor performance.

Simplicidade de uso: Rotas enxutas e objetivas, como /login para autenticação e /baixar_arquivo para download protegido.

Fluxo de funcionamento:

O usuário faz login enviando suas credenciais para /login.

Recebe um token JWT válido por tempo limitado.

Utiliza esse token no header da requisição para acessar /baixar_arquivo.

O servidor valida o token e, se autorizado, envia o arquivo solicitado.

Essa API é ideal para empresas, aplicações internas e sistemas que necessitam compartilhar arquivos sensíveis com segurança.
