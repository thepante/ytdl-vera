## Extractor Vera
Extractor que agrega la capacidad de descargar desde Vera (tv.vera.com.uy y veramas.com.uy).  

### "Parcheá"
Copiamos, pegamos esta linea en la terminal (es con sudo)
```bash
cd ~/.temp && git clone https://github.com/thepante/ytdl-vera.git && cd ./ytdl-vera && sudo sh ./install.sh
```
Con eso se abre el "instalador" (install.sh) que hace los pasos necesarios para integrar este extractor. Pero soy un queso, así que tanto el .py como el .sh son re precarios, hay maneras de hacerlo mejor claro está, pero bueno, no tengo casi experiencia con esto.

Si querés ayudar a mejorarlo, bárbaro, como ves soy alto kamikaze

## Status
- [x] Descargar videos desde tv.vera.com.uy  
- [ ] Funcionar bien con veramas.com.uy*  
- [ ] Probar extracciones de audio  
- [ ] Probar flags

> \* No escribí nada para ese dominio todavía. Así que por ahora detecta que es el extractor correspondiente para esa página (veramas), pero no puede extraer naranja. Cuando quede funcionando decentemente el dominio principal, me pongo con agregar las instrucciones para este secundario.
