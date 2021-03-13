import pandas as pd
from nltk.tokenize import word_tokenize

data = pd.read_csv('./Market_Basket_Optimisation.csv', header=None)
# print(data.values)

# 将数据存放到transactions中
transactions = []
# 存储字典key:vale
item_count = {}

for i in range(data.shape[0]):
    temp = []
    for j in range(data.shape[1]):
        item = str(data.values[i, j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transactions.append(temp)
# print('good transactions_list:',transactions)


from wordcloud import WordCloud


# 去掉停用词，即比较经常使用的词（虚词：你好，我的）
def remove_stop_words(f):
    global del_words_list
    stop_words =del_words_list                                           # 添加想删除的词
    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


def create_word_cloud(f,filename):
    f = remove_stop_words(f)
    cut_text = word_tokenize(f)
    cut_text = "     ".join(cut_text)
    # print('-'*10,cut_text)
    wc = WordCloud(
        max_words=100,
        width=2000,
        height=1200,
    )
    wordcloud = wc.generate(cut_text)
    wordcloud.to_file(filename)


# print(transactions)

# 生成词云
all_word = ' '.join('%s' % item for item in transactions)
# print('good string',all_word)
# print(transactions)
del_words_list=[]
create_word_cloud(all_word,"wordcloud.jpg")

# Top10的商品有哪些
print(sorted(item_count.items(), key=lambda x: x[1], reverse=True)[:10])
#


###################### 重新构造dataFrame,显示前X词云#######################
top_x=5                                                                         # 设置前x词汇
data_list=sorted(item_count.items(), key=lambda x: x[1], reverse=True)[:top_x]
print('*'*20,data_list)
dict_word={}
for i in range(top_x):
    a=[]
    for j in range(int(data_list[0][1])):
        if j>int(data_list[i][1]):
            a.append('nan')
        else:

            a.append(data_list[i][0])
    dict_word[i]=a

print(dict_word)
df_word=pd.DataFrame.from_dict(dict_word)
print(df_word)

# 将数据存放到transactions中
transactions = []
# 存储字典key:vale
item_count = {}

for i in range(df_word.shape[0]):
    temp = []
    for j in range(df_word.shape[1]):
        item = str(df_word.values[i, j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transactions.append(temp)

print(transactions)


# 生成词云
all_word = ' '.join('%s' % item for item in transactions)
# print('good string',all_word)
# print(transactions)
del_words_list=[]
create_word_cloud(all_word,"wordcloud_topx.jpg")

'''
陈博士：
为啥还显示了water mineral 词组？
'''
