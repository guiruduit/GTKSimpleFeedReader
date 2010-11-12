import gtk
# import webkit

class GUILogin(object):

	def __init__(self):
		self.construct_window()
		self.window.show_all()

	def run_gtk(self):
		gtk.main()

	def construct_window(self):
		self.window = gtk.Window()
		self.window.set_title("Login - Feed Reader")
		self.edit_login = gtk.Entry()
		label_login = gtk.Label("User: ")
		self.button_login = gtk.Button("Go to my Feeds")

		hbox = gtk.HBox()
		hbox.pack_start(label_login, False)
		hbox.pack_start(self.edit_login, False)

		vbox = gtk.VBox()
		vbox.pack_start(hbox, False)
		vbox.pack_start(self.button_login)
		self.window.add(vbox)

class GUIFeedReader(object):

	def __init__(self):
		self.construct_window()
		self.window.show_all()

	def run_gtk(self):
		gtk.main()

	def construct_window(self):
		self.window = gtk.Window()
		self.window.set_title("Feed Reader")
		self.window.resize(1000, 700)
		self.edit_add_feader = gtk.Entry()
		self.button_add = gtk.Button("Add")
		self.button_refresh = gtk.Button(stock = gtk.STOCK_REFRESH)
		self.combo_feaders = gtk.combo_box_new_text()
		self.combo_feeds = gtk.combo_box_new_text()
		# self.webview = webkit.WebView()

		hbox = gtk.HBox()
		hbox.pack_start(self.edit_add_feader)
		hbox.pack_start(self.button_add)
		hbox.pack_start(self.button_refresh)

		scrollframe = gtk.ScrolledWindow()
		# scrollframe.add(self.webview)

		# solution for now:
		textview = gtk.TextView()
		self.buffer = textview.get_buffer()
		scrollframe.add(textview)
		# -----------------

		vbox = gtk.VBox()
		vbox.pack_start(hbox, False)
		vbox.pack_start(self.combo_feaders, False)
		vbox.pack_start(self.combo_feeds, False)
		vbox.pack_start(scrollframe)
		self.window.add(vbox)
