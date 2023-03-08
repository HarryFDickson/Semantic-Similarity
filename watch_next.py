import spacy

# Load the spacy model
nlp = spacy.load("en_core_web_md")

# Define a function to calculate the similarity between two documents
def similarity(doc1, doc2):
    return doc1.similarity(doc2)

# Read in the movies from the file
movies = []
with open("movies.txt", "r") as f:
    for line in f:
        movies.append(line.strip())

# Define a function to find the most similar movie to a given description
def find_similar_movie(description):
    # Create a spacy document from the description
    desc_doc = nlp(description)

    # Calculate the similarity between the description and each movie
    sim_scores = []
    for movie in movies:
        movie_doc = nlp(movie.split(':')[1].strip())
        sim_scores.append(similarity(desc_doc, movie_doc))

    # Find the index of the most similar movie
    max_index = sim_scores.index(max(sim_scores))

    # Return the title of the most similar movie
    return movies[max_index].split(':')[0].strip()

# Test the function with the Planet Hulk description
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."
print(find_similar_movie(description))
