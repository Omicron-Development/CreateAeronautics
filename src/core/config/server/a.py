from pathlib import Path
import shutil
import fnmatch

CLIENT_FILE_NAMES = {
    "chat_heads.json5",
    "continuity.json",
    "entity_model_features.json",
    "entity_texture_features.json",
    "etf_warnings.json",
    "hiddenrecipebook.json5",
    "immediatelyfast.json",
    "iris.properties",
    "iris-excluded.json",
    "MouseTweaks.cfg",
    "notenoughanimations.json",
    "resourcepackoverrides.json",
    "serverbrowser.conf",
    "skinlayers.json",
    "sodium-fingerprint.json",
    "sodium-mixins.properties",
    "sodium-options.json",
    "xaerohud.txt",
    "xaeropatreon.txt",
}

CLIENT_DIR_NAMES = {
    "drippyloadingscreen",
    "euphoria_patcher",
    "fancymenu",
    "jade",
    "jei",
    "konkrete",
    "NoChatReports",
    "pickupnotifier",
    "simple-rpc",
    "xaero",
}

CLIENT_PATTERNS = [
    "*-client.toml",
    "*-client.snbt",
    "*.client.toml",
    "*-client.json",
    "*-client.json5",
]


def is_client_file(path: Path) -> bool:
    if path.name.endswith(".bak"):
        return False

    if path.name in CLIENT_FILE_NAMES:
        return True

    return any(fnmatch.fnmatch(path.name, pattern) for pattern in CLIENT_PATTERNS)


def move_safe(src: Path, dst: Path):
    if dst.exists():
        if src.is_dir():
            shutil.rmtree(dst)
        else:
            dst.unlink()

    shutil.move(str(src), str(dst))


current_dir = Path.cwd()
client_dir = current_dir / "client"
client_dir.mkdir(exist_ok=True)

moved = 0

for item in current_dir.iterdir():
    if item.name == "client":
        continue

    if item.is_dir() and item.name in CLIENT_DIR_NAMES:
        move_safe(item, client_dir / item.name)
        moved += 1

    elif item.is_file() and is_client_file(item):
        move_safe(item, client_dir / item.name)
        moved += 1

print(f"Готово. Перемещено клиентских конфигов: {moved}")