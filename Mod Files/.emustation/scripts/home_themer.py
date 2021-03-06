'''
	Script by Rocky5
	Used to build the home menu system.
'''
import fileinput, os, sys, time, xbmc, xbmcgui
#####	Start markings for the log file.
print "| .emustation\Scripts\home_themer.py loaded."
pDialog					= xbmcgui.DialogProgress()
dialog					= xbmcgui.Dialog()
## Not used now as I changed the source code to reload almost instantly.
#Select_Theme		= sys.argv[1:][0]
# try:
	# if Select_Theme == "1":
		# xbmc.executebuiltin( 'Skin.Theme(1)' )
# except: pass

# try:
	# if Select_Theme == "0":
		# xbmc.executebuiltin( 'Skin.Theme(-1)' )
# except: pass

# Delay to it gives the system time to update the current theme entry.
# time.sleep(0.2)

dialog				= xbmcgui.Dialog()
time.sleep(1)
HomeLayout 			= xbmc.getInfoLabel( 'Skin.CurrentTheme' )
Home_XML_Path		= xbmc.translatePath( 'special://skin/720p/Home.xml' )
Default_Layout_File	= xbmc.translatePath( 'special://xbmc/.emustation/layouts/home/skindefault.xml' )
Layout_File			= xbmc.translatePath( 'special://xbmc/.emustation/layouts/home/' + HomeLayout + '.xml' )
System_List			= xbmc.translatePath( 'special://xbmc/.emustation/layouts/home/other/system_list.xml' )
Header_Data			= '<window id="0">\n\
	<defaultcontrol always="true">9000</defaultcontrol>\n\
	<controls>\n\
		<control type="button" id="9100">\n\
			<posx>-500</posx>\n\
			<onclick>-</onclick>\n\
		</control>\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
			<onfocus>ActivateWindow(Screensaver)</onfocus>\n\
			<visible>!Player.HasAudio</visible>\n\
		</control>\n\
		<control type="button" id="9999">\n\
			<posx>-500</posx>\n\
			<onfocus>ActivateWindow(2006)</onfocus>\n\
			<visible>Player.HasAudio</visible>\n\
		</control>\n\
		<include>CommonBackground</include>\n\
		<control type="group">\n\
			<animation effect="fade" start="100" end="0" time="150" condition="Skin.HasSetting(favsloading)">Conditional</animation>\n\
			<animation effect="fade" start="0" end="100" delay="300" time="150" condition="!Skin.HasSetting(favsloading)">Conditional</animation>\n\
	'
Footer_Data				= '\n\
	</control>\n\
	</controls>\n\
</window>'
if os.path.isfile( Layout_File ):
	try:
		os.remove(Home_XML_Path)
		with open( Layout_File ) as layoutfile:
			with open(Home_XML_Path, "w") as inputfile:
				inputfile.write( Header_Data )
				for code in layoutfile:
					inputfile.write( code )
				inputfile.write( Footer_Data )
	except:
		pass
else:
	if os.path.isfile( Default_Layout_File ):
		try:
			os.remove(Home_XML_Path)
			with open( Default_Layout_File ) as layoutfile:
				with open(Home_XML_Path, "w") as inputfile:
					inputfile.write( Header_Data )
					for code in layoutfile:
						inputfile.write( code )
					inputfile.write( Footer_Data )
		except:
			pass
	else:
		dialog.ok("ERROR!","skindefault.xml is missing from","Q:\\.emustation\\layouts\\home\\","Reinstall this file to fix the issue.")
if os.path.isfile( System_List ):
	try:
		with open( System_List ) as fin:
				fin = fin.read()
				for line in fileinput.FileInput(Home_XML_Path,inplace=1):
					if '</focusedlayout>' in line:
						line = line.replace(line,line+fin)
					print line,
	except:
		pass
else:
	dialog.ok("ERROR!","system_list.xml is missing from","Q:\\.emustation\\layouts\\home\\other\\","Reinstall this file to fix the issue.")
xbmc.executebuiltin( 'ReloadSkin' ) # required for the custom them selector to reload the skin and apply the new theme.