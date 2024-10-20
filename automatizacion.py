import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pickle

# Ruta para almacenar las cookies
cookies_file = "whatsapp_cookies.pkl"

# Inicializa el WebDriver (usa Chrome en este )
driver = webdriver.Chrome()

# Intenta cargar las cookies de una sesión previa si existen
def cargar_cookies():
    try:
        driver.get("https://web.whatsapp.com")
        time.sleep(5)  # Esperar un poco a que cargue la página
        with open(cookies_file, "rb") as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(5)  # Esperar después de refrescar
        print("Sesión de WhatsApp Web restaurada con cookies.")
    except FileNotFoundError:
        print("No se encontraron cookies. Necesitas iniciar sesión por primera vez.")

# Guarda las cookies después de iniciar sesión
def guardar_cookies():
    with open(cookies_file, "wb") as cookiesfile:
        pickle.dump(driver.get_cookies(), cookiesfile)
    print("Cookies guardadas para futuras sesiones.")

# Abre WhatsApp Web y trata de restaurar la sesión con cookies
cargar_cookies()

# Esperar a que el usuario escanee el código QR si es la primera vez
input("Presiona ENTER después de haber iniciado sesión en WhatsApp Web...")

# Guardar cookies si es la primera vez que se inicia sesión
guardar_cookies()

# Leer los datos del archivo Excel
data = pd.read_excel("pruebas.xlsx", sheet_name='Hoja1')

# Iterar sobre el DataFrame
for i in range(len(data)):
    celular = str(data.loc[i, 'Celular'])
    nombre = data.loc[i,'Nombre']
    producto = data.loc[i,'Producto']
    
    # Crear mensaje personalizado
    #mensaje = "Hola, " + nombre + "! Gracias por comprar " + producto + " con nosotros 🙌"
    mensaje = f"""
    Estimado/a {nombre}:

    Espero que se encuentre muy bien. Mi nombre es Isidora Covarrubias y soy parte del equipo de Xinermed, una empresa especializada en servicios de hospitalización domiciliaria. 🏥

    Nos gustaría ofrecerle nuestros servicios para mejorar la calidad de atención de sus pacientes desde la comodidad de sus hogares, siempre garantizando un cuidado médico profesional y personalizado. ✅

    Le invito a guardar este número 📞 para que podamos estar en contacto directo 💬, y quedo a su disposición para cualquier consulta o información adicional.

    ¡Gracias por su tiempo y confianza! 🙏

    Saludos cordiales,
    Isidora Covarrubias
    Xinermed
    [Tu número de teléfono]
    """

    #print(mensaje)


    # Abre el chat de WhatsApp Web para ese número de teléfono
    url = f"https://web.whatsapp.com/send?phone={celular}&text={mensaje}"
    driver.get(url)
    
    # Esperar a que el botón de enviar aparezca
    time.sleep(10)  # Ajusta este tiempo si tu conexión es más lenta
    
    try:
        # Hacer clic en el botón de enviar (si ya tienes la sesión iniciada)
        enviar_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Enviar"]')
        enviar_button.click()  # Hacer clic en el botón de enviar
        time.sleep(2)  # Esperar un poco después de enviar el mensaje
    except Exception as e:
        print(f"No se pudo enviar el mensaje a {celular}: {e}")

# Cerrar el navegador
driver.quit()
