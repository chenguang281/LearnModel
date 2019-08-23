#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec


def searchByVector(word, max_len, first_num, top_num, word_li, model):
    """
    广度搜索和word相关的词语
    :param word: 输入词语
    :param max_len: 返回列表的最大长度±first_num
    :param first_num: 每次从topn中取出的长度
    :param top_num: topn的长度
    :param word_li: 准备返回的列表
    :param model: 词向量模型
    :return:
    """
    if len(word_li) > max_len:
        return word_li

    li = []  # 得到这一层的所有词向量,进行保存
    for w in word:
        if w in word_li:  # 如果查询过词向量,直接过.不再次查询
            continue
        word_li.append(w)
        li.extend(model.most_similar(w, topn=top_num))  # 得到一次前十个词语
    next_li = []  # 下一轮将要搜的词语
    for j in range(first_num):
        next_li.append(li[j][0])

    return searchByVector(next_li, max_len, first_num, top_num, word_li, model)

# if __name__ == '__main__':
#     model = word2vec.Word2Vec.load('train.model')  # 加载词向量模型
#     uuuuiiii = searchByVector(['说'], 50, 7, 10, [], model)
#     for i in uuuuiiii:
#         print(i)
