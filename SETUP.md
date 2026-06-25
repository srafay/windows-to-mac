# Setup — make a fresh Mac feel like Windows

Run top to bottom on a new machine. Steps 1–4 restore exactly what's in this repo; Step 5 fills the two gaps Windows users miss most (window snapping + per-window Alt-Tab); Step 6 is optional macOS tweaks.

```bash
git clone https://github.com/srafay/windows-to-mac.git
cd windows-to-mac
```

## 1. Install Homebrew (if needed)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## 2. Karabiner-Elements (the heart of the Windows key layer)

```bash
brew install --cask karabiner-elements
```

Then load the config (back up any existing one first):

```bash
mkdir -p ~/.config/karabiner
cp -n ~/.config/karabiner/karabiner.json ~/.config/karabiner/karabiner.json.bak 2>/dev/null || true
cp karabiner/karabiner.json ~/.config/karabiner/karabiner.json
```

Open Karabiner-Elements once and grant Input Monitoring permission — it auto-selects the **Home** profile. Prefer cherry-picking rules instead? Copy `karabiner/complex_modifications/*.json` into `~/.config/karabiner/assets/complex_modifications/` and enable them under **Complex Modifications → Add rule**.

## 3. VS Code & Cursor keybindings

```bash
# VS Code
cp vscode/keybindings.json "$HOME/Library/Application Support/Code/User/keybindings.json"
cp vscode/settings.json    "$HOME/Library/Application Support/Code/User/settings.json"

# Cursor (same keybindings)
cp vscode/keybindings.json "$HOME/Library/Application Support/Cursor/User/keybindings.json"
```

> `settings.json` has a few project-specific paths (Python `extraPaths`, `cfn-lint`) — edit or drop them.

## 4. Python F5 debug config (per project)

Copy into the root of any Python project for one-keypress debugging with colored logs:

```bash
cp -r python/.vscode /path/to/your/project/
```

See `python/README.md` for how it works.

## 5. The two gaps (not in this repo — nothing to capture, just install fresh)

These weren't installed on the old machine but complete the Windows experience:

```bash
# Aero Snap — Win+Arrow window tiling (left/right/maximize)
brew install --cask rectangle

# True per-window Alt-Tab with thumbnails (macOS Cmd+Tab only switches apps)
brew install --cask alt-tab
```

- **Rectangle** → open it, enable "Launch on login". macOS Sequoia has built-in tiling, but Rectangle is closer to Windows.
- **AltTab** → set the trigger to your liking. Note the Karabiner rule already maps physical `Alt+Tab`; AltTab makes it switch *windows* instead of *apps*.

## 6. Optional macOS system tweaks

These match (or extend) the old machine's settings. Run only the ones you want, then log out/in:

```bash
# Dock auto-hide (was on)
defaults write com.apple.dock autohide -bool true && killall Dock

# F1–F12 behave as standard function keys (Karabiner also handles this)
defaults write -g com.apple.keyboard.fnState -bool true

# --- Windows extras you may want (were NOT set on the old machine) ---
# Faster key repeat (Windows-like). Lower = faster.
# defaults write -g KeyRepeat -int 2
# defaults write -g InitialKeyRepeat -int 15

# Reverse scroll direction to Windows-style (old machine kept mac-natural)
# defaults write -g com.apple.swipescrolldirection -bool false

# Show all file extensions in Finder
# defaults write -g AppleShowAllExtensions -bool true && killall Finder
```

Done — clone, run, and the Mac feels like home.
