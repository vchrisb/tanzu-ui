# tkgi-ui

A Proof of Concept for a custom TKGi UI

## Client requirements

https://github.com/int128/kubelogin

'''
# Homebrew (macOS and Linux)
brew install int128/kubelogin/kubelogin

# Krew (macOS, Linux, Windows and ARM)
kubectl krew install oidc-login

# Chocolatey (Windows)
choco install kubelogin
''' 


## TKGi preparation

Create Kubernetes Profile:

```
tkgi create-kubernetes-profile oidc.json
```

```
{
   "name": "oidc-config",
   "description": "Kubernetes profile with OIDC configuration",
   "customizations": [
      {
         "component": "kube-apiserver",
         "arguments": {
            "oidc-client-id": "tkgi",
            "oidc-issuer-url": "https://keycloak.domain.com/auth/realms/master",
            "oidc-username-claim": "email"
         }
      }
   ]
}
```