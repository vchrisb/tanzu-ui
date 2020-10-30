### Postgresql

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install tkgi-postgresql bitnami/postgresql --set postgresqlDatabase=tkgi-ui
kubectl apply -k ./
kubectl exec -it tkgi-ui-6bcc45f7c8-md8zq -- python manage.py migrate
```