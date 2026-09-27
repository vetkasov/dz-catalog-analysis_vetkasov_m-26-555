import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155,
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies: list[dict]) -> float:
    """Calculation mean rating for provided movies"""
    ratings = [movie["rating"] for movie in movies]
    return round(sum(ratings) / len(ratings), 1)


def catalog_age_stats(movies: list[dict], current_year=2026) -> tuple:
    """Get years data for provided movies"""
    years = [
        current_year - movie["year"]
        for movie in movies
        if movie["year"] < current_year
    ]
    min_year = min(years)
    max_year = max(years)
    mean_year = math.ceil(round(sum(years) / len(years), 1))
    return (max_year, min_year, mean_year)


def duration_in_hours(minutes: int) -> str:
    """Get minutes into string format ##ч ##м"""
    duration = f"{minutes // 60}ч {minutes % 60}м"
    return duration


def rating_tier(rating: float) -> str:
    """Return movie category"""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    return "средне" if rating >= 5 else "слабо"


def decade_label(year: int) -> str:
    """Return movie label"""
    match year:
        case _ if year >= 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


def print_not_comedy_titles(movies: list[dict]) -> None:
    """Print titles without comedy genre"""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(movie["title"])


def print_first_masterpiece(movies: list[dict]) -> None:
    """Print first masterpiece title"""
    i = 0
    while i < len(movies):
        if movies[i]["rating"] >= 9:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies: list[dict], threshold = 120) -> int:
    """Count movies longer threshold"""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


def normalize_title(title: str) -> str:
    """Get title in title case"""
    words = title.split()
    normalized_words = []
    for word in words:
        normalized_words.append(word[0].upper() + word[1:])
    return " ".join(normalized_words)


def make_slug(title: str) -> str:
    """Get slug from title"""
    slug = title.lower().replace(" ", "-")
    return slug


def format_report_line(movie: dict) -> str:
    """Get movie report line"""
    title = normalize_title(movie["title"])
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    report_line = (
        f'"{title}" ({movie["year"]}) — '
        f'{movie["rating"]}/10, {duration}, жанры: {genres}'
    )
    return report_line


def titles_sorted_by_rating(movies: list[dict]) -> list[str]:
    """Get movie titles sorted by rating"""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    titles = []
    for movie in sorted_movies:
        titles.append(movie["title"])
    return titles


def top_n_by_rating(movies: list[dict], n=3) -> list[tuple]:
    """Get top movies by rating"""
    sorted_movies = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    top_movies = []
    for movie in sorted_movies[:n]:
        top_movies.append((movie["title"], movie["rating"]))
    return top_movies


def count_by_genre(movies: list[dict]) -> dict:
    """Count movies by genre"""
    genres_count = {}
    for movie in movies:
        for genre in sorted(movie["genres"]):
            genres_count[genre] = genres_count.get(genre, 0) + 1
    return genres_count


def actor_filmography(movies: list[dict]) -> dict:
    """Get actor filmography"""
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            actor_movies = filmography.get(actor, [])
            actor_movies.append(movie["title"])
            filmography[actor] = actor_movies
    return filmography


def ratings_above_average(movies: list[dict]) -> dict:
    """Get ratings above average"""
    mean_rating = average_rating(movies)
    ratings = {
        movie["title"]: movie["rating"]
        for movie in movies
        if movie["rating"] > mean_rating
    }
    return ratings


def all_genres(movies: list[dict]) -> set:
    """Get all unique genres"""
    genres = set()
    for movie in movies:
        genres = genres | movie["genres"]
    return genres


def common_actors(movie1: dict, movie2: dict) -> set:
    """Get common actors"""
    actors1 = set(movie1["actors"])
    actors2 = set(movie2["actors"])
    actors = actors1 & actors2
    return actors


def genres_only_in_one(movies_a: list[dict], movies_b: list[dict]) -> set:
    """Get genres only in first movie list"""
    genres_a = all_genres(movies_a)
    genres_b = all_genres(movies_b)
    genres = genres_a - genres_b
    return genres


def iter_high_rated(movies: list[dict], min_rating=8.0):
    """Iterate high rated movies"""
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie


def total_duration_above_rating(movies: list[dict], min_rating=7) -> int:
    """Get total duration for movies above rating"""
    total_duration = sum(
        movie["duration_min"]
        for movie in movies
        if movie["rating"] > min_rating
    )
    return total_duration


def print_high_rated_report(movies: list[dict]) -> None:
    """Print high rated movies report"""
    for movie in iter_high_rated(movies):
        print(format_report_line(movie))


def build_report(movies: list[dict]) -> None:
    """Print catalog report"""
    age_stats = catalog_age_stats(movies)
    genres_count = count_by_genre(movies)
    sorted_genres = sorted(
        genres_count.items(),
        key=lambda genre: (-genre[1], genre[0]),
    )
    genres = ", ".join(sorted(all_genres(movies)))

    print("ОТЧЕТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")
    print(f"Средний возраст фильмов: {age_stats[2]} лет")
    print()
    print("Топ-3 фильма:")
    for title, rating in top_n_by_rating(movies):
        for movie in movies:
            if movie["title"] == title and movie["rating"] == rating:
                print(f"  {format_report_line(movie)}")
                break
    print()
    print("Фильмов по жанрам:")
    for genre, count in sorted_genres:
        print(f"  {genre} — {count}")
    print()
    print(f"Все жанры каталога: {genres}")


def main():
    build_report(movies)


if __name__ == "__main__":
    main()
