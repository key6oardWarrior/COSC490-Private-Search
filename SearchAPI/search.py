from requests import get
from copy import deepcopy

from duckduckgo_search import DDGS

from results import Results

class Search:
	__PARAMS = {"q": None, "format": "json"}
	__URL = "https://api.duckduckgo.com/"
	__json_results: dict[str, str] = {
		"quick_answer": None,
		"quick_answer_source": None,
		"quick_answer_url": None,
		"definition": None,
		"definition_source": None,
		"definition_url": None
	}
	__MODELS = ["gpt-4o-mini", "llama-3.3-70b", "claude-3-haiku", "o3-mini", "mistral-small-3"]
	__search_engine = DDGS()

	def __init__(self) -> None:
		pass

	def query(self, query: str, max_results: int=25, safe_search: str="off") -> list[dict[str, str]]:
		'''
		# Description:
		Search for the internet for links related to the user's query.

		# Params:
		`query` - User's search query\n
		`max_results` (optional) - Max amount of results to return. Default 25\n
		`safe_search` (optional) - "on", "moderate", "off". Defaults to "off".

		# Returns:
		List of dictionaries with search results. The dict keys are "title",
		"herf", and "body"
		'''
		params = deepcopy(self.__PARAMS)
		params["q"] = query
		result = Results(get(self.__URL, params=params).json())

		if result.answer:
			self.__json_results["quick_answer"] = result.answer
			self.__json_results["quick_answer_source"] = result.source
			self.__json_results["quick_answer_url"] = result.url

		elif result.definition:
			self.__json_results["definition"] = result.definition
			self.__json_results["definition_source"] = result.source
			self.__json_results["definition_url"] = result.url

		return DDGS().text(query, max_results=max_results, safesearch=safe_search)

	def chat(self, msg: str, model: str="gpt-4o-mini", timeout: int=30) -> str:
		'''
		# Description:
		Chat with a model. To end chat type "end chat"

		# Params:
		`model` (optional) - The model to use: "gpt-4o-mini", "llama-3.3-70b",
		"claude-3-haiku", "o3-mini", "mistral-small-3". Defaults to
		"gpt-4o-mini".\n
		`timeout` (optional) -  Timeout value for the HTTP client. Defaults to 30.

		# Returns:
		Responce from the LLM
		'''
		return self.__search_engine.chat(msg, model=model, timeout=timeout)

	def news(self, keywords: str, region: str="wt-wt", safe_search: str="off", time_limit: str="w", max_results: int=25) -> list[dict[str, str]]:
		"""
		# Description:
		News search

		# Params:
		`keywords` - keywords for query\n
		`region` - "wt-wt", "us-en", "uk-en", etc. Defaults to "wt-wt"\n
		`safe_search` - "on", "moderate", "off". Defaults to "off"\n
		`time_limit` - "d", "w", "m". Defaults to Nonen\n
		`max_results` - max number of results. If None, returns results only from
		the first response. Defaults to 25

		# Returns:
		List of dictionaries with news search results. The keys are: "date",
		"title", "body", "url", "image", and "source"
		"""
		return DDGS().news(keywords=keywords, region=region, safesearch=safe_search, timelimit=time_limit, max_results=max_results)

	def get_assisted_answers(self) -> dict[str, str]:
		return self.__json_results

	@property
	def models(self) -> list[str]:
		return self.__MODELS
