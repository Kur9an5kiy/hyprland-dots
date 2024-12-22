import os
import subprocess
import random
from PIL import Image

def detect_user():
    global user  # Use the global variable
    if os.path.isfile("./user.md"):
        user_info = str(os.system("echo ./user.md"))
    else:
        user_info = str(os.popen("whoami").read()).strip()  # Get the username using whoami
    user = user_info

# Initialize the user variable
user = ""
detect_user()

def choose_wallpaper(user: str,
                     wallpaper_path: str = f"/home/{user}/.wallpapers/",
                     config_path: str = f"/home/{user}/.scripts/swww/config.md",
                     image_extensions: list = [".jpg", ".png", ".jpeg", ".gif"],
                     counter: int = 1) -> str:
    
    info_path = "/tmp/wallpaper_info.txt"
    os.system(f"cd {wallpaper_path}; ls . > {info_path}")

    with open(info_path, "r") as f:
        lines = f.readlines()

    availible_wallpapers = []

    for line in lines:
        line = line.strip()
        if any(line.endswith(ext) for ext in image_extensions):
            availible_wallpapers.append(line)
    availible_wallpapers.append("Random")

    if availible_wallpapers:
        for index, choice in enumerate(availible_wallpapers, start=1):
            print(f"{index} - {choice}")

        try:
            chosen_index = int(input("Choose a number >>> ")) - 1
            if chosen_index < 0 or chosen_index >= len(availible_wallpapers):
                print("Exiting...") 
                exit()
            elif chosen_index == len(availible_wallpapers) - 1:
                chosen_wallpaper = f"{wallpaper_path}{random.choice(availible_wallpapers[:-1])}"
            else:
                chosen_wallpaper = f"{wallpaper_path}{availible_wallpapers[chosen_index]}"
            with open(config_path, "w") as config:
                config.write(chosen_wallpaper)
        except ValueError:
            print("Invalid input! Exiting...")
            exit()

def set_wallpaper(user: str = user,
                  config_path: str = f"/home/{user}/.scripts/swww/config.md",
                  hyprlock_config_path: str = f"/home/{user}/.config/hypr/hyprlock.conf",
                  hyprlock_wallpaper_path: str = f"/home/{user}/.scripts/hyprlock_wallpaper/lock_wallpaper.jpeg"):
    path = ""
    lines = []
    with open(config_path, "r") as file:
        path = str(file.readline()).strip()
    subprocess.Popen(['swww-daemon'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, preexec_fn=os.setpgrp)
    os.system(f"swww img {path}; wal -i {path}; exit")

    with Image.open(path) as img:
        img.seek(0)
        img = img.convert("RGB")
        img.save(hyprlock_wallpaper_path, "JPEG")

    with open(hyprlock_config_path, "r") as file:
        lines = file.readlines()
    
    if len(lines) > 1:
        lines[1] = f"    path = {hyprlock_wallpaper_path}\n"

    with open(hyprlock_config_path, "w") as file:
        file.writelines(lines)