# Publicar el proyecto en GitHub sin comprometer secretos

## 1) Si ya tienes un repositorio de la Evaluación 1

**Es la opción recomendada.** No reemplaces su historia; clónalo para conservar los commits auténticos.

```powershell
git clone https://github.com/TU-USUARIO/TU-REPOSITORIO.git
cd TU-REPOSITORIO
```

Copia los archivos **actualizados** de este ZIP dentro de la copia clonada (pero **no** copies `.git/`, `.venv/`, `.env`, ni `db.sqlite3`). Haz la copia con Explorador de Windows, revisando que se reemplacen los archivos anteriores. Después:

```powershell
git status
git add .
git commit -m "Evaluacion 2: modelo, API REST, SQL, pruebas y documentacion"
git push
```

Confirma en GitHub que el nuevo commit se suma al historial anterior.

## 2) Si crearás un repositorio GitHub nuevo

Este ZIP incluye una carpeta oculta `.git/` con dos commits locales: el estado del ZIP recibido como punto de partida y la ampliación de la Evaluación 2. Es **historia reconstruida localmente**, no sustituto del historial original.

En GitHub crea un repositorio **vacío** (no marques README / gitignore automático). En la carpeta del proyecto:

```powershell
git status
git log --oneline
git remote add origin https://github.com/TU-USUARIO/TU-REPOSITORIO.git
git push -u origin main
```

Si ya hay `origin`, revisa con `git remote -v` y corrígelo con `git remote set-url origin ...` solo si es el repositorio correcto. **No utilices `git push --force` para resolver historiales divergentes**: puedes borrar avances previos.

> Si Windows no muestra `.git`, activa la visualización de elementos ocultos o usa `git log`. Si un ZIP no preservó la carpeta oculta, puedes ejecutar `git init -b main` y crear commits propios, pero ya no verás el historial preparado.

## 3) Configura tu autor para nuevos commits

```powershell
git config user.name "TU NOMBRE"
git config user.email "TU CORREO VINCULADO A GITHUB"
```

La autoría de los commits locales prearmados está marcada genéricamente como `Preparación académica` y **no representa un historial original tuyo**.

## 4) Antes de subir

```powershell
git status
git check-ignore .env
```

`.env` debe aparecer como ignorado. Si ya habías subido una clave real alguna vez, eliminarla de un commit nuevo no basta: hay que revocarla y revisar el historial. La evidencia de la pauta es la **URL pública o accesible del repositorio con commits**, algo que debes aportar desde tu propia cuenta.

**Antes de entregar:** anota la URL real del repositorio aquí o en tu LMS. El valor `TU-USUARIO/TU-REPOSITORIO` es un ejemplo y no corresponde a un repositorio creado.
