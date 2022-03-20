#app server bootstrapping program


def init_app():
	print "starting app"

Bitbucket : git@bitbucket.org:rubakanthan_n/crm-app.git 
Github : git@github.com:Rubakanthan/crm-app.git

git remote add bitbucket git@bitbucket.org:rubakanthan_n/crm-app.git
git remote add git@github.com:Rubakanthan/crm-app.git 

git push bitbucket master
git push github master

git push bitbucket staging
git push bitbucket prestaging
 git push bitbucket feature/contact
 git push bitbucket feature/lead
 git push bitbucket feature/deal