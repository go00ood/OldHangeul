
import os
import pickle

_ROOT=os.path.abspath(os.path.dirname(__file__))

'''Dictionary'''
#초성
with open(os.path.join(_ROOT,'data','nitial_jamo.pickle'), 'rb') as fr:
    initial_list = pickle.load(fr)

#중성 
with open(os.path.join(_ROOT,'data','medial_jamo.pickle'), 'rb') as fr:
    medial_list = pickle.load(fr)

#종성 
with open(os.path.join(_ROOT,'data','final_jamo.pickle'), 'rb') as fr:
    final_list = pickle.load(fr)

#ipf 모음
with open(os.path.join(_ROOT,'data','ipf.pickle'), 'rb') as fr:
    ipf = pickle.load(fr)

#jamo 대표 모음
with open(os.path.join(_ROOT,'data','jamo_list.pickle'), 'rb') as fr:
    jamo_list = pickle.load(fr)

#jamo 대표 제외 모음
with open(os.path.join(_ROOT,'data','jamo_list_all.pickle'), 'rb') as fr:
    jamo_list_all = pickle.load(fr)


#jamo 대표 제외 변환
with open(os.path.join(_ROOT,'data','jamo_list_key.pickle'), 'rb') as fr:
    jamo_list_key = pickle.load(fr)



