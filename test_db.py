from app.database import get_connection

try:
    conn = get_connection()
    print("Connexion à Neon réussie !")
    conn.close()
except Exception as e:
    print("Erreur de connexion :", e)