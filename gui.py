# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 25 2009)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__  ( self, parent, id = wx.ID_ANY, title = u"Kriptografija", pos = wx.DefaultPosition, size = wx.Size( 667,453 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 61, 173, 216 ) )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.biljeznica = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.biljeznica.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 90, False, wx.EmptyString ) )
		self.biljeznica.SetBackgroundColour( wx.Colour( 249, 248, 213 ) )
		
		self.SHA1_tab = wx.Panel( self.biljeznica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer3 = wx.GridSizer( 6, 2, 0, 0 )
		
		self.m_staticText6 = wx.StaticText( self.SHA1_tab, wx.ID_ANY, u"Ulazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		gSizer3.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.ulaz_dat = wx.FilePickerCtrl( self.SHA1_tab, wx.ID_ANY, u"ulaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.ulaz_dat.SetBackgroundColour( wx.Colour( 240, 239, 185 ) )
		
		gSizer3.Add( self.ulaz_dat, 1, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self.SHA1_tab, wx.ID_ANY, u"Izlazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer3.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.izlaz_dat = wx.FilePickerCtrl( self.SHA1_tab, wx.ID_ANY, u"izlaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.izlaz_dat.SetBackgroundColour( wx.Colour( 240, 239, 189 ) )
		
		gSizer3.Add( self.izlaz_dat, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.SHA1_tab, wx.ID_ANY, u"Sazetak:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.ispis_sazetak = wx.TextCtrl( self.SHA1_tab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ispis_sazetak.SetBackgroundColour( wx.Colour( 232, 230, 179 ) )
		
		gSizer3.Add( self.ispis_sazetak, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.generiraj_sazetak = wx.Button( self.SHA1_tab, wx.ID_ANY, u"Generiraj sazetak", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.generiraj_sazetak.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer3.Add( self.generiraj_sazetak, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.prikazi_dat = wx.Button( self.SHA1_tab, wx.ID_ANY, u"Prikazi ulaznu datoteku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prikazi_dat.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer3.Add( self.prikazi_dat, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.prikazi_izlaz = wx.Button( self.SHA1_tab, wx.ID_ANY, u"Prikazi izlaznu datoteku", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prikazi_izlaz.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer3.Add( self.prikazi_izlaz, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap2 = wx.StaticBitmap( self.SHA1_tab, wx.ID_ANY, wx.Bitmap( u"lock2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer3.Add( self.m_bitmap2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.SHA1_tab.SetSizer( gSizer3 )
		self.SHA1_tab.Layout()
		gSizer3.Fit( self.SHA1_tab )
		self.biljeznica.AddPage( self.SHA1_tab, u"SHA1", True )
		self.RSA_tab = wx.Panel( self.biljeznica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer31 = wx.GridSizer( 6, 3, 0, 0 )
		
		self.m_staticText15 = wx.StaticText( self.RSA_tab, wx.ID_ANY, u"Privatni kljuc:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		gSizer31.Add( self.m_staticText15, 0, wx.ALL, 5 )
		
		self.privatni_dat_rsa = wx.FilePickerCtrl( self.RSA_tab, wx.ID_ANY, u"privatni.txt", u"Odaberi privatni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.privatni_dat_rsa.SetBackgroundColour( wx.Colour( 237, 238, 181 ) )
		
		gSizer31.Add( self.privatni_dat_rsa, 0, wx.ALL, 5 )
		
		self.m_button26 = wx.Button( self.RSA_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button26.SetForegroundColour( wx.Colour( 54, 54, 54 ) )
		self.m_button26.SetBackgroundColour( wx.Colour( 237, 235, 163 ) )
		
		gSizer31.Add( self.m_button26, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.RSA_tab, wx.ID_ANY, u"Javni kljuc:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		gSizer31.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.javni_dat_rsa = wx.FilePickerCtrl( self.RSA_tab, wx.ID_ANY, u"javni.txt", u"Odaberi javni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.javni_dat_rsa.SetBackgroundColour( wx.Colour( 231, 230, 171 ) )
		
		gSizer31.Add( self.javni_dat_rsa, 0, wx.ALL, 5 )
		
		self.m_button27 = wx.Button( self.RSA_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button27.SetForegroundColour( wx.Colour( 49, 49, 49 ) )
		self.m_button27.SetBackgroundColour( wx.Colour( 236, 234, 159 ) )
		
		gSizer31.Add( self.m_button27, 0, wx.ALL, 5 )
		
		self.m_staticText21 = wx.StaticText( self.RSA_tab, wx.ID_ANY, u"Generiraj par kljuceva:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer31.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		rsa_kljuc_duljinaChoices = [ u"1024", u"2048" ]
		self.rsa_kljuc_duljina = wx.Choice( self.RSA_tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, rsa_kljuc_duljinaChoices, 0 )
		self.rsa_kljuc_duljina.SetSelection( 0 )
		self.rsa_kljuc_duljina.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		self.rsa_kljuc_duljina.SetBackgroundColour( wx.Colour( 227, 223, 136 ) )
		
		gSizer31.Add( self.rsa_kljuc_duljina, 0, wx.ALL, 5 )
		
		self.m_button28 = wx.Button( self.RSA_tab, wx.ID_ANY, u"Generiraj par kljuceva", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button28.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer31.Add( self.m_button28, 1, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.RSA_tab, wx.ID_ANY, u"Ulazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		gSizer31.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.ulaz_dat_rsa = wx.FilePickerCtrl( self.RSA_tab, wx.ID_ANY, u"ulaz_mini.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.ulaz_dat_rsa.SetBackgroundColour( wx.Colour( 230, 228, 172 ) )
		
		gSizer31.Add( self.ulaz_dat_rsa, 0, wx.ALL, 5 )
		
		self.ulaaaz = wx.Button( self.RSA_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ulaaaz.SetForegroundColour( wx.Colour( 42, 42, 42 ) )
		self.ulaaaz.SetBackgroundColour( wx.Colour( 233, 235, 150 ) )
		
		gSizer31.Add( self.ulaaaz, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.RSA_tab, wx.ID_ANY, u"Izlazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer31.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.izlaz_dat_rsa = wx.FilePickerCtrl( self.RSA_tab, wx.ID_ANY, u"izlaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.izlaz_dat_rsa.SetBackgroundColour( wx.Colour( 228, 227, 167 ) )
		
		gSizer31.Add( self.izlaz_dat_rsa, 0, wx.ALL, 5 )
		
		self.izlaaaz = wx.Button( self.RSA_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.izlaaaz.SetForegroundColour( wx.Colour( 53, 53, 53 ) )
		self.izlaaaz.SetBackgroundColour( wx.Colour( 237, 235, 154 ) )
		
		gSizer31.Add( self.izlaaaz, 0, wx.ALL, 5 )
		
		self.m_button31 = wx.Button( self.RSA_tab, wx.ID_ANY, u"Kriptiraj podatke", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button31.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer31.Add( self.m_button31, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button32 = wx.Button( self.RSA_tab, wx.ID_ANY, u"Dekriptiraj podatke", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button32.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer31.Add( self.m_button32, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap5 = wx.StaticBitmap( self.RSA_tab, wx.ID_ANY, wx.Bitmap( u"lock2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer31.Add( self.m_bitmap5, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.RSA_tab.SetSizer( gSizer31 )
		self.RSA_tab.Layout()
		gSizer31.Fit( self.RSA_tab )
		self.biljeznica.AddPage( self.RSA_tab, u"RSA", False )
		self.AES_tab = wx.Panel( self.biljeznica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer2 = wx.GridSizer( 6, 3, 0, 0 )
		
		self.m_staticText11 = wx.StaticText( self.AES_tab, wx.ID_ANY, u"Kljuc:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		gSizer2.Add( self.m_staticText11, 0, wx.ALL, 5 )
		
		self.kljuc_dat_aes = wx.FilePickerCtrl( self.AES_tab, wx.ID_ANY, u"aes_kljuc.txt", u"Odaberi kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.kljuc_dat_aes.SetBackgroundColour( wx.Colour( 238, 237, 181 ) )
		
		gSizer2.Add( self.kljuc_dat_aes, 0, wx.ALL, 5 )
		
		self.generiraj_aes_kljuc = wx.Button( self.AES_tab, wx.ID_ANY, u"Generiraj", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.generiraj_aes_kljuc, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.AES_tab, wx.ID_ANY, u"Ulazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer2.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.ulaz_dat_aes = wx.FilePickerCtrl( self.AES_tab, wx.ID_ANY, u"ulaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.ulaz_dat_aes.SetBackgroundColour( wx.Colour( 233, 230, 177 ) )
		
		gSizer2.Add( self.ulaz_dat_aes, 0, wx.ALL, 5 )
		
		self.prikazi_aes_ulaz = wx.Button( self.AES_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prikazi_aes_ulaz.SetBackgroundColour( wx.Colour( 230, 234, 151 ) )
		
		gSizer2.Add( self.prikazi_aes_ulaz, 0, wx.ALL, 5 )
		
		self.bla = wx.StaticText( self.AES_tab, wx.ID_ANY, u"Izlazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.bla.Wrap( -1 )
		gSizer2.Add( self.bla, 0, wx.ALL, 5 )
		
		self.izlaz_dat_aes = wx.FilePickerCtrl( self.AES_tab, wx.ID_ANY, u"izlaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.izlaz_dat_aes.SetBackgroundColour( wx.Colour( 236, 235, 179 ) )
		
		gSizer2.Add( self.izlaz_dat_aes, 0, wx.ALL, 5 )
		
		self.prikazi_aes_izlaz = wx.Button( self.AES_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.prikazi_aes_izlaz.SetBackgroundColour( wx.Colour( 236, 234, 155 ) )
		
		gSizer2.Add( self.prikazi_aes_izlaz, 0, wx.ALL, 5 )
		
		self.m_button17 = wx.Button( self.AES_tab, wx.ID_ANY, u"Kriptiraj podatke", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button17.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer2.Add( self.m_button17, 0, wx.ALL, 5 )
		
		self.m_button18 = wx.Button( self.AES_tab, wx.ID_ANY, u"Dekriptiraj podatke", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button18.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer2.Add( self.m_button18, 0, wx.ALL, 5 )
		
		self.m_button19 = wx.Button( self.AES_tab, wx.ID_ANY, u"Prikazi dekriptirane podatke", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button19.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer2.Add( self.m_button19, 0, wx.ALL, 5 )
		
		self.m_staticText14 = wx.StaticText( self.AES_tab, wx.ID_ANY, u"Velicina novog kljuca:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )
		gSizer2.Add( self.m_staticText14, 0, wx.ALL, 5 )
		
		izbor_aesChoices = [ u"128", u"192", u"256" ]
		self.izbor_aes = wx.Choice( self.AES_tab, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, izbor_aesChoices, 0 )
		self.izbor_aes.SetSelection( 0 )
		self.izbor_aes.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DDKSHADOW ) )
		self.izbor_aes.SetBackgroundColour( wx.Colour( 228, 226, 146 ) )
		
		gSizer2.Add( self.izbor_aes, 0, wx.ALL, 5 )
		
		self.prikazi_aes_kljuc = wx.Button( self.AES_tab, wx.ID_ANY, u"Prikazi novi kljuc", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.prikazi_aes_kljuc, 0, wx.ALL, 5 )
		
		self.AES_tab.SetSizer( gSizer2 )
		self.AES_tab.Layout()
		gSizer2.Fit( self.AES_tab )
		self.biljeznica.AddPage( self.AES_tab, u"AES", False )
		self.omotnica_tab = wx.Panel( self.biljeznica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer4 = wx.GridSizer( 7, 3, 0, 0 )
		
		self.m_staticText24 = wx.StaticText( self.omotnica_tab, wx.ID_ANY, u"Javni kljuc primatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gSizer4.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.om_javni_kljuc = wx.FilePickerCtrl( self.omotnica_tab, wx.ID_ANY, u"javni.txt", u"Odaberi javni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.om_javni_kljuc.SetBackgroundColour( wx.Colour( 231, 232, 179 ) )
		
		gSizer4.Add( self.om_javni_kljuc, 0, wx.ALL, 5 )
		
		self.m_button33 = wx.Button( self.omotnica_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button33.SetForegroundColour( wx.Colour( 46, 46, 46 ) )
		self.m_button33.SetBackgroundColour( wx.Colour( 238, 235, 164 ) )
		
		gSizer4.Add( self.m_button33, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.omotnica_tab, wx.ID_ANY, u"Tajni kljuc primatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		gSizer4.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.om_tajni_kljuc = wx.FilePickerCtrl( self.omotnica_tab, wx.ID_ANY, u"privatni.txt", u"Odaberi tajni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.om_tajni_kljuc.SetBackgroundColour( wx.Colour( 234, 233, 172 ) )
		
		gSizer4.Add( self.om_tajni_kljuc, 0, wx.ALL, 5 )
		
		self.m_button34 = wx.Button( self.omotnica_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button34.SetForegroundColour( wx.Colour( 51, 51, 51 ) )
		self.m_button34.SetBackgroundColour( wx.Colour( 240, 238, 159 ) )
		
		gSizer4.Add( self.m_button34, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.omotnica_tab, wx.ID_ANY, u"Ulazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gSizer4.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.om_ulaz_dat = wx.FilePickerCtrl( self.omotnica_tab, wx.ID_ANY, u"ulaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.om_ulaz_dat.SetBackgroundColour( wx.Colour( 238, 237, 176 ) )
		
		gSizer4.Add( self.om_ulaz_dat, 0, wx.ALL, 5 )
		
		self.m_button35 = wx.Button( self.omotnica_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button35.SetForegroundColour( wx.Colour( 40, 40, 40 ) )
		self.m_button35.SetBackgroundColour( wx.Colour( 240, 238, 153 ) )
		
		gSizer4.Add( self.m_button35, 0, wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self.omotnica_tab, wx.ID_ANY, u"Izlazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gSizer4.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.om_izlaz_dat = wx.FilePickerCtrl( self.omotnica_tab, wx.ID_ANY, u"izlaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.om_izlaz_dat.SetBackgroundColour( wx.Colour( 238, 235, 174 ) )
		
		gSizer4.Add( self.om_izlaz_dat, 0, wx.ALL, 5 )
		
		self.m_button36 = wx.Button( self.omotnica_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button36.SetForegroundColour( wx.Colour( 45, 45, 45 ) )
		self.m_button36.SetBackgroundColour( wx.Colour( 240, 238, 153 ) )
		
		gSizer4.Add( self.m_button36, 0, wx.ALL, 5 )
		
		self.m_staticText29 = wx.StaticText( self.omotnica_tab, wx.ID_ANY, u"Digitalna omotnica:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText29.Wrap( -1 )
		gSizer4.Add( self.m_staticText29, 0, wx.ALL, 5 )
		
		self.omotnica_dat = wx.FilePickerCtrl( self.omotnica_tab, wx.ID_ANY, u"omotnica.txt", u"Odaberi omotnicu", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.omotnica_dat.SetBackgroundColour( wx.Colour( 239, 238, 186 ) )
		
		gSizer4.Add( self.omotnica_dat, 0, wx.ALL, 5 )
		
		self.m_button37 = wx.Button( self.omotnica_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button37.SetForegroundColour( wx.Colour( 44, 44, 44 ) )
		self.m_button37.SetBackgroundColour( wx.Colour( 236, 238, 153 ) )
		
		gSizer4.Add( self.m_button37, 0, wx.ALL, 5 )
		
		self.m_button38 = wx.Button( self.omotnica_tab, wx.ID_ANY, u"Generiraj digitalnu omotnicu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button38.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer4.Add( self.m_button38, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button39 = wx.Button( self.omotnica_tab, wx.ID_ANY, u"Otvori digitalnu omotnicu", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button39.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer4.Add( self.m_button39, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap6 = wx.StaticBitmap( self.omotnica_tab, wx.ID_ANY, wx.Bitmap( u"lock2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.m_bitmap6, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.omotnica_tab.SetSizer( gSizer4 )
		self.omotnica_tab.Layout()
		gSizer4.Fit( self.omotnica_tab )
		self.biljeznica.AddPage( self.omotnica_tab, u"Digitalna omotnica", False )
		self.potpis_tab = wx.Panel( self.biljeznica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer5 = wx.GridSizer( 7, 3, 0, 0 )
		
		self.m_staticText30 = wx.StaticText( self.potpis_tab, wx.ID_ANY, u"Tajni kljuc posiljatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		gSizer5.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.pt_tajni_dat = wx.FilePickerCtrl( self.potpis_tab, wx.ID_ANY, u"privatni.txt", u"Odaberi tajni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pt_tajni_dat.SetBackgroundColour( wx.Colour( 232, 231, 168 ) )
		
		gSizer5.Add( self.pt_tajni_dat, 0, wx.ALL, 5 )
		
		self.m_button40 = wx.Button( self.potpis_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button40.SetForegroundColour( wx.Colour( 59, 59, 59 ) )
		self.m_button40.SetBackgroundColour( wx.Colour( 239, 238, 175 ) )
		
		gSizer5.Add( self.m_button40, 0, wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.potpis_tab, wx.ID_ANY, u"Javni kljuc posiljatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		gSizer5.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.pt_javni_dat = wx.FilePickerCtrl( self.potpis_tab, wx.ID_ANY, u"javni.txt", u"Odaberi javni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pt_javni_dat.SetBackgroundColour( wx.Colour( 233, 230, 171 ) )
		
		gSizer5.Add( self.pt_javni_dat, 0, wx.ALL, 5 )
		
		self.m_button41 = wx.Button( self.potpis_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button41.SetForegroundColour( wx.Colour( 55, 55, 55 ) )
		self.m_button41.SetBackgroundColour( wx.Colour( 235, 237, 165 ) )
		
		gSizer5.Add( self.m_button41, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.potpis_tab, wx.ID_ANY, u"Ulazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		gSizer5.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.pt_ulaz_dat = wx.FilePickerCtrl( self.potpis_tab, wx.ID_ANY, u"ulaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pt_ulaz_dat.SetBackgroundColour( wx.Colour( 238, 240, 172 ) )
		
		gSizer5.Add( self.pt_ulaz_dat, 0, wx.ALL, 5 )
		
		self.m_button42 = wx.Button( self.potpis_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button42.SetForegroundColour( wx.Colour( 53, 53, 53 ) )
		self.m_button42.SetBackgroundColour( wx.Colour( 237, 235, 167 ) )
		
		gSizer5.Add( self.m_button42, 0, wx.ALL, 5 )
		
		self.m_staticText33 = wx.StaticText( self.potpis_tab, wx.ID_ANY, u"Digitalni potpis:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText33.Wrap( -1 )
		gSizer5.Add( self.m_staticText33, 0, wx.ALL, 5 )
		
		self.pt_izlaz_dat = wx.FilePickerCtrl( self.potpis_tab, wx.ID_ANY, u"potpis.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pt_izlaz_dat.SetBackgroundColour( wx.Colour( 234, 232, 159 ) )
		
		gSizer5.Add( self.pt_izlaz_dat, 0, wx.ALL, 5 )
		
		self.m_button43 = wx.Button( self.potpis_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button43.SetForegroundColour( wx.Colour( 55, 55, 55 ) )
		self.m_button43.SetBackgroundColour( wx.Colour( 236, 234, 164 ) )
		
		gSizer5.Add( self.m_button43, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.potpis_tab, wx.ID_ANY, u"Generiraj/provjeri:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		gSizer5.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_button46 = wx.Button( self.potpis_tab, wx.ID_ANY, u"Generiraj digitalni potpis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button46.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer5.Add( self.m_button46, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button47 = wx.Button( self.potpis_tab, wx.ID_ANY, u"Provjeri digitalni potpis", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button47.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer5.Add( self.m_button47, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText37 = wx.StaticText( self.potpis_tab, wx.ID_ANY, u"Rezultat provjere:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		gSizer5.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.rez_provjera = wx.TextCtrl( self.potpis_tab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rez_provjera.SetBackgroundColour( wx.Colour( 224, 226, 177 ) )
		
		gSizer5.Add( self.rez_provjera, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap4 = wx.StaticBitmap( self.potpis_tab, wx.ID_ANY, wx.Bitmap( u"lock2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.m_bitmap4, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
		
		self.potpis_tab.SetSizer( gSizer5 )
		self.potpis_tab.Layout()
		gSizer5.Fit( self.potpis_tab )
		self.biljeznica.AddPage( self.potpis_tab, u"Digitalni potpis", False )
		self.pecat_tab = wx.Panel( self.biljeznica, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		gSizer6 = wx.GridSizer( 9, 3, 0, 0 )
		
		self.m_staticText38 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Ulazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		gSizer6.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.pc_ulaz_dat = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"ulaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_ulaz_dat.SetBackgroundColour( wx.Colour( 234, 233, 181 ) )
		
		gSizer6.Add( self.pc_ulaz_dat, 0, wx.ALL, 5 )
		
		self.m_button48 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button48.SetForegroundColour( wx.Colour( 59, 59, 59 ) )
		self.m_button48.SetBackgroundColour( wx.Colour( 238, 236, 166 ) )
		
		gSizer6.Add( self.m_button48, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Javni kljuc primatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		gSizer6.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.pc_javni_primatelja_dat = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"javni_primatelja.txt", u"Odaberi javni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_javni_primatelja_dat.SetBackgroundColour( wx.Colour( 240, 237, 181 ) )
		
		gSizer6.Add( self.pc_javni_primatelja_dat, 0, wx.ALL, 5 )
		
		self.m_button49 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button49.SetForegroundColour( wx.Colour( 56, 56, 56 ) )
		self.m_button49.SetBackgroundColour( wx.Colour( 233, 226, 152 ) )
		
		gSizer6.Add( self.m_button49, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Tajni kljuc posiljatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		gSizer6.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.pc_tajni_posiljatelja_dat = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"privatni_posiljatelja.txt", u"Odaberi tajni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_tajni_posiljatelja_dat.SetBackgroundColour( wx.Colour( 234, 230, 176 ) )
		
		gSizer6.Add( self.pc_tajni_posiljatelja_dat, 0, wx.ALL, 5 )
		
		self.m_button50 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button50.SetForegroundColour( wx.Colour( 51, 51, 51 ) )
		self.m_button50.SetBackgroundColour( wx.Colour( 232, 227, 153 ) )
		
		gSizer6.Add( self.m_button50, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Digitalna omotnica:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		gSizer6.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.pc_omotnica_dat = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"omotnica.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_omotnica_dat.SetBackgroundColour( wx.Colour( 236, 232, 183 ) )
		
		gSizer6.Add( self.pc_omotnica_dat, 0, wx.ALL, 5 )
		
		self.m_button51 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button51.SetForegroundColour( wx.Colour( 51, 51, 51 ) )
		self.m_button51.SetBackgroundColour( wx.Colour( 234, 230, 153 ) )
		
		gSizer6.Add( self.m_button51, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Digitalni potpis:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		gSizer6.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.pc_potpis_dat = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"potpis.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_potpis_dat.SetBackgroundColour( wx.Colour( 235, 239, 180 ) )
		
		gSizer6.Add( self.pc_potpis_dat, 0, wx.ALL, 5 )
		
		self.m_button52 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button52.SetForegroundColour( wx.Colour( 65, 65, 65 ) )
		self.m_button52.SetBackgroundColour( wx.Colour( 232, 230, 149 ) )
		
		gSizer6.Add( self.m_button52, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Javni kljuc posiljatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		gSizer6.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		self.pc_javni_posiljatelja = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"javni_posiljatelja.txt", u"Odaberi javni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_javni_posiljatelja.SetBackgroundColour( wx.Colour( 235, 233, 188 ) )
		
		gSizer6.Add( self.pc_javni_posiljatelja, 0, wx.ALL, 5 )
		
		self.m_button53 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button53.SetForegroundColour( wx.Colour( 62, 62, 62 ) )
		self.m_button53.SetBackgroundColour( wx.Colour( 233, 235, 160 ) )
		
		gSizer6.Add( self.m_button53, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Tajni kljuc primatelja:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		gSizer6.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.pc_tajni_primatelja = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"privatni_primatelja.txt", u"Odaberi tajni kljuc", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_tajni_primatelja.SetBackgroundColour( wx.Colour( 234, 233, 179 ) )
		
		gSizer6.Add( self.pc_tajni_primatelja, 0, wx.ALL, 5 )
		
		self.m_button54 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button54.SetForegroundColour( wx.Colour( 54, 54, 54 ) )
		self.m_button54.SetBackgroundColour( wx.Colour( 231, 235, 158 ) )
		
		gSizer6.Add( self.m_button54, 0, wx.ALL, 5 )
		
		self.m_staticText45 = wx.StaticText( self.pecat_tab, wx.ID_ANY, u"Izlazna datoteka:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		gSizer6.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.pc_izlaz_dat = wx.FilePickerCtrl( self.pecat_tab, wx.ID_ANY, u"izlaz.txt", u"Odaberi datoteku", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		self.pc_izlaz_dat.SetBackgroundColour( wx.Colour( 230, 228, 176 ) )
		
		gSizer6.Add( self.pc_izlaz_dat, 0, wx.ALL, 5 )
		
		self.m_button55 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Prikazi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button55.SetForegroundColour( wx.Colour( 53, 53, 53 ) )
		self.m_button55.SetBackgroundColour( wx.Colour( 235, 231, 158 ) )
		
		gSizer6.Add( self.m_button55, 0, wx.ALL, 5 )
		
		self.m_button56 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Generiraj digitalni pecat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button56.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer6.Add( self.m_button56, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button57 = wx.Button( self.pecat_tab, wx.ID_ANY, u"Otvori digitalni pecat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button57.SetBackgroundColour( wx.Colour( 121, 188, 255 ) )
		
		gSizer6.Add( self.m_button57, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.rez_otvaranja = wx.TextCtrl( self.pecat_tab, wx.ID_ANY, u"Uspjesnost otvaranja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rez_otvaranja.SetBackgroundColour( wx.Colour( 226, 222, 175 ) )
		
		gSizer6.Add( self.rez_otvaranja, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.pecat_tab.SetSizer( gSizer6 )
		self.pecat_tab.Layout()
		gSizer6.Fit( self.pecat_tab )
		self.biljeznica.AddPage( self.pecat_tab, u"Digitalni pecat", False )
		
		bSizer3.Add( self.biljeznica, 1, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"traka4.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_bitmap1, 0, wx.ALL, 5 )
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		# Connect Events
		self.izlaz_dat.Bind( wx.EVT_FILEPICKER_CHANGED, self.func_definiran_izlaz )
		self.generiraj_sazetak.Bind( wx.EVT_BUTTON, self.func_generiraj_sazetak )
		self.prikazi_dat.Bind( wx.EVT_BUTTON, self.func_ulaz )
		self.prikazi_izlaz.Bind( wx.EVT_BUTTON, self.func_izlaz )
		self.m_button26.Bind( wx.EVT_BUTTON, self.prikazi_rsa_privatni )
		self.m_button27.Bind( wx.EVT_BUTTON, self.prikazi_rsa_javni )
		self.rsa_kljuc_duljina.Bind( wx.EVT_CHOICE, self.func_postavi_rsa )
		self.m_button28.Bind( wx.EVT_BUTTON, self.func_generiraj_kljuceve )
		self.ulaaaz.Bind( wx.EVT_BUTTON, self.prikazi_ulaz_rsa )
		self.izlaaaz.Bind( wx.EVT_BUTTON, self.prikazi_izlaz_rsa )
		self.m_button31.Bind( wx.EVT_BUTTON, self.func_rsa_kriptiraj )
		self.m_button32.Bind( wx.EVT_BUTTON, self.func_rsa_dekriptiraj )
		self.generiraj_aes_kljuc.Bind( wx.EVT_BUTTON, self.func_gen_kljuc_aes )
		self.prikazi_aes_ulaz.Bind( wx.EVT_BUTTON, self.aes_ulaz_dat )
		self.prikazi_aes_izlaz.Bind( wx.EVT_BUTTON, self.aes_dat_izlaz )
		self.m_button17.Bind( wx.EVT_BUTTON, self.func_aes_kriptiraj )
		self.m_button18.Bind( wx.EVT_BUTTON, self.func_aes_dekriptiraj )
		self.m_button19.Bind( wx.EVT_BUTTON, self.func_prikazi_aes_dec )
		self.izbor_aes.Bind( wx.EVT_CHOICE, self.func_postavi_kljuc )
		self.prikazi_aes_kljuc.Bind( wx.EVT_BUTTON, self.func_prikazi_aes_kljuc )
		self.m_button33.Bind( wx.EVT_BUTTON, self.prikazi_om_javni )
		self.m_button34.Bind( wx.EVT_BUTTON, self.prikazi_om_tajni )
		self.m_button35.Bind( wx.EVT_BUTTON, self.prikazi_om_ulaz )
		self.m_button36.Bind( wx.EVT_BUTTON, self.prikazi_om_izlaz )
		self.m_button37.Bind( wx.EVT_BUTTON, self.prikazi_om )
		self.m_button38.Bind( wx.EVT_BUTTON, self.func_generiraj_omotnicu )
		self.m_button39.Bind( wx.EVT_BUTTON, self.func_otvori_omotnicu )
		self.m_button40.Bind( wx.EVT_BUTTON, self.prikazi_pt_tajni )
		self.m_button41.Bind( wx.EVT_BUTTON, self.prikazi_pt_javni )
		self.m_button42.Bind( wx.EVT_BUTTON, self.prikazi_pt_ulaz )
		self.m_button43.Bind( wx.EVT_BUTTON, self.prikazi_pt )
		self.m_button46.Bind( wx.EVT_BUTTON, self.func_generiraj_potpis )
		self.m_button47.Bind( wx.EVT_BUTTON, self.func_provjeri_potpis )
		self.m_button48.Bind( wx.EVT_BUTTON, self.prikazi_pc_ulaz )
		self.m_button49.Bind( wx.EVT_BUTTON, self.prikazi_pc_javni_primatelja )
		self.m_button50.Bind( wx.EVT_BUTTON, self.prikazi_pc_tajni_posiljatelja )
		self.m_button51.Bind( wx.EVT_BUTTON, self.prikazi_pc_omotnica )
		self.m_button52.Bind( wx.EVT_BUTTON, self.prikazi_pc_potpis )
		self.m_button53.Bind( wx.EVT_BUTTON, self.prikazi_pc_javni_posiljatelja )
		self.m_button54.Bind( wx.EVT_BUTTON, self.prikazi_pc_tajni_primatelja )
		self.m_button55.Bind( wx.EVT_BUTTON, self.prikazi_pc_izlaz_dat )
		self.m_button56.Bind( wx.EVT_BUTTON, self.func_generiraj_pecat )
		self.m_button57.Bind( wx.EVT_BUTTON, self.func_otvori_pecat )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def func_definiran_izlaz( self, event ):
		event.Skip()
	
	def func_generiraj_sazetak( self, event ):
		event.Skip()
	
	def func_ulaz( self, event ):
		event.Skip()
	
	def func_izlaz( self, event ):
		event.Skip()
	
	def prikazi_rsa_privatni( self, event ):
		event.Skip()
	
	def prikazi_rsa_javni( self, event ):
		event.Skip()
	
	def func_postavi_rsa( self, event ):
		event.Skip()
	
	def func_generiraj_kljuceve( self, event ):
		event.Skip()
	
	def prikazi_ulaz_rsa( self, event ):
		event.Skip()
	
	def prikazi_izlaz_rsa( self, event ):
		event.Skip()
	
	def func_rsa_kriptiraj( self, event ):
		event.Skip()
	
	def func_rsa_dekriptiraj( self, event ):
		event.Skip()
	
	def func_gen_kljuc_aes( self, event ):
		event.Skip()
	
	def aes_ulaz_dat( self, event ):
		event.Skip()
	
	def aes_dat_izlaz( self, event ):
		event.Skip()
	
	def func_aes_kriptiraj( self, event ):
		event.Skip()
	
	def func_aes_dekriptiraj( self, event ):
		event.Skip()
	
	def func_prikazi_aes_dec( self, event ):
		event.Skip()
	
	def func_postavi_kljuc( self, event ):
		event.Skip()
	
	def func_prikazi_aes_kljuc( self, event ):
		event.Skip()
	
	def prikazi_om_javni( self, event ):
		event.Skip()
	
	def prikazi_om_tajni( self, event ):
		event.Skip()
	
	def prikazi_om_ulaz( self, event ):
		event.Skip()
	
	def prikazi_om_izlaz( self, event ):
		event.Skip()
	
	def prikazi_om( self, event ):
		event.Skip()
	
	def func_generiraj_omotnicu( self, event ):
		event.Skip()
	
	def func_otvori_omotnicu( self, event ):
		event.Skip()
	
	def prikazi_pt_tajni( self, event ):
		event.Skip()
	
	def prikazi_pt_javni( self, event ):
		event.Skip()
	
	def prikazi_pt_ulaz( self, event ):
		event.Skip()
	
	def prikazi_pt( self, event ):
		event.Skip()
	
	def func_generiraj_potpis( self, event ):
		event.Skip()
	
	def func_provjeri_potpis( self, event ):
		event.Skip()
	
	def prikazi_pc_ulaz( self, event ):
		event.Skip()
	
	def prikazi_pc_javni_primatelja( self, event ):
		event.Skip()
	
	def prikazi_pc_tajni_posiljatelja( self, event ):
		event.Skip()
	
	def prikazi_pc_omotnica( self, event ):
		event.Skip()
	
	def prikazi_pc_potpis( self, event ):
		event.Skip()
	
	def prikazi_pc_javni_posiljatelja( self, event ):
		event.Skip()
	
	def prikazi_pc_tajni_primatelja( self, event ):
		event.Skip()
	
	def prikazi_pc_izlaz_dat( self, event ):
		event.Skip()
	
	def func_generiraj_pecat( self, event ):
		event.Skip()
	
	def func_otvori_pecat( self, event ):
		event.Skip()
	

