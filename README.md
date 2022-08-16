## How the API works
Sending a post request to the `/predict_iris` URI with the desired iris 
parameters in json format yields the prediction.
### Iris Parameters
`sepal_length_in_cm`, `sepal_width_in_cm`, `petal_length_in_cm`, 
`petal_width_in_cm`

## How to test

#### 1.Build docker container
From the root folder, build the image  
`docker build --tag python-iris .`
#### 2.Run container
Run the detached container exposing the port 5000  
`docker run -d -p 5000:5000 python-iris`
#### 3.Send a post request to the exposed port

#### Example
    import requests
    local_URI = f"http://127.0.0.1:5000/predict_iris"
    payload = {
        "sepal_length_in_cm": 6.4,
        "sepal_width_in_cm": 3.2,
        "petal_length_in_cm": 5.3,
        "petal_width_in_cm": 2.3,
    }
    response = requests.post(local_URI, json=payload)
    print('response from server:', response.text)
Running the above code results in  
    
    response from server: "virginica"