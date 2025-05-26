-- Consulta para obtener el nombre de la música, compositores, nombre del álbum y nombre del artista
-- de la playlist con ID 5, ordenado por el nombre del artista
-- de la base de datos Chinook
SELECT "Track"."Name" AS "Nombre de la Música",
"Track"."Composer" AS "Compositores",
"Album"."Title" AS "Nombre del Album",
"Artist"."Name" AS "Nombre del Artista"
FROM "Playlist"
JOIN "PlaylistTrack"
USING ("PlaylistId")
JOIN "Track"
USING ("TrackId")
JOIN "Album"
USING ("AlbumId")
JOIN "Artist"
USING ("ArtistId")
WHERE "Track"."Composer" IS NOT NULL AND "Playlist"."PlaylistId" = 5
ORDER BY "Nombre del Artista";