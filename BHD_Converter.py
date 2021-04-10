import wx
from wx.lib.embeddedimage import PyEmbeddedImage
"""Icon文件代码化（PyEmbeddedImage）"""
AppIcon = PyEmbeddedImage(
    b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAABBBJ'
    b'REFUWIW1V71LO00Qfm7vFCMnGtTKlFZaWNgGUbGwMGIK/RMULPz4AwR7G/GjEBEsRGwUfmCh'
    b'chIUsRJRuMaAIkhUUONXMLm73Z23kLv3ffXOS9TfwJLL7C7z7MzOM7PK29sbIUAURYGiKEHT'
    b'RQkRgSjQBLSgCcYYcrkcXl5efgSgvLwc0WgUjDFfIL4AGGNIpVKYmprC1dUViOhbniAiRCIR'
    b'JJNJjI2NIRKJfAbx9vZGH8fz8zP19PQQgF8Z1dXVlEqlyLKsT7aYH3IhBJ6fn0s+cZDk83k8'
    b'Pj76ejHwDriL4/E4BgYGvrxIQfszmQzm5uZg23bg/kAArjQ3N2N4eBhSypIAqKqK09NTLC0t'
    b'wbKswHW+IfgopZ6+lD2hHshkMkilUiWDYIzh4uICjuN8mUGhALa2tmAYRknGXSEiWJaFsrKy'
    b'7wPgnINz/i0AxUgogKamJsTjcQD/3uzt7W20tbWhsbHRIynTNHF6eore3l7oug5FUfDw8IDN'
    b'zU0IIYIN+BFRNpultrY2AkCDg4NkWRYVCgVyHId2dnZI13VaWVkhzjkVCgXinNP09DTFYjFK'
    b'p9Nk2zbZtk1HR0dUV1dHmqbR+vo62bZdHBH9V9xiIqX8X2Fxde74qA8rQkWHQFEUMPaOkzHm'
    b'fbt6d7g33dUXW0lDAby+vuLy8hJEBFVVcXt7Cykl7u7ucHl5CSEEVFVFNpsF5xyZTMYDcnNz'
    b'83X8ASh+/UChUEBfXx/29/eh6zpqamq8OcuycH9/j2g0isrKSk+fy+Xw+vqK+vp6aNr7uRzH'
    b'wd3dHVRVxdraGhKJxKeMCvVAS0sL+vv7AbyHIJ1OY3FxEYlEAq2trZBSgjGG/f19GIaBwcFB'
    b'1NbWAngnsfn5edi2HWwgLAuGhoaIc062bZOUkgzDIF3XaXV1lYiIbNsmIqKZmRmKxWJ0fn5O'
    b'nHMSQtDx8XFoFoR6QEoJzrlXjNyYCiHgOI7nUlfvEpeiKKHxB4oIAWMMqqp6v6qqeno31pqm'
    b'edlRqhRVjHZ3d70sODk5gRACpmnCMAwvC87Ozv4OAMMwcHh46P3nnKNQKGB2dhYLCwuePp/P'
    b'o66u7vcBdHV1YXR0FFJKzwMTExMYHR1FR0cHhBDQNA0bGxv48+fP7wNoaGhAe3u7FwLgvdtp'
    b'ampCZ2cnOOfQNA2maZZsvCgAUkoIIT5lgZsdbhaU2rIVDcDl9I/8HlYL3O9vA3Ar2cHBAUZG'
    b'RkBEYIzh+voalmVheXkZBwcHHhOapomnpydMTk6iqqrK6wdyudzXhcmPCV9eXiiZTP7awyQa'
    b'jdLe3p7vw8TXA+Xl5RgfH4cQAtls9scP1O7ubrS0tPgyo281BN6ZzrKsoug0TCoqKqAoim+D'
    b'EgjAW/DD0wNfvxH+AcCqI8azUT0QAAAAAElFTkSuQmCC')

class MainFrame(wx.Frame): # 显示程序(内部结构)
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(600, 400)) # 继承父类的属性
        """程序大体框架"""
        self.icon = AppIcon.getIcon()
        self.SetIcon(self.icon)

        panel = wx.Panel(self, -1)  # 定义显示内容的主面板
        title = wx.StaticText(panel, wx.ID_ANY, "进制转换器", (200, 30), (200, -1), wx.ALIGN_CENTER)
        font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        title.SetFont(font)

        """作者信息"""

        self.author = wx.StaticText(panel, -1, "Copyright by Ming", (370, 45), (150, 55))  # 作者信息
        self.author_font = wx.Font(10, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_SLANT, wx.FONTWEIGHT_NORMAL)
        self.author.SetFont(self.author_font)



        """TextCtrl(单行文本框,输入内容)"""
        self.info = wx.StaticText(panel, -1, "输入想要转换的数: ", (10, 70))
        self.input = wx.TextCtrl(panel, -1, '', (10, 90), (250, -1)) #  TextCtrl：单行输入文本框 (显示区域，parent，标题，大小，位置)
        self.input_number = 0  # 初始化输入数据

        """RadioBox(选择进制的单选框)"""
        choosing_list = ['二进制', '八进制', '十进制', '十六进制']
        self.box = wx.RadioBox(panel, -1, "选择输入的进制格式", (280, 70), wx.DefaultSize, choosing_list, 4, wx.RA_SPECIFY_COLS) # wx.RA_SPECIFY_COLS排成一列
        self.Bind(wx.EVT_RADIOBOX, self.Choosing, self.box) # wx.EVT_RADIOBOX!!!!捕捉所选的项目
        self.result = 0

        """TextCtrl(输出内容框) wx.TextCtrl(parent, id, value, pos, size, style)"""
        self.binary_result = 0
        self.output_binary_text = wx.StaticText(panel, -1, "二进制:", (10, 150), (70, -1))
        self.output_binary = wx.TextCtrl(panel, -1, '', (80, 147), (300, -1), wx.TE_READONLY) # style=wx.TE_READONLY 文本不可编辑

        self.octonary_result = 0
        self.output_octonary_text = wx.StaticText(panel, -1, "八进制:", (10, 200), (70, -1))
        self.output_octonary = wx.TextCtrl(panel, -1, '', (80, 197), (300, -1), wx.TE_READONLY)

        self.decimal_result = 0
        self.output_decimal_text = wx.StaticText(panel, -1, "十进制:", (10, 250), (70, -1))
        self.output_decimal = wx.TextCtrl(panel, -1, '', (80, 247), (300, -1), wx.TE_READONLY)

        self.hexadecimal_result = 0
        self.output_hexadecimal_text = wx.StaticText(panel, -1, "十六进制:", (10, 300), (70, -1))
        self.output_hexadecimal = wx.TextCtrl(panel, -1, '', (80, 297), (300, -1), wx.TE_READONLY)

        """输出转换后的数据 """
        self.Bind(wx.EVT_TEXT, self.Input_convert, self.input)  # Bind(wx.EVT_TEXT, self.OnText, text) 监听键盘输入后的事件 输出转换后的数据 (事件，事件发生后干什么， 监听谁的事件)

    def Choosing(self, event):
        self.result = event.GetInt()
        print(self.result)

    def Input_convert(self, event):
        self.input_number = self.input.GetValue() # 格式化输入
        if self.result == 0:  # 输入为二进制  #（下一步检测输入，与正则表达式匹配）
            self.binary_result = self.input_number
            self.output_binary.SetValue("%s" % self.binary_result)  # 重新设置输出值

            self.octonary_result = oct(int(self.input_number, 2))  # 二进制转十进制再转八进制
            self.output_octonary.SetValue("%s" % self.octonary_result[2:])  # 重新设置输出值

            self.decimal_result = int(self.input_number, 2)  # 二进制转十进制
            self.output_decimal.SetValue("%d" % self.decimal_result)  # 重新设置输出值

            self.hexadecimal_result = hex(int(self.input_number, 2))  # 二进制转十进制再转十六进制
            self.output_hexadecimal.SetValue("%s" % self.hexadecimal_result[2:])  # 重新设置输出值)

        elif self.result == 1:  # 输入为八进制
            self.binary_result = bin(int(self.input_number, 8))   # 八进制转十进制再转二进制
            self.output_binary.SetValue("%s" % self.binary_result[2:])  # 重新设置输出值

            self.octonary_result = self.input_number  # 八进制
            self.output_octonary.SetValue("%s" % self.octonary_result)  # 重新设置输出值

            self.decimal_result = int(self.input_number, 8)  # 八进制转十进制
            self.output_decimal.SetValue("%d" % self.decimal_result)  # 重新设置输出值

            self.hexadecimal_result = hex(int(self.input_number, 8))  # 八进制转十六进制
            self.output_hexadecimal.SetValue("%s" % self.hexadecimal_result[2:])  # 重新设置输出值)

        elif self.result == 2: #  输入为十进制
            self.binary_result = bin(int(self.input_number))  # 十进制转二进制
            self.output_binary.SetValue("%s" % self.binary_result[2:])  # 重新设置输出值

            self.octonary_result = oct(int(self.input_number)) # 十进制转八进制
            self.output_octonary.SetValue("%s" % self.octonary_result[2:])  # 重新设置输出值

            self.decimal_result = int(self.input_number)  # 十进制
            self.output_decimal.SetValue("%d" % self.decimal_result)  # 重新设置输出值

            self.hexadecimal_result = hex(int(self.input_number))  # 十进制转十六进制
            self.output_hexadecimal.SetValue("%s" % self.hexadecimal_result[2:])  # 重新设置输出值)

        elif self.result == 3: #  输入为十六进制
            self.binary_result = bin(int(self.input_number, 16))  # 十六进制转十进制再转二进制
            self.output_binary.SetValue("%s" % self.binary_result[2:])  # 重新设置输出值

            self.octonary_result = oct(int(self.input_number, 16)) # 十六进制转十进制再转八进制
            self.output_octonary.SetValue("%s" % self.octonary_result[2:])  # 重新设置输出值

            self.decimal_result = int(self.input_number, 16)  # 十六进制转十进制
            self.output_decimal.SetValue("%d" % self.decimal_result)  # 重新设置输出值

            self.hexadecimal_result = self.input_number  # 十六进制
            self.output_hexadecimal.SetValue("%s" % self.hexadecimal_result)  # 重新设置输出值)


class App(wx.App): #　应用程序的内部结构，运行程序
    def __init__(self):
        wx.App.__init__(self)

    def OnInit(self): # 利用app显示
        self.version = u"v1.0"
        self.title = u"BHD_Converter" + " " + self.version
        frame = MainFrame(parent=None, id=-1, title=self.title)
        frame.Show() #　显示窗口，显示定义的东西
        return True


if __name__ == "__main__": # python主程序入口
    app = App()
    app.MainLoop() #程序入口
