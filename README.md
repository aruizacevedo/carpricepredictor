# carpricepredictor

## Testing

### Create conda environment

```
conda env create -f conda/carpricepredictor.yml

# If needed, remove previous existing environment using:
conda env remove -n carpricepredictor
```

### Development

Normally Independent end-to-end ML applications can be developed in 3 steps

- 1. Build ML Model (In our case we are going for regression model, car price prediction. You may choose other ml technics like classification, clustering etc.)

- 2. Develop REST API as Backend (we are going to use FastAPI framework in python for our case, you may choose other frameworks like Django, Flask etc.)

- 3. Develop Front End UI (we are going to use Streamlit but you can use other technologies to design frontend like HTML, CSS, etc.)


### Source:

https://medium.com/@goradbj/how-to-build-complete-end-to-end-ml-model-backend-restapi-using-fastapi-and-front-end-ui-using-22f64bf04476

### How to run:

*RestAPI Backend*
```
conda activate carpricepredictor
python api/main.py
```
Note: Swagger UI can be accessed using http://127.0.0.1:8000/docs

*Streamlit Frontend*
Using another Terminal:
```
conda activate carpricepredictor
streamlit run ui/car_price.py
```


