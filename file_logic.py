# -*- coding: utf-8 -*-
import os


def new_user(user_id):
	path = os.path.join(".", "users", f"{user_id}")
	os.mkdir(path)


def create_new_list(user_id, name):
	if str(user_id) not in os.listdir(os.path.join(".", "users")):
		new_user(user_id)
	if name in os.listdir(os.path.join(".", "users", f"{user_id}")):
		return False
	else:
		f = open(os.path.join(".", "users", f"{user_id}", f"{name}"), "w")
		f.close()
		return True


def show_my_lists(user_id):
	return os.listdir(os.path.join(".", "users",f"{user_id}"))
