# Multiplication 

import random
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout



page = Builder.load_string('''

#: import random random



<Multi_page>:

    orientation: 'vertical'
    spacing : 10
    padding : 10    

    Button:
        id : 'bt1'
        #text : 'Start Learning Number Multiplication - press here'
        text : 'start learning-press here'
        font_name: 'arial'
        font_size: '20sp' 
        on_press: root.on_pressBt1(s1.text)
        on_release: T1.focus = True
        back_color: (0.157,0.566,0.444,1)
        border_radius: [20]

    
    Label:
        id : lb2
        font_size : '40sp'
        bcolor: 1,0,0,1
        
    TextInput:
        multiline : False
        font_size: '25sp'
        id : T1
        halign : 'center'
        font_name : 'arial'
        
    Button:
        id : 'bt2'
        text : 'Check the answer'
        font_name :'arial'
        font_size: '20sp'
        on_press: root.on_pressBt2()
        
    Spinner:
        id : s1
        text : 'Table 1 : 10'
        values :[str(i) for i in  range(1,11)] + ['Table 1 : 10']
        bold: True

    Label:
        text : 'Made  by Muneer Al Hashim - email: muneer4k@yahoo.com  - Freeware  - Date : 12Dec2020 -Saudi Arabia '
        halign : 'justify'
        size_hint_y: None
        italic : True
        underline:True
        bold: True
               
    


''')


def stNo(): 
    stNo =  random.randint(1,10)
    return stNo

def seNo():
    seNo =  random.randint(1,10)
    return seNo



class Multi_page(BoxLayout):
    def __init__(self,**kwargs):
        super(Multi_page,self).__init__(**kwargs)

    def on_pressBt1(self, spinner_value):
        if spinner_value == 'Table 1 : 10':
            st, se = stNo(), seNo()
        else:
            st, se = int(spinner_value), seNo()

        textLb2 = f' = {st}  X  {se} '
        self.ids['lb2'].text= textLb2
        self.ids['T1'].text =''
        self.ids['T1'].background_color = (255,255,255,1)
        global answer_m
        answer_m   = st*se
        return answer_m
    

    def on_pressBt2(self):
        check = self.ids['T1'].text.isnumeric()

        if check==True and answer_m !='':
            value = int(self.ids['T1'].text)
        
            if value == answer_m:
                txt = 'Excellent the answer is correct'
                self.ids['T1'].text = f' {txt} {answer_m} '
                self.ids['T1'].background_color = (0,250,0,1)
            else:
                txt = 'Sorry the the correct answer is '
                self.ids['T1'].text = f'{txt} {answer_m} '
                self.ids['T1'].background_color = (250,0,0,1)
        else:
            txt = 'Please enter the number or press the top button'
            self.ids['T1'].text = f'{txt}'


# specific number
def multi(x):
    for  i in range(10):
        print (f'{x} X {i+1} = {x * (i+1)}')



class MultiApp(App):
    def build(self):
        self.title = 'Multiple (mathematics)'
        return Multi_page()

if __name__ == '__main__':
    MultiApp().run()

