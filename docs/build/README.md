# Validación y distribución

Se requiere GNU Make y Python 3.10 o posterior.

```sh
make validate-modes
make package-modes
make release
make validate-artifact
```

`validate-modes` revisa los entrypoints de Confogl y los destinos de los
`exec` contra el [mapa de producto](../../scripts/package/package-map.json).
`package-modes` prepara `.build/package-modes/`. `release` crea
`dist/release/t1-zm-local.zip`. `validate-artifact` compara las entradas
y sus bytes con los archivos de producto. Es posible fijar el nombre con
`RELEASE_BASENAME` en ambos comandos.

El ZIP contiene `cfg/cfgogl/t1_zm/` y los documentos raíz del producto.
Copia la carpeta del modo al directorio `left4dead2/cfg/cfgogl/` y registra
`t1_zm` según el [README](../../README.md).

L4D2-Competitive-Rework aporta Confogl, ReadyUp, los plugins que se cargan
desde las configuraciones y el árbol `cfg/stripper/zonemod`. El perfil de
servidor aporta `confogl_rates.cfg` y `confogl_personalize.cfg`. Verifica su
disponibilidad y la de los plugins con los nombres exactos antes de activar el
modo. La compatibilidad del conjunto se comprueba en SRCDS cargando y
descargando `t1_zm` y verificando la aplicación y restauración de las cvars.

El ZIP local se genera sin SDK y sirve para comprobar el contenido del paquete.
La validación de proveedores y el ensayo en SRCDS son pasos de integración.

El validador comprueba el texto de la licencia GNU y el enlace CC BY-SA 3.0
en `NOTICES.md` antes de empaquetar.

## GitHub Actions

El [workflow de empaquetado](../../.github/workflows/mode-package.yml) ejecuta
`make validate-modes`, `make release` y `make validate-artifact` en un solo
job. Usa GNU Make y Python del runner. El ZIP se guarda como artefacto de la
ejecución con el nombre `t1-zm-<sha>.zip`.
