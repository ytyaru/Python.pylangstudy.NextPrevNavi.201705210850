#!python3
#encoding: utf-8
class HtmlWrapper(object):
    def __init__(self):
        pass

    """
    パンくずリストのHTML文字列を生成する。
    @param {str} htmlはHTML文字列。
    @param {str} element_nameはhtmlをラップしたいHTML要素名。
    @param {str} id_はHTML属性idの値。Pythonの予約語と重複せぬようアンダーバーを付与した。
    @param {str} class_はHTML属性classの値。Pythonの予約語と重複せぬようアンダーバーを付与した。
    @param {dict} attributesはHTML属性のキー名と値を入れた辞書。id_,class_が指定されている時にid="",class=""が指定されるとid_,class_を優先する。
    """
    def Wrap(self, inner_html, element_name, id_=None, class_=None, **attributes):
        attr = self.CreateAttributes(id_, class_, **attributes)
        html = self.__CreateStartElement(element_name, attr)
        html += inner_html
        html += '</{0}>'.format(element_name)
        return html
        
    """
    HTMLの属性文字列を返す。
    @param {str} id_はHTML属性idの値。Pythonの予約語と重複せぬようアンダーバーを付与した。
    @param {str} class_はHTML属性classの値。Pythonの予約語と重複せぬようアンダーバーを付与した。
    @param {dict} attributesはHTML属性のキー名と値を入れた辞書。id_,class_が指定されている時にid="",class=""が指定されるとid_,class_を優先する。
    """
    def CreateAttributes(self, id_=None, class_=None, **attributes):
        attr_str = ''
        if id_:
            attr_str = 'id="{0}"'.format(id_)
        if class_:
            attr_str = 'class="{0}"'.format(class_)
        for key in attributes.keys():
            if (id_ and 'id' == key) or (class_ and 'class' == key): # id_, class_, を優先する
                continue
            attr_str += key + '="' + attributes[key] + '" '
        return attr_str
    
    """
    HTMLの要素文字列を返す。
    @param {str} element_nameはHTML要素の名前。<{element_name}></{element_name}>となる。
    @param {str} text_node_valueはHTML要素のテキストノード値。<>{text_node_value}</>となる。
    @param {str} id_はHTML属性idの値。Pythonの予約語と重複せぬようアンダーバーを付与した。
    @param {str} class_はHTML属性classの値。Pythonの予約語と重複せぬようアンダーバーを付与した。
    @param {dict} attributesはHTML属性のキー名と値を入れた辞書。id_,class_が指定されている時にid="",class=""が指定されるとid_,class_を優先する。
    """
    def CreateElement(self, element_name, text_node_value=None, id_=None, class_=None, **attributes):
        html = self.__CreateStartElement(element_name, self.CreateAttributes(id_, class_, **attributes))
        if text_node_value:
            html += text_node_value
        html += '</{0}>'.format(element_name)
        return html
    
    """
    HTMLの開始要素タグ文字列を返す。属性文字列があればつけて返す。ないときはタグ文字列のみ返す。
    @param {str} element_nameはHTML要素の名前。<{element_name}></{element_name}>となる。
    @param {str} attr_strはHTML属性の文字列。
    """
    def __CreateStartElement(self, element_name, attr_str):
        if attr_str:
            html = '<{0} {1}>'.format(element_name, attr_str)
        else:
            html = '<{0}>'.format(element_name)
        return html
