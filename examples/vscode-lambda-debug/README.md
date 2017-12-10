# Debug in vscode (Visual Studio Code)

## Install `lambda-local-python`

```bash
pip install lambda-local-python
```

## Usage

- open `vscode-lambda-debug` as a project in vscode (root directory)
- set `python.pythonPath` and `python.lambdaLocalPythonPath` in your vscode settings, e.g.
```json
{
    "python.pythonPath": "/path/to/.conda/envs/py27/bin/python",
    "python.lambdaLocalPythonPath": "/path/to/.conda/envs/py27/bin/lambda-local-python",
}
```
- change settings to what you want in `.vscode/launch.json`
