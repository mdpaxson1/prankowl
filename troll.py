from bs4 import BeautifulSoup
import mechanize

url = 'http://www.prankowl.com/#operatorprank'
numbers={
		'Will'    : 9044519026,
		'Me'      : 9043034359,
		'Alex'    : 9045716116,
		'Brandon' : 9045241603,
		'Austin'  : 9042546406
	}


br = mechanize.Browser()
#br.set_all_readonly(False)
br.set_handle_robots(False)
br.set_handle_refresh(False)
br.addheaders=[('User-agent', 'Firefox')]

site = br.open(url, timeout=5)
print site.read()

#find the forms
for form in br.forms():
	print "Form name:", form.name
	print form


br.select_form('sound_prank')
#br.form["number1"] = numbers['Alex']
#br.form["callerid1"] = numbers['Alex']
#br.form["numbers2"] = numbers['Brandon']
#br.form["callerid2"] = numbers['Brandon']


for control in br.form.controls:
	print control
	print "type=%s, name=%s, value=%s"%(control.type,control.name,br[control.name])
		
	

#soup = BeautifulSoup(browser.response().read())
#body_tag = soup.body

