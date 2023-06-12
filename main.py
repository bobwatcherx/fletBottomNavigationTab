from flet import *

def main(page:Page):
	page.window_width=300
	page.scroll = "always"

	# DEFINE ICONS
	myicons = [
	"home","create","person","settings",
	"favorite","grade","shopping_cart_checkout",
	"expand_circle_down"
	]

	def youchange(e):
		# AND IF YOU CHANGE ICON THEN 
		# I WILL CHANGE SCREEN Text NAME AND ICON
		# AND GET YOU SELECTED INDEX IN YOU TAB
		youindex = e.control.selected_index
		# GET ICON NAME IN YOU TAB CLICK
		namescreen = e.control.tabs[youindex].tab_content.name

		if youindex == 0 :
			# THIS FOR CHANGE ICON
			mylist.content.controls[0].name = namescreen
			# AND THIS FOR CHANGE TEXT SCREN NAME
			mylist.content.controls[1].value = f"{namescreen} screen"
		if youindex == 1:
			mylist.content.controls[0].name = namescreen
			mylist.content.controls[1].value = f"{namescreen} screen"
		if youindex == 2:
			# THIS FOR CHANGE ICON
			mylist.content.controls[0].name = namescreen
			# AND THIS FOR CHANGE TEXT SCREN NAME
			mylist.content.controls[1].value = f"{namescreen} screen"
		if youindex == 3 :
			mylist.content.controls[0].name = namescreen
			mylist.content.controls[1].value = f"{namescreen} screen"
				
		if youindex == 4 :
			# THIS FOR CHANGE ICON
			mylist.content.controls[0].name = namescreen
			# AND THIS FOR CHANGE TEXT SCREN NAME
			mylist.content.controls[1].value = f"{namescreen} screen"
		if youindex == 5 :
			mylist.content.controls[0].name = namescreen
			mylist.content.controls[1].value = f"{namescreen} screen"
		if youindex == 6 :
			# THIS FOR CHANGE ICON
			mylist.content.controls[0].name = namescreen
			# AND THIS FOR CHANGE TEXT SCREN NAME
			mylist.content.controls[1].value = f"{namescreen} screen"
		if youindex == 7 :
			mylist.content.controls[0].name = namescreen
			mylist.content.controls[1].value = f"{namescreen} screen"
					
		page.update()




	# NOW CREATE TABS
	t = Tabs(
		selected_index=0,
		animation_duration=100,
		indicator_color="white",
		divider_color="green",
		scrollable=True,
		on_change=youchange,
		tabs=[]

		)

	# NOW YOU ICON ICON APPEND TO TABS
	for x in myicons:
		t.tabs.append(
			Tab(
				tab_content=Icon(
					name=x,
					size=25,
					color="white"
					)
				)
			)



	mylist = Container(
		margin=margin.only(
			top=page.window_height/2
			),
		content=Column([
			Icon(name="home",size=50),
			Text("home Screen",size=30)
			],alignment="center")
		)
	listnavicon = Container(
		# ADD SHADOW TO Container
		shadow = BoxShadow(
			spread_radius=1,
			blur_radius=15
			),
		margin=margin.only(
			top=page.window_height-100,
			left=10,
			right=10
			),
		border_radius=30,
		width=page.window_width,
		bgcolor="green",
		padding=10,
		content=t


		)

	def youtaphere(e):
		# IF YOU CLICK CIRCLE ADD THEN OPEN DIALOG
		page.dialog = AlertDialog(
			title=Text("Open you dialog",size=30),
			content=Text("this sample"),
			actions=[
			ElevatedButton("CLose"),
			ElevatedButton("test")
			],

			)
		page.dialog.open = True
		page.update()



	# AND NOW CREATE BOTTOM NAVIGATION IN BOTTOM
	page.overlay.append(
		Stack([
			ResponsiveRow([
				Column(col=12,controls=[
					listnavicon
					])
				]),
			# AND CREATE CIRCLE ADD ICON CONTAINER
			Container(
				padding=10,
			margin=margin.only(
			top=page.window_height-150,
			left=page.window_width/2-35,
			right=page.window_width/2-35,
				),
			bgcolor="green",
			border=border.all(5,"white"),
			shape=BoxShape.CIRCLE,
			content=GestureDetector(
				mouse_cursor=MouseCursor.CLICK,
				on_tap=youtaphere,
				content=Icon(name="add",size=40)
				)
				)

			])


		)



	page.add(
		Row([
			mylist
			],alignment="center")
		)

flet.app(target=main)
