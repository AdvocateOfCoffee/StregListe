from django.db import models

class Vejleder(models.Model):
    class Meta:
        verbose_name_plural = 'Vejledere'
        verbose_name = 'Vejleder'
        ordering = ['nrBeers']
    name = models.CharField('navn', max_length=200)
    nickName = models.CharField('Kælenavn', max_length=200, blank=True)
    mail = models.EmailField('email')
    nrBeers = models.IntegerField('Antal bajere', default=0)

    def __str__(self):
        return self.name

    def toDict(self):
        info = {
            'name' : self.name,
            'mail' : self.mail,
            'nrBeers' : self.nrBeers
        }
        if self.nickName:
            info['name'] = self.nickName
        return info


class Indkoeb(models.Model):
    class Meta:
        verbose_name_plural = 'Indkøb'
        verbose_name = 'Indkøb'
        ordering = ['date']
    date = models.DateField('Dato')
    price = models.IntegerField('Pris')
    indkoeber = models.ForeignKey(Vejleder)
    nrBeers = models.IntegerField('Antal øl', default=1337)
    event = models.CharField('Anledning', max_length=300)
    descripton = models.CharField('Hvad har du købt?', max_length=300)
    refunded = models.BooleanField('Refunderet', default=False)

    def __str__(self):
        return str(self.date) + " : " + self.event

    def toDict(self):
        info = {
        'date' : self.date,
        'price' : self.price,
        'event' : self.event,
        'descripton' : self.descripton,
        }
        return info


class Indtag(models.Model):
    class Meta:
        verbose_name_plural = 'Indtag'
        verbose_name = 'Indtag'
        ordering = ['event']
    vejleder = models.ForeignKey(Vejleder)
    event    = models.ForeignKey(Indkoeb)
    nrBeers  = models.IntegerField('Hvor mange øl drak personen')
