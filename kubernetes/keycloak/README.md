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



### Azure Federation

#### Azure

* create new Enterprise Application in Azure Active Directory
* disable `User assignment required` in Application Properties
* Enable `SAML` in Single Sign-on

Identifier: https://keycloak.domain.com/auth/realms/master
Reply URL: https://keycloak.domain.com/auth/realms/master/broker/<IDP alias>/endpoint

#### Keycloak

* create new IDP
* Alias: `azure`
* import App Federation Metadata Url
* enable `Trust email`
* Create Mapper for email:
  * Mapper Type: `Attribute Importer`
  * Attribute Name: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name`
  * User Attribute Name: `email`
* Create Mapper for Last Name:
  * Mapper Type: `Attribute Importer`
  * Attribute Name: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname`
  * User Attribute Name: `lastName`
* Create Mapper for First Name:
  * Mapper Type: `Attribute Importer`
  * Attribute Name: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname`
  * User Attribute Name: `firstName`