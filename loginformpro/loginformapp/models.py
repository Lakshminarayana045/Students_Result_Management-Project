from django.db import models

class studentdata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    hallno=models.IntegerField()
    marathi=models.IntegerField()
    hindi=models.IntegerField()
    english=models.IntegerField()
    math=models.IntegerField()
    science=models.IntegerField()
    socialsci=models.IntegerField()

class hscdata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    hallno=models.IntegerField()
    english=models.IntegerField()
    marathi=models.IntegerField()
    math=models.IntegerField()
    physics=models.IntegerField()
    chemistry=models.IntegerField()
    biology=models.IntegerField()

class degreedata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    hallno=models.IntegerField()
    bcomunication=models.IntegerField()
    pm=models.IntegerField()
    dbms=models.IntegerField()
    clanguage=models.IntegerField()
    bstatistics=models.IntegerField()

class btechdata(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    hallno=models.IntegerField()
    cd=models.IntegerField()
    se=models.IntegerField()
    ai=models.IntegerField()
    dcs=models.IntegerField()
    aca=models.IntegerField()
    mad=models.IntegerField()

