## Extractor Vera
Extractor que agrega la capacidad de descargar desde Vera (tv.vera.com.uy y veramas.com.uy).  

## Tenelo
Copiá y pegá esta línea en la terminal
```bash
cd ~/.temp && git clone https://github.com/thepante/ytdl-vera.git && cd ./ytdl-vera && sudo sh ./install.sh && cd ~/
```
Con eso se abre el "instalador" (install.sh) que hace los pasos necesarios para integrar este extractor. Pero soy un queso, así que tanto el .py como el .sh son precarios, hay maneras de mejorarlos claro está, pero bueno, no tengo experiencia con esto.

### O de manera manual
Nota: `<youtube_dl>` = ruta donde se encuentra instalado youtube-dl.
1. Obtener el `vera.py`, clonando o descargando el `.zip` del repo
2. Copiar ese archivo en `<youtube_dl>/extractor/`
3. Integrarlo agregando la línea `from .vera import VeraIE` al final en el archivo `<youtube_dl>/extractor/extractors.py`

----

Si querés ayudar a mejorarlo, bárbaro avisame, como ves soy alto kamikaze

## Status
- [x] Descarga videos desde tv.vera.com.uy<sup>**</sup>
- [ ] Descarga listas desde tv.vera
- [ ] Descarga videos/listas desde veramas.com.uy<sup>*</sup>
- [ ] Probar más extracciones de audio<sup>**</sup>
- [ ] Probar con otros flags

> \* No escribí nada para ese dominio todavía. Así que por ahora solo detecta que es el extractor correspondiente para esa página (veramas), pero no puede extraer naranja. Cuando quede funcionando decentemente el dominio principal, me pongo con agregar las instrucciones para esta dirección secundaria.

> \*\* Extrae audio pero igual (normal) descarga el video entero a máxima calidad. En mis prueba a llegado a pesar 1GB de descarga un capitulo de 45min. Tengo que ver como se hace para tomar diferentes calidades para poder elegir.

**Por ahora funciona para lo básico**
