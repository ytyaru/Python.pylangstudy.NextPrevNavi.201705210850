#!python3
#encoding: utf-8
import HtmlWrapper
class Breadcrumbs(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = HtmlWrapper.HtmlWrapper()
    
    """
    パンくずリストのHTML文字列を生成する。
    @param {list} datas=[{'href': '', 'text': ''},{...},...]
    @param {bool} is_child_firstがTrueなら"孫 < 子 < 親"の順に並ぶ。Falseなら"親 > 子 > 孫"の順に並ぶ。
    """
    def CreateHtml(self, datas, is_child_first=False):
        if not datas:
            return None
        return self.__wrapper.Wrap(self.__CreateInnerHtml(datas, is_child_first), 'ul')
    
    """
    パンくずリストのHTML文字列を生成するためにdict引数を分解して内部メソッドに渡す。
    """
    def __CreateInnerHtml(self, datas, is_child_first=False):
        li_str = ''
        for data in datas:
            text_node_value = data['text']
            del data['text']
            li_str += self.__wrapper.Wrap(
                self.__WrapDirectionalIcond(
                    is_child_first, 
                    self.__wrapper.CreateElement('a', text_node_value=text_node_value, **data)
                ), 'li')
        return li_str
    
    def __WrapDirectionalIcond(self, is_child_first, li_str):
        if is_child_first:
            li_str = self.__CreateDirectionalIcon(is_child_first=is_child_first) + li_str
        else:
            li_str += self.__CreateDirectionalIcon(is_child_first=is_child_first)
        return li_str
    
    def __CreateDirectionalIcon(self, is_child_first=False):
        if self.__directional_icon_type == "FontAwesome":
            return self.__CreateDirectionalIcon_FontAwesome(is_child_first)
        else:
            return self.__CreateDirectionalIcon_Character(is_child_first)
    
    """
    FontAwesomeのアイコン。
    http://fontawesome.io/icons/
    """
    def __CreateDirectionalIcon_FontAwesome(self, is_child_first=False):
        if is_child_first:
            return '<i class="fa fa-angle-left" aria-hidden="true"></i>'
        else:
            return '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    
    def __CreateDirectionalIcon_Character(self, is_child_first=False):
        if is_child_first:
            text_node_value = '&lt;'
        else:
            text_node_value = '&gt;'
        return self.__wrapper.CreateElement('span', text_node_value=text_node_value, class_='DirectionalIcon')


if __name__ == '__main__':
    b = Breadcrumbs()
    """
    html = b.CreateHtml([
        {'text': '親', 'href': 'http://0'},
        {'text': '子', 'href': 'http://1'},
        {'text': '孫', 'href': 'http://2'}], is_child_first=False)
    """
    html = b.CreateHtml([
        {'text': '孫', 'href': 'http://2'},
        {'text': '子', 'href': 'http://1'},
        {'text': '親', 'href': 'http://0'}], is_child_first=True)
    print(html)

