from view import GUIFeedReader
from model import Feader, Feed

class FeedReader(object):

	feaders = []; feeds = []

	def __init__(self):
		self.gui = GUIFeedReader()
		self.gui.button_add.connect('clicked', self.add_feader)
		# self.gui.button_refresh.connect('clicked', self.refresh_feeds)
		self.gui.combo_feaders.connect('changed', self.select_feader)
		self.gui.combo_feaders.append_text('Todos')
		self.gui.combo_feeds.connect('changed', self.select_feed)
		self.gui.window.show_all()

	def add_feader(self, button):
		new_feader = Feader(self.gui.edit_add_feader.get_text())
		self.gui.edit_add_feader.set_text('')
		# add feader
		self.feaders.append(new_feader)
		self.gui.combo_feaders.append_text(new_feader.title)
		# add feader feeds
		self.feeds = self.__quicksort(self.feeds + new_feader.get_feeds())
		self.__add_all_feeds_to_combo_feeds()

	def __quicksort(self, list_feeds):
		if len(list_feeds) <= 1:
			return list_feeds
		middle = list_feeds[0].date
		return self.__quicksort([feed for feed in list_feeds if feed.date > middle]) + \
			[feed for feed in list_feeds if feed.date == middle] + \
			self.__quicksort([feed for feed in list_feeds if feed.date < middle])

	def __clear_combo_feeds(self):
		model = self.gui.combo_feeds.get_model()
		model.clear()

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
		if self.gui.combo_feaders.get_active_text() == 'Todos':
			self.__add_all_feeds_to_combo_feeds()
		else:
			feader_selected = [feader for feader in self.feaders if feader.title == self.gui.combo_feaders.get_active_text()]
			if feader_selected: self.__add_feader_feeds_to_combo_feeds(feader_selected[0])
			else: print 'error'

	def select_feed(self, combobox):
		feed_selected = None
		while not feed_selected:
			feed_selected = [feed.description for feed in self.feeds if feed.title == self.gui.combo_feeds.get_active_text()]
			if not feed_selected: feed_selected = ' '
		self.gui.buffer.set_text(feed_selected[0])

	def refresh_feeds(self, btn):
		self.feeds = []
		self.__clear_combo_feeds()
		for feader in self.feaders:
			feader.reset()
			self.feeds = self.feeds + feaders.get_feeds()
