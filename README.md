# Qtile Config

This repository contains a custom configuration for [Qtile](https://www.qtile.org/), a highly configurable, tiling window manager for X11. This configuration is tailored to my personal workflow and includes keybindings, layouts, widgets, and startup applications.

## Features

- **Layouts**:
  - MonadTall
  - Columns
  - Max
  - Floating
- **Keybindings**:
  - Launch terminal, browser, file manager
  - Switch layouts, close windows, and more
- **Widgets**:
  - Current layout
  - Group box with current screen highlight
  - Window name, clock, systray, volume, and battery status
- **Startup Applications**:
  - Nitrogen for wallpaper
  - Picom for compositor
  - Network Manager applet
  - Volume control icon

## Installation

1. **Install Qtile**:
   Follow the instructions on the [Qtile website](https://www.qtile.org/) to install Qtile on your system.

2. **Clone this repository**:
   Clone this repository to your home directory or any directory where you store your configuration files.

   ```bash
   git clone https://github.com/your-username/qtile-config.git ~/.config/qtile

Apply the configuration: After cloning, restart Qtile or run the following command to apply the configuration
-qtile cmd-obj -o cmd -f restart
