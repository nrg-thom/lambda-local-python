## Run example

### 1 Install `lambda-local-python`

```bash
pip install lambda-local-python
```

### 2 Run lambda locally

```bash
# change working directory to examples/simple-lambda
ENV=dev lambda-local-python -f main.handler -e "{\"data\": [{\"name\": \"exampe1\", \"value\": 10}, {\"name\": \"exampe2\", \"value\": 11}]}"
```
