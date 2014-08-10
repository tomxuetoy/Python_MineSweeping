// myHello2.cpp : Defines the initialization routines for the DLL.
//

#include "stdafx.h"
#include "myHello2.h"
#include <stdio.h>
#include <windows.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

//
//TODO: If this DLL is dynamically linked against the MFC DLLs,
//		any functions exported from this DLL which call into
//		MFC must have the AFX_MANAGE_STATE macro added at the
//		very beginning of the function.
//
//		For example:
//
//		extern "C" BOOL PASCAL EXPORT ExportedFunction()
//		{
//			AFX_MANAGE_STATE(AfxGetStaticModuleState());
//			// normal function body here
//		}
//
//		It is very important that this macro appear in each
//		function, prior to any calls into MFC.  This means that
//		it must appear as the first statement within the 
//		function, even before any object variable declarations
//		as their constructors may generate calls into the MFC
//		DLL.
//
//		Please see MFC Technical Notes 33 and 58 for additional
//		details.
//

// CmyHello2App

BEGIN_MESSAGE_MAP(CmyHello2App, CWinApp)
END_MESSAGE_MAP()


// CmyHello2App construction

CmyHello2App::CmyHello2App()
{
	// TODO: add construction code here,
	// Place all significant initialization in InitInstance
}

void CmyHello2App::sayHello()
{
	printf("hello tom 3\n");
}

void CmyHello2App::printColorStr(int color, char *str)
{
	HANDLE hd;

	hd = GetStdHandle(STD_OUTPUT_HANDLE);
	switch (color) {
	case 1: //red
		SetConsoleTextAttribute(hd,
			FOREGROUND_RED |
			FOREGROUND_INTENSITY);
		break;
	case 2: //green
		SetConsoleTextAttribute(hd,
			FOREGROUND_GREEN |
			FOREGROUND_INTENSITY);
		break;
	case 3: //yellow
		SetConsoleTextAttribute(hd,
			FOREGROUND_RED |
			FOREGROUND_GREEN |
			FOREGROUND_INTENSITY);
		break;
	case 4: //blue
		SetConsoleTextAttribute(hd,
			FOREGROUND_BLUE |
			FOREGROUND_INTENSITY);
		break;
	default: //white
		SetConsoleTextAttribute(hd,
			FOREGROUND_RED |
			FOREGROUND_GREEN |
			FOREGROUND_BLUE);
	}

	printf("%s", str);
}

/*
*功能:
输入彩色闪烁字符串
*输入参数：
count:闪烁次数
str:修饰的字符串
*/
int CmyHello2App::printTwinkleStr(int count, char *str)
{
	int i, len;
	char *cstr;
	len = strlen(str);
	cstr = (char*)malloc(sizeof(char)*(len + 2));
	sprintf_s(cstr, len+2, "%s\r", str);
	for (i = 1; i <= 4; i++) {
		printColorStr(i % 5, cstr);
		Sleep(200);
	}
	printColorStr(4, "\n");

	return len;
}

// The one and only CmyHello2App object

CmyHello2App theApp;


// CmyHello2App initialization

BOOL CmyHello2App::InitInstance()
{
	CWinApp::InitInstance();

	return TRUE;
}
