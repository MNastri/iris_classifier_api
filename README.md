### How the API works
Sending a post request to the `/predict_iris` URI with the desired iris 
parameters in json format yields the prediction.
### Iris Parameters
`sepal_length_in_cm`, `sepal_width_in_cm`, `petal_length_in_cm`, 
`petal_width_in_cm`
### Build docker container
From the root folder, build the image  
`docker build --tag python-iris .`
### Run container
Run the detached container exposing the port 5000  
`docker run -d -p 5000:5000 python-iris`
