## Create Storage Class if necessary

```
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: thin-disk
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/vsphere-volume
```

### Postgresql

```
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install tanzu-postgresql bitnami/postgresql --set postgresqlDatabase=tanzu-ui
kubectl apply -k ./
# apply django database migration
kubectl exec -it tanzu-ui-6bcc45f7c8-md8zq -- python manage.py migrate
```

`Pks Uaa Management Admin Client` can be used for `TKGI_CLIENT_SECRET`