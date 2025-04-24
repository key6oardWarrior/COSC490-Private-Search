from sys import platform
from sys import path
from os.path import join
path.append(join(path[0], "SearchAPI"))

from PyGUI import Window, Button, Text, Column

from SearchAPI.search import Search
from AnonSystem import AnonSystem
from helper import exit_app, WIN_NAME, WIDTH, HEIGHT

def break_up_text(text: str) -> str:
	cnt = 0
	for ii in range(len(text)):
		if (cnt >= 200) and (text[ii] == " "):
			cnt = 0
			text = text[0: ii] + "\n" + text[ii + 1:]
		else:
			cnt += 1
	return text

def query_page(anon: AnonSystem, query: str, query_type: str, safe_search: str) -> None:
	search = Search()
	results: list[dict[str, str]] = None
	SEPARATOR = "----------"

	if query_type == "web":
		results = search.query(query, safe_search=safe_search)
	else:
		results = search.news(query, safe_search=safe_search)

	quick_answer: dict[str, str] = search.get_assisted_answers()

	layout = []
	if quick_answer["quick_answer"] is None and quick_answer["definition"] is None:
		layout.append([Text("Quick Answer: None")])
	else:
		if quick_answer["quick_answer"]:
			ans = break_up_text(quick_answer["quick_answer"])
			source = quick_answer["quick_answer_source"]
			url = quick_answer["quick_answer_url"]
			layout.append([Text(f"Quick Answer:\n{ans}")])
			layout.append([Text(f"Source: {source}")])
			layout.append([Button(f"URL: {url}"), Button(f"Open in Tor", key=f"tor-{url}")])
		else:
			ans = break_up_text(quick_answer["definition"])
			source = quick_answer["definition_source"]
			url = quick_answer["definition_url"]
			layout.append([Text(f"Quick Answer:\n{ans}")])
			layout.append([Text(f"Source: {source}")])
			layout.append([Button(f"URL: {url}", Button(f"Open in Tor", key=f"tor-{url}"))])

	layout.append([Text(SEPARATOR)])

	results_layout = []
	url_key = "href" if query_type == "web" else "url"
	for result in results:
		href = result[url_key]
		title = result["title"]
		body = break_up_text(result["body"])
		results_layout.append([Button(f"URL: {href}"), Button(f"Open in Tor", key=f"tor-{href}")])
		results_layout.append([Text(f"Title: {title}")])
		results_layout.append([Text(f"Body: {body}")])
		results_layout.append([Text(SEPARATOR)])

	results_column = Column(results_layout, key='-RESULTS-', scrollable=True, size=(WIDTH, HEIGHT))
	layout.append([results_column])

	results_page = Window(WIN_NAME, layout, finalize=True)

	while True:
		event, values = results_page.read()
		if exit_app(event, results_page, False):
			return
		
		if "URL: " in event:
			href = event.split("URL: ")[1]
			if platform == "linux":
				anon.proxychains(href)

		elif "tor-" in event:
			if platform == "linux":
				try:
					anon.tor(event[4:])
				except FileNotFoundError:
					Window("ERROR", [[Text("Tor browser location not set", text_color="red")]]).read()