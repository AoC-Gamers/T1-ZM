# Trabajo en T1-ZM

Consulta [el índice de documentación](docs/README.md) y
[la guía de distribución](docs/build/README.md) antes de editar.

- Conserva el identificador `t1_zm`, las rutas de Confogl y el orden de carga.
- Declara los archivos instalables en `scripts/package/package-map.json`.
  Usa el Makefile raíz para validar y empaquetar en `.build/` y `dist/`.
- Mantén los proveedores de juego como prerrequisitos y conserva autoría y licencias.
- Distingue la validación offline de la aceptación en SRCDS.
  Los cambios remotos y el despliegue requieren autorización.
