from libqtile import bar, layout, widget
from libqtile.config import Key, Group, Screen, Drag, Click
from libqtile.command import lazy
from libqtile.lazy import lazy
import os
import subprocess

mod = "mod4"  # Super key
terminal = "alacritty"
browser = "firefox"
file_manager = "thunar"

keys = [
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "f", lazy.spawn(file_manager), desc="Launch file manager"),
    Key([mod], "Tab", lazy.next_layout(), desc="Switch layout"),
    Key([mod], "w", lazy.window.kill(), desc="Close window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),
    Key([mod], "p", lazy.spawn("flameshot gui"), desc="Take a screenshot"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.append(Key([mod], i.name, lazy.group[i.name].toscreen()))
    keys.append(Key([mod, "shift"], i.name, lazy.window.togroup(i.name)))

layouts = [
    layout.MonadTall(margin=12, border_width=4, border_focus="#ff79c6", border_normal="#282a36"),
    layout.Columns(border_focus="#ff5555"),
    layout.Max(),
    layout.Floating()
]

widget_defaults = dict(font="FiraCode Nerd Font", fontsize=14, padding=5)

screens = [
    Screen(
        bottom=bar.Bar([
            widget.CurrentLayoutIcon(scale=0.8),
            widget.GroupBox(highlight_method='line', this_current_screen_border="#ff79c6"),
            widget.Prompt(),
            widget.WindowName(foreground="#50fa7b"),
            widget.Clock(format="%A, %B %d - %H:%M", foreground="#8be9fd"),
            widget.Systray(),
            widget.Volume(fmt="Vol: {}", foreground="#ff5555"),
            widget.Battery(format="Battery: {percent:2.0%}", foreground="#f1fa8c"),
        ], 28, background="#282a36"),
    )
]

defaults = dict(auto_fullscreen=True, focus_on_window_activation="smart")

from libqtile import hook

def start_once():
    subprocess.Popen(["nitrogen", "--restore"])  # Set wallpaper
    subprocess.Popen(["picom", "--config", "~/.config/picom.conf"])  # Compositor
    subprocess.Popen(["nm-applet"])  # Network Manager
    subprocess.Popen(["volumeicon"])  # Volume control icon

hook.subscribe.startup_once(start_once)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

if __name__ in ["config", "__main__"]:
    from libqtile import qtile
