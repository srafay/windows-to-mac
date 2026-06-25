# mac-pc-keybindings

My macOS setup for working with **Windows / PC-style keyboard shortcuts** — Karabiner-Elements key remaps plus VS Code (and Cursor) keybindings. Drop these in on a fresh Mac to get muscle-memory back instantly.

> **New machine? Start with [SETUP.md](SETUP.md)** — a top-to-bottom walkthrough (Homebrew, Karabiner, editors, plus Rectangle + AltTab for window snapping and per-window Alt-Tab).

## Contents

```
karabiner/
  karabiner.json                              # full config — profile "Home", 35 PC-style rules
  complex_modifications/
    windows-keyboard-on-mac.json              # importable rule set: Windows keyboard on Mac
    function-keys-then-media-keys.json         # importable rule set: F-keys in apps, else media keys
vscode/
  keybindings.json                            # custom keybindings (identical for VS Code & Cursor)
  settings.json                               # editor settings (some paths are project-specific)
python/
  .vscode/                                    # F5 debug config + auto colored logging (see python/README.md)
```

## Karabiner-Elements

[Karabiner-Elements](https://karabiner-elements.pqrs.org/) remaps keys at the system level so a PC keyboard / PC muscle memory behaves the way it does on Windows.

### Install the whole config (fastest)

```bash
cp karabiner/karabiner.json ~/.config/karabiner/karabiner.json
```

Then open Karabiner-Elements → it picks up the **Home** profile automatically. (Back up any existing `~/.config/karabiner/karabiner.json` first.)

### Or import just the rule sets

```bash
cp karabiner/complex_modifications/*.json ~/.config/karabiner/assets/complex_modifications/
```

Then in Karabiner-Elements → **Complex Modifications → Add rule** → enable the ones you want.

### What the "Home" profile does (PC-style remaps)

- Swap **Command ↔ Option** (left & right) so Ctrl/Alt sit where Windows expects them
- **Ctrl+C / V / X / Z / Y** → Copy / Paste / Cut / Undo / Redo
- **Ctrl+A** Select-All, **Ctrl+S** Save, **Ctrl+N** New, **Ctrl+F** Find, **Ctrl+O** Open
- **Ctrl+B / I / U** → Bold / Italic / Underline
- **Ctrl+R / F5** → Reload, **Ctrl+T** → New Tab, **Ctrl+W** → Close Window
- **Home / End** → start / end of line (and Command+Left/Right for sentence)
- **Ctrl+Home / End**, Ctrl+Arrow word-jumps, Ctrl+Delete / Backspace
- **Alt+Tab** → app switcher (Command+Tab)
- **Alt+F4** → Quit (Command+Q), **Alt+Left/Right** → Back / Forward
- **Ctrl + / - / 0** → Browser zoom
- **PrintScreen** → screenshot to file / clipboard
- Emoji picker, Spotlight, input switch, lock screen — PC-style bindings
- Ctrl+Insert / Shift+Insert copy-paste for JIS/PC keyboards

## VS Code & Cursor

The same `keybindings.json` works for both editors.

| Editor | Path (macOS) |
| --- | --- |
| VS Code | `~/Library/Application Support/Code/User/` |
| Cursor | `~/Library/Application Support/Cursor/User/` |

```bash
# VS Code
cp vscode/keybindings.json ~/Library/Application\ Support/Code/User/keybindings.json
cp vscode/settings.json    ~/Library/Application\ Support/Code/User/settings.json

# Cursor
cp vscode/keybindings.json ~/Library/Application\ Support/Cursor/User/keybindings.json
```

### Keybinding highlights
- **Cmd+Left / Right** → navigate back / forward (history)
- **Cmd+G** → Go to line
- **Cmd+C in terminal** → send Ctrl-C (terminate) when nothing is selected, copy when text is selected
- **F2** in the file explorer → rename file
- **Shift+Enter** in terminal → send escape + return

> `settings.json` contains a few project-specific paths (e.g. Python `extraPaths`, `cfn-lint` path). Adjust or drop those on a new machine.
