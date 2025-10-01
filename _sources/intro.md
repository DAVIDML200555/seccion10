# **Introducción y Contextualización**

Las enfermedades cardiovasculares (ECV) constituyen una de las principales causas de mortalidad a nivel mundial, representando aproximadamente el 32% de todas las muertes globales según la Organización Mundial de la Salud (OMS). Dentro de este grupo, la insuficiencia cardíaca es una afección grave y crónica que ocurre cuando el corazón no puede bombear la sangre de manera eficiente para satisfacer las necesidades del organismo. Su diagnóstico temprano y preciso es, por tanto, un pilar fundamental en la medicina moderna, con el potencial de salvar innumerables vidas y mejorar significativamente la calidad de vida de los pacientes.

En la era actual, la ciencia de datos y el aprendizaje automático (Machine Learning) han emergido como herramientas transformadoras en el campo de la salud. La capacidad de analizar grandes volúmenes de datos clínicos para identificar patrones complejos y relaciones no evidentes para el ojo humano ofrece un nuevo paradigma para el apoyo al diagnóstico y la prognosis. La aplicación de estos algoritmos puede auxiliar a los profesionales de la salud en la identificación de pacientes de alto riesgo, permitiendo intervenciones más tempranas y personalizadas.

## **Presentación del Dataset**

Este proyecto se centra en el análisis del dataset **"Heart Failure Prediction"**, disponible públicamente en Kaggle. Este conjunto de datos reúne información clínica y de estilo de vida de 918 pacientes, con el objetivo principal de predecir la presencia de una enfermedad cardíaca.

La principal fortaleza de este dataset reside en su conjunto de **12 atributos** que capturan una visión integral de cada paciente. A continuación, se detalla el significado de cada variable:

*   **Age:** Edad del paciente expresada en años.
*   **Sex:** Sexo del paciente [M: Masculino, F: Femenino].
*   **ChestPainType:** Tipo de dolor torácico [TA: Angina Típica, ATA: Angina Atípica, NAP: Dolor No Anginoso, ASY: Asintomático].
*   **RestingBP:** Presión arterial en reposo medida en mm Hg.
*   **Cholesterol:** Colesterol sérico medido en mm/dl.
*   **FastingBS:** Glucemia en ayunas [1: si FastingBS > 120 mg/dl, 0: en caso contrario].
*   **RestingECG:** Resultados del electrocardiograma en reposo [Normal: Normal, ST: presencia de anomalía en la onda ST-T, LVH: hipertrofia ventricular izquierda probable o definitiva].
*   **MaxHR:** Frecuencia cardíaca máxima alcanzada durante el ejercicio, valor numérico entre 60 y 202.
*   **ExerciseAngina:** Presencia de angina inducida por el ejercicio [Y: Sí, N: No].
*   **Oldpeak:** Depresión del segmento ST inducida por el ejercicio en relación al reposo, medida en unidades.
*   **ST_Slope:** Pendiente del segmento ST durante el ejercicio máximo [Up: ascendente, Flat: plana, Down: descendente].
*   **HeartDisease:** Variable objetivo que indica la presencia (1) o ausencia (0) de enfermedad cardíaca.

Estos atributos pueden clasificarse en las siguientes categorías para su análisis:
*   **Variables Demográficas:** Edad, Sexo.
*   **Variables Clínicas:** Tipo de dolor torácico (ChestPainType), presión arterial en reposo (RestingBP), colesterol sérico (Cholesterol), glucemia en ayunas (FastingBS), resultados electrocardiográficos en reposo (RestingECG), frecuencia cardíaca máxima alcanzada (MaxHR).
*   **Indicadores de Enfermedad Coronaria:** Angina inducida por ejercicio (ExerciseAngina).
*   **Mediciones de Prueba de Esfuerzo:** Depresión del segmento ST (Oldpeak), pendiente del segmento ST (ST_Slope).

La variable objetivo (**HeartDisease**) es binaria, lo que permite abordar el problema como una tarea de clasificación supervisada.

## **Objetivos del Proyecto**

El presente proyecto tiene como objetivo general **desarrollar y evaluar un modelo predictivo de aprendizaje automático que determine con alta precisión la probabilidad de que un paciente sufra una enfermedad cardíaca, basándose en sus características clínicas y demográficas.**

Para alcanzar este objetivo general, se han definido los siguientes **objetivos específicos**:

1.  **Análisis Exploratorio de Datos (EDA):** Realizar una exploración exhaustiva del dataset para comprender la distribución de cada variable, identificar valores atípicos (outliers), missing values (si los hubiera) y descubrir relaciones preliminares entre las características y la variable objetivo.
2.  **Preprocesamiento e Ingeniería de Características:** Preparar los datos para el modelado, lo que incluye la codificación de variables categóricas, la normalización/escalado de variables numéricas y la posible creación de nuevas características que puedan mejorar el poder predictivo de los modelos.
3.  **Modelado y Entrenamiento:** Implementar y entrenar una variedad de algoritmos de clasificación supervisada, tales como Regresión Logística, Árboles de Decisión, K Vecinos Más Cercanos, Random Forest y algoritmos de boosting como XGBoost.
4.  **Evaluación y Comparación de Modelos:** Evaluar el rendimiento de cada modelo utilizando métricas robustas y apropiadas para problemas de clasificación binaria en el ámbito de la salud, como la precisión (Accuracy), la sensibilidad (Recall), la precisión (Precision), la métrica F1-score y el área bajo la curva ROC (AUC-ROC). La sensibilidad será de especial interés, ya que es crucial identificar correctamente a la mayor cantidad posible de pacientes enfermos (minimizar falsos negativos).
5.  **Interpretación del Modelo Final:** Una vez seleccionado el mejor modelo, se buscará interpretar sus resultados para identificar qué características son las más influyentes en la predicción. Esta interpretabilidad es clave para que el modelo no sea una "caja negra" y sus resultados puedan ser comprendidos y validados por expertos en cardiología.

## **Relevancia y Potencial Impacto**

La culminación exitosa de este proyecto tiene el potencial de demostrar el valor de los modelos predictivos como sistemas de apoyo a la decisión clínica. Un modelo confiable podría ser integrado en entornos hospitalarios o clínicos para ayudar a los médicos a priorizar pacientes, confirmar diagnósticos o sugerir la necesidad de pruebas más exhaustivas. Si bien un modelo de machine learning no reemplaza el criterio de un profesional, sirve como una herramienta poderosa para aumentar la eficiencia y la precisión en la detección temprana de una de las enfermedades más críticas de nuestro tiempo.
