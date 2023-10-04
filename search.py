class SimpleSearchEngine:
    def __init__(self):
        self.documents = {}

    def add_document(self, doc_id, content):
        self.documents[doc_id] = content

    def search(self, query):
        results = []
        for doc_id, content in self.documents.items():
            if query.lower() in content.lower():
                results.append(doc_id)
        return results


# Creating an instance of the search engine
search_engine = SimpleSearchEngine()

# Adding documents
search_engine.add_document(1, "Python is a popular programming language.")
search_engine.add_document(2, "Web development with Django is fun.")
search_engine.add_document(3, "Searching algorithms are important in computer science.")

# Performing searches
query = input("Enter your search query: ")
search_results = search_engine.search(query)

if search_results:
    print("Search results:")
    for doc_id in search_results:
        print(f"Document {doc_id}: {search_engine.documents[doc_id]}")
else:
    print("No results found.")
