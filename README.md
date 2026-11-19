# Tier1 ZoneMod v2.9.2b

[EN] [translation](https://translate.google.com/translate?sl=es&tl=en&u=https://github.com/AoC-Gamers/t1_zm)

*T1 ZM* es una configuración competitiva para Left 4 Dead 2, cuyo objetivo es proporcionar la experiencia de zonemod para jugadores nuevos.

## Características

Tier1 ZM se basa en ZoneMod 4v4 v2.9.2b. Sus reglas propias son:

- Bonus oficial del juego.
- Sin cuotas de SMG ni de escopetas.
- Reaparición de infectados bot habilitada.
- Lerp de 0 a 100 ms.
- Pausa manual disponible. Se omite la pausa automática.

## Instalación
1. T1 ZM requiere el proyecto base [L4D2-Competitive-Rework](https://github.com/SirPlease/L4D2-Competitive-Rework). Descárgalo e instálalo primero.
2. Genera el ZIP local con `make release` y compruébalo con `make validate-artifact`.
3. Copia `cfg/cfgogl/t1_zm/` al directorio `left4dead2/cfg/cfgogl/` del servidor.
4. Registra el modo según la sección de configuración y reinicia el servidor.

### Complementos sugeridos
- [anti-friendly_fire](https://github.com/fbef0102/L4D1_2-Plugins/tree/master/anti-friendly_fire)

## Configuración

### Agregar modo de juego
Para habilitar *T1 ZM* en las votaciones del servidor, edita el archivo `addons/sourcemod/configs/matchmodes.txt` y agrega:

```plaintext
"MatchModes"
{
    "Tier1 ZM Configs"
    {
        "t1_zm"
        {
            "name" "Tier1 ZM"
        }
    }
}
```
Luego, reinicia el servidor para aplicar los cambios.

## Contribuciones
Gracias por tu interés en contribuir a *T1 ZM*, Puedes reportar problemas o sugerir mejoras a través de la [página de issues](https://github.com/AoC-Gamers/t1_zm/issues) o enviando un *pull request* en el [repositorio de GitHub](https://github.com/AoC-Gamers/t1_zm/pulls).

## Licencia
*T1 ZM* está licenciado bajo la licencia **CC-BY-SA 3.0**. Para más información, consulta el [texto completo de la licencia](http://creativecommons.org/licenses/by-sa/3.0/legalcode).

# Copyright
*Tier1 ZM* es es una adaptación de "ZoneMod".
Todos los complementos y códigos acondicionados son de sus respectivos autores.
```
- https://github.com/SirPlease/L4D2-Competitive-Rework
```
