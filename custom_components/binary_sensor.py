import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (
    CONF_NAME,
    CONF_HOST,
    CONF_TOKEN,
)
from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_OCCUPANCY,
    BinarySensorEntity,
)
from homeassistant.components.sensor import (PLATFORM_SCHEMA)
from miio.device import Device

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_HOST): cv.string,
    vol.Required(CONF_TOKEN): cv.string,
})


def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    # get config
    name = config.get(CONF_NAME)
    host = config.get(CONF_HOST)
    token = config.get(CONF_TOKEN)
    # init sensor
    toilet = XjxToilet(name, host, token)
    add_devices_callback([toilet])


class XjxToilet(BinarySensorEntity):
    def __init__(self, name, host, token):
        self._name = name
        self._device = Device(ip=host, token=token)
        self._state = False

    def update(self):
        try:
            seating = self._device.get_properties(properties=['seating'])
            self._state = seating[0] == 1
        except Exception:
            _LOGGER.error('Update seating state error.', exc_info=True)

    @property
    def name(self):
        """Return the name of the device if any."""
        return self._name

    @property
    def is_on(self) -> bool:
        """Return True if the switch is on based on the state machine."""
        if self._state is None:
            return False
        return self._state

    @property
    def device_class(self):
        """Return the device class of this entity."""
        return DEVICE_CLASS_OCCUPANCY


