Default Python 기준
```
python -m venv .venv
```

Python 버전 특정 시
```
py -3.11 -m venv .venv
```

활성화
```
.venv\Scripts\activate
```

VS코드 콘솔 열 때 자동 활성화
.vscode/settings.json
```
{
    "python.terminal.activateEnvironment": true,
    "python.venvPath": "${workspaceFolder}/.venv",
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "terminal.integrated.defaultProfile.osx": "zsh",
    "terminal.integrated.defaultProfile.linux": "bash",
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "args": ["-NoExit", "-Command", "& {.\\.venv\\Scripts\\Activate.ps1}"]
        }
    },
    "terminal.integrated.profiles.osx": {
        "zsh": {
            "path": "zsh",
            "args": ["-l", "-c", "source .venv/bin/activate; zsh"]
        }
    },
    "terminal.integrated.profiles.linux": {
        "bash": {
            "path": "bash",
            "args": ["--init-file", ".venv/bin/activate"]
        }
    },
    "python.analysis.extraPaths": [
        "${workspaceFolder}/src"
    ],
    "cursorpyright.analysis.extraPaths": [
        "${workspaceFolder}/src"
    ]
}
```