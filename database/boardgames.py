# Boardgames
#
# Game: id, title, selling_price, min_players, max_players, playing_time, age_from, genre (FK to genre)

# Designer: id, first_name, last_name, age

# Publisher: id, publisher_name, printed_quantity, printing_price

# Artist: id, game_id, first_name, last_name, age
#        *games, *publishers, *designers

# Genres: id, genre

# Many to Many
# designer_id FK to designer:id, game_id FK to games:id
# designer_id, publisher_id
# designer_id, artist_id

# publisher_id, game_id
# publisher_id, artist_id

# artist_id, game_id

games_table = """CREATE TABLE IF NOT EXISTS boardgames (
                                                        id integer PRIMARY KEY,
                                                        game_title text NOT NULL,
                                                        year_published date NOT NULL,
                                                        selling_price numeric NOT NULL,
                                                        min_players integer NOT NULL,
                                                        max_players integer NOT NULL,
                                                        playing_time integer NOT NULL,
                                                        age_from integer NOT NULL,
                                                        genre_id integer NOT NULL,
                                                        )"""

designers_table = """CREATE TABLE IF NOT EXISTS designers (
                                                        id integer PRIMARY KEY,
                                                        first_name text NOT NULL,
                                                        last_name text NOT NULL,
                                                        age integer NOT
                                                        )"""

publishers_table = """CREATE TABLE IF NOT EXISTS publishers (
                                                        id integer PRIMARY KEY,
                                                        publisher_name text NOT NULL,
                                                         text NOT NULL,
                                                        printed_quantity integer NOT NULL,
                                                        printing_price integer NOT NULL
                                                        )"""