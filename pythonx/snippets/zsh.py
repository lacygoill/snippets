# coding: utf-8

import re
import px.whitespaces
import px.buffer

def is_zgen_section():
	line = px.buffer.get_prev_nonempty_line()
	if re.search('zgen load', line):
		return True

	return False
