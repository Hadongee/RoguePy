import json

class Settings:
    def __init__(self, screen_width: int, screen_height: int, tilesheet: str, tilesheet_width: int, tilesheet_height: int, title: str, vsync: bool, max_health: int, max_energy: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.tilesheet = tilesheet
        self.tilesheet_width = tilesheet_width
        self.tilesheet_height = tilesheet_height
        self.title = title
        self.vsync = vsync
        self.max_health = max_health
        self.max_energy = max_energy

class SettingsHandler:
    def __init__ (self):
        self.settings = None
        self.load_settings()
    
    def load_settings (self):
        f = open("data/settings.json",)
        data = json.load(f)
        self.settings = Settings(
            data["screen_width"],
            data["screen_height"],
            data["tilesheet"],
            data["tilesheet_width"],
            data["tilesheet_height"],
            data["title"],
            data["vsync"],
            data["max_health"],
            data["max_energy"]
        )


