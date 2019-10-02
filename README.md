# crawler-google-news

download craw_google_news.py and run


or 


run with docker (two methods)

1.pull from docker hub:

	docker pull hyuyu1544/pycraw
	docker run -it hyuyu1544/pycraw bash	
#:

	python pythoncode/craw_google_news.py
	cat google_news.csv

2.build with dockerfile:

create [file] then download Dockerfile and craw_google_news.py
	
	cd [file]
	docker build -t pycraw . --no-cache
	docker run -it pycraw bash
#:	

	python craw_google_news.py
	cat google_news.csv
