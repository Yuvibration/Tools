import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
import requests
import imageio
from wordcloud import WordCloud
from bs4 import BeautifulSoup
#豆瓣图书评论抓取，并得出其关键词
def fetch_douban_comments():#评论抓取，写入subject文件
    r = requests.get('https://book.douban.com/subject/1829226/comments/')
    soup = BeautifulSoup(r.text, 'lxml')
    pattern = soup.find_all('p', 'comment-content')
    with open('subjects.txt', 'w', encoding='utf-8') as f:
        for s in pattern:
            f.write(s.string)
def extract_words():
    with open('subjects.txt','r',encoding='utf-8') as f:
        comment_subjects = f.readlines()
    #加载stopword
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    commentlist = []
    for subject in comment_subjects:
        if subject.isspace():continue
        # segment words line by line
        word_list = pseg.cut(subject)#分词
        for word, flag in word_list:
            if not word in stop_words and flag == 'n':
                commentlist.append(word)
    d = path.dirname(__file__)
    mask_image = imageio.imread(path.join(d, "mickey.png"))
    content = ' '.join(commentlist)
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey",  mask=mask_image, max_words=40).generate(content)
    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
if __name__ == "__main__":
    fetch_douban_comments()
    extract_words()