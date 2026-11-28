# 💎 El Buscador del Tesoro

Juego por consola en Python en el que hay que encontrar un tesoro escondido en un mapa. Tiene inicio de sesión con usuarios y roles, sistema de pistas, estadísticas con gráficos y registro de eventos.

Proyecto final de la **UD4 de Sistemas de Gestión Empresarial (SGE)** · DAM 2 · CIFP Virgen de Gracia (Puertollano) · Curso 2026/2027.

**Autores:** Iván Hergueta Losa e Ismael.

---

## 📋 Índice

- [Requisitos previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Ejecución](#-ejecución)
- [Cómo se juega](#-cómo-se-juega)
- [Menús](#-menús)
- [Registro de eventos (logs)](#-registro-de-eventos-logs)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Decisiones de diseño](#-decisiones-de-diseño)
- [Reparto de requisitos](#-reparto-de-requisitos)

---

## 🧰 Requisitos previos

| Herramienta | Versión |
|---|---|
| Python | 3.13 (mínimo 3.9) |
| matplotlib | la que instala `requirements.txt` |
| Git | cualquiera reciente |

> El proyecto se ha desarrollado con **PyCharm**, pero funciona desde cualquier terminal.

---

## ⚙️ Instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/nivkoly-Ivan/ProyectoSGEII.git
   cd ProyectoSGEII
   ```

2. **Crea y activa un entorno virtual** (recomendado)

   ```bash
   python -m venv .venv
   ```

   - Windows: `.venv\Scripts\activate`
   - Linux / macOS: `source .venv/bin/activate`

3. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

   En PyCharm también se puede hacer desde *Settings → Project → Python Interpreter → +*, buscando `matplotlib`.

---

## 🔧 Configuración

Los usuarios están en el fichero **`users.txt`**, en la raíz del proyecto. Cada línea es un usuario con el formato:

```
usuario;contraseña;rol
```

Hay dos roles posibles, siempre **en minúscula**:

| Rol | Qué puede hacer |
|---|---|
| `usuario` | Jugar partidas y consultar sus estadísticas y su historial. |
| `admin` | Todo lo anterior, más el menú de administrador. |

Ejemplo:

```
jugador1;1234;usuario
jefe;abcd;admin
```

> ⚠️ No dejes líneas vacías en el fichero. Solo pueden entrar los usuarios que estén en `users.txt`.

---

## ▶️ Ejecución

Desde la raíz del proyecto:

```bash
python main.py
```

En PyCharm: abre `main.py` y pulsa ▶️ (o `Mayús + F10`).

> La aplicación busca `users.txt` y crea la carpeta `log/` **en la carpeta desde la que se ejecuta**, así que hay que lanzarla desde la raíz del proyecto.

---

## 🎮 Cómo se juega

1. Inicia sesión con un usuario de `users.txt`.
2. En el menú principal, elige **1 · Empezar partida**.
3. Elige la dificultad:

   | Opción | Nivel | Mapa |
   |---|---|---|
   | 1 | Básica | 5 × 5 |
   | 2 | Media | 8 × 8 |
   | 3 | Avanzada | 10 × 10 |

4. Escribe la **fila** y la **columna** de la casilla que quieres probar (empiezan en 0).

### Leyenda del mapa

| Símbolo | Significado |
|---|---|
| `?` | Casilla sin explorar |
| `-` | Casilla explorada sin tesoro |
| `💎` | Tesoro encontrado |

### 💡 Pistas

A partir del **tercer intento fallido**, cada vez que falles el juego te dice si te has quedado **cerca** (el tesoro está en una casilla de alrededor, en horizontal, vertical o diagonal) o **lejos**. La pista nunca revela la posición exacta.

### 🏳️ Abandonar

Escribe **`-1`** en la fila o en la columna para abandonar la partida. Cuenta como **abandonada** en las estadísticas.

---

## 🗂️ Menús

### Menú principal

| Opción | Acción |
|---|---|
| 1 | Empezar partida |
| 2 | Estadísticas de la sesión (con gráficos) |
| 3 | Historial de partidas de la sesión |
| 4 | Cambiar de sesión |
| 5 | Salir de la aplicación |
| 6 | Opciones de administrador *(solo `admin`)* |

### Menú de administrador

| Opción | Acción |
|---|---|
| 1 | Estadísticas de **todas** las partidas de la sesión |
| 2 | Historial de **todas** las partidas: jugador, posición del tesoro, casillas probadas, pistas y mapa |
| 3 | Activar *cheats*: el tesoro se ve en el mapa durante la partida. Se desactivan al cerrar sesión |
| 4 | Volver al menú principal |

### 📊 Estadísticas

Se calculan con las partidas jugadas **mientras la aplicación está abierta**:

- Partidas iniciadas, finalizadas, ganadas y abandonadas.
- Porcentaje de victorias sobre las partidas finalizadas.
- Total de intentos, media de intentos y media de intentos en las partidas ganadas.
- Partidas ganadas por nivel de dificultad.
- Partidas realizadas por cada usuario.
- Dos gráficos con `matplotlib`: **partidas por dificultad** y **ganadas frente a abandonadas**.

> Los gráficos se abren en una ventana. Al cerrarla aparece el siguiente y después se vuelve al menú.

---

## 📝 Registro de eventos (logs)

Todo lo que pasa en la aplicación se guarda con el módulo **`logging`** de Python en:

```
log/AAAAMMDD-log.log
```

Cada línea lleva la fecha y la hora, el nivel y el mensaje con el usuario:

```
[2026-11-28 12:01:41] [INFO] Usuario Ivan login correcto
[2026-11-28 12:01:46] [INFO] [PARTIDA] INICIO DE PARTIDA, DIFICULTAD : 1 POR Ivan
```

Se registran: el inicio y el fin de la aplicación, los inicios de sesión correctos e incorrectos, el inicio de cada partida y su dificultad, cada intento con sus coordenadas, los intentos fuera de rango, las partidas ganadas (con el número de intentos) y las abandonadas.

> La carpeta `log/` está en el `.gitignore`, así que no se sube al repositorio.

---

## 🏗️ Estructura del proyecto

```
ProyectoSGEII/
├── main.py            # Punto de entrada: arranca la aplicación
├── menu.py            # Menú de inicio, menú principal y menú de administrador
├── control_users.py   # Lectura de users.txt y validación del login
├── juego.py           # Partida: dificultad, mapa, intentos, pistas y abandono
├── estadisticas.py    # Estadísticas, historial y gráficos
├── logs.py            # Clase Log: configuración del módulo logging
├── users.txt          # Credenciales de los usuarios
├── requirements.txt   # Dependencias (matplotlib)
└── log/               # Ficheros de log (se crea al ejecutar)
```

---

## 🧠 Decisiones de diseño

- **Datos en memoria:** las partidas se guardan en la lista `partidas` de `juego.py`, una lista de diccionarios con una partida cada uno (usuario, dificultad, tesoro, intentos, pistas, estado…). Al cerrar la aplicación se pierden, como pide el enunciado. Los únicos ficheros son `users.txt` y el log.
- **Ganadas frente a perdidas:** en este juego no se puede perder, solo ganar o abandonar. Por eso, en las estadísticas y en el gráfico, las **perdidas son las abandonadas**.
- **Abandono:** el enunciado no dice cómo se abandona una partida. Hemos elegido escribir `-1` en la fila o en la columna.
- **Historial:** a un usuario normal no se le enseña la posición del tesoro de sus partidas abandonadas, para que no pueda usarlo como trampa. El administrador sí la ve.
- **Estadísticas de usuario y de administrador:** un usuario ve sus estadísticas y cuántas partidas lleva cada usuario. El administrador ve las de toda la sesión.

---

## 👥 Reparto de requisitos

| Requisito | Descripción | Responsable |
|---|---|---|
| Req001 | Autenticación y gestión de usuarios | Iván |
| Req002 | Configuración de la partida y dificultad | Ismael |
| Req003 | Desarrollo de la partida | Ismael |
| Req004 | Sistema de pistas | Ismael |
| Req005 | Funciones del administrador | Iván / Ismael |
| Req006 | Registro de eventos (logging) | Iván |
| Req007 | Estadísticas y gráficos | Iván |
| Req008 | Datos de las partidas en memoria | Iván / Ismael|
| Req009 | Menú principal | Iván / Ismael|

---

<p align="center">Hecho con python por Iván e Ismael</p>
