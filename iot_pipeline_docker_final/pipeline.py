import pandas as pd
import time
import psycopg2
from sqlalchemy import create_engine, text

DB_USER = 'postgres'
DB_PASSWORD = '1234'
DB_HOST = 'db'
DB_PORT = '5432'
DB_NAME = 'postgres'
CSV_FILE = 'temperature-readings.csv'

print("Esperando o banco de dados ficar pronto...")
while True:
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        conn.close()
        print("Banco de dados está pronto.")
        break
    except psycopg2.OperationalError:
        time.sleep(1)

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Carrega e processa o CSV
df = pd.read_csv(CSV_FILE)
df = df.rename(columns={
    'room_id/id': 'device_id',
    'noted_date': 'timestamp',
    'temp': 'temperature'
})
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True, errors='coerce')
df = df[['device_id', 'timestamp', 'temperature']].dropna()
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
print("Dados inseridos com sucesso.")

with engine.begin() as conn:
    row_count = conn.execute(text("SELECT COUNT(*) FROM temperature_readings")).scalar()
    print(f"{row_count} registros encontrados na tabela temperature_readings")

    if row_count == 0:
        print("❌ Nenhum dado encontrado na tabela. Views não serão criadas.")
    else:
        try:
            conn.execute(text("""
                CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
                SELECT device_id, AVG(temperature) as avg_temp
                FROM temperature_readings
                GROUP BY device_id;
            """))
            print("✅ View avg_temp_por_dispositivo criada com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao criar avg_temp_por_dispositivo: {e}")

        try:
            conn.execute(text("""
                CREATE OR REPLACE VIEW leituras_por_hora AS
                SELECT EXTRACT(HOUR FROM timestamp) as hora, COUNT(*) as contagem
                FROM temperature_readings
                GROUP BY hora;
            """))
            print("✅ View leituras_por_hora criada com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao criar leituras_por_hora: {e}")

        try:
            conn.execute(text("""
                CREATE OR REPLACE VIEW temp_max_min_por_dia AS
                SELECT DATE(timestamp) as data,
                       MAX(temperature) as temp_max,
                       MIN(temperature) as temp_min
                FROM temperature_readings
                GROUP BY data;
            """))
            print("✅ View temp_max_min_por_dia criada com sucesso.")
        except Exception as e:
            print(f"❌ Erro ao criar temp_max_min_por_dia: {e}")
