# python

VS Code debug setup for Python — one-keypress (F5) debugging of the current file with colored logging, no boilerplate.

## Contents

```
.vscode/
  launch.json          # debugpy "launch current file" config (sets AWS profile + PYTHONPATH)
  sitecustomize.py     # auto-run by Python on startup; imports logs_for_local
  logs_for_local.py    # configures root logger (colored output if `coloredlogs` is installed)
```

## How it works

1. `launch.json` adds `.vscode` to `PYTHONPATH` for the debug session.
2. Python automatically executes any `sitecustomize.py` it finds on the path at interpreter startup.
3. That `sitecustomize.py` imports `logs_for_local.py`, which attaches a `StreamHandler` to the root logger — so `logging.info(...)` shows up in the Debug Console with timestamps, filename:lineno, and level. Install [`coloredlogs`](https://pypi.org/project/coloredlogs/) for colored output.

The result: hit **F5** on any `.py` file and you get readable, leveled logs immediately — no `logging.basicConfig` needed in your code.

## Install

Copy `.vscode/` into the root of a Python project:

```bash
cp -r .vscode /path/to/your/project/
```

Adjust the env block in `launch.json` (`AWS_PROFILE`, `AWS_DEFAULT_REGION`) to taste — those are project-specific.
