import newspaper
cnn_paper = newspaper.build('https://indianexpress.com/')
for article in cnn_paper.articles:
    print(article.url)