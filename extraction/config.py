# -*- coding: utf-8 -*-
# @Author       : NaomiatLibrary
# @Project      : KeyGAN_keyword
# @FileName     : config.py
# @Time         : Created at 2021-10-08
# @Description  :
# Copyrights (C) 2021. All Rights Reserved.

import os

dataset=os.getcwd()+"/dataset/lifehacker"
train_file_pass=dataset+"_train_text/"
train_key_file_pass=dataset+"_train_keywords/"
test_file_pass=dataset+"_test_text/"
test_key_file_pass=dataset+"_test_keywords/"
is_already_tokenized=True

max_key_len=5

