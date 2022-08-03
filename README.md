# shop-music-api

Shop Music API usign python FastAPI - UCAB Project.

 To run the project first you need to clone the repository.

 ```python
git clone https://github.com/CodeIota/shop-music-api.git
```

After clone the repository it's necesary create a virtual env.

 ```python
 python -m venv venv
```

Run the virtual env.

 ```python
source venv/bin/activate
```

Install the necesary packages to run the project.

 ```python
pip install -r requirements.txt
```

Run the backend project.

 ```python
uvicorn main:app --reload
```

Go to the browser and check the endpoins using Swiger interface

 ```python
localhost:8080/docs
```

To run the tests.

 ```python
pytest -v
```

And that's it!
