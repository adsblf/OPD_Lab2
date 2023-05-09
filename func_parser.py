from icrawler.builtin import GoogleImageCrawler
import random
def parser():
    string = ['Стэтэм', 'Чак Норис', 'Сталоне', 'Рокки', 'Деньги', 'Спорт', 'Учеба', 'Бизнес', 'Сталин', 'Ленин',
              'Бредд Пит', 'МакКонахи', 'Генри Форд', 'Джим Керри', 'Успех', ' ', ' ', ' ', 'музыка', 'Медитация',
              'диета', 'здоровый образ жизни', 'победа', 'бокс', 'саморазвитие', 'личностный рост', 'инвестиции']
    google_crawler = GoogleImageCrawler(storage={'root_dir': 'C:/Users/main/Desktop/OPD_2/pic'})
    google_crawler.crawl(keyword = "Мотивирующая цитата " + string[random.randint(0, len(string))] + " на картинке",
                     max_num=10,
                     file_idx_offset='auto')

def call_parser():
    for i in range(5):
        parser()