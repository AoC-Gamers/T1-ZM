# Base de ZoneMod para T1-ZM

| Referencia | Valor |
| --- | --- |
| Base | [SirPlease/L4D2-Competitive-Rework](https://github.com/SirPlease/L4D2-Competitive-Rework) |
| Perfil de origen | `cfg/cfgogl/zonemod` · ZoneMod **4v4 v2.9.2b** |
| Revisión comparada | [`85139a242fafc913add3862c7066880b0ed9b991`](https://github.com/SirPlease/L4D2-Competitive-Rework/tree/85139a242fafc913add3862c7066880b0ed9b991/cfg/cfgogl/zonemod) |
| Perfil de destino | `cfg/cfgogl/t1_zm` · Confogl ID `t1_zm` · T1-ZM **v2.9.2b** |

La sincronización adopta las reglas y el orden de carga de ZoneMod 4v4. Las variantes `zm3v3`, `zm2v2` y `zm1v1` se consultaron como referencia para formatos reducidos. La base de T1 es el perfil de 4v4.

## Cambios de la base en `85139a24`

El bloqueador de la rejilla de Death Toll 2 se recibe del árbol Stripper de ZoneMod instalado con la base. [Cambio de ZoneMod](https://github.com/SirPlease/L4D2-Competitive-Rework/commit/59c1b56f).

## Diferencias que se conservan

| Regla | ZoneMod 4v4 v2.9.2b | T1-ZM | Archivo de T1 |
| --- | --- | --- | --- |
| Bonus oficial del juego | Carga `optional/l4d2_hybrid_scoremod_zone.smx` y configura cuatro Cvars del bonus híbrido | Omite el plugin y sus cuatro Cvars `sm2_*` | [shared_plugins.cfg](../../cfg/cfgogl/t1_zm/shared_plugins.cfg), [shared_settings.cfg](../../cfg/cfgogl/t1_zm/shared_settings.cfg) |
| Sin cuotas de SMG y escopetas | Registra cuotas para SMG, silenciada y MP5, y para escopeta de bombeo y Chrome | Omite esas dos reglas `l4d_wlimits_add`. Conserva las reglas de Magnum y rifles de precisión y el cierre con `l4d_wlimits_lock` | [t1_zm.cfg](../../cfg/cfgogl/t1_zm/t1_zm.cfg) |
| Infectados bot habilitados | `director_allow_infected_bots 0` | `director_allow_infected_bots 1` | [shared_cvars.cfg](../../cfg/cfgogl/t1_zm/shared_cvars.cfg) |
| Lerp de 0 a 100 ms | `sm_min_lerp 0.000`, `sm_max_lerp 0.067` | `sm_min_lerp 0.000`, `sm_max_lerp 0.100`. Los valores se expresan en segundos | [shared_settings.cfg](../../cfg/cfgogl/t1_zm/shared_settings.cfg) |
| Pausa manual sin pausa automática | Carga `optional/autopause.smx` y registra `autopause_enable`, `autopause_force` y `autopause_apdebug` | Omite esa carga y sus tres Cvars. La pausa manual la aporta `optional/pause.smx` | [confogl_plugins.cfg](../../cfg/cfgogl/t1_zm/confogl_plugins.cfg), [t1_zm.cfg](../../cfg/cfgogl/t1_zm/t1_zm.cfg), [shared_plugins.cfg](../../cfg/cfgogl/t1_zm/shared_plugins.cfg) |

La identidad de T1 se refleja en las rutas de Confogl, el nombre `t1_zm.cfg` y el título de ReadyUp. ReadyUp usa el plugin estándar de ZoneMod y su política de cancelación. La sincronización también incorporó `mapinfo.txt`, la descarga con `pm_unload_plugins refresh` y la ejecución de `cvar_tracking.cfg`. La base aporta Plugin Manager, Stripper y ese CFG de validación de clientes. El [mapa de empaquetado](../../scripts/package/package-map.json) declara las llamadas a CFG externos.

Para la revisión indicada arriba se verificaron el diff de los CFG activos, las referencias a plugins en la base local y el ZIP de configuración.
