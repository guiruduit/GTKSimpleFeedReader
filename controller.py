from view import GUIFeedReader, GUILogin
from model import Feader, Feed

class FeedReader(object):

	feaders = []; feeds = []

	# For GUILogin window:

	def __init__(self):
		self.gui_login = GUILogin()
		self.gui_login.button_login.connect('clicked', self.load_user_urls)
		self.gui_login.run_gtk()

	def load_user_urls(self, button):
		self.gui = GUIFeedReader()
		self.user_file_name = 'GTKSimpleFeedReader/user_files/' + self.gui_login.edit_login.get_text() + '.txt'
		user_file = open(self.user_file_name, "r")
		user_url_list = user_file.readlines()
		for url in user_url_list: self.add_feader(url)
		self.start_FeedReader()

	# For GUIFeedReader window:

	def start_FeedReader(self):
		self.gui.combo_feaders.append_text('Todos')
		self.connect_FeedReader_events()
		self.gui.run_gtk()

	def connect_FeedReader_events(self):
		self.gui.button_add.connect('clicked', self.create_and_add_new_feader)
		self.gui.button_refresh.connect('clicked', self.refresh_feeds)
		self.gui.combo_feaders.connect('changed', self.select_feader)
		self.gui.combo_feeds.connect('changed', self.select_feed)

	def create_and_add_new_feader(self, button):
		url = self.gui.edit_add_feader.get_text()
		self.clear_edit_add_feader()
		self.add_feader(url)
		user_file = open(self.user_file_name, "a")
		user_file.write(url + '\n')
		user_file.close()

	def clear_edit_add_feader(self):
		self.gui.edit_add_feader.set_text('')

	def add_feader(self, url):
		new_feader = Feader(url)
		self.feaders.append(new_feader)
		self.gui.combo_feaders.append_text(new_feader.title)
		self.add_feader_feeds(new_feader)

	def add_feader_feeds(self, new_feader):
		self.feeds.extend(new_feader.get_feeds())
		self.feeds = self.__quicksort(self.feeds)
		self.__add_all_feeds_to_combo_feeds()

	def __quicksort(self, list_feeds):
		if len(list_feeds) <= 1:
			return list_feeds
		middle = list_feeds[0].date
		return self.__quicksort([feed for feed in list_feeds if feed.date > middle]) + \
			[feed for feed in list_feeds if feed.date == middle] + \
			self.__quicksort([feed for feed in list_feeds if feed.date < middle])

	def __add_all_feeds_to_combo_feeds(self):
		self.__clear_combo_feeds()
		for feed in self.feeds:
			self.gui.combo_feeds.append_text(feed.title)

	def __add_feader_feeds_to_combo_feeds(self, feader):
		self.__clear_combo_feeds()
		list_feeds = feader.get_feeds()
		for feed in list_feeds:
			self.gui.combo_feeds.append_text(feed.title)

	def select_feader(self, combobox):
		if self.gui.combo_feaders.get_active_text() == 'Todos': self.__add_all_feeds_to_combo_feeds()
		else:
			feader_selected = [feader for feader in self.feaders if feader.title == self.gui.combo_feaders.get_active_text()]
			if feader_selected: self.__add_feader_feeds_to_combo_feeds(feader_selected[0])
			else: print 'error'

	def select_feed(self, combobox):
		feed_selected = None
		while not feed_selected:
			feed_selected = [feed.description for feed in self.feeds if feed.title == self.gui.combo_feeds.get_active_text()]
			if not feed_selected: feed_selected = ' '
		self.gui.webview.load_html_string(feed_selected[0], '')

	def clear_feeds(self):
		self.feeds = []
		self.__clear_combo_feeds()

	def __clear_combo_feeds(self):
		model = self.gui.combo_feeds.get_model()
		model.clear()

	def refresh_feeds(self, btn):
		self.clear_feeds()
		for feader in self.feaders:
			feader.reset()
			self.feeds.extend(feader.get_feeds())
