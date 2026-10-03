# API de Procesamiento - Simulación de Temperatura CNC

Microservicio desarrollado en Python con **Flask** para simular la etapa de procesamiento de datos de temperatura de una máquina de control numérico computarizado (CNC). Diseñado para ejecutarse en entornos locales y listo para despliegue en **Google Cloud Run**.

---

## 📋 Características

- **Formato:** Respuestas en formato JSON.
- **Campo obligatorio:** `"repositorio": 1`.
- **Rango de temperatura simulada:** Entre 40 y 80 °C.
- **Reglas de clasificación:**
  - `< 60 °C` &rarr; Estado: `Normal` | Acción: `Operacion normal`
  - `60 °C a < 70 °C` &rarr; Estado: `Advertencia` | Acción: `Revisar sistema de enfriamiento`
  - `>= 70 °C` &rarr; Estado: `Alarma` | Acción: `Detener maquina y revisar`
- **Compatibilidad con Google Cloud Run:** Escucha en `0.0.0.0` y respeta la variable de entorno `PORT` (por defecto `8080`).

---

## 📂 Estructura del Proyecto

```text
api-procesamiento/
├── .gitignore
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```

---

## 🚀 Cómo Probarlo Localmente

### Opción 1: Con Python directo

1. **Crear y activar un entorno virtual (opcional pero recomendado):**
   - En Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - En Linux / macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```
   *(Opcional) Si deseas probar con otro puerto:*
   - En Windows PowerShell:
     ```powershell
     $env:PORT="5000"; python main.py
     ```
   - En Linux / macOS:
     ```bash
     PORT=5000 python main.py
     ```

4. **Consultar la API:**
   Abre tu navegador o ejecuta en otra terminal:
   ```bash
   curl http://localhost:8080/
   ```
   O también:
   ```bash
   curl http://localhost:8080/procesar
   ```

---

### Opción 2: Con Docker

1. **Construir la imagen:**
   ```bash
   docker build -t api-procesamiento .
   ```

2. **Correr el contenedor:**
   ```bash
   docker run -p 8080:8080 -e PORT=8080 api-procesamiento
   ```

3. **Realizar una petición:**
   ```bash
   curl http://localhost:8080/
   ```

---

## 📡 Ejemplo de Respuesta JSON

```json
{
  "accion": "Revisar sistema de enfriamiento",
  "estado": "Advertencia",
  "maquina": "CNC-01",
  "proceso": "procesamiento_temperatura_cnc",
  "repositorio": 1,
  "temperatura_c": 64.52
}
```

---

## ☁️ Despliegue en Google Cloud Run

1. **Autenticar y configurar proyecto en gcloud CLI:**
   ```bash
   gcloud config set project TU_ID_PROYECTO
   ```

2. **Construir y desplegar directamente desde el código fuente:**
   ```bash
   gcloud run deploy api-procesamiento \
     --source . \
     --region us-central1 \
     --allow-unauthenticated
   ```
Despliegue en Google Cloud Run.
