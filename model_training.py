import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Cargar los datos
csv_path = 'mining_data.csv'
datos = pd.read_csv(csv_path)

# Seleccionar características y etiquetas
X = datos[['numero_trabajadores', 'equipos_operativos', 'produccion_obtenida', 'consumo_energia', 'calidad_mineral']]
y = datos['etiqueta']

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo de Árbol de Decisión
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Evaluar el modelo
predicciones = modelo.predict(X_test)
accuracy = accuracy_score(y_test, predicciones)
print(f"Precisión del modelo: {accuracy * 100:.2f}%")
print("Informe de clasificación:")
print(classification_report(y_test, predicciones))

# Guardar el modelo entrenado
joblib.dump(modelo, 'modelo_arbol_decision.pkl')
