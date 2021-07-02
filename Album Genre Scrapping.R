library(spotifyr)
library(readr)
pass_file <- "data/usuarioyclave.txt"
claves <- read.csv(pass_file, header = T)
Sys.setenv(SPOTIFY_CLIENT_ID = claves$client_id[1])
Sys.setenv(SPOTIFY_CLIENT_SECRET = claves$client_secret[1])

acces_token <- get_spotify_access_token()

df_audio_features_raw <- read.csv("data/audio_features_plano_sin_duplicados.csv")

genres <- df_audio_features_raw %>% distinct(artist_id, artist_name)

x <- lapply(genres$artist_id, function(x) paste(get_artist(x)$genre, collapse = ","))

genres$genres <- unlist(x)

write.csv(genres, file = "data/genres_by_artist_id.csv", row.names = F)
