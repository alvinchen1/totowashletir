"""Common entities for Toto Washlet IR."""

from homeassistant.components.infrared import InfraredEmitterConsumerEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN


class TotoWashletEntity(InfraredEmitterConsumerEntity):
    """Base entity that sends commands through an infrared emitter."""

    _attr_has_entity_name = True

    def __init__(
        self, entry: ConfigEntry, emitter_entity_id: str, unique_id_suffix: str
    ) -> None:
        """Initialize a Toto Washlet entity."""
        self._infrared_emitter_entity_id = emitter_entity_id
        self._attr_unique_id = f"{entry.entry_id}_{unique_id_suffix}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name="Toto Washlet",
            manufacturer="TOTO",
        )
