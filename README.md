# Heart Disease MLOps

Proyecto de despliegue de un modelo de Machine Learning para predecir enfermedades cardíacas.  
Incluye entrenamiento, despliegue con FastAPI + Docker, orquestación con Kubernetes, integración continua con GitHub Actions y monitoreo de deriva de datos con Evidently.

---

## Arquitectura y tecnologías utilizadas

- **FastAPI**: servir modelos como API REST.
- **Kubernetes**: orquestación de contenedores y escalabilidad.
- **GitHub Actions**: integración continua, pruebas y despliegue automático.
- **Evidently**: monitoreo de deriva de datos y performance de los modelos.

## Instrucciones de uso

1. Clonamos el repositorio de github
`git clone https://github.com/DAVIDML200555/seccion10.git`

2. Accedemos a la carpeta donde se encuentra el flujo de trabajo 
`cd heart-disease-mlops`

3. Construimos la imagen del Docker
`docker build -t heart-api .`

4. Levantamos el contenedor
`docker run -d -p 8000:8000 heart-api`

5. Probar la API, podemos hacerlo de dos maneras.

Opción 1
- Desde el Powershell de Windows: 

curl -Method POST http://localhost:8000/predict `
     -Headers @{ "Content-Type" = "application/json" } `
     -Body '{
       "model_name": "KNN",
       "features": {
         "Sex": "M",
         "ChestPainType": "ASY",
         "FastingBS": 0,
         "RestingECG": "Normal",
         "ExerciseAngina": "Y",
         "Oldpeak": 0.0,
         "ST_Slope": "Flat"
       }
     }'

La API retornará un JSON con el modelo utilizado y la predicción (1 = enfermedad, 0 = no enfermedad).

Opción 2
- Abre en el navegador http://127.0.0.1:8000/docs
- Selecciona el endpoint /predict → "Try it out".
- Ingresa un ejemplo de entrada como este:
{
    "model_name": "KNN",
    "features": {
        "Sex": "M",
        "ChestPainType": "ASY",
        "FastingBS": 0,
        "RestingECG": "Normal",
        "ExerciseAngina": "Y",
        "Oldpeak": 0.0,
        "ST_Slope": "Flat"
    } 
}
Haz clic en "Execute" y revisa la respuesta JSON que contiene la predicción.

Opciones de modelos:
-Logistic Regression
-KNN
-GaussianNB
-BernoulliNB
-MultinomialNB
-Decision Tree
-Random Forest
-XGBoost

Importante usar estos nombre exactos