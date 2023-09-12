# LittleLemon
Repo for the Meta Back-End Developer Capstone

Please test the following endpoints:

Menu items GET POST
```
/restaurant/menu/
```

Menu item  GET PUT DELETE

```
/restaurant/menu/<int:pk>/
```

Table bookings GET POST PUT DELETE

```
/restaurant/booking/tables/
```

Authorization POST

```
/restaurant/api-token-auth/
```

---------------------------------------

Note that there is no `/api/` prefix to any of these.

In addition, the normal djoser urls are present at
```
/auth/
```

The static images can be demonstrated at the index, http://127.0.0.1:8000/