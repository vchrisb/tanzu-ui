# Ingress

## deploy

'kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.40.2/deploy/static/provider/cloud/deploy.yaml`

## create default wildcard ingress cert
'''
lego -d "apps.domain.com" -d "*.apps.domain.com" -m admin@domain.com --key-type rsa2048 --dns manual --path ~/.lego run
kubectl create secret tls default-ingress-secret --cert=cert.crt --key=cert.key
''' 
