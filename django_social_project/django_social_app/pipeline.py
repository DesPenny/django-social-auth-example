#from social.backends.facebook import FacebookOAuth2
from django_social_app.models import UserProfile
def pic_pipeline(strategy, backend, details, response, uid, user, social, *args, **kwargs):


	if user is None:
		return

	image_url = None
    	if backend.name == "facebook":
        	image_url = "https://graph.facebook.com/{0}/picture?type=large".format(uid)
     
        	print image_url
        	
        	
        	profile = UserProfile.objects.get_or_create(user = user)[0]
    		profile.photo = image_url
    		profile.save()
    	#elif strategy.backend.name == "twitter":
        #    image_url = response['profile_image_url']

	#if strategy.backend.name == 'facebook':
	#	response = kwargs['response']
	#	print response