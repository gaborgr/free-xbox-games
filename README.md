# Scraping de Juegos Gratis en la Tienda de Xbox

Este es un proyecto personal que utiliza `Selenium` y `BeautifulSoup` para scrapear la tienda de Xbox en busca de juegos gratuitos. El script navega por la tienda, carga todos los juegos disponibles y filtra aquellos que son gratuitos, mostrando su nombre, precio y enlace.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado lo siguiente:

- Python 3.x
- Selenium
- BeautifulSoup4
- Un navegador compatible con Selenium (por ejemplo, Chrome)

Puedes instalar las dependencias necesarias ejecutando:

```bash
pip install selenium beautifulsoup4
```

## Configuración

1. **Descargar el controlador de Chrome**: Asegúrate de tener el controlador de Chrome (`chromedriver`) instalado y que esté en tu PATH. Puedes descargarlo desde [aquí](https://developer.chrome.com/docs/chromedriver/downloads?hl=es-419).

2. **Configurar las opciones de Selenium**: El script está configurado para usar Chrome como navegador. Si deseas usar otro navegador, deberás modificar las opciones de Selenium en el código.

## Uso

Para ejecutar el script, simplemente ejecuta el siguiente comando en tu terminal:

```bash
python nombre_del_archivo.py
```

## El script hará lo siguiente:

1. Abrirá la tienda de Xbox en el navegador.
2. Cargará todos los juegos disponibles haciendo clic en el botón **"Cargar más"** hasta que no haya más juegos para cargar.
3. Filtrará los juegos que sean gratuitos (etiquetados como **"Gratis"** o **"Free"**).
4. Imprimirá en la consola el nombre, precio y enlace de cada juego gratuito.

## Ejemplo de Salida

El script imprimirá algo similar a lo siguiente:

```bash
Nombre del Juego - Gratis - https://www.xbox.com/es-CL/games/nombre-del-juego
Otro Juego - Free - https://www.xbox.com/es-CL/games/otro-juego
```

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un **fork** del repositorio y enviar un **pull request** con tus mejoras. Las contribuciones son bienvenidas, especialmente en las siguientes áreas:

- Mejoras en la eficiencia del **scraping**.
- Adición de nuevas funcionalidades, como la exportación de resultados a un archivo **CSV**.
- Soporte para otras tiendas o plataformas.

## Licencia

Este proyecto está bajo la licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme a través de mi perfil de **GitHub** o por correo electrónico.

---

¡Gracias por visitar este repositorio!
