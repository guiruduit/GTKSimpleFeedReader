#!/usr/bin/env python
# -*- encoding: utf-8 -*-

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
		self.gui_login.window.destroy()
		self.start_FeedReader()

	# For GUIFeedReader window:

	def start_FeedReader(self):
		self.gui.combo_feaders.append_text('Todos')
		self.connect_FeedReader_events()
		self.gui.run_gtk()

	def connect_FeedReader_events(self):
		self.gui.button_add.connect('clicked', self.get_url_to_feader)
		self.gui.button_refresh.connect('clicked', self.refresh_feeds)
		self.gui.combo_feaders.connect('changed', self.select_feader)
		self.gui.combo_feeds.connect('changed', self.select_feed)

	def get_url_to_feader(self, button):
		url = self.gui.edit_add_feader.get_text()
		# self.clear_data_from([self.gui.edit_add_feader])

		# solution for now:
		self.gui.edit_add_feader.set_text('')
		#-----------------

		self.add_feader(url)
		self.add_feader_url_to_file(url)

	def add_feader(self, url):
		new_feader = Feader(url)
		self.feaders.append(new_feader)
		self.gui.combo_feaders.append_text(new_feader.title)
		self.add_feader_feeds(new_feader)

	def add_feader_url_to_file(self, url):
		user_file = open(self.user_file_name, "a")
		user_file.write(url + '\n')
		user_file.close()

	def add_feader_feeds(self, new_feader):
		self.feeds.extend(new_feader.get_feeds())
		self.feeds = self.__quicksort(self.feeds)
		self.add_feeds_to_combo_from()

	def __quicksort(self, list_feeds):
		if len(list_feeds) <= 1: return list_feeds
		middle = list_feeds[0].date
		return self.__quicksort([feed for feed in list_feeds if feed.date > middle]) + \
			[feed for feed in list_feeds if feed.date == middle] + \
			self.__quicksort([feed for feed in list_feeds if feed.date < middle])

	def add_feeds_to_combo_from(self, feader=None):

		# self.clear_data_from([self.gui.combo_feeds.get_model()])
		# solution for now:
		model = self.gui.combo_feeds.get_model()
		model.clear()
		# -----------------

		if feader == None: feeds_list = self.feeds
		else: feeds_list = feader.get_feeds()
		for feed in feeds_list: self.gui.combo_feeds.append_text(feed.title)

	def select_feader(self, combobox):
		if self.gui.combo_feaders.get_active_text() == 'Todos': self.add_feeds_to_combo_from()
		else:
			feader_selected = [feader for feader in self.feaders if feader.title == self.gui.combo_feaders.get_active_text()]
			# se retornar vazio a funcao add_feeds_to_combo_from() coloca todos os feeds na combo
			self.add_feeds_to_combo_from(feader_selected[0])

	def select_feed(self, combobox):
		if self.gui.combo_feeds.get_active_text() != '':
			feed_selected = [feed.description for feed in self.feeds if feed.title == self.gui.combo_feeds.get_active_text()]
			# self.gui.webview.load_html_string(feed_selected[0], '')
			self.gui.buffer.set_text(feed_selected[0])

	def refresh_feeds(self, btn):
		# self.clear_data_from([self.feeds, self.combo_feeds.get_model()])

		# solution for now:
		self.feeds = []
		model = self.gui.combo_feeds.get_model()
		model.clear()
		# ----------------
		
		for feader in self.feaders:
			feader.reset()
			self.feeds.extend(feader.get_feeds())

# Doesn't work yet:

	def clear_data_from(self, objs):
		# dict_clear_function = {
		# 	'list': lambda obj: clear_list(obj),
		# 	'gtk.Entry': lambda obj: obj.set_text(''),
		# 	'gtk.combo_box_new_text': lambda obj: obj.clear(),
		# }
		# for obj in objs: dict_clear_function.get(type(obj))()
		# def clear_list(l): l = []
		for obj in objs:
			if type(obj) == 'list': obj = []
			elif type(obj) == 'gtk.Entry': obj.set_text('')
			elif type(obj) == 'gtk.ListStore': obj.clear()
			else: pass
