from django.db import models

# Create your models here.

class usertwitx(models.Model):    #for user
  user_id=models.AutoField
  user_name=models.CharField(max_length=50)
  tweet_id=models.CharField(max_length=100,unique=True)
  user_c=models.CharField(max_length=50)
  desc= models.TextField(max_length=500)
  url_p=models.TextField(max_length=500)



class friendtweet(models.Model):  #for user following accounts
  friend_id=models.AutoField
  friend_name=models.CharField(max_length=50)
  tweetf_id=models.CharField(max_length=100,unique=True)
  desc2= models.TextField(max_length=500)
  url_p2=models.TextField(max_length=500)
  




    
