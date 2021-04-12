from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
import requests
from .models import usertwitx,friendtweet
from django.db.models import Count


# Home View
class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError

from social_django.models import UserSocialAuth
import tweepy
import json

class SettingsView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user = request.user

        try:
            twitter_login = user.social_auth.get(provider='twitter')
            print(twitter_login.access_token)
            userid=twitter_login.access_token['user_id']
            screen_name=twitter_login.access_token['screen_name']
            auth = tweepy.OAuthHandler('okwoO0j3AxHqTTgvxH0Imb1OD','1iZgQDRs7IPv4HsUh36iHQuyBp3Ayn6g2l6iI83E8Hiu75NL3B')
            auth.set_access_token('1129150375720677377-ulmKDn7cD9YkbfSBykS5C2cBo4RHYp','f99siM42vcTDueq4treAVkquuJ80ptnP1li2Llr72lBVQ')
            api=tweepy.API(auth) 
            tweets = api.user_timeline(screen_name=screen_name)
       #    print(tweets.text)

            friendl=api.friends(screen_name)
          #  print(friendl.status)

            listf=[]
            for friend in friendl:
                listf.append(friend.screen_name)


    #        print(listf)


            try:
                response = requests.get('https://sleepy-ridge-86379.herokuapp.com/results?bm='+screen_name)
                parsed = response.json()    #api for getting tweets
            except ValueError:
                parsed={}
                print("json error")

            

    


            
            
 
            ff=api.get_user(userid)
            profiler_photo=ff.profile_image_url_https

            uu=profiler_photo.replace('_normal','')
            print(ff.name)




            for i in range(0,len(parsed)):                #looping through dict
                user_c=parsed[i]["created_at"]
                desc=parsed[i]["text"]
                url="https://twitter.com/geeksforgeeks/status/"+str(parsed[i]["id_str"])

                try:                                                          #for  catching integrity errros
                    tw_inf=usertwitx(user_name=screen_name,tweet_id=parsed[i]["id_str"],user_c=user_c,desc=desc,url_p=url)
                    tw_inf.save()

                except IntegrityError as e:
                    print("duplicacy")
                    break


                    
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")




            for i in listf:

                try:
                    response2 = requests.get('https://sleepy-ridge-86379.herokuapp.com/results?bm='+i)
                    parsed2 = response2.json()    #api for getting tweets
                except ValueError:
                    parsed2={}
                    continue
                    print("json error")

                screen_namef=parsed2[0]["user"]["screen_name"]

                for i in range(0,len(parsed2)):
                    '''
                    hasht=parsed2[i]["entities"]["hashtags"]
                    tags=[]
                    if hasht:
                        tags = [li["text"] for li in hasht]
                    print(tags)
                    '''    
                    desc2=parsed2[i]["text"]
                    url2="https://twitter.com/geeksforgeeks/status/"+str(parsed2[i]["id_str"])

                    try:                                                          #for  catching integrity errros
                        tw_inf=friendtweet(friend_name=screen_namef,tweetf_id=parsed2[i]["id_str"],desc2=desc2,url_p2=url2)
                        tw_inf.save()

                    except IntegrityError as e:
                        print("duplicacy")
                        break 
                    
                                




 


            
                


            





    

             
  #          print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
   #         tmp=[] 


  
      
    #        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
    #       for j in tweets_for_csv:
    #            tmp.append(j) 
                              
    #        print(tmp)

            


        except UserSocialAuth.DoesNotExist:
            twitter_login = None


        can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

        return render(request, 'core/settings.html', {

            'twitter_login': twitter_login,
            'profiler': ff,
            'uu':uu,
            'parsed': parsed,
            

            'can_disconnect': can_disconnect
        })




def db_store_view(request):               #database queries for rendering to frontend
    all_tweets=usertwitx.objects.all
 #  print(type(all_tweets))
    a=usertwitx.objects.values_list('user_name').annotate(user_count=Count('user_name')).order_by('-user_count')
    size_m=len(a)
    total_tweets=0
    top=a[0][0]
    for p in a:
        total_tweets+=p[1]                 #total no of tweets saved

    print(total_tweets)






    friend_tweets=friendtweet.objects.all       #db2 of following
    b=friendtweet.objects.values_list('friend_name').annotate(user2_count=Count('friend_name')).order_by('-user2_count')
    print(b)
    size_f=len(b)
    print(size_f)

    total_ftweets=0

    topf=b[0][0]

    for q in b:
        total_ftweets+=q[1] 

    print(total_ftweets)  





    return render(request,'db.html',{'all':all_tweets,'top':top,'total_tweets':total_tweets, 'total_master':size_m,'friend_tweets':friend_tweets,'size_f':size_f,'total_ftweets':total_ftweets,'topf':topf})












'''

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})
'''
