# Task 3: Movie Rating Management System

movies = [
    ("Inception", "Sci-Fi"),
    ("Titanic", "Romance"),
    ("Avengers", "Action")
]

ratings = {}

for movie, genre in movies:
    print(f"\nEnter 3 ratings (1–10) for {movie} ({genre}):")
    movie_ratings = []
    for i in range(3):
        rate = int(input(f"Rating {i+1}: "))
        movie_ratings.append(rate)
    ratings[movie] = movie_ratings

print("\n--- Movie Ratings ---")
for movie, genre in movies:
    avg = sum(ratings[movie]) / len(ratings[movie])
    print(f"{movie} ({genre}) - Average Rating: {avg:.2f}")
    
    if avg >= 8:
        print("→ Highly Rated ")
    elif avg >= 5:
        print("→ Average Movie ")
    else:
        print("→ Needs Improvement ")
