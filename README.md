## Extractor Vera
Extractor que agrega la capacidad de descargar desde Vera (tv.vera.com.uy y veramas.com.uy).  

### "Parcheá"
Copiamos, pegamos esta linea en la terminal (es con sudo)
```bash
cd ~/.temp && git clone https://github.com/thepante/ytdl-vera.git && cd ./ytdl-vera && sudo sh ./install.sh && cd ~/
```
Con eso se abre el "instalador" (install.sh) que hace los pasos necesarios para integrar este extractor. Pero soy un queso, así que tanto el .py como el .sh son re precarios, hay maneras de hacerlo mejor claro está, pero bueno, no tengo casi experiencia con esto.

Si querés ayudar a mejorarlo, bárbaro, como ves soy alto kamikaze

## Status
- [x] Descarga videos desde tv.vera.com.uy<sup>**</sup>
- [ ] Descarga listas desde tv.vera
- [ ] Descarga videos/listas desde veramas.com.uy<sup>*</sup>
- [ ] Probar más extracciones de audio<sup>**</sup>
- [ ] Probar con otros flags

> \* No escribí nada para ese dominio todavía. Así que por ahora solo detecta que es el extractor correspondiente para esa página (veramas), pero no puede extraer naranja. Cuando quede funcionando decentemente el dominio principal, me pongo con agregar las instrucciones para esta dirección secundaria.
> \*\* Extrae audio pero igual (normal) descarga el video entero a máxima calidad. En mis prueba a llegado a pesar 1GB de descarga un capitulo de 45min. Tengo que ver como se hace para tomar diferentes calidades para poder elegir.

**Por ahora funciona para lo básico**
