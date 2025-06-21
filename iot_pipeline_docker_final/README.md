# Pipeline de Dados com IoT e Docker (versão Docker Compose)

Este projeto implementa um pipeline que:
- Lê dados de sensores IoT a partir de um CSV real
- Insere os dados em um banco PostgreSQL via Docker
- Cria views SQL com agregações úteis
- Gera um dashboard interativo com Streamlit

## 🚀 Como rodar o projeto

### 1. Pré-requisitos
- Docker e Docker Compose instalados
- Baixe o CSV original do Kaggle e renomeie para:
```
temperature-readings.csv
```
Coloque-o na raiz do projeto.

### 2. Subir tudo com Docker Compose
```bash
docker-compose up
```

Acesse o dashboard em: http://localhost:8501

## Views criadas
- `avg_temp_por_dispositivo`
- `leituras_por_hora`
- `temp_max_min_por_dia`