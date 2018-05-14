# Minimalistic example for how to deploy a model and create a Flask webapp

- Notebook contains example of a deployment.
- `IBM_CLOUD_APP` contains a cloud foundery app which can be deployed in the IBM Cloud

## Deploy a flask app on the IBM Cloud (TAFKAB)

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
