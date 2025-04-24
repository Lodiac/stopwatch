# Cronómetro Python con Interfaz Gráfica

Un cronómetro sencillo pero funcional construido con Python y Tkinter, con una interfaz gráfica amigable que permite realizar un seguimiento preciso del tiempo y registrar vueltas.

## Descripción

Esta aplicación proporciona un cronómetro digital completo con funcionalidades para iniciar/detener, reiniciar, registrar vueltas y visualizar los tiempos parciales. Ideal para actividades deportivas, cocina, estudios con la técnica Pomodoro, o cualquier otra situación donde necesites medir el tiempo con precisión.

## Requisitos

- Python 3.x
- Tkinter (incluido en la mayoría de las instalaciones estándar de Python)

## Instalación

1. Clona este repositorio o descarga el archivo `stopwatch_gui.py`
2. Asegúrate de tener Python 3.x instalado en tu sistema

```bash
# Para comprobar la versión de Python
python --version
```

## Cómo usar

1. Ejecuta el script desde la línea de comandos o tu IDE favorito

```bash
python stopwatch_gui.py
```

2. Una vez que se abra la aplicación, utiliza los botones para controlar el cronómetro:
   - **Iniciar/Detener**: Comienza o pausa el cronómetro
   - **Reiniciar**: Vuelve el cronómetro a cero
   - **Vuelta**: Registra un tiempo parcial mientras el cronómetro sigue corriendo
   - **Limpiar Vueltas**: Elimina todos los registros de vueltas

## Características

- Interfaz gráfica intuitiva y fácil de usar
- Visualización de tiempo en formato hh:mm:ss.ms
- Registro de vueltas con tiempos totales e intervalos
- Área de desplazamiento para revisar todas las vueltas registradas
- Indicador de estado que muestra la acción actual
- Diseño limpio y moderno

## Estructura del código

El código está organizado en una clase principal `StopwatchApp` que maneja:
- La creación de la interfaz gráfica
- La lógica del cronómetro
- El registro y visualización de vueltas
- El formateo de tiempo

## Personalización

Puedes modificar fácilmente el diseño y la apariencia ajustando las variables de:
- Colores (bg, fg)
- Fuentes (font)
- Tamaños (width, height)
- Distribución (padding, grid)

## Capturas de pantalla

[Aquí puedes añadir capturas de pantalla de la aplicación en funcionamiento]

## Mejoras posibles

- Añadir sonidos para las acciones de inicio, parada y vuelta
- Implementar temas claro/oscuro
- Guardar los tiempos en un archivo
- Añadir temporizador de cuenta regresiva
- Implementar alarmas o notificaciones

## Licencia

Este proyecto está disponible bajo la licencia MIT. Siéntete libre de modificarlo y distribuirlo según tus necesidades.

---

Desarrollado con ❤️ usando Python y Tkinter
