# Minimalistic example for how to deploy a model and create a Flask webapp


## 1 - Create a Model in Watson Studio and Deploy

Notebook contains example of a deployment, using Madrid Housing Data.

## 2 - Create a Flask Webapp which uses the online model to score on data points

`IBM_CLOUD_APP` contains a Flask webapp. To run locally;

Install the requirements
```
pip3 install -r requirements.txt
```

Run the webapp
```
python3 app.py
```

The website should run on port 5000.

## 3 (Optional) - Deploy the Flask Webapp in the IBM Cloud

- Install 
https://docs.cloudfoundry.org/cf-cli/install-go-cli.html
(Use a Package Manager)

Endpoint:
https://api.ng.bluemix.net

Login and deploy the application

```
cf login --sso
cf push
```
