# Install
helm upgrade keycloak codecentric/keycloak -f values.yaml

# Configure

## User
* Create user with email address and enable "Email Verified"
* set password

## Client for UI

* Create new client with openid-connect
* set Access Type to "confidential"
* configure Redirec URL `https://<tkgi-u>/oidc/callback/`

## Client for kubelogin

* Create new client with openid-connect
* configure Redirec URL `http://localhost:8000` and `http://localhost:18000`