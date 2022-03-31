# restapi-with-drf

## Add default data
```
python manage.py shell
```
```
Item.objects.create(name="Item #1")
Item.objects.create(name="Item #2")
Item.objects.create(name="Item #3")
```

## Get data
```
python manage.py runserver
```
```
curl 127.0.0.1:8000
```

## Add data
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "hogefuga"}' 127.0.0.1:8000/add/
```