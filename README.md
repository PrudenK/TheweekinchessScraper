## TheweekinchessScraper

Proyecto destinado a descargar las partidas subidas en `https://theweekinchess.com/twic`: 


### Descomprimir todos los zips en `descargas`:

```bash
  cd descargas
  for file in *.zip; do unzip -o "$file" -d ./; done
```

### Borrar todos los zip en `descargas`:

```bash
  cd descargas
  rm *.zip
```

### Comando para `cron`:

```
  0 */2 * * 2 cd /home/pruden/PycharmProjects/TheweekinchessScraper && /home/pruden/PycharmProjects/TheweekinchessScraper/.venv/bin/python3 SacarDatosPorSemana.py
```