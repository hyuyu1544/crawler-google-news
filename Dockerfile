



FROM python
RUN pip install requests
RUN pip install bs4

RUN pip install pandas
ADD craw_google_news.py /











 



