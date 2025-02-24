
# WorkFlow of the Project

1. Create env
```bash
conda create -p myenv python -y
```

2. activate env
```bash
conda activate (path to myenv)
```

3. Create Requirements.txt

4. Install requirements.txt
```bash
pip install -r requirements.txt
```

5. Initilize git
```bash
git init
```

6. Initilize DVC
```bash
dvc init
```

7. Add data to DVC
```bash
dvc add data_given/winequality.csv
```

8. 
```bash
git add . && git commit -m "first commit"
git push origin main
```

9. Create params.yaml

10. create get_data.py and load_data.py to get data and add the load_data stage to dvc.yaml

11. create split_data.py to split data and add the split_data stage to dvc.yaml

12. create train_and_evaluate.py to train & evaluate model and add the train_and_evaluate stage to dvc.yaml

13. Tox
```bash
tox
tox -r  #for rebuilding use this else only tox
```

14. pytest
```bash
pytest -v
```

15. setup command
```bash
pip install -e .
```

16. build your own package
```bash
python setup.py sdist bdist_wheel
```

17. create the need webapp structure

18. Create app.py 

19. Add github action workflow

20. Create an articat folder

21. MLflow server command
```bash
mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host 127.0.0.1 -p 1234
```