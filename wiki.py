import wikipedia

def get_page_summary():
   while True:
       title = input("Enter a Wikipedia page title or search phrase (or press ENTER to quit): ")
       if title == '':
           break
       try:
           page = wikipedia.page(title, autosuggest=False)
           print("Title:", page.title)
           print("Summary:", page.summary)
           print("URL:", page.url)
       except wikipedia.exceptions.DisambiguationError as e:
           print(f"DisambiguationError: {e.options}")
       except wikipedia.exceptions.PageError:
           print("Error: Page not found.")

if __name__ == "__main__":
    get_page_summary()