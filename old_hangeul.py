import unicodedata
from .make_dic import initial_list, medial_list, final_list, ipf, jamo_list, jamo_list_all, jamo_list_key

def pua_to_ipf(ascii_pua:int):
    if 57532<=ascii_pua<=61439:
        return ipf[ascii_pua-57532]
    else:
        return ipf[ascii_pua-57788]


class OLD_TEXTS:
    def __init__(self,sent:str):
        
        self.ori=sent
        self.sen=self.__make()
        self.text=self.__get_text()

        self.jamo=[]
        self.jamo_c=[]
    def __len__(self):
        return len(self.sen)
    def __getitem__(self, item):
        return self.sen[item]
    def __str__(self):
        return self.text
    
    def __get_text(self):

        text=''
        for a in self.sen:
            if a=='_':
                text+=' '
            else:
                text+=a
        text=unicodedata.normalize('NFD', text)
        return text
        
    def get_text(self):
        return self.text
        
    def get_jamo(self, Compatibility: bool, spacing:bool):
        '''
        Convert text into jamo. Optional keyword arguments:

        Compatibility: Integrates the initial and final consonants for processing.
        spacing: Processed with consideration of spaces (represented by '_').
        '''
        text=self.ori
        jamo=text_to_jamo(text, Compatibility,spacing)
        if Compatibility:
            self.jamo_c=jamo
        else:
            self.jamo=jamo
        return jamo
    
    def __make(self):
        text=self.ori
        text_list=[]
        text_tem=''
        cnt=0
        for word in text:
            cnt+=1
            if word==' ':
                if text_tem!='':
                    text_list.append(text_tem)
                    text_tem=''

                text_list.append('_')
            else:
                try:
                    word_ord=ord(word)
                    
                    if 44032<=word_ord<=55203 or  57532<=word_ord<=61439 or 61696<=word_ord<=63086:

                        if 57532<=word_ord<=61439 or 61696<=word_ord<=63086:
                            word=PUA_TO_IPF(word_ord)

                        if text_tem!='':
                            text_list.append(text_tem)
                            text_tem=''
                        text_list.append(word)

                    elif cnt!=1 and str(word_ord) in initial_list:

                        if text_tem!='':
                            text_list.append(text_tem)
                        text_tem=word
                    elif str(word_ord) in medial_list or str(word_ord) in final_list or str(word_ord) in initial_list:
                        text_tem+=word
                        if len(text)==cnt:

                            text_list.append(text_tem)
                    else:
                        if text_tem!='':
                            text_list.append(text_tem)
                        text_list.append(word)
                except:
                    pass
            
        return text_list


def __get_unicode(word):
    word_list=[]
    if word=='_':
        return word
    else:
        one_word=unicodedata.normalize('NFD', word)
        for jamo in one_word:
            word_list.append(jamo)
        return word_list 


def change_jamo(jamo):
    
    if jamo in jamo_list_all:
        change_index=jamo_list_all.index(jamo)
        change_index=jamo_list_key[change_index]
        jamo=jamo_list[change_index]
    return jamo


def text_to_jamo(text:str, Compatibility: bool=True, spacing:bool=True):
    '''
    Convert text into jamo. Optional keyword arguments:

    Compatibility: Integrates the initial and final consonants for processing.
    spacing: Processed with consideration of spaces (represented by '_').
    '''
    text=OLD_TEXTS(text)
    text_jamo=''
    text_jamo_list=[]
    for a in text.sen:
        one=unicodedata.normalize('NFD', a)
        one_jamo_list=__get_unicode(one)
        if Compatibility and one_jamo_list !='_':
            tem_jamo_list=[]
            for one_jamo in one_jamo_list:
                tem_jamo_list.append(change_jamo(one_jamo))
            one_jamo_list=tem_jamo_list
        text_jamo_list.append(one_jamo_list)
    text.jamo= text_jamo_list

    for word in text_jamo_list:
        if word=='_':
            if spacing ==True:
                text_jamo+=word
                text_jamo+=' '
        else:
            for one_word in word:

                text_jamo+=one_word
                text_jamo+=' '
    text_jamo=text_jamo[:-1]
    return text_jamo



def hNFD(text:str):
    '''Convert pre-composed Unicode characters to decomposed Unicode characters'''
    texts=OLD_TEXTS(text)
    return texts.text

def old_hNFD(text: str):
    """
    Convert only old hangeul characters in the text to decomposed Unicode characters (NFD).
    """
    texts = OLD_TEXTS(text)
    
    converted_text = ''
    
    for item in texts.sen:
        if item == '_':
            converted_text += ' '
            continue
        
        if len(item) > 1:
            for char in item:
                char_code = ord(char)
                if 44032 <= char_code <= 55203 or 57532 <= char_code <= 61439 or 61696 <= char_code <= 63086:
                    converted_text += unicodedata.normalize('NFD', char)
                else:
                    converted_text += char
        else:
            char_code = ord(item)
            if 57532 <= char_code <= 61439 or 61696 <= char_code <= 63086:
                converted_text += unicodedata.normalize('NFD', item)
            else:
                converted_text += unicodedata.normalize('NFC', item)
    
    return converted_text

def hNFC(text:str):
    '''Convert decomposed Unicode characters to pre-composed Unicode characters''' 
    texts=OLD_TEXTS(text)
    failed=''
    tem_sen=''
    for word in range(len(texts.sen)):
        work=False
        try:
            num=ord(unicodedata.normalize('NFC', texts.sen[word]))
            
            if 44032<=num<=55203:
                tem_sen+=chr(num)
                work=True

            elif texts.sen[word]=='_':
                tem_sen+=' '
                work=True
            
        except:
            if texts.sen[word] in ipf:

                num=ipf.index(texts.sen[word])
                if num>=3908:
                    tem_sen+=chr(num+57788)
                    work=True
                else:
                    tem_sen+=chr(num+57532)
                    work=True
            
        if not work:
            tem_sen+=texts.sen[word]
            if len(unicodedata.normalize('NFC', texts.sen[word]))!=1: 
                failed+=texts.sen[word]
                failed+=' '
    if failed!='':
        print('activation failed :',failed)
    
    return tem_sen


