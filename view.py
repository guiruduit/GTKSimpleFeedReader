import gtk
# import webkit

class GUIFeedReader(object):

	def __init__(self):
		self.construct_window()
		self.window.show_all()

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
		
		textview = gtk.TextView()
		self.buffer = textview.get_buffer()
		
		hbox = gtk.HBox()
		hbox.pack_start(self.edit_add_feader)
		hbox.pack_start(self.button_add)
		hbox.pack_start(self.button_refresh)
		
		scrollframe = gtk.ScrolledWindow()
		# scrollframe.add(self.webview)
		scrollframe.add(textview)
		
		vbox = gtk.VBox()
		vbox.pack_start(hbox, False)
		vbox.pack_start(self.combo_feaders, False)
		vbox.pack_start(self.combo_feeds, False)
		vbox.pack_start(scrollframe)

		self.window.add(vbox)
