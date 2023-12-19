from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

# PostgreSQL veritabanına bağlantı için gerekli bilgileri burada ayarlayın
DATABASE_URL = "postgresql://your_database_user:your_database_password@localhost/your_database_name"

engine = create_engine(DATABASE_URL)

metadata = MetaData()

# Örnek bir tablo tanımı
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
)

if __name__ == "__main__":
    metadata.create_all(engine)