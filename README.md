
### pre requirement
python version > 3.6
pip3
```
apt-get install python3-pip
```

### setting venv
```
apt-get install python3-venv
python3 -m venv env
source env/bin/activate
```


### how to install python library
```
python3 -m pip install fastapi uvicorn
python3 -m pip install pyjwt==1.7.1
```

### how to execute
```
uvicorn main:app --reload
```

### how to test
```
http://127.0.0.1:8000/
http://127.0.0.1:8000/docs

```

### k8s debugging using telepresence
```
kubectl apply -f ./ops
```
```
telepresence --context {YOUR K8S} --namespace {YOUR NAMESPACE} --swap-deployment fastapi-app1 --expose 8000 --run bash
```
