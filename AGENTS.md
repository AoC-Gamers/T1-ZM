# Trabajo en T1-ZM

Consulta [el índice de documentación](docs/README.md) y
[la guía de distribución](docs/build/README.md) antes de editar.

- Conserva el identificador `t1_zm`, las rutas de Confogl y el orden de carga.
- Declara los archivos instalables en `scripts/package/package-map.json`.
  Usa el Makefile raíz para validar y empaquetar en `.build/` y `dist/`.
- Mantén los proveedores de juego como prerrequisitos y conserva autoría y licencias.
- Distingue la validación offline de la aceptación en SRCDS.
  Los cambios remotos y el despliegue requieren autorización.

## Actualizar la base de ZoneMod

1. Usa la versión y el SHA de la [referencia técnica](docs/mode/zonemod-baseline.md).
   Compara esa revisión con la nueva en el perfil 4v4. Sigue los `exec` y
   revisa los cambios en los proveedores, incluida la configuración de
   clientes y Stripper.
2. Aplica los cambios a `t1_zm` y conserva las diferencias de diseño
   de la referencia técnica. Compara los CFG activos y el orden de carga
   con la nueva base. Actualiza el mapa de empaquetado si cambian los archivos
   instalables o los destinos externos de `exec`.
3. Ejecuta `make validate-modes`, `make release` y `make validate-artifact`.
   Registra por separado la prueba de carga, inicio y descarga en SRCDS.
   Actualiza la revisión de origen en la referencia técnica y usa la misma
   versión de ZoneMod en las cabeceras de los CFG, el título de ReadyUp y el
   README. Revisa el changelog. Mantén la atribución a ZoneMod en
   `NOTICES.md` independiente de la versión.
