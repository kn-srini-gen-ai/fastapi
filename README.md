# fastapi
# build fast api and automate cicd.
# uvicorn app.main:app --reload
# python -m pytest tests/
# pytest tests/ -v
# Build the Docker image 
docker build -t fastapi-app .
# run docker image locally
docker run -p 80:80 fastapi-app
# Access the FastAPI app at http://localhost:80.
# deploying to kubernetes
kubectl apply -f deployment.yaml
# check status of deployment
kubectl get pods
# Access the FastAPI app using the external IP of the LoadBalancer service:
kubectl get svc



fastapi_project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── calculator.py
│   │   │   ├── models/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── calculator.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── .github/
│   ├── workflows/
│   │   ├── build-deploy.yaml