# 🛡️ Don Quijote RPG - Español

**Trabajo escolar de Español – Nikolas Lopes da Silva – 472 I**

En este RPG textual interactivo, Don Quijote renace en el siglo XXI y ve el mundo moderno como un campo de batalla lleno de “monstruos invisibles”. Con una visión romántica e idealista, interpreta la realidad contemporánea a su manera y lucha contra las injusticias actuales, guiando al jugador a través de decisiones críticas en su aventura.

---

## 🗂️ Estructura del Proyecto
```
RPG_Espanhol/
├── main.py            # Archivo principal del juego
├── colors.py          # Define colores para la salida en terminal
└── History/
    ├── session1.py    # Primera decisión (BUENA o MALA)
    ├── session2.py    # Segunda decisión (BUENA o MALA)
    ├── session3.py    # Tercera decisión (BUENA o MALA)
    └── sessionLast.py # Final feliz: ¡Don Quijote gana!
```
---

## 🎮 Sobre el Juego

El jugador toma el rol de Don Quijote, enfrentando “enemigos” modernos desde su perspectiva noble y distorsionada. A cada paso, debe elegir sabiamente: una buena decisión permite continuar la historia; una mala, termina su travesía.

---

## 📜 Archivos del Juego

### ▶️ `main.py`
- Muestra el título e introducción del juego.
- Inicia un bucle (`while`) con opciones disponibles para el jugador.
- Controla el progreso de la narrativa según las decisiones tomadas.

### 📘 Sesiones de la Historia

#### `session1.py`, `session2.py`, `session3.py`
- Reciben la elección del jugador.
- Si es BUENA: continúa la historia.
- Si es MALA: el juego finaliza con un mensaje narrativo.

#### `sessionLast.py`
- Presenta el desenlace victorioso de Don Quijote.
- Finaliza el juego felicitando al jugador.

---

## 🎨 Estilo Visual

El módulo `colors.py` define los colores usados en los textos del juego, agregando claridad y emoción visual durante la ejecución en consola.

---

## ✅ Requisitos

- Python 3.x instalado
- Terminal que soporte códigos ANSI (colores)

---

## 🧪 Cómo Ejecutar el Juego

1. Descarga o clona el repositorio:
```bash
git clone https://github.com/usuario/RPG_Espanhol.git
