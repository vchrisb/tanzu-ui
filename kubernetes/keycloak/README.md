# Install
helm upgrade keycloak codecentric/keycloak -f values.yaml

# Configure

## User
* Create user with email address and enable "Email Verified"
* set password

## Client

* Create new client with openid-connect
* set Access Type to "confidential"
* configure Redirec URL `http://127.0.0.1:8000/oidc/callback/`