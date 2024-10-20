# WhatsApp Message Sender Script

Este script está diseñado para enviar mensajes personalizados a través de WhatsApp Web utilizando Selenium para automatizar el navegador y Pandas para leer los datos de un archivo de Excel. Es ideal para campañas donde deseas enviar mensajes a múltiples contactos con un texto personalizado.

## Requisitos

1. **Python 3.x**
2. **Selenium WebDriver** (asegúrate de tener el controlador adecuado para tu navegador, en este caso, Chrome).
3. **Pandas** para manejar los datos desde un archivo de Excel.
4. **Chrome WebDriver** (debe estar en el PATH o especificar su ruta).
5. **Archivo de Excel** con una estructura que incluya columnas como `Celular`, `Nombre`, y `Producto`.

### Instalación de dependencias

Ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install selenium pandas openpyxl
