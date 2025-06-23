# Bot de Candidatura no LinkedIn 🤖

![linkedineasyapplygif](https://user-images.githubusercontent.com/34207598/128695728-6efcb457-0f75-42e2-987a-f7a0c239a235.gif)

Um bot em Python criado por **wesmoura** para se candidatar automaticamente a vagas de emprego no LinkedIn (Easy Apply), baseado nas suas preferências.

* Duas opções disponíveis para usar este bot: com ou sem digitar a senha — totalmente seguro, nenhuma credencial é armazenada.
* Exporta todos os resultados e ofertas em um arquivo .txt.
* Preferências de vaga totalmente personalizáveis.
* Pode ser usado em várias plataformas de busca de emprego como LinkedIn, Glassdoor, AngelCo, Greenhouse, Monster, GlobalLogic e Djinni.

Para modificar, utilizar ou obter a documentação, entre em contato com **wesmoura**.

---

## Comprar Materiais e Guias 😍

Você pode adquirir um tutorial completo e detalhado explicando como este bot funciona, uma sessão de uma hora em chamada onde **wesmoura** configura o bot passo a passo em seu computador, ou 5 vídeos demonstrando o uso do bot.

* **Vídeos de demonstração do bot**
* **Suporte técnico por chamada para instalação no Windows**
* **Suporte técnico por chamada para Linux**
* **Suporte técnico por chamada para Mac OS**
* **Documentação para Windows**
* **Documentação para Linux**
* **Documentação para Mac OS**

(Para adquirir, entre em contato diretamente com **wesmoura**.)

---

## Instalação 🔌

1. Clone o repositório: `git clone https://github.com/aminblm/linkedin-application-bot`
   *(Recomenda-se criar um fork para sua conta GitHub com os devidos créditos a **wesmoura**)*
2. Certifique-se de que o Python e pip estão instalados
3. Instale as dependências: `pip3 install -r requirements.yaml`
4. Crie um perfil no Firefox e insira o caminho na linha 8 do arquivo `config.py`, ou digite suas credenciais do LinkedIn nas linhas 11 e 12 de `config.py`
5. Modifique o `config.py` conforme suas preferências
6. Execute o bot com `python3 linkedin.py`
7. Verifique o arquivo `.txt` gerado na pasta `/data` com os dados das candidaturas

---

## Funcionalidades 💡

* Filtrar vagas por "Easy Apply", localização (Mundial, Europa, Polônia, etc.), palavras-chave (Python, React, Node), experiência, tipo de vaga e data da publicação.
* Candidatura automática com base na sua expectativa salarial (funciona melhor com vagas dos EUA)
* Aplica automaticamente para vagas simples (página única)
* Também aplica para vagas mais longas (com múltiplas etapas), desde que os dados estejam salvos no LinkedIn (experiência, direitos legais, currículo, etc.)
* Salva os resultados em um arquivo `.txt` para análise posterior
* Lista links de vagas que não pôde se candidatar automaticamente (para candidatura manual)
* Insere pausas entre ações para evitar bloqueios
* Executa em segundo plano
* Compatível com Firefox e Chrome
* Segue as preferências do usuário
* Opção de seguir ou não a empresa após se candidatar
* E muito mais!

---

## Testes 🔦

Há uma pasta específica para testes. Siga estes passos:

1. Vá para a pasta `tests` e execute: `python3 setupTests.py` — verifica se Python, pip, selenium, dotenv e Firefox estão corretamente instalados.
2. Execute: `python3 seleniumTest.py` — verifica se o Selenium e o Geckodriver estão funcionando corretamente.
3. Execute: `python3 linkedinTest.py` — tenta fazer login no LinkedIn com base no caminho especificado no arquivo `.env`. Certifique-se de que o perfil do Firefox foi criado e login feito manualmente antes.

Resultado esperado dos testes:
![test1](https://user-images.githubusercontent.com/34207598/189535308-c2c546de-caec-4460-823d-dd5ca208c480.png)

---

## Configuração Manual 🛠

Tutorial passo a passo para configurar o bot:

1. Instale o Firefox ou Chrome (o exemplo é com Firefox)
2. Instale o Python
3. Baixe o [Geckodriver](https://github.com/mozilla/geckodriver/releases) e coloque na pasta de instalação do Python
4. Instale pip: `get-pip.py`
5. Instale Selenium: `pip install selenium`
6. Clone o código
7. Crie um perfil no Firefox: digite `about:profiles` no navegador
8. Abra o novo perfil, acesse linkedin.com e faça login
9. Copie o diretório raiz do perfil criado (`about:profiles`)
10. Cole esse caminho na variável `firefoxProfileRootDir` no arquivo `config.py`
11. Modifique o `config.py` conforme suas preferências
12. Após cada execução, revise as vagas não aplicadas e salve as preferências manualmente no LinkedIn
13. Nas execuções seguintes, o bot se tornará mais eficaz
14. Sinta-se à vontade para entrar em contato com **wesmoura** para dúvidas ou sugestões

---

## Demonstração 🖥

![banner](https://github.com/aminblm/linkedin-application-bot/assets/25132838/b0dda2f0-b531-48af-b769-fc1370d88fdb)
![1](https://github.com/aminblm/linkedin-application-bot/assets/25132838/1caeeff1-7f70-423a-ae51-ae97ba00bc99)
![2](https://github.com/aminblm/linkedin-application-bot/assets/25132838/3cb59d82-b167-40ad-8fef-d8e1430bf6c1)

---

## Implementações Futuras

* Execução em modo headless (sem abrir o navegador)
* Mais robustez para diferentes áreas profissionais
* Lista negra de vagas no LinkedIn
* Relatório de campos incompletos no perfil do LinkedIn
* Suporte a outras grandes plataformas de emprego (Glassdoor, AngelCo, Greenhouse, Monster, GlobalLogic, Djinni)
* AngelCo - [https://angel.co/l/2xRADV](https://angel.co/l/2xRADV)

---
