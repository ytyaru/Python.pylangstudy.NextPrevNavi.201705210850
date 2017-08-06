#!python3
#encoding: utf-8
import HtmlWrapper
class NextPrevNavi(object):
    def __init__(self, directional_icon_type='FontAwesome'):
        self.__directional_icon_type = directional_icon_type
        self.__wrapper = HtmlWrapper.HtmlWrapper()
    
    """
    前後ナビのHTML文字列を生成する。
    実際は水平配置(False,False), 垂直配置(True,True)の組合せしか使わない。
    @param {str} prevは左または上に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    @param {str} nextは右または下に配置される。{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}
    @param {bool} is_varticalがFalseなら"<前 次>"の水平配置。Trueなら"<前
                                                                    >次"の垂直配置。
    """
    def CreateHtml(self, prev, next, is_vartical=False):
        if not prev or not next:
            raise Exception("引数エラー1。prev, nextは`{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}`の形にしてください。")
            return None
        if not 'text' in prev or not 'href' in prev or not 'text' in next or not 'href' in next:
            raise Exception("引数エラー2。prev, nextは`{'text': 'a要素のテキストノード', 'href': 'a要素のhref属性値'}`の形にしてください。")
            return None
        if not prev['text'] or not prev['href'] or not next['text'] or not next['href']:
            raise Exception('引数エラー3。prev, nextの各キーに値を指定してください。')
            return None
        return self.__wrapper.Wrap(self.__CreateInnerHtml(prev, next, is_vartical), 'ul', id_='NextPrevNavi')
    
    def __SplitTextNodeAndAttributes(self, data):
        text_node_value = data['text']
        del data['text']
        return (text_node_value, data)
    
    """
    パンくずリストのHTML文字列を生成するためにdict引数を分解して内部メソッドに渡す。
    @param {list} datas=[{'href': '', 'text': ''},{...},...]
    @param {bool} is_next_firstがTrueなら"次,前"の順に並ぶ。Falseなら"前,次"の順に並ぶ。
    """
#    def __CreateInnerHtml(self, datas, is_next_first=False):
    def __CreateInnerHtml(self, prev, next, is_vartical=False):
#        is_left = not(is_vartical)
#        is_left = is_vartical
        is_next = False
        is_left = True
        li_str = ''
        for data in (prev, next):
            text_node_value, attrs = self.__SplitTextNodeAndAttributes(data)
            li_str += self.__wrapper.Wrap(
                self.__AppendDirectionalIcon(
                    is_next,
                    is_left, 
                    self.__wrapper.CreateElement('a', text_node_value=text_node_value, **attrs)
                ), 'li')
            if not is_vartical:
                is_left = not(is_left)
            is_next = True
        return li_str
    
    def __AppendDirectionalIcon(self, is_next, is_left, a_str):
        if is_left:
            a_str = self.__CreateDirectionalIcon(is_next=is_next, is_left=is_left) + a_str
        else:
            a_str += self.__CreateDirectionalIcon(is_next=is_next, is_left=is_left)
        return a_str
        
    def __CreateDirectionalIcon(self, is_next, is_left=False):
        if is_next and is_left:
            is_left = False
        if self.__directional_icon_type == "FontAwesome":
            return self.__CreateDirectionalIcon_FontAwesome(is_left)
        else:
            return self.__CreateDirectionalIcon_Character(is_left)
    
    """
    def __AppendDirectionalIcon(self, is_left, a_str):
        if is_left:
            a_str = self.__CreateDirectionalIcon(is_left=is_left) + a_str
        else:
            a_str += self.__CreateDirectionalIcon(is_left=is_left)
        return a_str
        
    def __CreateDirectionalIcon(self, is_left=False):
        if self.__directional_icon_type == "FontAwesome":
            return self.__CreateDirectionalIcon_FontAwesome(is_left)
        else:
            return self.__CreateDirectionalIcon_Character(is_left)
    """
    def __CreateDirectionalIcon_FontAwesome(self, is_left=False):
        if is_left:
            return '<i class="fa fa-angle-left" aria-hidden="true"></i>'
        else:
            return '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    
    def __CreateDirectionalIcon_Character(self, is_left=False):
        text_node_value = ''
        if is_left:
            text_node_value = '&lt;'
        else:
            text_node_value = '&gt;'
        return self.__wrapper.CreateElement('span', text_node_value=text_node_value, class_='DirectionalIcon')


if __name__ == '__main__':
    n = NextPrevNavi()
    """
    html = n.CreateHtml([
        {'text': '前のページ', 'href': 'http://prev'},
        {'text': '次のページ', 'href': 'http://next'}], is_next_first=False)
    """
    """
    html = n.CreateHtml([
        {'text': '次のページ', 'href': 'http://next'},
        {'text': '前のページ', 'href': 'http://prev'}], is_next_first=True)
    html = n.CreateHtml([
        {'text': '前のページ', 'href': 'http://prev'},
        {'text': '次のページ', 'href': 'http://next'}], is_next_first=True)
    """

    html = n.CreateHtml(
        prev={'text': '前のページ', 'href': 'http://prev'},
        next={'text': '次のページ', 'href': 'http://next'},
        is_vartical=False)
    html += '\n\n'
    html += n.CreateHtml(
        prev={'text': '前のページ', 'href': 'http://prev'},
        next={'text': '次のページ', 'href': 'http://next'},
        is_vartical=True)
    print(html)

