Marjorie
========

Just a little data dump that tkes whatever json you throw at it and stores it.

Use Case
--------

If you need a place to store some form results and don't want to expose your participants to Google Forms.

How To
------

```
docker run -p 5000:5000 -v /your/data/dump/dir:/data doublemalt/marjorie
```
