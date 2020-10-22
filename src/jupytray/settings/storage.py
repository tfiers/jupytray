import sys
from pathlib import Path

from PyQt5.QtCore import QSettings


def create_settings_property(key: str, default_value):
    def getter(self: "Settings"):
        return self.settings_store.value(key, default_value, type(default_value))

    def setter(self: "Settings", value):
        self.settings_store.setValue(key, value)

    return property(getter, setter)


class Settings:
    def __init__(self):
        self.settings_store = QSettings("tfiers", "Jupytray")

    auto_run_at_boot = create_settings_property("AUTO_RUN_AT_BOOT", True)

    jupyter_root_dir = create_settings_property(
        "JUPYTER_ROOT_DIR",
        str(Path(sys.executable).drive) + "/",  # E.g. "C:/"
    )

    open_browser = create_settings_property("OPEN_BROWSER", True)


settings = Settings()