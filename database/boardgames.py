# Boardgames
#
# Game: id, title, designer, publisher, year, artist, selling_price,
#       min_players, max_players, playing_time, age_from, genre, mechanics
#                 *designers, *artists, *publishers

# Designer: game_id, first_name, last_name, age, sex,
#           *publishers, *games, *artists

# Publisher: game_id, publisher_name, game_title, printed_quantity, printing_price, designer, artist
#       *games, *designers, *artists

# Artist: game_id, first_name, last_name, age, sex,
#        *games, *publishers, *designers

games_table = """CREATE TABLE IF NOT EXISTS boardgames (
                                                        id integer PRIMARY KEY,
                                                        game_title text NOT NULL,
                                                        designer text,
                                                        publisher text,
                                                        year_published date,
                                                        artist text,
                                                        selling_price numeric,
                                                        min_players integer,
                                                        max_players integer,
                                                        playing_time integer,
                                                        age_from integer,
                                                        genre text,
                                                        mechanics text
                                                        )"""