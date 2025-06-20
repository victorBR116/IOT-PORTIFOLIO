
# Pipeline de Dados com IoT e Docker

Este projeto demonstra um pipeline de dados para leitura de sensores IoT, utilizando Python, Docker, PostgreSQL e Streamlit para visualização.

## 🔧 Tecnologias Utilizadas
- Python
- PostgreSQL
- Docker
- Streamlit
- Pandas, SQLAlchemy, Plotly

## 📁 Estrutura
- `pipeline.py`: script que lê o CSV e insere os dados no PostgreSQL
- `dashboard.py`: app Streamlit com gráficos interativos
- `views.sql`: criação de três views SQL
- `requirements.txt`: dependências Python

## ▶️ Como Rodar

### 1. Subir o PostgreSQL com Docker:
```bash
docker run --name postgres-iot -e POSTGRES_PASSWORD=1234 -p 5432:5432 -d postgres
```

### 2. Instalar dependências:
```bash
pip install -r requirements.txt
```

### 3. Executar o pipeline:
```bash
python pipeline.py
```

### 4. Executar o dashboard:
```bash
streamlit run dashboard.py
```

## 📊 Views SQL Criadas
- Média de temperatura por dispositivo
- Leituras por hora do dia
- Temperaturas máximas e mínimas por dia

## 🗂️ Dataset
Baixar manualmente do Kaggle:
https://www.kaggle.com/datasets/atulanandjha/temperature-readings-iot-devices

## ✍️ Autor
Victor Hugo Santos
