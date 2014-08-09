# -*- coding: utf-8 -*-
'''@author: Rayment
   @version: 1.0
   @note: 实现扫雷游戏(2011-9-20)
          测试环境:python2.5.2
'''
import sys
import random
import string
import ctypes  
  
STD_INPUT_HANDLE = -10  
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12  
  
FOREGROUND_BLACK = 0x0  
FOREGROUND_BLUE = 0x01 # text color contains blue.  
FOREGROUND_GREEN= 0x02 # text color contains green.  
FOREGROUND_RED = 0x04 # text color contains red.  
FOREGROUND_INTENSITY = 0x08 # text color is intensified.  
  
BACKGROUND_BLUE = 0x10 # background color contains blue.  
BACKGROUND_GREEN= 0x20 # background color contains green.  
BACKGROUND_RED = 0x40 # background color contains red.  
BACKGROUND_INTENSITY = 0x80 # background color is intensified.  

class MineSweeping():
    '''扫雷主程序
    '''

    def __init__(self):
        '''初始化函式
        '''
        
        self.ROW = 16
        self.LINE = 16
        self.SCORE = 0 #扫雷得分
        self.MineNum = 60 #地雷总数
        self.xy_list= [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
        
        
    def iniData(self):
        '''x,y坐标初始状态值函数
           0-没有地雷;1-有地雷
        '''
        
        #游戏开始前所有数值归零
        for l in range(self.LINE):
            for r in range(self.ROW):
                self.xy_list[l][r]= 0
        
        Max = self.MineNum
        for x in range(self.LINE):
            for y in range(self.ROW):
                if 0 > Max:
                    self.xy_list[x][y]= 0
                else:
                    #为了增加地雷分布范围,选择0到4随机数
                    if 1 == random.randint(0,4): 
                        self.xy_list[x][y]= 1
                        Max = Max - 1
                        
    
    def getX(self):
        '''获得x坐标值
           @return : 返回x坐标值
           @type : int
        '''
        
        sys.stdout.write('Y=')
        xRet = raw_input()
        while xRet=='' or (False == self.isNumber(xRet))\
             or 0>int(xRet) or int(xRet)>self.ROW:
            print 'Wrong number!(please input 0-7)'
            sys.stdout.write('Y=')
            xRet = raw_input()
        return int(xRet)
        
        
    def getY(self):
        '''获得y坐标值
           @return : 返回y坐标值
           @type : int
        '''
        
        sys.stdout.write('X=')
        yRet = raw_input()
        while yRet=='' or (False == self.isNumber(yRet))\
             or 0>int(yRet) or int(yRet)>self.LINE:
            print 'Wrong number!(please input 0-7)'
            sys.stdout.write('X=')
            yRet = raw_input()
        return int(yRet)
    
    
    def isNumber(self,strVal):
        '''检查是否数值
           @param : 需检查的字符串 
           @type : str
        '''
        
        nums = string.digits
        for i in strVal:
            if i not in nums:
                return False
        return True
    

    def checkMine(self,xPos,yPos):
        '''检查输入坐标是否有雷
           0-没有地雷;1-有地雷;2-已经清扫
           @param 1: x坐标
           @type : int
           @param 2: y坐标
           @type : int
           @return : 0-没有地雷;1-有地雷;2-已经清扫
           @rtype : int
        ''' 
        
        if 0 == self.xy_list[xPos][yPos]:
            self.xy_list[xPos][yPos] = 2
            return 0
        elif 2 == self.xy_list[xPos][yPos]:
            return 2
        else:
            return 1
        
                
    def play(self):
        '''游戏运行函数
        '''
        
        self.display(1)
        self.SCORE = 0
        self.iniData()
        #print self.xy_list
        
        while(1):
            y = self.getY()
            x = self.getX() 
            while(2 == self.checkMine(x,y)):
                print 'values of x,y had inputed, please input new values!'
                y = self.getY()
                x = self.getX()
            if 1 == self.checkMine(x,y):
                self.endGame()
                break
            else:
                self.display(2)
                self.SCORE = self.SCORE + 1
                
            
    def endGame(self):
        '''游戏结束函数
        '''
        
        self.display(3)
        print '+===================================+'
        print '+             Game Over             +'
        print '+===================================+'
        print '   Your score is: %d    '%self.SCORE
        

    def display(self,kind):
        '''图形输出函数
           @param:1-初始;2-运行;3-结束
           @type:int
        '''
        
        if kind==1:
            clr = Color()
            clr.print_red_text('red')
            print '+===================================+'
            print '+             Game Start            +'
            print '+===================================+'
            print '*--0-1-2-3-4-5-6-7-8-9-a-b-c-d-e-f--*'
            print
            for i in range(self.LINE):
                print '%x  ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ? ' %(i)
            print 'Please input values of x,y(0-15):'
        elif kind==2:
            #输出已经清扫位置
            print '*--0-1-2-3-4-5-6-7-8-9-a-b-c-d-e-f--*'
            print
            for i in range(self.LINE):
                print '%x  ' %(i),
                for k in range(self.ROW):
                    if 2 == self.xy_list[i][k]:
                        sys.stdout.write('0 ')
                    else:
                        sys.stdout.write('? ')
                print
            print
            print 'Please input values of x,y(0-15):'           
        else:
            #输出所有的地雷与已经清扫位置
            print '*--0-1-2-3-4-5-6-7-8-9-a-b-c-d-e-f--*'
            print
            for i in range(self.LINE):
                print '%x  ' %(i),
                for k in range(self.ROW):
                    if 2 == self.xy_list[i][k]:
                        sys.stdout.write('0 ')
                    elif 1== self.xy_list[i][k]:
                        sys.stdout.write('X ')
                    else:
                        sys.stdout.write('? ')
                print
        

class Color:  
    ''''' See 
    STD_OUTPUT_HANDLE: http://msdn.microsoft.com/zh-cn/subscriptions/ms683231.aspx 
    SetConsoleTextAttribute: http://baike.baidu.com/view/4237672.htm?fr=aladdin
    GetStdHandle: http://baike.baidu.com/view/1934694.htm?fr=aladdin
    for information on Windows APIs.'''  
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)  
      
    def set_cmd_color(self, color, handle=std_out_handle):  
        """(color) -> bit 
        Example: set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY) 
        """  
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)  
        return bool  
      
    def reset_color(self):  
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)  
      
    def print_red_text(self, print_text):  
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)  
        print print_text  
        self.reset_color()  
          
    def print_green_text(self, print_text):  
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)  
        print print_text  
        self.reset_color()  
      
    def print_blue_text(self, print_text):   
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)  
        print print_text  
        self.reset_color()  
            
    def print_red_text_with_blue_bg(self, print_text):  
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY)  
        print print_text  
        self.reset_color()      


if __name__ == '__main__':
    '''自测试
    '''
    ms = MineSweeping()
    while(1):
        ms.play()
        print '\n----------------------------------------------'
        print 'Quit game press \'q\',otherwise press other key!'
        print '----------------------------------------------'
        inputVal = raw_input()
        if 'q' == inputVal:
            break
