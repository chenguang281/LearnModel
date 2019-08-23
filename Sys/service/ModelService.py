#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gensim.models import word2vec


def searchByVector(word, threshold, word_li):
    """
    根据词向量,查找词的相关词语
    :param word: 词语 str
    :param threshold: 阈值
    :param word_li: 得到的词语集合
    :return:
    """

    model = word2vec.Word2Vec.load('train.model')  # 加载词向量模型

    li = model.most_similar(word, topn=10)  # 得到一次前十个词语

    re_word = word_li
    for i in li:
        if i[1] > threshold:
            re_word.add
    return re_word
