import psycopg2
import os

db_url = "postgresql://postgres:[PASSWORD]@db.ebujagqqgpbkvevfuqjl.supabase.co:5432/postgres"

conn = psycopg2.connect(db_url)
cursor = conn.cursor()

