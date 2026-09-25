"""Button platform for Toto Washlet IR commands."""

from infrared_protocols.commands.pronto import ProntoCommand

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import COMMANDS, CONF_INFRARED_EMITTER_ENTITY_ID, WashletCommand
from .entity import TotoWashletEntity

PARALLEL_UPDATES = 1


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up buttons for a config entry."""
    emitter_entity_id: str = entry.data[CONF_INFRARED_EMITTER_ENTITY_ID]
    async_add_entities(
        WashletButton(entry, emitter_entity_id, command)
        for command in COMMANDS
    )


class WashletButton(TotoWashletEntity, ButtonEntity):
    """A button that sends a Washlet Pronto IR command."""

    entity_description: ButtonEntityDescription

    def __init__(
        self,
        entry: ConfigEntry,
        emitter_entity_id: str,
        command: WashletCommand,
    ) -> None:
        """Initialize the button."""
        self._command = command
        super().__init__(
            entry,
            emitter_entity_id,
            command.key,
        )
        self.entity_description = ButtonEntityDescription(
            key=command.key,
            name=command.name,
            translation_key=command.key,
        )

    async def async_press(self) -> None:
        """Send each Pronto sequence for this button."""
        for step in self._command.steps:
            for _ in range(step.times):
                await self._send_command(ProntoCommand.from_pronto_hex(step.pronto))
