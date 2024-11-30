from supabase import create_client
import toml

try:
    secrets_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'secrets.toml'))
    secrets = toml.load(secrets_path)
except FileNotFoundError:
    print('El archivo secrets.toml no se encontró. Asegúrate de que esté presente en el directorio raíz.')
    raise
SUPABASE_URL = secrets['SUPABASE_URL']
SUPABASE_KEY = secrets['SUPABASE_KEY']

supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insertar_datos_mineria(datos):
    response = supabase_client.table("datos_mineria").insert(datos).execute()
    return response

def obtener_datos_mineria():
    response = supabase_client.table("datos_mineria").select("*").execute()
    return response.data

def insertar_resultado_prediccion(datos):
    response = supabase_client.table("resultados_prediccion").insert(datos).execute()
    return response