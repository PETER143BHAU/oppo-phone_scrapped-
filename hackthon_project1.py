from selenium import webdriver
from bs4 import BeautifulSoup
from pprint import pprint as pp
import time,os
import json
def main():
	final_list=[]
	if os.path.exists('hackthon.json') :
		opened=open('hackthon.json','r')
		po=json.load(opened)
		time.sleep(8)
		pp(po)
		pass		
	else:	
		for main in range(4): 
			driver=webdriver.Chrome('/home/peter/chromedriver_linux (1)/chromedriver')
			a=driver.get('https://www.flipkart.com/search?q=oppo+phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY'+'&suggestionId=oppo+phone&requestId=a032e5fe-45cd-41e7-bb85-3d7ed9c098a7&page='+str(main))
			html=driver.execute_script('return document.documentElement.outerHTML;')
			soup=BeautifulSoup(html,'html.parser')
			driver.close()
			div=soup.find_all('div',class_='bhgxx2 col-12-12')
			# photo_data=soup.find_all('div',class_='_3BTv9X')
			

			count=1
			count_1=1
			# for ph in photo_data:
				# photo=(ph.img['src'])
			for j in div:
				last=1
				time.sleep(2)					
				names=j.find_all('div',class_='_3wU53n')
				price=j.find_all('div',class_='_1vC4OE _2rQ-NK')
				ram=j.find_all('li',class_='tVe95H')


				co=1				
				for data in names:
					list_1=(data).get_text()
				for pr in price:
					list_2=(pr.get_text())
				for r in ram:
					det=(r.get_text())
					op=(co,det)
					co+=1
					countant=1
					for s in op:
						if s==1:
							list_3=(det[0:9])
							list_4=(det[11:21])
						if s==2:
							list_5=(det)
						if s==5:
							list_6=(det)
							final_dic={'name_of_phone':list_1,'price':list_2,'ram':list_3,'rom':list_4,'display':list_5,'processor':list_6,'position':count_1}
							count_1+=1
							pp(final_dic)
							final_list.append(final_dic)
													
							if final_dic['position']==24:
								print('NEXT PAGE::::',)
								countant+=1
	ope=open('hackthon.json','a')
	js=json.dump(final_list,ope,indent=4)
	ope.close()
	main3=open('phone.html','w+')
	names1=main3.write('<html>\n')
	names2=main3.write('<head>\n')
	names3=main3.write('<title>oppo</title>\n')
	names4=main3.write('</head>\n')
	names5=main3.write('<body>\n')
	names6=main3.write('<table border=1px>\n')
	names7=main3.write('<tr style="font-size:30px">\n<td>s no.</td>\n<td>NAME OF PHONE</td>\n<td>PRICE</td>\n<td>RAMS</td>\n<td>ROMS</td>\n<td>DISPLAY</td>\n<td>PROCESSOR</td>\n</tr>\n')
	names8=main3.write('<tr style="font-size:20px">')
	main_count=1
		
	for main_data in final_list:
		nam1=main_data['name_of_phone']
		nam2=main_data['price']
		nam3=main_data['ram']
		nam4=main_data['rom']
		nam5=main_data['display']
		nam6=main_data['processor']

		names9=main3.write('<td>'+str(main_count)+'</td>'+'<td>'+nam1+'</td>'+'<td>'+nam2+'</td>'+'<td>'+nam3+'</td>'+'<td>'+nam4+'</td>'+'<td>'+nam5+'</td>'+'<td>'+nam6+'</td>'+'<tr style="font-size:20px">')
	
		main_count+=1
	names10=main3.write('</tr>')

	names8=main3.write('</table>')

	names9=main3.write('</body>')
	names10=main3.write('</html>')
main()



























			





		


# 																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																									