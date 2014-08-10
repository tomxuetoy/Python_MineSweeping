// myHello2.h : main header file for the myHello2 DLL
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CmyHello2App
// See myHello2.cpp for the implementation of this class
//

class CmyHello2App : public CWinApp
{
public:
	CmyHello2App();
	void sayHello();
	void printColorStr(int color, char *str);
	int printTwinkleStr(int count, char *str);

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};
