# Como Executar o Projeto Localmente

Este documento contém os passos necessários para executar o Backend (FastAPI) e o Frontend (Angular) do projeto.

---

## 🐍 1. Executando o Backend (FastAPI)

### Pré-requisitos
* Python 3.8+ instalado.

### Passos:

1. **Navegue até a pasta do backend:**
   ```bash
   cd BackEnd
   ```

2. **Crie e ative o ambiente virtual:**
   * **Windows (PowerShell):**
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```
   * **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicie o servidor local:**
   ```bash
   uvicorn app.main:app --reload
   ```

   > **URLs Úteis:**
   > * **API:** `http://127.0.0.1:8000`
   > * **Documentação (Swagger UI):** `http://127.0.0.1:8000/docs`
   > * **Documentação Alternativa (ReDoc):** `http://127.0.0.1:8000/redoc`

---

## 🅰️ 2. Executando o Frontend (Angular)

### Pré-requisitos
* Node.js (versão LTS recomendada)
* Angular CLI instalado globalmente (`npm install -g @angular/cli`) ou via `npx`.

### Passos:

1. **Navegue até a pasta do frontend:**
   ```bash
   cd caminho/para/seu-frontend
   ```

2. **Instale as dependências do projeto:**
   ```bash
   npm install
   ```

3. **Inicie a aplicação Angular:**
   ```bash
   ng serve --open
   ```
   *(A flag `--open` ou `-o` abrirá o navegador automaticamente).*

   > **URL Principal:** `http://localhost:4200`

---

## 💡 Comandos Úteis & Dicas

* **Mudar porta do FastAPI:**
  ```bash
  uvicorn app.main:app --reload --port 8080
  ```
* **Mudar porta do Angular:**
  ```bash
  ng serve --port 4300
  ```