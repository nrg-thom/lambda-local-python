## Run example

### 1 Install `lambda-local-python`

#### 1.1 Install from source

```bash
git clone https://github.com/willwhy/lambda-local-python.git
cd lambda-local-python
pip install -e .
```

#### 1.2 Install using pip

Coming later..

### 2 Run lambda locally

```bash
# change working directory to examples/simple-lambda
ENV=dev lambda-local-python -f main.handler -e "{\"data\": [{\"name\": \"exampe1\", \"value\": 10}, {\"name\": \"exampe2\", \"value\": 11}]}"
```
